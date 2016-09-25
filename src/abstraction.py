# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 19:54:25 2016

@author: aditya vora
"""
from __future__ import division
import cv2
import numpy as np
"""
This script contains two function i.e. quantize and detectEdge. 
quantize: quantizes the image pixel values to the quantization level passed as
          input argument
detectEdge: detects edges in the image. The effect can be controled by passing 
            phiE, sigmaE and T as arguments
"""


def quantize(image, q_level):
    im_shape = image.shape
    for j in range(im_shape[1]):
        for i in range(im_shape[0]):
            if image[i,j] > 0 and image[i,j] <=10:
                image[i,j] = q_level
            elif image[i,j] > 10 and image[i,j] <= 20:
                image[i,j] = 2*q_level
            elif image[i,j] > 20 and image[i,j] <= 30:
                image[i,j] = 3*q_level
            elif image[i,j] > 30 and image[i,j] <= 40:
                image[i,j] = 4*q_level
            elif image[i,j] > 40 and image[i,j] <= 50:
                image[i,j] = 5*q_level
            elif image[i,j] > 50 and image[i,j] <= 60:
                image[i,j] = 6*q_level
            elif image[i,j] > 60 and image[i,j] <= 70:
                image[i,j] = 7*q_level
            elif image[i,j] > 70 and image[i,j] <= 80:
                image[i,j] = 8*q_level
            elif image[i,j] > 80 and image[i,j] <= 90:
                image[i,j] = 9*q_level
            elif image[i,j] > 90 and image[i,j] <= 100:
                image[i,j] = 10*q_level
    return image
    
def detectEdge(I, sigE, T, phiE):
    I1 = cv2.GaussianBlur(I, (5,5), sigE)
    I2 = cv2.GaussianBlur(I, (5,5), np.sqrt(1.6)*sigE)
    out = (I1 - T*I2)
    out_shape = out.shape
    for j in range(out_shape[1]):
        for i in range(out_shape[0]):
            if out[i,j] > 0:
                out[i,j] = 1
            elif out[i,j] <= 0:
                out[i,j] = 1+np.tanh(phiE*out[i,j])
    return out