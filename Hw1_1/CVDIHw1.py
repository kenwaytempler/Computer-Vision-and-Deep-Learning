#For question1 pls always run find corners first
#If encounter no response or other errors please restart program
# eg. Between Q1 and Q2 may need to restart program
#     Between 2.1 and 2.2 may need to restart too  
from ast import Interactive
import cv2 as cv
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import numpy as np
from GUI import Ui_MainWindow
import glob
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import W, filedialog
dataset1=[]
dataset2=[]
dataset3=[]
dataset4=[]
imagel=[]
imager=[]
intrinsic = []
extrinsic1 = []
extrinsic2 = []
distortion = []
objpoints = [] 
imgpoints = []  
imgpts=[]

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # in python3, super(Class, self).xxx = super().xxx
        dataset1.clear()
        dataset2.clear()
        dataset3.clear()
        dataset4.clear()
        intrinsic.clear()
        extrinsic1.clear()
        extrinsic2.clear()
        imagel.clear()
        imager.clear()
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.control()
    
    def control(self):
        self.ui.LoadFolder.clicked.connect(self.loadfolder)
        self.ui.FindCorner.clicked.connect(self.findcorner)
        self.ui.FindIntrinsic.clicked.connect(self.findintrinsic)
        self.ui.FindExtrinsic.clicked.connect(self.findextrinsic)
        self.ui.FindDisortion.clicked.connect(self.finddisortion)
        self.ui.ShowResult.clicked.connect(self.findundisortedresult)
        self.ui.ShowWordsonBoard.clicked.connect(self.showordonboard)
        self.ui.ShowWordsonVertically.clicked.connect(self.showwordvertically)
        self.ui.LoadImage_L.clicked.connect(self.loadimagel)
        self.ui.LoadImageR.clicked.connect(self.loadimager)
        self.ui.SteroDisparity.clicked.connect(self.stero)
    
    def loadimagel(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilenames()
        print(file_path)
        image=cv.imread(file_path[0])
        imagel.append(image)



        # cv.namedWindow("Find Corners", cv.WINDOW_NORMAL)
        # cv.imshow("Find Corners", imagel[0])
        # cv.waitKey(500)
    
    def loadimager(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilenames()
        print(file_path)
        image=cv.imread(file_path[0])
        imager.append(image)

        # cv.namedWindow("Find Corners", cv.WINDOW_NORMAL)
        # cv.imshow("Find Corners", imager[0])
        # cv.waitKey(500)

    def loadfolder(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilenames()
        print(file_path)
        for file in file_path:
            image=cv.imread(file)
            dataset1.append(image)
            dataset2.append(image)
            dataset3.append(image)
            dataset4.append(image)
        # for file in dataset1:
        #     cv.namedWindow("test")
        #     cv.imshow("test",file)
        #     cv.waitKey(0)
        # print("done")
        return

    def findcorner(self): 
        x = 11
        y = 8    
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001) 
        objp = np.zeros((11 * 8, 3), np.float32)   
        objp[:, :2] = np.mgrid[0:11, 0:8].T.reshape(-1, 2)   
        for image in dataset3:             
            gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)       
            ret, corners = cv.findChessboardCorners(image, (x, y), None)
            if ret == True: 
                objpoints.append(objp)
                imgpoints.append(corners)

                       
                cv.drawChessboardCorners(image, (x, y), corners, ret)
                image = cv.resize(image, (700, 425), interpolation=cv.INTER_AREA)
                cv.namedWindow("Find Corners") 
                cv.imshow("Find Corners", image)
                cv.waitKey(500)
                

        ret2, intr, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
        intrinsic.append(intr)
        extrinsic1.append(rvecs)
        extrinsic2.append(tvecs)
        distortion.append(dist)
        #print(intr)
        return

    def findintrinsic(self):
        print("Intrinsic:")
        print(intrinsic[0])


    def findextrinsic(self):
        imagenumber=self.ui.comboBox.currentIndex()       
        rotation, g = cv.Rodrigues(extrinsic1[0][imagenumber])
        ext = np.column_stack((rotation, extrinsic2[0][imagenumber]))
        print("Extrinsic:")
        print(ext)
        return
    
    def finddisortion(self):
        print("Disortion:")
        print(distortion[0])
        return

    def findundisortedresult(self):        
        for image in dataset3:
            cv.namedWindow("Disorted Result", cv.WINDOW_NORMAL)
            cv.imshow("Disorted Result", image)
            y, x = image.shape[:2]
            newcameramatrix, roi = cv.getOptimalNewCameraMatrix(intrinsic[0], distortion[0], (x,y), 0, (x,y))
            image2 = cv.undistort(image, intrinsic[0], distortion[0], None, newcameramatrix)
            cv.namedWindow("Undisorted Result", cv.WINDOW_NORMAL)
            cv.imshow("Undisorted Result", image2)
            cv.waitKey(500)
        return

    def showordonboard(self):
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        objp = np.zeros((8 * 11, 3), np.float32)
        objp[:, :2] = np.mgrid[0:11, 0:8].T.reshape(-1, 2)
        objpoints2 = []  
        imgpoints2 = []

        position=[[7,5,0], [4,5,0], [1,5,0], [7,2,0], [4,2,0], [1,2,0]]
        position=np.array(position,np.float32)
        character = cv.FileStorage("Q2_Image/Q2_lib/alphabet_lib_onboard.txt", cv.FILE_STORAGE_READ)
        word = self.ui.lineEdit.text()

        for i in range(len(dataset1)):
            image = dataset1[i]
            gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            ret, corners = cv.findChessboardCorners(gray, (11, 8), None)
            if ret == True:
                corners = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
                objpoints2.append(objp)
                imgpoints2.append(corners)
                ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints2, imgpoints2, gray.shape[::-1], None, None)
                
                for index, w in enumerate(list(word)):
                    ch = character.getNode(w).mat()
                    for edge in ch: #print each character
                        shift = position[index] + edge
                        shift = np.array(shift, np.float32)
                        imgpts, jac = cv.projectPoints(shift, rvecs[i], tvecs[i], mtx, dist)
                        cv.line(image,(imgpts[1][0][0], imgpts[1][0][1]) , (imgpts[0][0][0], imgpts[0][0][1]),(0, 0, 255), 8)    

                
                image = cv.resize(image, (700, 425), interpolation=cv.INTER_AREA)
                cv.namedWindow('img')
                cv.imshow('img', image)
                cv.waitKey(1000)
        objpoints2.clear()
        imgpoints2.clear()

        return 

    def showwordvertically(self):
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        objp = np.zeros((8 * 11, 3), np.float32)
        objp[:, :2] = np.mgrid[0:11, 0:8].T.reshape(-1, 2)
        objpoints2 = []  
        imgpoints2 = []
        position=[[7,5,0], [4,5,0], [1,5,0], [7,2,0], [4,2,0], [1,2,0]]
        position=np.array(position,np.float32)
        character = cv.FileStorage("Q2_Image/Q2_lib/alphabet_lib_vertical.txt", cv.FILE_STORAGE_READ)
        word = self.ui.lineEdit.text()

        for j in range(len(dataset2)):
            image2 = dataset2[j]
            gray = cv.cvtColor(image2, cv.COLOR_BGR2GRAY)
            ret2, corners2 = cv.findChessboardCorners(gray, (11, 8), None)
            print(j)
            if ret2 == True:               
                corners2 = cv.cornerSubPix(gray, corners2, (11, 11), (-1, -1), criteria)
                objpoints2.append(objp)
                imgpoints2.append(corners2)
                ret2, mtx2, dist2, rvecs2, tvecs2 = cv.calibrateCamera(objpoints2, imgpoints2, gray.shape[::-1], None, None)
                
                for index, w in enumerate(list(word)):
                    ch = character.getNode(w).mat()
                    for edge in ch: #print each character
                        shift = position[index] + edge
                        shift = np.array(shift, np.float32)
                        imgpts2, jac = cv.projectPoints(shift, rvecs2[j], tvecs2[j], mtx2, dist2)
                        cv.line(image2, (imgpts2[1][0][0], imgpts2[1][0][1]), (imgpts2[0][0][0], imgpts2[0][0][1]), (0, 0, 255), 8)    
               
                image2 = cv.resize(image2, (700, 425), interpolation=cv.INTER_AREA)
                cv.namedWindow('img2')
                cv.imshow('img2', image2)
                cv.waitKey(1000)
        objpoints2.clear()
        imgpoints2.clear()        
        return
    
    def stero(self):
        templ = cv.cvtColor(imagel[0], cv.COLOR_BGR2GRAY)
        templl = cv.cvtColor(imagel[0], cv.COLOR_BGR2GRAY)
        tempr = cv.cvtColor(imager[0], cv.COLOR_BGR2GRAY)
        temprr = cv.cvtColor(imager[0], cv.COLOR_BGR2GRAY)
        stereo = cv.StereoBM_create(256, 25)
        disparity = (stereo.compute(templ, tempr).astype(np.float32) /16.0) + 1
        #print(disparity) 
        disparity = disparity.astype(np.uint8)
        disparity = cv.resize(disparity, (700, 425), interpolation=cv.INTER_AREA)

        stereo2 = cv.StereoBM_create(128, 13)
        templl = cv.resize(templl, (700, 425), interpolation=cv.INTER_AREA)
        temprr = cv.resize(temprr, (700, 425), interpolation=cv.INTER_AREA)
        disparity2 = (stereo2.compute(templl, temprr).astype(np.float32) /16.0) + 1
        disparity2 = disparity2.astype(np.uint8)
        disparity2 = cv.resize(disparity2, (700, 425), interpolation=cv.INTER_AREA)
        imagel[0] = cv.resize(imagel[0], (700, 425), interpolation=cv.INTER_AREA)
        imager[0] = cv.resize(imager[0], (700, 425), interpolation=cv.INTER_AREA)
        

        
        def draw(event, x, y, flags, param):
            if event == cv.EVENT_LBUTTONDOWN:
                cv.circle(imagel[0], (x, y), 1, (0, 255, 0), thickness = 2)
                cv.circle(imager[0], (x - disparity2[y][x], y), 1, (0, 255, 0), thickness = 2)
                cv.imshow('imagel', imagel[0])
                cv.imshow('imager', imager[0])
                cv.imshow('image_disparity', disparity)
        
        while(1):
            cv.namedWindow('imagel')
            cv.setMouseCallback('imagel', draw)
            cv.imshow('imagel', imagel[0])
            cv.imshow('imager', imager[0])
            cv.imshow('image_disparity', disparity)
            cv.waitKey(0)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())