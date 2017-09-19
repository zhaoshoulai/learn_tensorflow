# -*- coding: utf-8 -*-
import sys
import tensorflow as tf

reload(sys)
sys.setdefaultencoding('utf-8')

# 定义常量
a = tf.constant([1.0, 2.0], name='a')
b = tf.constant([2.0, 3.0], name='b')

result = a + b

print a.graph is tf.get_default_graph()
print result

# 定义一个计算图
g1 = tf.Graph()

# 在g1计算图中定义一个变量v
with g1.as_default():
    v = tf.get_variable("v", shape=[2, 2], initializer=tf.zeros_initializer())

# 指定g1使用设备cpu:0运行
with g1.device('/cpu:0'):
    with tf.Session(graph=g1) as sess:
        tf.initialize_all_variables().run()
        with tf.variable_scope('', reuse=True):
            print sess.run(tf.get_variable('v'))

# 计算模型 -- graph
# 数据模型 -- tensor
# 运行模型 -- session
