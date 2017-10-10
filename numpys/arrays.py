# -*- coding: utf-8 -*-

# @Time    : 2017/9/22 9:33
# @Author  : zhaosl
import sys

"""
reload(sys)
sys.setdefaultencoding('utf-8')
"""

import numpy as np

# 一个numpy数组是一个由不同数值组成的网格。
# 网格中的数据都是同一种数据类型，可以通过非负整型数的元组来访问。
# 维度的数量被称为数组的阶，数组的大小是一个由整型数构成的元组，可以描述数组不同维度上的大小。

a = np.array([1, 2, 3])

print(type(a))
print(a.shape)

a[0] = 5 # 赋值
print(a[0])

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.shape)

