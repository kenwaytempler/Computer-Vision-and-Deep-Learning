# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Q5.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(240, 70, 261, 381))
        self.groupBox.setObjectName("groupBox")
        self.loadimage = QtWidgets.QPushButton(self.groupBox)
        self.loadimage.setGeometry(QtCore.QRect(60, 50, 141, 28))
        self.loadimage.setObjectName("loadimage")
        self.showimage = QtWidgets.QPushButton(self.groupBox)
        self.showimage.setGeometry(QtCore.QRect(60, 100, 141, 28))
        self.showimage.setObjectName("showimage")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 150, 141, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 200, 141, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 250, 141, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(60, 300, 141, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.groupBox.setTitle(_translate("MainWindow", "RedNet50"))
        self.loadimage.setText(_translate("MainWindow", "Load Image"))
        self.showimage.setText(_translate("MainWindow", "1.Show Image"))
        self.pushButton_3.setText(_translate("MainWindow", "2.Show Distribution"))
        self.pushButton_4.setText(_translate("MainWindow", "3.Show Model Struc"))
        self.pushButton_5.setText(_translate("MainWindow", "4.Show Comparison"))
        self.pushButton_6.setText(_translate("MainWindow", "5.Inference"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

