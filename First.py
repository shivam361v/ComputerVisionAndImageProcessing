# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

img = cv2.imread('C:\\Users\\SHIVAM VISHWAKARMA\\OneDrive\\Pictures\\Saved Pictures\\MANITLogo.png', -1);
img = cv2.resize(img, (500, 500));
cv2.imshow('FirstImage', img);

key = cv2.waitKey();

if key == ord("s"):
    cv2.imwrite("D:\Projects\IP+CV\\manit.jpg", img);
    cv2.destroyAllWindows();
else:
    cv2.destroyAllWindows();