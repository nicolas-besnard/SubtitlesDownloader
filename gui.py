# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/mainwindow.ui'
#
# Created: Thu Feb  7 15:08:21 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 260)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 321, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.fileListLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.fileListLayout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.fileListLayout.setContentsMargins(0, -1, -1, -1)
        self.fileListLayout.setObjectName("fileListLayout")
        self.fileList = QtGui.QListWidget(self.gridLayoutWidget)
        self.fileList.setObjectName("fileList")
        self.fileListLayout.addWidget(self.fileList, 0, 0, 1, 1)
        self.downloadBtn = QtGui.QPushButton(self.gridLayoutWidget)
        self.downloadBtn.setObjectName("downloadBtn")
        self.fileListLayout.addWidget(self.downloadBtn, 1, 0, 1, 1)
        self.gridLayoutWidget_2 = QtGui.QWidget(self.centralWidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(340, 10, 290, 179))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.searchInfosLayout = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.searchInfosLayout.setContentsMargins(0, 0, 0, 0)
        self.searchInfosLayout.setObjectName("searchInfosLayout")
        self.showInput = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.showInput.setObjectName("showInput")
        self.searchInfosLayout.addWidget(self.showInput, 0, 1, 1, 3)
        self.directoryLabel = QtGui.QLabel(self.gridLayoutWidget_2)
        self.directoryLabel.setObjectName("directoryLabel")
        self.searchInfosLayout.addWidget(self.directoryLabel, 2, 0, 1, 1)
        self.episodeLabel = QtGui.QLabel(self.gridLayoutWidget_2)
        self.episodeLabel.setObjectName("episodeLabel")
        self.searchInfosLayout.addWidget(self.episodeLabel, 1, 2, 1, 1)
        self.episodeInput = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.episodeInput.setObjectName("episodeInput")
        self.searchInfosLayout.addWidget(self.episodeInput, 1, 3, 1, 1)
        self.seasonInput = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.seasonInput.setObjectName("seasonInput")
        self.searchInfosLayout.addWidget(self.seasonInput, 1, 1, 1, 1)
        self.seasonLabel = QtGui.QLabel(self.gridLayoutWidget_2)
        self.seasonLabel.setObjectName("seasonLabel")
        self.searchInfosLayout.addWidget(self.seasonLabel, 1, 0, 1, 1)
        self.showLabel = QtGui.QLabel(self.gridLayoutWidget_2)
        self.showLabel.setObjectName("showLabel")
        self.searchInfosLayout.addWidget(self.showLabel, 0, 0, 1, 1)
        self.directoryInput = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.directoryInput.setObjectName("directoryInput")
        self.searchInfosLayout.addWidget(self.directoryInput, 2, 1, 1, 3)
        self.searchBtn = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.searchBtn.setObjectName("searchBtn")
        self.searchInfosLayout.addWidget(self.searchBtn, 3, 2, 1, 2)
        self.HDSelected = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.HDSelected.setObjectName("HDSelected")
        self.searchInfosLayout.addWidget(self.HDSelected, 3, 0, 1, 1)
        self.languagesComboBox = QtGui.QComboBox(self.gridLayoutWidget_2)
        self.languagesComboBox.setObjectName("languagesComboBox")
        self.searchInfosLayout.addWidget(self.languagesComboBox, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 640, 25))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.showInput, self.seasonInput)
        MainWindow.setTabOrder(self.seasonInput, self.episodeInput)
        MainWindow.setTabOrder(self.episodeInput, self.directoryInput)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadBtn.setText(QtGui.QApplication.translate("MainWindow", "Download", None, QtGui.QApplication.UnicodeUTF8))
        self.directoryLabel.setText(QtGui.QApplication.translate("MainWindow", "Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.episodeLabel.setText(QtGui.QApplication.translate("MainWindow", "Episode", None, QtGui.QApplication.UnicodeUTF8))
        self.seasonLabel.setText(QtGui.QApplication.translate("MainWindow", "Season", None, QtGui.QApplication.UnicodeUTF8))
        self.showLabel.setText(QtGui.QApplication.translate("MainWindow", "Show", None, QtGui.QApplication.UnicodeUTF8))
        self.searchBtn.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.HDSelected.setText(QtGui.QApplication.translate("MainWindow", "HD", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

