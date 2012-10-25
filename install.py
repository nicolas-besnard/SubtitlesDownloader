import _winreg
import os
import sys
import shutil



def moove_file(path):
	current_path = os.getcwd()
	for filename in os.listdir("."):
		if filename == "install.exe":
			continue
		shutil.move(current_path + "\\"+ filename, path)

def create_registery_entry(path):
	print "Creation dans le registre"
	register_name = _winreg.HKEY_CLASSES_ROOT
	register_path = "*\\shell\\"
	new_register_name = "DownloadSubtitle"
	try:
		# Create main register
		reg = _winreg.CreateKey(register_name, register_path)
		_winreg.SetValue(reg, "DownloadSubtitle", _winreg.REG_SZ, "Download subtitle")
		_winreg.CloseKey(reg)
		# Create sub register
		reg = _winreg.CreateKey(_winreg.HKEY_CLASSES_ROOT, register_path + new_register_name)
		_winreg.SetValue(reg, "command", _winreg.REG_SZ, "\""+ path +"\main.exe\" \"%1\"")
		_winreg.CloseKey(reg)
	except:
		print "registre"

def create_exe_dir(path):
	print "Installation des fichiers"
	try:
		print os.mkdir(path)
	except WindowsError:
		print "Already Install"

install_dir =  os.environ.get("USERPROFILE")
install_dirname = "DownloadSubtitle"
install_dir += "\\"+ install_dirname
create_exe_dir(install_dir)
create_registery_entry(install_dir)
moove_file(install_dir)
os.system("pause")

