﻿'''
**************************************************************************
*                  IMAGE PROCESSING (e-Yantra 2014)
*                  ================================
*  This software is intended to teach image processing concepts
*
*  MODULE: Fundamentals
*  Filename: camVideo.py
*  Version: 1.0.0  
*  Date: November 3, 2014
*  
*  Author: Arun Mukundan, e-Yantra Project, Department of Computer Science
*  and Engineering, Indian Institute of Technology Bombay.
*  
*  Software released under Creative Commons CC BY-NC-SA
*
*  For legal information refer to:
*        http://creativecommons.org/licenses/by-nc-sa/4.0/legalcode 
*     
*
*  This software is made available on an “AS IS WHERE IS BASIS”. 
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using 
*  ICT(NMEICT)
*
**************************************************************************
'''
############################################
## Import OpenCV
import numpy as np
import cv2
# Initialize camera
cap = cv2.VideoCapture(0)
############################################
#cap.set(3,320)
#cap.set(4,240)
############################################
## Video Loop
while(1):
    
    ## Read the image
    ret, img = cap.read()
    #print img[320,240,:]
    #img = img[:,40:280,:]
    ## Do the processing
    cv2.imshow('image1',img)
    img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower = np.array([164,166,164])
    upper = np.array([255,255,255])
    mask = cv2.inRange(img_hsv,lower,upper)
    cv2.imshow('mask',mask)
    img_result = cv2.bitwise_and(img,img,mask=mask)
    gray = cv2.cvtColor(img_result,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    l= len(contours)
    if l > 0:
        print "red"
        break
    
    lower = np.array([126,76,255])
    upper = np.array([166,85,255])
    mask = cv2.inRange(img_hsv,lower,upper)
    cv2.imshow('mask',mask)
    img_result = cv2.bitwise_and(img,img,mask=mask)
    gray = cv2.cvtColor(img_result,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    l= len(contours)
    if l > 0:
        print "pink"
        break
    lower = np.array([45,100,100])
    upper = np.array([75,255,255])
    mask = cv2.inRange(img_hsv,lower,upper)
    cv2.imshow('mask',mask)
    img_result = cv2.bitwise_and(img,img,mask=mask)
    gray = cv2.cvtColor(img_result,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    l= len(contours)
    if l > 0:
        print "green"
        break
    lower = np.array([135,125,125])
    upper = np.array([155,255,255])
    mask = cv2.inRange(img_hsv,lower,upper)
    cv2.imshow('mask',mask)
    img_result = cv2.bitwise_and(img,img,mask=mask)
    gray = cv2.cvtColor(img_result,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    l= len(contours)
    if l > 0:
        print "blue"
        break
    lower = np.array([92,1119,142])
    upper = np.array([111,255,255])
    mask = cv2.inRange(img_hsv,lower,upper)
    cv2.imshow('mask',mask)
    img_result = cv2.bitwise_and(img,img,mask=mask)
    gray = cv2.cvtColor(img_result,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    l= len(contours)
    if l > 0:
        print "sky-blue"
        break
    '''gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    ret,thresh = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    l= len(contours)
    for i in range(0,l):
        if(cv2.arcLength(contours[i],True)>50 and cv2.arcLength(contours[i],True)<800 and cv2.contourArea(contours[i]) > 2000 and cv2.contourArea(contours[i])<12000 ):
            print "Area = ",i, cv2.contourArea(contours[i])
            #for i in range(0,l):
            #   if cv2.contourArea(contours[i]) > 2000:# and cv2.contourArea(contours[i])<2000:
            cv2.drawContours(img,contours[i],-1,(0,255,0),3)
            l= len(contours)
            for i in range(0,l):
                    if(cv2.arcLength(contours[i],True)>50 and cv2.arcLength(contours[i],True)<800 and cv2.contourArea(contours[i]) > 2000 and cv2.contourArea(contours[i])<12000 ):
                            print "Area = ",i, cv2.contourArea(contours[i])
                            M = cv2.moments(contours[i])
                            cx = int(M['m10']/M['m00'])
                            cy = int(M['m01']/M['m00'])
                            print "Centroid = ", cx, ", ", cy
                            cv2.circle(img,(cx,cy), 5, (0,0,255), -1)
                            print img[cx,cy,:]'''
            ############################################
            
    ## Do the processing
    
    ## Show the image
    cv2.imshow('image',img)

    ## End the video loop
    if cv2.waitKey(1) == 27:  ## 27 - ASCII for escape key
        break
############################################

############################################
## Close and exit
cap.release()
cv2.destroyAllWindows()
############################################
