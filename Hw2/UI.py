# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(774, 853)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(290, 50, 171, 171))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.loadvideo = QtWidgets.QPushButton(self.groupBox)
        self.loadvideo.setGeometry(QtCore.QRect(40, 20, 93, 28))
        self.loadvideo.setObjectName("loadvideo")
        self.loadimage = QtWidgets.QPushButton(self.groupBox)
        self.loadimage.setGeometry(QtCore.QRect(40, 60, 93, 28))
        self.loadimage.setObjectName("loadimage")
        self.loadfolder = QtWidgets.QPushButton(self.groupBox)
        self.loadfolder.setGeometry(QtCore.QRect(40, 100, 93, 28))
        self.loadfolder.setObjectName("loadfolder")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(260, 280, 241, 71))
        self.groupBox_2.setObjectName("groupBox_2")
        self.backgroundsubstraction = QtWidgets.QPushButton(self.groupBox_2)
        self.backgroundsubstraction.setGeometry(QtCore.QRect(10, 20, 221, 28))
        self.backgroundsubstraction.setObjectName("backgroundsubstraction")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(259, 380, 241, 101))
        self.groupBox_3.setObjectName("groupBox_3")
        self.preprocessing = QtWidgets.QPushButton(self.groupBox_3)
        self.preprocessing.setGeometry(QtCore.QRect(10, 20, 221, 28))
        self.preprocessing.setObjectName("preprocessing")
        self.videotracking = QtWidgets.QPushButton(self.groupBox_3)
        self.videotracking.setGeometry(QtCore.QRect(10, 60, 221, 28))
        self.videotracking.setObjectName("videotracking")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(260, 520, 241, 71))
        self.groupBox_5.setObjectName("groupBox_5")
        self.perspectivetransform = QtWidgets.QPushButton(self.groupBox_5)
        self.perspectivetransform.setGeometry(QtCore.QRect(10, 20, 221, 28))
        self.perspectivetransform.setObjectName("perspectivetransform")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(260, 610, 241, 101))
        self.groupBox_6.setObjectName("groupBox_6")
        self.imagereconstruction = QtWidgets.QPushButton(self.groupBox_6)
        self.imagereconstruction.setGeometry(QtCore.QRect(10, 20, 221, 28))
        self.imagereconstruction.setObjectName("imagereconstruction")
        self.constructionerror = QtWidgets.QPushButton(self.groupBox_6)
        self.constructionerror.setGeometry(QtCore.QRect(10, 60, 221, 28))
        self.constructionerror.setObjectName("constructionerror")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 774, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loadvideo.setText(_translate("MainWindow", "Load Video"))
        self.loadimage.setText(_translate("MainWindow", "LoadIimage"))
        self.loadfolder.setText(_translate("MainWindow", "Load Folder"))
        self.groupBox_2.setTitle(_translate("MainWindow", "1. Background Substraction"))
        self.backgroundsubstraction.setText(_translate("MainWindow", "1.1 Background Substraction"))
        self.groupBox_3.setTitle(_translate("MainWindow", "2. Optical Flow"))
        self.preprocessing.setText(_translate("MainWindow", "2.1 Preprocessing"))
        self.videotracking.setText(_translate("MainWindow", "2.2 Video Tracking"))
        self.groupBox_5.setTitle(_translate("MainWindow", "3. Perspective Transform"))
        self.perspectivetransform.setText(_translate("MainWindow", "3.1 Perspective Transform"))
        self.groupBox_6.setTitle(_translate("MainWindow", "4. PCA"))
        self.imagereconstruction.setText(_translate("MainWindow", "4.1 Image Reconstruction"))
        self.constructionerror.setText(_translate("MainWindow", "4.2 Compute the reconstruction error"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

