# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 19:46:51 2016

@author: aditya vora
"""
from __future__ import division

import numpy as np
import scipy.stats as st


"""
bilateralFilter function implements the bilateral filtering algorithm as described 
in the paper: 
[1] Tomasi, Carlo, and Roberto Manduchi. "Bilateral filtering for gray and color images." 
    Computer Vision, 1998. Sixth International Conference on. IEEE, 1998.
bilateral filter are edge preserving filter which do not smooth across the edges
of the image like conventional filters like local averaging or gaussian filter. 

Takes three parameter as input: 
kernel_size: kernel window for filtering operation
space sigma parmeter: increasing spatial sigma parameter smooths larger features
range sigma parameter: increasing the range sigma parameter makes it closure to gaussian blur.
"""



def gaussian_kernel(kernal_size, sigma):
    interval = (2*sigma+1.)/(kernal_size)
    x = np.linspace(-sigma-interval/2., sigma+interval/2., kernal_size+1)
    kern1d = np.diff(st.norm.cdf(x))
    kernel_raw = np.sqrt(np.outer(kern1d, kern1d))
    kernel = kernel_raw/kernel_raw.sum()
    return kernel

def bilateralFilter(image, K, ksig):
    ss = ksig[0]
    sr = ksig[1]
    G = gaussian_kernel(2*K+1, ss)
    dimI = image.shape
    out = np.zeros(dimI)
    for i in range(dimI[0]):
        for j in range (dimI[1]):
            imin = max(i-K, 1);
            imax = min(i+K, dimI[0]);
            jmin = max(j-K, 1);
            jmax = min(j+K, dimI[1]);
            region = image[imin:imax, jmin:jmax]
            H = np.exp(-(region-image[i,j])**2/(2*(sr**2)));
            F = H*G[imin-i+K+1:imax-i+K+1,jmin-j+K+1:jmax-j+K+1];
            out[i,j] = sum(np.array(F).flatten()*np.array(region).flatten())/sum(np.array(F).flatten());
    return out