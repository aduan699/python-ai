# 1:可迭代对象   Tterable
# 遍历（迭代）：依次从对象中取出一个个对象的过程

# 1.2：可迭代对象的条件
# 1：对象可以实现__iter__()方法
# 2：__iter__()方法返回了迭代器对象

# 1.3：for循环的工作原理
# 1：先通过__iter__()获取可迭代对象的迭代器
# 2：对获取到的迭代器不断调用__next__()方法来获取下一个值并将其赋值给临时变量i

# 1.4：isinstance()：判断一个对象是否是可迭代对象或者是已知的数据类型
# 导入模块
# from collections.abc import Iterable
# isinstance(o,t)    o：对象   t：类型
# print(isinstance('123',(int,Iterable)))

# 2：迭代器   Iterator
# 是一个可以记住遍历位置的对象，在上次停留的位置继续做事情
# li = [1,2,3,4,5]
# for i in li:
#     print(i)
# iter()：获取可迭代对象的迭代器
# next()：一个个取元素，取完元素会引发一个异常
# li  = [1,2,3,4,5]
# 创建迭代器对象
# li2 = iter(li)
# li2 = li.__iter__()
# print(li2)
# 获取下一条数据
# print(next(li2))
# print(next(li2))
# print(next(li2))
# print(next(li2))
# print(next(li2))
# print(li2.__next__()) 
# 3：取完元素后再调用next()会引发报错：StopIteration
# print(next(li2))

# 步骤：
# 1：iter()：调用对象的__iter__()这个魔法方法，把__iter__()的返回结果作为自己的返回值
# 2：next()：调用对象的__next__()这个魔法方法，一个个取元素
# 3：所有元素取完了，__next__()将引发报错StopIteration

# 2.2：可迭代对象Iterable和迭代器Iterator
# 凡是可以作用于for循环的对象就是可迭代对象
# 凡是可以作用于next()的都是迭代器
# from collections.abc import Iterable,Iterator
# name = 'bingbing'
# print(isinstance(name,Iterable))     #True
# print(isinstance(name,Iterator))     #False
# # 说明可迭代对象不一定是迭代器对象
# name2 = iter(name)
# print(isinstance(name2,Iterable))    #True
# print(isinstance(name2,Iterator))    #True
# print(dir(name))
# print(dir(name2))
# 说明迭代器对象一定是可迭代对象
# 总结：
# 1：可迭代对象可以通过iter()方法转换成迭代器对象
# 2：如果一个对象有__iter__()方法，那么他就是可迭代对象，如果一个对象同时有__iter__()方法和__next__()方法，
#    那么他就是迭代器对象
# 3：dir()：查看对象中的所有属性和方法

# 2.3：迭代器协议

# 2.4：自定义迭代器类
# 两个特性：__iter__()和__next__()
# class MyIterator(object):
#     def __init__(self):
#         self.num = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.num == 10:
#             raise StopIteration('终止迭代，数据已经取完了')
#         self.num += 1
#         return self.num
# mi = MyIterator()
# # print(mi)
# # print(next(mi))
# for i in mi:
#     print(i)

# 3：生成器    generator
# python中一边循环一边计算的机制叫做生成器
# 3.1：生成器表达式
# li = [i*5 for i in range(5)]
# gen = (i*5 for i in range(5))     #列表推导式的[]变成()就变成了生成器表达式
# print(li)
# print(gen)

# 3.2：生成器函数
# python中，使用了yield关键字的函数就称之为生成器函数
# yield的作用：
# 1：类似于return,将一个值或者多个值返回给调用者
# 2：yield语句一次返回一个结果，在每个结果中间，挂起函数；当执行next()时，再重新从挂起点继续往下执行
# 生成器函数
# def gen():
#     print('开始了')
#     yield 'a'          #返回了一个a，并且暂停了函数，在此处挂起了，下一次再执行的时候从这里继续执行
#     yield 'b'
#     yield 'c'
# gen1 = gen()
# print(gen1)
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# def gen2(n):
#     li = []
#     for i in range(n):
#         li.append(i)
#         yield i
#     # i = 0
#     # while  i < n:
#     #     li.append(i)
#     #     i += 1
#     print(li)
# for i in gen2(6):
#     print(i)

# 4:三者关系
# 可迭代对象：指实现了python的迭代协议，可以通过for循环遍历的对象，也包括了迭代器和生成器
# 迭代器：可以记住自己遍历位置的对象，直观体现就是可以使用next()函数返回值，迭代器对象只能取下一个值
#        不能取上一个值，当遍历完毕后，next()会抛出异常StopIteration
# 生成器：是一种特殊的迭代器，它是python中提供的简便的写出迭代器的一种手段
# 包含关系：可迭代对象包含了迭代器，迭代器里面又包含了生成器