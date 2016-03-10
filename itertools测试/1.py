#! /usr/bin/env python
#coding=utf-8

'''
Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
'''

import itertools


#count()会创建一个无限的迭代器:
tmp_count = itertools.count()
print next(tmp_count)
print next(tmp_count)
print next(tmp_count)


#cycle()会把传入的一个序列无限重复下去：
cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
for c in cs:
	print c


#repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
ns = itertools.repeat('A', 10)
for n in ns:
	print n


#通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
for n in ns:
	print n

#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
for c in chain('ABC', 'XYZ'):
	print c


#-----------------------------开始-----------------------------------#
#groupby()把迭代器中相邻的重复元素挑出来放在一起:
for key, group in itertools.groupby('AAABBBCCAAA'):
	print key, list(group) # 为什么这里要用list()函数呢？

'''
#结果:
A ['A', 'A', 'A']
B ['B', 'B', 'B']
C ['C', 'C']
A ['A', 'A', 'A']
'''

#实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
	print key, list(group)


'''
#结果:
A ['A', 'a', 'a']
B ['B', 'B', 'b']
C ['c', 'C']
A ['A', 'A', 'a']
'''
#-----------------------------结束-----------------------------------#


#-----------------------------开始-----------------------------------#
'''
#--- imap()
#--- imap()和map()的区别在于，imap()可以作用于无穷序列，并且，如果两个序列的长度不一致，以短的那个为准。
'''
for x in itertools.imap(lambda x, y: x * y, [10, 20, 30], itertools.count(1)):
	print x
'''
#结果:
10
40
90
'''

'''
#--- 注意imap()返回一个迭代对象，而map()返回list。当你调用map()时，已经计算完毕
#--- 当你调用imap()时，并没有进行任何计算
'''
r = map(lambda x: x*x, [1, 2, 3])
r # r已经计算出来了
'''
#结果:
[1, 4, 9]
'''

r = itertools.imap(lambda x: x*x, [1, 2, 3])
r 	# r只是一个迭代对象
'''
#结果:
<itertools.imap object at 0x103d3ff90>
'''

#必须用for循环对r进行迭代，才会在每次循环过程中计算出下一个元素：
for x in r:
	print x
'''
#结果:
1
4
9
'''

'''
#--- 这说明imap()实现了“惰性计算”，也就是在需要获得结果的时候才计算。类似imap()这样能够实现惰性计算的函数就可以处理无限序列：
'''
r = itertools.imap(lambda x: x*x, itertools.count(1))
for n in itertools.takewhile(lambda x: x<100, r):
	print n

'''
结果是什么?
如果把imap()换成map()去处理无限序列会有什么结果？
'''
r = map(lambda x: x*x, itertools.count(1))

ifilter()

不用多说了，ifilter()就是filter()的惰性实现。