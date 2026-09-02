# 1，递归函数
# 1.1：含义：
# 如果一个函数在内部不调用其他函数，而是调用它本身的话，这个函数就叫做递归函数
# 1.2：条件
#     1：必须要有一个明确的结束条件 ————递归出口
#     2：每进行更深一次的递归，问题规模都要比上一次有所减少
#     3：相邻两次重复之间有紧密的联系
# 普通函数实现1-100累加和
# def add():
#     s = 0
#     for i in range(1,101):
#         s += i
#     print(s)
# add()
# 递归函数实现累加和
# def add2(n):
#     if n == 1:     ***明确的结束条件
#         return 1
#     return n + add2(n-1)
# print(add2(100))
# 斐波那契数列
# 1，1，2，3，5，8，13
# def funa(n):
#     if n == 1 or n ==2:
#         return 1
# # 判断结束条件还可以：
#     if n <= 1:
#         return n
#     return funa(n-2) + funa(n-1)
# print(funa(3))
# 1.3：优点：
# 简洁，逻辑清晰，解题更具有思路
# 1.4：缺点：
# 使用递归函数时需要反复调用函数，耗内存，效率低

# 2，闭包
# 2.1：条件：
#     1：函数嵌套（函数里面再定义函数）
#     2：内层函数使用外层函数的局部变量
#     3：外层函数的返回值是内层函数的函数名
# def outer():     #外层函数
#     n = 10     #外层函数的局部变量
#     def inner():     #内层函数
#         print(n)     #内层函数调用外层函数的局部变量
#     return inner     #外层函数的返回值是内层函数的变量名
# print(outer())     #返回的是内部函数的内存地址
# 第一种调用写法：
# outer()()
# 第二种调用写法：
# ot = outer()
# ot()
# 2.2：函数引用
# def funa():
#     print(123)
# print(funa)     #函数名里面保存了函数名所在地址的引用
# id（）：判断两个变量是否为同一个值的引用
# a = 1   a只不过是一个变量名，存的是1这个数值所在的地址，就是a里面存了数值1的引用（类似于指针）
# def test():
#     print('这是test函数')
# te = test
# te()    # ***通过引用调用函数
# 2.3：内次开启内函数时，都在使用同一个闭包变量
# def outer(m):
#     print('这是外函数中的变量：',m)
#     def inner(n):
#         print('这是内函数中的变量：',n)
#         return m+n
#     return inner
# ot = outer(10)
# # 第一次调用内函数
# print(ot(10))
# # 第二次调用内函数
# print(ot(20))
# 总结：在使用闭包的过程中，一旦外函数被调用了一次，返回了内函数的引用，虽然每次调用内函数，会开启一个函数，执行后消亡
#      但是实际上闭包变量只有一份，每次开启内函数都在使用同一份闭包变量

# 3，装饰器
# def test2():
#     print('来袭')
# def test1(fn):
#     print('开始注册')
#     print('登录')
#     fn()
# test1(test2)
# 3.1：作用：在不改变原有代码的情况下给函数添加新功能
# 3.2：条件：
#     1：不修改原程序或函数的代码
#     2：不改变原程序或函数的调用方法
# 3.3：含义
# 装饰器本质上就是一个闭包函数，它可以在不修改原代码的情况下增添新功能
# 3.4：标准版装饰器
# 被装饰的函数
# def send():
#     print('发送消息')
# def outer(fn):      #***fn是形参，但是往里面传的是被装饰的函数名
#     # 在内函数中即包含原有功能，又包含新功能
#     def inner():
#         print('登录。。。')
#         fn()
#     return inner
# ot = outer(send)
# ot()
# 装饰器的原理就是将原有的函数名重新定义为以原函数为参数的闭包
# def add(a,b):
#     return a+b
# def outer(fn):
#     def inner(a,b):
#         result = fn(a,b)
#         new = a*b
#         return new,result
#     return inner
# ot = outer(add)
# print(ot(4,3))
# 3.5：语法糖
# 格式：@装饰器名称
# def outer(fn):
#     def inner():
#         print('登录。。。')
#         fn()
#     return inner
# # 注意：装饰器函数后面不要加（），否则就变成了调用装饰器函数
# @outer
# def send():
#     print('发送消息')
# send()
# def outer(fn):
#     def inner(a,b):
#         result = fn(a,b)
#         new = a*b
#         return new,result
#     return inner
# @outer
# def add(a,b):
#     return a+b
# print(add(3,4))
# 3.6：被装饰的函数有参数
# def outer(fn):
#     def inner(name):
#         print(f'{name}是内函数中的参数')
#         fn(name)
#     return inner
# @outer
# def func(name):
#     print('这是被装饰的函数')
# func('wen')
# 3.7：多个装饰器
# 第一个装饰器
# def deco1(fn):
#     def inner():
#         return '哈哈哈' + fn() + '呵呵呵'
#     return inner
# 第二个装饰器
# def deco2(fn):
#     def inner():
#         return '奈斯' + fn() + '不赖不赖'
#     return inner
# @deco1
# @deco2
# def test1():
#     return '晚上在学习python基础'
# print(test1())
# 多个装饰器的装饰过程：离函数最近的函数先装饰，然后外面的装饰器再装饰，由内而外的装饰过程