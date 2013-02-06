# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT Project/SubtitlesDownloader/mainwindow.ui'
#
# Created: Tue Feb  5 18:14:29 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(860, 420)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 411, 331))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.fileListLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.fileListLayout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.fileListLayout.setContentsMargins(0, -1, -1, -1)
        self.fileListLayout.setObjectName(_fromUtf8("fileListLayout"))
        self.fileList = QtGui.QListWidget(self.gridLayoutWidget)
        self.fileList.setObjectName(_fromUtf8("fileList"))
        self.fileListLayout.addWidget(self.fileList, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtGui.QWidget(self.centralWidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(430, 10, 411, 179))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.searchInfosLayout = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.searchInfosLayout.setMargin(0)
        self.searchInfosLayout.setObjectName(_fromUtf8("searchInfosLayout"))
        self.searchBtn = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.searchBtn.setObjectName(_fromUtf8("searchBtn"))
        self.searchInfosLayout.addWidget(self.searchBtn, 3, 1, 1, 2)
        self.showInput = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.showInput.setObjectName(_fromUtf8("showInput"))
        self.searchInfosLayout.addWidget(self.showInput, 0, 1, 1, 3)
        self.directoryLabel = QtGui.QLabel(self.gridLayoutWidget_2)
        self.directoryLabel.setObjectName(_fromUtf8("directoryLabel"))
        self.searchInfosLayout.addWidget(self.directoryLabel, 2, 0, 1, 1)
        self.episodeLabel = QtGui.QLabel(self.gridLayoutWidget_2)
        self.episodeLabel.setObjectName(_fromUtf8("episodeLabel"))
        self.searchInfosLayout.addWidget(self.episodeLabel, 1, 2, 1, 1)
        self.episodeInput = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.episodeInput.setObjectName(_fromUtf8("episodeInput"))
        self.searchInfosLayout.addWidget(self.episodeInput, 1, 3, 1, 1)
        self.showLabel = QtGui.QLabel(self.gridLayoutWidget_2)
        self.showLabel.setObjectName(_fromUtf8("showLabel"))
        self.searchInfosLayout.addWidget(self.showLabel, 0, 0, 1, 1)
        self.seasonLabel = QtGui.QLabel(self.gridLayoutWidget_2)
        self.seasonLabel.setObjectName(_fromUtf8("seasonLabel"))
        self.searchInfosLayout.addWidget(self.seasonLabel, 1, 0, 1, 1)
        self.seasonInput = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.seasonInput.setObjectName(_fromUtf8("seasonInput"))
        self.searchInfosLayout.addWidget(self.seasonInput, 1, 1, 1, 1)
        self.directoryInput = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.directoryInput.setObjectName(_fromUtf8("directoryInput"))
        self.searchInfosLayout.addWidget(self.directoryInput, 2, 1, 1, 3)
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 860, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.fileList, self.showInput)
        MainWindow.setTabOrder(self.showInput, self.seasonInput)
        MainWindow.setTabOrder(self.seasonInput, self.episodeInput)
        MainWindow.setTabOrder(self.episodeInput, self.directoryInput)
        MainWindow.setTabOrder(self.directoryInput, self.searchBtn)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.searchBtn.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.directoryLabel.setText(QtGui.QApplication.translate("MainWindow", "Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.episodeLabel.setText(QtGui.QApplication.translate("MainWindow", "Episode", None, QtGui.QApplication.UnicodeUTF8))
        self.showLabel.setText(QtGui.QApplication.translate("MainWindow", "Show", None, QtGui.QApplication.UnicodeUTF8))
        self.seasonLabel.setText(QtGui.QApplication.translate("MainWindow", "Season", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

