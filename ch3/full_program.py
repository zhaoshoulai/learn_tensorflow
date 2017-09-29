# -*- coding: utf-8 -*-

# @Time    : 2017/9/25 9:09
# @Author  : zhaosl
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import tensorflow as tf
from numpy.random import RandomState

# 定义训练数据batch的大小
batch_size = 8

# 定义神经网络的参数，两层结构每层的输入：w1和w2
w1 = tf.Variable(tf.random.normal([2,3], stddev=1,seed=1))
w2 = tf.Variable(tf.random.normal([3,1], stddev=1,seed=1))

x = tf.placeholder(tf.float32, shape=(None,2),name='x-input')
y_ = tf.placeholder(tf.float32, shape=(None,1),name='y-input')

# 定义神经网络前向传播过程
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

# 定义损失函数和反向传播过程
