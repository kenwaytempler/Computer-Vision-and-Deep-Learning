import os
import numpy as np
import cv2 as cv2
import glob
import sys
import matplotlib.pyplot as plt
import tkinter as tk
import math
import re
from ast import Interactive
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from UI import Ui_MainWindow
from tkinter import W, filedialog
from sklearn.decomposition import PCA
#Parameter for question2
params = cv2.SimpleBlobDetector_Params()
params.minThreshold = 1
params.maxThreshold = 255
params.filterByArea = True
params.minArea = 35
params.maxArea = 90
params.filterByCircularity = 1.0
params.filterByConvexity = False
params.filterByInertia = False
video1 = []
image1 = []
images = []
filenames = []
errorimage = []

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

def loadfolder(folder):
    images.clear()
    filenames.clear()
    for filename in sorted_alphanumeric(os.listdir(folder)):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            filenames.append(filename)
            images.append(img)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        video1.clear()
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.control()

    def control(self):
        self.ui.loadvideo.clicked.connect(self.lv)
        self.ui.backgroundsubstraction.clicked.connect(self.backgroundsub)
        self.ui.preprocessing.clicked.connect(self.preprocessing2_1)
        self.ui.videotracking.clicked.connect(self.vtrack)
        self.ui.perspectivetransform.clicked.connect(self.perspectivet)
        self.ui.loadimage.clicked.connect(self.li)
        self.ui.imagereconstruction.clicked.connect(self.imager)
        self.ui.constructionerror.clicked.connect(self.error)
        self.ui.loadfolder.clicked.connect(self.lf)
        

    def lv(self):
        video1.clear()
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilenames()
        print(file_path)
        video1.append(file_path[0])
        
    def li(self):
        image1.clear()
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilenames()
        print(file_path)
        image1.append(file_path[0])

    def lf(self):
        filename=QFileDialog().getExistingDirectory(self,"Load Folder")
        if(filename==''): return
        loadfolder(filename)
    

    def backgroundsub(self):
        cap = cv2.VideoCapture(video1[0])
        width = int(cap.get(3))
        height = int(cap.get(4))
        average = np.zeros((height, width), np.float32)
        std = np.zeros((height, width), np.float32) 
        framecount=0
        while(cap.isOpened()):
            ret, frame = cap.read()
            if(framecount <= 25):      
                if ret == True:
                    framecount += 1
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    #cv2.imshow('Frame', gray)
                    average += gray
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        break
            else:
                break
        average = average / 25
        framecount = 0
        cap.release()
        cv2.destroyAllWindows()
        cap = cv2.VideoCapture(video1[0])
        while(cap.isOpened()):
            ret, frame = cap.read()
            if(framecount <= 25):
                if ret == True:
                    framecount += 1
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    std += np.float32(np.abs(gray - average)) ** 2
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        break
            else:
                break                
        std = std / 25
        std=np.sqrt(std)
        std[ std < 5 ] = 5
        std *= 5
        cap.release()   

        
        framecount = 0
        cap = cv2.VideoCapture(video1[0])
        gray = np.zeros((height, width), np.uint8)
        framemask2 = np.zeros((height, width), np.uint8)
        framemask3 = np.zeros_like(frame)
        while(cap.isOpened()):
            ret, frame = cap.read()
            framemask2.fill(0)        
            if ret:
                frame2 = frame.copy() 
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)               
                framemask2[np.uint8(np.abs(gray.astype(int) - average)) >= std] = 255
                frame[:,:,0] = frame[:,:,0] & framemask2
                frame[:,:,1] = frame[:,:,1] & framemask2
                frame[:,:,2] = frame[:,:,2] & framemask2
                framemask3[:,:,0] = framemask2
                framemask3[:,:,1] = framemask2
                framemask3[:,:,2] = framemask2
                Hori = np.concatenate((frame2,framemask3, frame), axis=1)
                cv2.imshow('Result' , Hori)
                cv2.waitKey(25)
                
            else:
                break  
        cap.release()
        cv2.destroyAllWindows()
        video1.clear()

  
    def preprocessing2_1(self):
        cap = cv2.VideoCapture(video1[0])
        while(cap.isOpened()):
            ret, frame = cap.read()
            break
        detector = cv2.SimpleBlobDetector_create(params)
        keypoints = detector.detect(frame)
        for i in range(len(keypoints)):
            x = keypoints[i].pt[0]
            y = keypoints[i].pt[1]
            cv2.rectangle(frame, (int(x)-6, int(y)-6), (int(x)+6, int(y)+6), (0, 0, 255), 1)
            cv2.line(frame, (int(x), int(y)-6), (int(x), int(y)+6), (0, 0, 255), 1)
            cv2.line(frame, (int(x)-6, int(y)), (int(x)+6, int(y)), (0, 0, 255), 1)
        cv2.imshow("Frame", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        video1.clear()
        return


    def vtrack(self):
        cap = cv2.VideoCapture(video1[0])
        ret, old_frame = cap.read()
        detector = cv2.SimpleBlobDetector_create(params)
        keypoints = detector.detect(old_frame)
        keypointsnp = []
       
        for i in range(len(keypoints)):
            x = keypoints[i].pt[0]
            y = keypoints[i].pt[1]
            cor=(x,y)
            cor=np.array(cor)
            keypointsnp.append(cor.astype(np.float32))
        keypointsnp = np.array(keypointsnp)
        lk_params = dict( winSize = (15, 15), maxLevel = 2, criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10, 0.03))
        old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
        mask = np.zeros_like(old_frame)

        while(True):
            if(ret):    
                ret, frame = cap.read()
                frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
               
                p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, keypointsnp, None, **lk_params)
                good_new = []
                good_old = []
            
                for i,item in enumerate(st):
                    if(item[0]):
                        good_new.append(p1[i])

                for i,item in enumerate(st):
                    if(item[0]):
                       good_old.append(keypointsnp[i])

                for i, (new, old) in enumerate(zip(good_new, good_old)):
                    x1, y1 = new.ravel()
                    x2, y2 = old.ravel()
                    mask = cv2.line(mask, (x1, y1), (x2, y2), (0, 255, 255), 2)
                    frame = cv2.circle(frame, (x2, y2), 5, (0, 255, 255), 1)
          
                img = cv2.add(frame, mask)
                cv2.imshow('Result', img)
                k = cv2.waitKey(25)
                if k == 27:
                    break
                old_gray = frame_gray.copy()
                keypointsnp = p1
  
        cv2.destroyAllWindows()
        cap.release()
        video1.clear()
        return


    def perspectivet(self):
        cap = cv2.VideoCapture(video1[0])
        ret, old_frame = cap.read()
        while(1):
            if(ret):
                img = cv2.imread(image1[0])
                height = img.shape[0]
                width = img.shape[1]
                projection = np.zeros((height, width, 3), np.uint8)
                projection.fill(255)
                sourcepts = np.array([[0, 0], [width, 0], [width, height], [0, height]])
                ret, frame = cap.read()
            
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_250)
            
                parameters = cv2.aruco.DetectorParameters_create()
                parameters.cornerRefinementMethod= cv2.aruco.CORNER_REFINE_SUBPIX
                parameters.maxMarkerPerimeterRate = 2
                parameters.minCornerDistanceRate = 0.15
                corners, ids, _= cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
                if(np.size(ids)<4):
                    continue
                framecorners = np.empty([4,2],dtype = int)
                for i in range(4):
                    if(ids[i][0]==1):
                        framecorners[0] = corners[i][0][0]
                    
                    elif(ids[i][0]==2):
                        framecorners[1] = corners[i][0][1]
                    
                    elif(ids[i][0]==3):
                        framecorners[2] = corners[i][0][2]
                    
                    elif(ids[i][0]==4):
                        framecorners[3] = corners[i][0][3]
                    
                #print(framecorners)
                h, status = cv2.findHomography(sourcepts, framecorners)
                out = cv2.warpPerspective(img, h, (frame.shape[1],frame.shape[0]))
                mask = cv2.warpPerspective(projection, h, (frame.shape[1],frame.shape[0]))
                mask = ~mask
                frame = frame & mask
                frame = frame | out
                cv2.imshow('Result', frame)
                cv2.waitKey(25)
        cv2.destroyAllWindows()
        return


    def imager(self):
        imagesf = []

        for img in images:
            imagesf.append(img.flatten())

        imahi = images[0].shape[0]
        imaw = images[0].shape[1]
        pca = PCA(n_components = 27)
        pca.fit(imagesf)
        imgtr = pca.transform(imagesf)
        imginverse = pca.inverse_transform(imgtr)
        errorimage.clear()
        imagere1= []
        
        for i in range(30):
            imagere2 = imginverse[i]
            imagere2 = (imagere2 - imagere2.min()) * 255 / (imagere2.max() - imagere2.min())
            imagere2 = imagere2.astype(np.uint8)
            imagere1.append( imagere2.reshape(imahi, imaw, 3) )
        
        for i, image in enumerate(imagere1):
            plt.subplot(4, 15, int(i / 15) * 30 + i % 15 + 1)
            plt.imshow(cv2.cvtColor(imagesf[i].reshape(imahi, imaw,3), cv2.COLOR_BGR2RGB))
            plt.axis('off')
            plt.subplot(4, 15, int(i / 15) * 30 + ( i % 15 + 16 ))
            plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            plt.axis('off')
            
        plt.show()
    
    
    def error(self):
        imagesf = []
        
        for img in images:
            imagesf.append(img.flatten())

        imah = images[0].shape[0]
        imaw = images[0].shape[1]
        pca = PCA(n_components = 27)
        pca.fit(imagesf)
        imgtr=pca.transform(imagesf)
        imgi = pca.inverse_transform(imgtr)
        errorimage.clear()
        
        for i in range(30):
            imgre = imgi[i]
            imgre = (imgre - imgre.min()) * 255 / (imgre.max() - imgre.min())
            imgre = imgre.astype(np.uint8)
            mask = images[i]
            mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
            re = imgre.reshape(imah, imaw,3)
            re = cv2.cvtColor(re, cv2.COLOR_BGR2GRAY)
            err = np.sum((mask - re) ** 2)
            errorimage.append(int( math.sqrt(err) ))
        
        print(errorimage)
       
       
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())