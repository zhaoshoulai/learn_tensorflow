# -*- coding: utf-8 -*-

# @Time    : 2017/9/21 9:43
# @Author  : zhaosl
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

d = {'cat': 'cute', 'dog': 'furry'}  # Create a new dictionary with some data
print d['cat']       # Get an entry from a dictionary; prints "cute"
print 'cat' in d     # Check if a dictionary has a given key; prints "True"
d['fish'] = 'wet'    # Set an entry in a dictionary
print d['fish']      # Prints "wet"
# print d['monkey']  # KeyError: 'monkey' not a key of d
print d.get('monkey', 'N/A')  # Get an element with a default; prints "N/A"
print d.get('fish', 'N/A')    # Get an element with a default; prints "wet"
del d['fish']        # Remove an element from a dictionary
print d.get('fish', 'N/A') # "fish" is no longer a key; prints "N/A"



d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:  # 这样遍历的是key
    legs = d[animal]
    print 'A %s has %d legs' % (animal, legs)
    # Prints "A person has 2 legs", "A spider has 8 legs", "A cat has 4 legs"

# 遍历key 和 value  iteritems 效率高  items 效率没有这个高
d = {'person': 2, 'cat': 4, 'spider': 8}
for animal, legs in d.iteritems():
    print 'A %s has %d legs' % (animal, legs)
    # Prints "A person has 2 legs", "A spider has 8 legs", "A cat has 4 legs"

# 移除字典数据pop()方法的作用是：删除指定给定键所对应的值，返回这个值并从字典中把它移除。
# 注意字典pop()方法与列表pop()方法作用完全不同。
print d.pop('person')  # --2
print d.popitem()  # 随机删除一项 效率很高
print d.clear()  # 清除所有元素
