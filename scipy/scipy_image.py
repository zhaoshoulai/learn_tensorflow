# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     scipy_image
   Description :
   Author :       qzhd
   Date：          2017/10/10
-------------------------------------------------
   Change Activity:
                   2017/10/10:
-------------------------------------------------
"""
__author__ = 'qzhd'

from scipy.misc import imread, imsave, imresize

img = imread('id.jpg')
print(img.shape)

img2 = img * [0.5, 1, 0.5]

img2 = imresize(img2,(500, 1000))
imsave('id2.jpg', img2)

