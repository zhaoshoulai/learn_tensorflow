# -*- coding: utf-8 -*-

# @Time    : 2017/9/22 9:18
# @Author  : zhaosl
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# object 是被继承的类 Inheritance
class Greeter(object):

    # Constructor
    def __init__(self, name):
        self.name = name  # Create an instance variable

    # Instance method
    def greet(self, loud=False):
        if loud:
            print 'HELLO, %s!' % self.name.upper()
        else:
            print 'Hello, %s' % self.name

g = Greeter('Fred')  # Construct an instance of the Greeter class
g.greet()            # Call an instance method; prints "Hello, Fred"
g.greet(loud=True)   # Call an instance method; prints "HELLO, FRED!"