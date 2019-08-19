# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 12:06:31 2019

@author: Momina Moetesum
"""
#Comment: Currently used libraries. Add any if required....

import os
import cv2
import random
import pandas as pd
import numpy as np
from keras.preprocessing.image import img_to_array
from imutils import paths

#Uncomment following incase image resizing is required due to computational requirements.....Value can be modified accordingly....

#image_height = 30   
#image_width = 30    
#channel = 3            #For RGB images, 1 for greyscale images
#input_imageShape = (image_height, image_width, channel) 
#input_imageSize = (image_height, image_width)        

def load_data(image_dir, csv_filename):
    image_data = []
    class_labels = []    
    imagePaths = sorted(list(paths.list_images(image_dir)))             #To load images from the respective folder
    df = (pd.read_csv(csv_filename, header = None, index_col = False))  #To read class labels from .csv file
    random.seed(42)                                                     #Seed value can be modified accordingly
    random.shuffle(imagePaths)
    print("[INFO] loading images and class labels...")
    for imagePath in imagePaths:
        image = cv2.imread(imagePath)
        #image = cv2.resize(image, input_imageSize)    #Uncomment if required....
        image = img_to_array(image)
        image_data.append(image)    
        fullname = os.path.basename(imagePath)        #Complete image name with extension e.g. "1.png" etc.
        image_name = os.path.splitext(fullname)[0]    #Removing extension i.e. "1" etc.
        temp=df[df[0] == int(image_name)]             #Finding image name in respective .csv file
        label = temp.iloc[0,1]                        #Finding respective class label 
        class_labels.append(label)
    print("[INFO] Creating Numpy Arrays...")
    X = np.array(image_data)                        #Creating required Numpy array of images
    Y = np.array(class_labels)                      #Creating required Numpy array of class labels
    return X, Y

#######################################################################################################################
    
#Comment: Start from here ....(Uncomment the required statements....)
    
#image_dir = #Enter complete path to the folder {Training/Validation/Test} containing images
#csv_filename = #Enter complete name of the .csv file containing class labels
#(X, Y) = load_data(image_dir, csv_filename)
    
#######################################################################################################################
    
#Comment: Add you network code here ...
    
#######################################################################################################################

#Comment: To save predicted results with image names in a .csv file, uncomment the following statements

#######################################################################################################################
    
#test_dir = #Enter complete path of the folder containing test images here
#test_id=[]
#prediction=[]
#test_imagePaths = list(paths.list_images(test_dir))
#for imagePath in test_imagePaths:                                         #Loading each image one by one
#    images = cv2.imread(imagePath)
#    images = cv2.resize(images, input_imageSize)                          #Uncomment if resizing is required
#    images = img_to_array(images)
#    preds = model.predict_classes(np.expand_dims(images, axis=0))[0]      #Predicting class labels
#    prediction.append(preds)                                              
#    base = os.path.basename(imagePath)                                    
#    image_name = os.path.splitext(base)[0]                                #Image name without extension
#    test_id.append(image_name)
    
#prediction_df = pd.DataFrame(prediction, test_id)                         #Creating a dataframe of image names and predictions
#prediction_df.to_csv('prediction.csv', header=None)                       #Saving results in a .csv file

#######################################################################################################################

#Comment: To save the model and learned weights, uncomment the following statements

#######################################################################################################################
    
#model_json = model.to_json()
#with open('sketch_model.json','w') as json_file:                    
#    json_file.write(model_json)                                           #Saving model as json file

#model.save_weights('sketch_model.h5')                                     #Saving learned weights
