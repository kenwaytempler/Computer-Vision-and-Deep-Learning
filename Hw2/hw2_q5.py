import numpy as np
import os
import re
import tkinter as tk
import cv2 as cv2
import matplotlib.pyplot as plt
from Q5UI import Ui_MainWindow
from tkinter import W, filedialog
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow.python.keras.models import Model
from tensorflow.keras.applications import ResNet50
from tensorflow.python.keras.layers import Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam 
image1 = []
images = []
filename = []


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        image1.clear()
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.control()

    def control(self):
        #self.ui.loadimage.clicked.connect(self.li)
        self.ui.showimage.clicked.connect(self.si)
        self.ui.pushButton_3.clicked.connect(self.sd)
        self.ui.pushButton_4.clicked.connect(self.build_model)
        self.ui.loadimage.clicked.connect(self.loadimage)
    
    def loadimage(self):
        global filename
        filename=QFileDialog().getExistingDirectory(self,"Load Folder")

    def sd(self):
        names = ['cat', 'dog']
        values = [5412, 10788]
        plt.figure(figsize=(7, 7))
        plt.subplot(111)
        plt.bar(names, values)
        #plt.xticks(values[0],values[1])
        plt.ylabel("number of images")
        for index, value in enumerate(values):
            plt.text(index, value, str(value))
        plt.show()
        return

    def si(self):

        image_size = (224, 224)
        batch_size = 2

        train_ds = tf.keras.preprocessing.image_dataset_from_directory(
            filename,
            validation_split=0.2,
            subset="training",
            seed=1337,
            image_size=image_size,
            batch_size=batch_size,
        )
        
        plt.figure(figsize=(10, 5))
        for images, labels in train_ds.take(2):
            for i in range(batch_size):
                plt.subplot(1, 2, i + 1)
                plt.imshow(images[i].numpy().astype("uint8"))
                if(i==0):plt.title("cat")
                if(i==1):plt.title("dog")
                plt.axis("off")
        plt.show()

    
    def build_model(preModel=ResNet50, num_classes=2):   
        FREEZE_LAYERS = 2
        net = ResNet50(include_top=False, weights='imagenet', input_tensor=None,input_shape=(224,224,3))
        x = net.output
        output_layer = Dense(1, activation='sigmoid', name='sigmoid')(x)
        net_final = Model(inputs=net.input, outputs=output_layer)
        print(net_final.summary())
        
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())