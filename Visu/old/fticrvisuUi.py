# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lio/Documents/bitbucket/draft/Visu/util/fticrResol.ui'
#
# Created: Sun Apr 20 14:34:58 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from __future__ import print_function

from PySide import QtCore, QtGui
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(908, 758)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 340, 91, 81))
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.toolButton = QtGui.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(20, 420, 41, 31))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(760, 670, 111, 41))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 0, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 251, 211))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.layoutD = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.layoutD.setObjectName(_fromUtf8("layoutD"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 670, 731, 41))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_5 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 240, 161, 22))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 220, 251, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 270, 101, 21))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 300, 211, 16))
        self.label_9.setText(_fromUtf8(""))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(110, 270, 91, 21))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_10 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(100, 350, 51, 51))
        self.pushButton_10.setText(_fromUtf8(""))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.pushButton_11 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(150, 350, 51, 51))
        self.pushButton_11.setText(_fromUtf8(""))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 320, 61, 21))
        self.pushButton_2.setMaximumSize(QtCore.QSize(115, 32))
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 320, 61, 21))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(610, 10, 141, 20))
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 460, 261, 201))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.scale_zoom = QtGui.QWidget()
        self.scale_zoom.setObjectName(_fromUtf8("scale_zoom"))
        self.lineEdit_2 = QtGui.QLineEdit(self.scale_zoom)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 110, 211, 21))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_10 = QtGui.QLabel(self.scale_zoom)
        self.label_10.setGeometry(QtCore.QRect(10, 90, 191, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.pushButton_9 = QtGui.QPushButton(self.scale_zoom)
        self.pushButton_9.setGeometry(QtCore.QRect(140, 30, 71, 21))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.label_3 = QtGui.QLabel(self.scale_zoom)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 73, 19))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label = QtGui.QLabel(self.scale_zoom)
        self.label.setGeometry(QtCore.QRect(90, 0, 72, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.scale_zoom)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 73, 45))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.scale_zoom)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 30, 113, 22))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.pushButton_6 = QtGui.QPushButton(self.scale_zoom)
        self.pushButton_6.setGeometry(QtCore.QRect(80, 140, 71, 21))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_13 = QtGui.QPushButton(self.scale_zoom)
        self.pushButton_13.setGeometry(QtCore.QRect(170, 136, 41, 27))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.tabWidget.addTab(self.scale_zoom, _fromUtf8(""))
        self.profile_peaks = QtGui.QWidget()
        self.profile_peaks.setObjectName(_fromUtf8("profile_peaks"))
        self.label_13 = QtGui.QLabel(self.profile_peaks)
        self.label_13.setGeometry(QtCore.QRect(0, 10, 201, 20))
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.pushButton_8 = QtGui.QPushButton(self.profile_peaks)
        self.pushButton_8.setGeometry(QtCore.QRect(60, 70, 114, 41))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.lineEdit_4 = QtGui.QLineEdit(self.profile_peaks)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 40, 171, 22))
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.pushButton_12 = QtGui.QPushButton(self.profile_peaks)
        self.pushButton_12.setGeometry(QtCore.QRect(60, 110, 114, 41))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.tabWidget.addTab(self.profile_peaks, _fromUtf8(""))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 420, 91, 41))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(771, 10, 121, 21))
        self.label_12.setText(_fromUtf8(""))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 908, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Visualization", None))
        self.pushButton_3.setToolTip(_translate("MainWindow", "original view", None))
        self.toolButton.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Load file</p></body></html>", None))
        self.toolButton.setText(_translate("MainWindow", "...", None))
        self.label_8.setText(_translate("MainWindow", "taille", None))
        self.label_7.setText(_translate("MainWindow", "Size:", None))
        self.label_5.setText(_translate("MainWindow", "File :", None))
        self.label_6.setText(_translate("MainWindow", "fich", None))
        self.label_4.setText(_translate("MainWindow", "name of fticr dataset (.png or .pdf) :", None))
        self.pushButton_5.setText(_translate("MainWindow", "save picture", None))
        self.pushButton_7.setText(_translate("MainWindow", "saveprofile", None))
        self.pushButton_2.setToolTip(_translate("MainWindow", "Zoom forward", None))
        self.pushButton.setToolTip(_translate("MainWindow", "Zoom back", None))
        self.label_11.setText(_translate("MainWindow", "highest intensity: ", None))
        self.label_10.setText(_translate("MainWindow", "zoom coord (llx, lly, urx, ury):", None))
        self.pushButton_9.setText(_translate("MainWindow", "new scale", None))
        self.label_3.setText(_translate("MainWindow", "scale :", None))
        self.label.setText(_translate("MainWindow", "scaleval", None))
        self.label_2.setText(_translate("MainWindow", "res", None))
        self.pushButton_6.setText(_translate("MainWindow", "zoom", None))
        self.pushButton_13.setText(_translate("MainWindow", "3D", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scale_zoom), _translate("MainWindow", "scale zoom", None))
        self.label_13.setText(_translate("MainWindow", "profile coord (llx, lly, urx, ury):", None))
        self.pushButton_8.setText(_translate("MainWindow", "profile", None))
        self.pushButton_12.setText(_translate("MainWindow", "peaks", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.profile_peaks), _translate("MainWindow", "profile & peaks", None))
        self.pushButton_4.setText(_translate("MainWindow", "pt or m/z", None))

