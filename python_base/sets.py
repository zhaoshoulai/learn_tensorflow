# -*- coding: utf-8 -*-

# @Time    : 2017/9/22 9:08
# @Author  : zhaosl
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

animals = {'cat', 'dog'}
print 'cat' in animals   # Check if an element is in a set; prints "True"
print 'fish' in animals  # prints "False"

# 添加元素
animals.add('fish')      # Add an element to a set
print 'fish' in animals  # Prints "True"
print len(animals)       # Number of elements in a set; prints "3"
animals.add('cat')       # Adding an element that is already in the set does nothing
print len(animals)       # Prints "3"
animals.remove('cat')    # Remove an element from a set
print len(animals)       # Prints "2"


# 循环Loops：在集合中循环的语法和在列表中一样，但是集合是无序的，
# 所以你在访问集合的元素的时候，不能做关于顺序的假设
animals = {'cat', 'dog', 'fish'}
for idx, animal in enumerate(animals):
    print '#%d: %s' % (idx + 1, animal)

# 集合推到和 list一样 只不过是{}
from math import sqrt
nums = {int(sqrt(x)) for x in range(30)}
print nums  # Prints "set([0, 1, 2, 3, 4, 5])"