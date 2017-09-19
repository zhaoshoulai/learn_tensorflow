# -*- coding: utf-8 -*-
import sys
import tensorflow as tf

reload(sys)
sys.setdefaultencoding('utf-8')

# 所有变量  持久化TensorFlow时用
print tf.GraphKeys.VARIABLES

# 可学习的变量
print tf.GraphKeys.TRAINABLE_VARIABLES

# 日志生成相关的张量， 计算可视化
print tf.GraphKeys.SUMMARIES

# 处理输入的QueueRunner
print tf.GraphKeys.QUEUE_RUNNERS

# 所有计算了滑动平均值的变量
print tf.GraphKeys.MOVING_AVERAGE_VARIABLES
