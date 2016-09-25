# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 16:43:25 2016

@author: aditya vora
"""
from __future__ import division
import argparse
import cv2
from src.cartoon import cartoonize
"""
The code implements the image abstraction technique that is described in the 
paper of real time video abstraction: 
[1] Winnemöller, Holger, Sven C. Olsen, and Bruce Gooch. "Real-time video abstraction." 
    ACM Transactions On Graphics (TOG). Vol. 25. No. 3. ACM, 2006.

The code consists of 3 modules: 
1) cartoonize: which implements the entire algorithm 
2) bilateralfilter: for bilateral filtering of the image
3) abstraction: which consists of functions that quantize the image as well detect edges in the image

USAGE: 
The python script main.py can be run by passing proper command line arguments. 
image_path - path where the image is stored
kernel size - kernel size of the bilateral filter
kernel sigma - space and range parameters of the bilateral filter
quantization level - level to thresold the image
sigmaE - spatial scale for edge detection
phiE - controls the sharpness of the activation cutoff
T - determines the sensitivity of the edge detector. 
"""   
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("image_path", help="location where the image is stored")
    parser.add_argument("--kernel_size", help="kernel size of the bilateral filter", type=int, default=5)
    parser.add_argument("--kernel_sigma", help="space and range parameters for the bilateral filter", default=[3,2])
    parser.add_argument("--q_level", help="quantization level to thresold the image",type=int,default=10)
    parser.add_argument("--sigmaE", help="determines the spatial scale for edge detection", type=float, default=0.5)
    parser.add_argument("--phiE", help="controls the sharpness of the activation cutoff", type=float, default=1.0)
    parser.add_argument("--T", help="determines the sensitivity of the edge detector", type=float, default=0.99)
    args = parser.parse_args()
    kwargs = vars(args).copy()    
    del kwargs['image_path']
    out_final = cartoonize(args.image_path, **kwargs)
    cv2.imshow('result', out_final)
    cv2.waitKey()
    cv2.destroyAllWindows()    
    
    
if __name__ == "__main__":
    main()