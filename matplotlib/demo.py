# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     demo
   Description :
   Author :       qzhd
   Date：          2017/10/10
-------------------------------------------------
   Change Activity:
                   2017/10/10:
-------------------------------------------------
"""
__author__ = 'qzhd'

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.subplot(2,2,4)
plt.plot(x,y_cos)
plt.title('Cos')

plt.subplot(1,2,1)
plt.plot(x,y_sin)
plt.title('Sine')



plt.show()

