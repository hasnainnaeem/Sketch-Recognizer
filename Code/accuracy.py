# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 20:45:54 2019

@author: bushra
"""
#Comment: Use the following code to test your results
import csv
from sklearn.metrics import accuracy_score

#truelabel_csv = Enter the complete path to the .csv file containing test images ids and their actual class labels
#predlabel_csv = Enter the complete path to the .csv file containing test images ids and their predicted class labels

truelabel=[]
predlabel=[]

with open(truelabel_csv, "r") as f:
    reader = csv.reader(f)
    true=list(reader)
with open(predlabel_csv, "r") as f1:
    reader1 = csv.reader(f1)
    pred=list(reader1)
for x in range(len(pred)):
    for x1 in range(len(true)):
        data=true[x1][0]
        p=pred[x][0]
        if(data==p):
            truelabel.append(true[x1][1])
            predlabel.append(pred[x][1]) 

accuracy = accuracy_score(truelabel, predlabel, normalize = False) 
print(accuracy*100)        




    
         




    
    