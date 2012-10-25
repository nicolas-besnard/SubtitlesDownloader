# -*- coding:UTF-8 -*-

import re
import os
import sys
import time
import urllib
from urllib import urlopen, urlretrieve
from xml.dom.minidom import parseString
import zipfile
import hashlib
import json
import glob

class Serie:
	"""
	"""
	
	subtitles_exts = ['.srt']
	
	def __init__(self):
		self.apiKey = "260563B3BDEA"
		self.defaultUrl = "http://api.betaseries.com/"
		self.errorCode = -1
		self.subtitlesLanguage = "VF"
		self.serieName = ""
		self.serieSeason = 0
		self.serieEpisode = 0
		self.serieNameFromServer = ""
		self.login = "cappie013"
		self.password = "fa35ad09c9f866b03507db0c441a1194"
		self.fileName = ""
		self.fileExtension = ""
		self.allowed_video_ext = ['avi', 'mkv', 'mp4']
		#self.password = hashlib.md5("toto").hexdigest()

	def getFiletype(self, fileName):
		info = os.path.splitext(fileName)
		return (info[0], info[1][1::].lower())


	def fileIsAvailable(self, fileName):
		self.fileName, self.fileExtenstion = self.getFiletype(fileName)		
		if any(self.fileExtension == extension for extension in self.allowed_video_ext):
			return True
		return False

	def urlConstructor(self, modele, param = ""):
		protocol = "http"
		site = "api.betaseries.com"
		key = "key=%s" % self.apiKey
		param = "%s&%s" % (key, param)
		url = protocol +"://"+ site +"/"+ modele +"?"+ param
		return (url)

	def getSerieInfosFromFilename(self, filename):
		"""
		Getting serie name, serie seaon & serie episode
		from the file name 
		"""
		episode_rexps = [
							#S01E01
							(r'(?P<season>[0-9]{1,2})(?P<episode>(?:[Ee][0-9]{1,2})+)[^0-9]', 1),
							#01x01
							(r'(?P<season>[0-9]{1,2})(?P<episode>(?:[xX][0-9]{1,2})+)[^0-9]', 2)						
						]
		# Filename is a path
		if filename.rfind('\\') != -1:	
			filename = filename[filename.rfind('\\') + 1:len(filename)]
		self.fileIsAvailable(filename)
		for regex, regex_num in episode_rexps:
			match = re.search(regex, filename, re.IGNORECASE)
			if match:
				break
		if match:
			if regex_num == 1:
				filename = self.fileName[0:match.start() - 2]
			elif regex_num == 2:
				filename = self.fileName[match.end() + 1::]
			self.serieName = filename.replace('.', ' ')
			self.serieSeason = match.groupdict()['season']
			self.serieEpisode = match.groupdict()['episode'][1::]
			print self.serieName
			print self.serieSeason
			print self.serieEpisode
			self.getSerieNameFromServer()
		else:
			print "Can't find file information."
			os.system("pause")

	def getSerieInfosFromInput(self):
		"""
		Getting serie name, serie season & serie episode
		from user
		"""
		while not self.serieName:
			self.serieName = raw_input("Serie Name : ")
		while self.serieSeason <= 0 or self.serieSeason > 100:
			try:
				self.serieSeason = input("Season : ")
			except ValueError:
				pass
		while self.serieEpisode <= 0 or self.serieEpisode > 100:
			try:
				self.serieEpisode = input("Episode : ")
			except ValueError:
				pass
		print self.serieName
		print self.serieSeason
		print self.serieEpisode

	def getSerieNameFromServer(self):
		"""
		Getting serie's name from the server
		"""
		modele = "shows/search.xml"
		param = "title={}".format(self.serieName)
		serie = urlopen(self.urlConstructor(modele, param))
		content = serie.read()
		serie.close()
		dom = parseString(content)
		if len(dom.getElementsByTagName('url')) == 0:
			print "Serie not found : "+ self.serieName
			os.system("pause")
		else:
			self.serieNameFromServer = dom.getElementsByTagName('url')[0].toxml().replace('<url>', '').replace('</url>', '')
			self.serieName = dom.getElementsByTagName('title')[0].toxml().replace('<title>', '').replace('</title>', '')			
			self.searchSubtitle()

	def searchSubtitle(self):
		modele = "subtitles/show/{}.xml".format(self.serieNameFromServer)
		param = "season={}&episode={}&language={}".format(self.serieSeason, self.serieEpisode, self.subtitlesLanguage)
		subtitles = urlopen(self.urlConstructor(modele, param))
		content = subtitles.read()
		subtitles.close()
		dom = parseString(content)
		if len(dom.getElementsByTagName('url')) == 0:
			print "Not subtitles available at this time in "+ self.subtitlesLanguage +"."
			os.system("pause")
		else:
			self.url = dom.getElementsByTagName('url')[0].toxml().replace('<url>','').replace('</url>','')
			self.downloadSubtitle()

	def downloadSubtitle(self):
		print self.url
		print "Download of "+ self.serieName +" S"+ self.serieSeason +"E"+ self.serieEpisode
		os.system("pause")
		# define subtitle file name
		subtitle_file_name = self.serieName + self.serieSeason + self.serieEpisode
		urlretrieve(self.url, subtitle_file_name)
		zFile = zipfile.ZipFile(subtitle_file_name, "r")
		for data in zFile.infolist():
			# Get file name / extension of current file in zip
			fileName, fileExtension = self.getFiletype(data.filename)
			
			info = zFile.read(data.filename)
			fout = open(self.fileName +"."+ fileExtension, "w")
			fout.write(info +"."+ self.fileExtension)
			fout.close()
		zFile.close()
		os.remove(subtitle_file_name)

if __name__ == "__main__":
	if (len(sys.argv) >= 2):
		name = sys.argv[1]	
		subtitle = Serie()
		subtitle.getSerieInfosFromFilename(name)

	"""url = "http://api.betaseries.com/subtitles/show/suits.xml?language=VF&season=1&episode=1&key=260563B3BDEA&format=json"
	serie = urlopen(url)
	content = serie.read()
	serie.close()
	json_data = json.loads(content)
	data = json_data['root']
	print data['subtitles']['0']"""
	"""for nomfich in glob.glob(r'G:/Series/Suits/*.mkv'):
		print nomfich 
	print "-"*20"""
	"""
	dir_content = os.listdir(r'G:/Series/Suits')


				"""
