# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 20:30:28 2016

@author: vision
"""
from __future__ import division
import cv2
from src.bilateralfilter import bilateralFilter
from src.abstraction import quantize, detectEdge
from scipy.misc import imresize
import numpy as np
"""
cartoonize: implements the entire abstraction algorithm. 
"""

def normalize_lab(image_lab):
    return image_lab[:,:,0]*(100/255)

def cartoonize(image_path, kernel_size=5, kernel_sigma=[3,2], q_level=10, sigmaE=0.5, phiE=1.0, T=0.99):
    image = cv2.imread(image_path)
    image = imresize(image, 0.5)
    shape = image.shape
    cv2.imshow('original image', image)
    cv2.waitKey()
    cv2.destroyAllWindows()     
    print "The original image dimension: %dx%dx%d"%(shape[0], shape[1], shape[2])
    image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    image_l = normalize_lab(image_lab)
    counter = 0
    print "Applying bilateral filter..."  
    
    while counter<2:    
        image_l = bilateralFilter(image_l, kernel_size, kernel_sigma)
        counter += 1
    counter = 0
    I1 = quantize(image_l, q_level)
    print "image quantized."
    print "Applying bilateral filter..."
    while counter<2: 
        image_l = bilateralFilter(image_l, kernel_size, kernel_sigma)
        counter += 1
    I2 = detectEdge(image_l, sigmaE, T, phiE)
    print "edges in the images detected."
    print "creating final image..."
    out = np.multiply(I1,I2)
    out_final = np.empty(shape, dtype=np.uint8)
    out_final[:,:,0] = out
    out_final[:,:,1] = image_lab[:,:,1]
    out_final[:,:,2] = image_lab[:,:,2]
    return cv2.cvtColor(out_final, cv2.COLOR_LAB2BGR)
