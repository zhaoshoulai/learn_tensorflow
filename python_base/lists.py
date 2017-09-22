# -*- coding: utf-8 -*-

# @Time    : 2017/9/21 9:21
# @Author  : zhaosl
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# 列表 类型可以不同

xs = [2,3,4]
xs[2] = 'foo' # 赋值
print xs[2]
xs.append('bar') # 添加元素
print xs
# Remove and return the last element of the list
item = xs.pop()
print xs,item

# 列表支持切片(查询，赋值，修改)

xs.append(3)
xs.append(4)

print xs[0:2] # Get a slice from index 0 to 2(排除)
print xs[:-1] # 从0到倒数第一个
print xs[-1]  # 倒数第一个

xs[2:4] = [8,9]
print xs

# 循环
for item in xs:
    print item

# 循环并访问索引 enumerate 枚举
for index,item in enumerate(xs):
    print index,item

# 列表推导
nums = range(5)
squares = [x ** 2 for x in nums]
print squares

# 列表推导 带条件
squares = [x ** 2 for x in nums if x % 2 == 0]
print squares