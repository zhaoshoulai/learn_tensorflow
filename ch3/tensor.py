# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import tensorflow as tf

config = tf.ConfigProto(allow_soft_placement=True, log_device_placement=True)

g = tf.Graph()

with g.as_default():
    a = tf.get_variable('a', shape=(5, 8), initializer=tf.ones_initializer())


# 下面这样写是有问题的，还不知道问题在哪里
#sess = tf.Session(config=config, graph=g)
#with sess.as_default():
    #tf.initialize_all_variables().run()
    #with tf.variable_scope('', reuse=True):
        #print (tf.get_variable('a').eval(session=sess))

# 嵌套顺序还是不太明白  这几个with
with tf.Session(config=config, graph=g) as sess:
    tf.initialize_all_variables().run()
    with tf.variable_scope('', reuse=True):
        with g.device('/gpu:0'):
            print (tf.get_variable('a').eval())
