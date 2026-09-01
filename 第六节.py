# 1，作用域
# 1.1：含义：指的是变量生效的范围，分为全局变量和局部变量两种
# 1.2：全局变量
# 含义：函数外部定义的变量，在整个文件中都是有效的
# a = 100
# def test1():
#     print('这是test1中a的值',a)
# def test2():
#     a = 120   ***此时的a时局部变量
#     print('这是test2中a的值',a)
# test1()
# test2()
# print(a)    ***a没有被覆盖是因为函数调用时会先从函数内部找变量，没有的话才会从外面找
# 1.3：局部变量
# 含义：函数内部定义的变量，从函数开始到函数结束有效
# 作用：在函数内部临时定义变量保存数据，函数调用结束后就会销毁数据
# ***想要在函数内部声明全局变量，可以使用关键字global
# 1.4：global
# 格式：global 变量名1，变量名2
# a = 100
# def test1():
#     print('这是test1中a的值',a)
# def test2():
#     global a
#     a = 120   ***此时a就变成了全局变量
#     print('这是test2中a的值',a)
# test1()
# test2()
# print(a)
# 1.5：nonlocal
# 作用：用来声明外层的局部变量，只能在嵌套函数中使用，在外部函数先进行声明，内部函数进行nonlocal声明
# 注意：nonocal只能对上一级进行修改，不是修改全部

# 2，匿名函数
# 2.1：基本语法
# 函数名 = lambda 形参 ： 返回值（表达式）
# 调用：结果 = 函数名（实参）
#    普通函数:
# def add(a,b):
#     return a+b
# print(add(1,3))
#    匿名函数:
# add = lambda a,b:a+b   ***a,b就是匿名函数的形参，a+b是匿名函数的返回值的表达式
# print(add(1,3))        ***匿名函数不需要写返回，表达式本身就是返回值
# 2.2：lambda的参数形式
# 2.2.1：无参数
# funa = lambda :'一桶水果茶'
# print(funa())
# 2.2.2:一个参数
# funb = lambda name:name
# print(funb('wen'))
# 2.2.3默认参数
# func = lambda name,age=18:(name,age)   ***返回值要以元组的形式
# print(func('bingbing'))
# print(func('biingbing',20))
# ***注意：默认参数必须写在非默认参数后面
# 2.2.4：关键字参数
# fund = lambda **kwargs:kwargs
# print(fund(name='bingbing',age=18))
# 2.3:lambda结合if判断
# a = 8
# b = 5
# ***三目运算：为真的结果 if 条件 else 为假的结果
# print('a比b大') if a>b else print('a小于等于b')
# comp = lambda a,b : 'a比b大' if a>b else 'a小于等于b'
# print(comp(5,8))
# 2.4：lambda的特点
# lambda只能实现简单的逻辑运算，如果逻辑复杂且代码量大，不建议使用lambda，降低代码的可读性

# 3，内置函数
# 3.1：查看所有的内置函数
# import builtins
# print(dir(builtins))
# 大写字母开头一般是内置常量名，小写字母开头一般是内置函数名
# 3.2：内置函数一
# 3.2.1：abs（）：返回绝对值
# print(abs(-10))
# 3.2.2:sum():求和
# print(sum([1,2,3]))     ***sum函数内要放可迭代对象（但是字符串和字典不能相加）
# print(sum({1.5,2.5,3}))   #***运算时只要有一个为浮点数，结果必为浮点数
# 3.3：内置函数二
# 3.3.1：min（）：求最小值
# 3.3.2：max（）：求最大值
# print(min(4,1,8))
# print(max(4,1,8))
# print(min(-8,5,key = abs))   ***传入了求绝对值函数，参数就会先求绝对值
# 3.3.3：zip（）：将可迭代对象作为一个参数，将对象中的元素打包成一个个元组
# li = [1,2,3,4]
# li2 = ['a','b','c','d']
# print(zip(li,li2))
# ***取出zip（）中的元素
#  第一种方式：通过for循环
# for i in zip(li,li2):
#     print(i)
# 注意：如果元素个数不一样，就会按照长度最短的返回
#  第二种方式：转换成列表打印
# print(list(zip(li,li2)))   #***注意：用list打印时zip（）里面的必须都是可迭代对象
# 3.3.4map（）：可以对可迭代对象中的每一个元素进行映射，分别去执行
# map（func，iter1）：func是自己定义的函数，iter1是放进去的可迭代对象
# 简单来说就是每一个对象都会执行这个函数
# li = [1,2,3]
# def func(a):
#     return a*5
# func = lambda a: a+5   ***使用匿名函数进行简化
# mp = map(func,li)
# print(list(mp))
# for i in mp:
#     print(i)
# 3.3.5reduce：先把对象中的两个元素取出来，计算后把这个计算值保存，再用这个计算值与第三个元素计算
# ***注意：reduce需要先导包
# from functools import reduce
# # reduce(function,sequence):function是一个必须有两个参数的函数，sequence是序列：可迭代对象
# def add(x,y):
#     return x*y
# li = [1,2,3,4,5]
# ad = reduce(add,li)
# print(ad)

# 4,拆包
# 4.1：含义：对应于函数中多个返回的数据，去掉元组，列表或者字典，直接获取里面数据的过程
# tua = (1,2,3,4)
# print(tua)
# 要取出元组内的元素
# ***方法一
# a,b,c,d = tua
# print('a=',a,'b=',b,'c=',c,'d=',d)
# 此方法要求元组内的元素个数与定义的的元素个数相同，如果不一致会报错
# 此方法一般在获取元组的值的时候使用
# ***方法二
# a,*b = tua
# print(a,b)
# c,d,e = b
# print(c,d,e)
# 先把单独的取完，剩下的交给带*的变量（可变变量）
# 此方法一般在函数调用时使用