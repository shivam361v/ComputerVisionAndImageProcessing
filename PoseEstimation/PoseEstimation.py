# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 11:26:29 2024

@author: SHIVAM VISHWAKARMA
"""

import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(r'D:\Projects\ComputerVisionAndImageProcessing\PoseEstimation\Workout.mp4')

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1000, 500))
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)