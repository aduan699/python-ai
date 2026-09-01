# 1，函数
# 1.1：含义：将独立的代码块组织成一个整体，使其成为具有特殊功能的代码集
# 1.2：作用：提高代码的复用性，使代码看上去更简练
# 1.3：基本格式
# （1）定义函数
# def 函数名（）：
#     函数体
# （2）调用函数
# 函数名（）
# def morning():
#     print('早上好啊bb')
# def afternoon():
#     print('下午好啊bb')
# def evening():
#     print('晚上好啊bb')
# def night():
#     print('大晚上的让不让人休息了')
# a = int(input('现在几点了：'))
# if 6<= a <12:
#     morning()
# elif 12<= a <18:
#     afternoon()
# elif 18<= a <24:
#     evening()
# else:
#     night()

# 2,返回值 return
# 函数执行结束后最后给调用者的结果
# 作用：
# （1）return会给函数的执行者返回值
# （2）函数中遇到return，表示此函数结束了，不会继续执行
# def buy():
#     return "一桶水果茶",20    ***return返回多个值，以元组的形式返回
#     return 20               ***return下面的代码不会执行
# print(buy())
# ***return和print的区别
#     1，return表示此函数已经结束，而print会一直执行
#     2，return是返回计算值，print是返回打印结果

# 3，参数
# 3.1:形参&实参
# 定义格式：
# def 函数名（形参1，形参2）：
#     函数体
# 调用格式：
# 函数名（实参a，实参b）
# def add(a,b):
#     return a+b
# print(add(1,5))
# 3.2：函数参数
# 3.2.1：必备参数（位置参数）
# 含义：传递和定义参数的顺序以及个数必须一致
# 3.2.2：默认参数
# 含义：为参数提供默认值，调用函数时可以不传该参数的值
# 注意：所有的位置参数都必须出现在默认参数前，包括函数的定义和调用
# 3.2.3：可变参数
# 含义：传入的值的数量是可以改变的，可以传入多个，也可以不传
# 格式：def func（*args）     ***必须在位置参数前面加上*，args是约定俗成的不是必须的
# def func(*args):
#     print(args)
# func(1,2)          ***以元组的形式接收
# 3.2.4：关键字参数
# 格式：def func(**kwargs)
# def func(**kwargs):
#     print(kwargs)
#     print(type(kwargs))   #***返回字典
# func()
# func(name = 'bingbing',age = 18)   ***传值的时候，需要以键=值的形式去传
# 作用：可以扩展函数的功能

# 4，函数嵌套
# 4.1：嵌套调用
# 含义：在一个函数里面调用另外一个函数
# def study():
#     print('晚上在学习')
# def course():
#     study()                ***在course（）内调用study（）
#     print('python基础')
# study()
# course()
# 4.2：嵌套定义
# 含义：在一个函数里面定义另外一个函数
# def study():
#     print('晚上在学习',end = '')
#     def course():
#          print('python基础')    # ***不要在内层函数中调用外层函数，否则会陷入死循环
#     course()
# study()
