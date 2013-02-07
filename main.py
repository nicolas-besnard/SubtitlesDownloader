# -*- coding: utf-8 -*-

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

from PySide.QtCore import *
from PySide.QtGui import *

from	gui		import *
from	form		import *



class GUI(QMainWindow):
	def __init__(self, parent = None):
		QMainWindow.__init__(self)
		ui = Ui_MainWindow()
		self.ui = ui
		ui.setupUi(self)
		self.init_languageComboBox()

	def init_languageComboBox(self):
		self.ui.languagesComboBox.addItem("French", 0)
		self.ui.languagesComboBox.addItem("English", 1)
		
	def showWindow(self):
		self.show()

	def clearFileList(self):
		self.ui.fileList.clear()

	def addElemToFileList(self, tmp_file, tmp_url):
		item = QtGui.QListWidgetItem(tmp_file)
		item.setData(12, tmp_url)
		self.ui.fileList.insertItem(12, item)

class GUI_Form(QMainWindow):
	def __init__(self, parent = None):
		self.window = QtGui.QMainWindow()
		ui = Ui_Form()
		self.ui = ui
		ui.setupUi(self.window)
		
class Serie(GUI):
	"""
	"""	
	subtitles_exts = ['.srt']
	
	def __init__(self, directory, filename = ""):
		GUI.__init__(self)
		self.ui.directoryInput.setText(directory)
		self.apiKey = "260563B3BDEA"
		self.defaultUrl = "http://api.betaseries.com/"
		self.errorCode = -1
		self.subtitlesLanguage = "VF"
		self.subtitlesHD = false
		self.serieName = ""
		self.season = ""
		self.episode = ""
		self.serieNameFromServer = ""
		self.login = "cappie013"
		self.password = "fa35ad09c9f866b03507db0c441a1194"
		self.filename = filename
		self.fileExtension = ""
		self.allowed_video_ext = ['avi', 'mkv', 'mp4']
		self.ui.searchBtn.clicked.connect(self.doSearch)
		self.ui.downloadBtn.clicked.connect(self.doDownload)
		#self.password = hashlib.md5("toto").hexdigest()

	def doSearch(self):
		self.clearFileList()
		self.serieName = self.ui.showInput.text()
		self.season = self.ui.seasonInput.text()
		self.episode = self.ui.episodeInput.text()
		self.subtitlesHD = self.ui.HDSelected.isChecked()
		languageSelected = self.ui.languagesComboBox.itemData(self.ui.languagesComboBox.currentIndex())
		if (languageSelected == 0):
			self.subtitlesLanguage = "VF"
		else:
			self.subtitlesLanguage = "VO"
		if (self.serieName and self.season and self.episode):
			self.getSerieNameFromServer()

	def doDownload(self):
		if self.ui.fileList.currentItem():
			print self.ui.fileList.currentItem().data(12)
			#self.url = self.ui.fileList.currentItem().data(1)
			#self.downloadSubtitle()
		
	def getFiletype(self, fileName):
		info = os.path.splitext(fileName)
		return (info[0], info[1][1::].lower())

	def fileIsAvailable(self, fileName):
		"""
		"""
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

	def getSerieInfosFromFilename(self):
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
		if self.filename.rfind('\\') != -1:	
			self.filename = self.filename[self.filename.rfind('\\') + 1:len(self.filename)]
		self.fileIsAvailable(self.filename)
		for regex, regex_num in episode_rexps:
			match = re.search(regex, self.filename, re.IGNORECASE)
			if match:
				break
		if match:
			if regex_num == 1:
				self.filename = self.fileName[0:match.start() - 2]
			elif regex_num == 2:
				self.filename = self.fileName[match.end() + 1::]
			self.serieName = self.filename.replace('.', ' ')
			self.season = match.groupdict()['season']
			self.episode = match.groupdict()['episode'][1::]
			self.showInput.setText(self.serieName)
			self.seasonInput.setText(self.season)
			self.episodeInput.setText(self.episode)
			self.getSerieNameFromServer()
		else:
			print "Can't find file information."

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
		else:
			self.showFromServer = dom.getElementsByTagName('url')[0].toxml().replace('<url>', '').replace('</url>', '')
			self.serieNameFromServer = dom.getElementsByTagName('title')[0].toxml().replace('<title>', '').replace('</title>', '')			
			self.searchSubtitle()

	def searchSubtitle(self):
		modele = "subtitles/show/{}.xml".format(self.serieNameFromServer)
		param = "season={}&episode={}&language={}".format(self.season, self.episode, self.subtitlesLanguage)
		subtitles = urlopen(self.urlConstructor(modele, param))
		content = subtitles.read()
		subtitles.close()
		dom = parseString(content)
		if len(dom.getElementsByTagName('url')) == 0:
			print "No subtitles available at this time in "+ self.subtitlesLanguage +"."
		else:
			for url in dom.getElementsByTagName('subtitle'):
				tmp_file = url.getElementsByTagName('file')[0].toxml().replace('<file>','').replace('</file>', '')
				tmp_url = url.getElementsByTagName('url')[0].toxml().replace('<url>','').replace('</url>', '')
				self.addElemToFileList(tmp_file, tmp_url)
				self.url = dom.getElementsByTagName('url')[0].toxml().replace('<url>','').replace('</url>','')
				
	def downloadSubtitle(self):
		print self.url
		print "Download of "+ self.serieName +" S"+ self.season +"E"+ self.episode
		# define subtitle file name
		subtitle_file_name = self.serieName + self.season + self.episode
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
	# Init App
	app = QtGui.QApplication(sys.argv)
	
	if (len(sys.argv) >= 2):
		test = Serie(os.getcwd(), sys.argv[1])
		test.getSerieInfosFromFilename()
	else:
		test = Serie(os.getcwd())
	test.show()
	sys.exit(app.exec_())

"""
# J S O N  T E S T
url = "http://api.betaseries.com/subtitles/show/suits.xml?language=VF&season=1&episode=1&key=260563B3BDEA&format=json"
	serie = urlopen(url)
	content = serie.read()
	serie.close()
	json_data = json.loads(content)
	data = json_data['root']
	print data['subtitles']['0']
	for nomfich in glob.glob(r'G:/Series/Suits/*.mkv'):
		print nomfich 
	print "-"*20
	
	dir_content = os.listdir(r'G:/Series/Suits')
"""
