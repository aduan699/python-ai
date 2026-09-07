# 1:__init__()和__new__()
# 1.1:__init__():初始化对象

# 1.2:__new__():object基类提供的内置的静态方法
# 作用:1：为对象创建空间    2：返回对象的引用
# class test(object):
#     def __init__(self):
#         print('这里是__init__')
#     def __new__(cls):
#         print('这里是__new__')
#         print(cls)
#         return super().__new__(cls)
# te = test()
# print(te)

# 执行步骤：
# 一个对象实例化的过程：
#     首先执行__new__()，如果没有写__new__()默认调用object里面自带的__new__()
#     返回一个实例对象，然后再调用__init__()，对对象进行初始化
# class person(object):
#     def __new__(cls,*args,**kwargs):
#         print("这是new方法")
#         obj = super().__new__(cls)
#         print("返回值：",obj)
#         return obj
#     def __init__(self,name):
#         self.name = name
#         print(self.name)
# pe = person('wen')
# print(pe)
# pe2 = person('susu')
# print(pe2)
# 总结：__init__()和__new__()
# 1：__new__()是创建对象，__init__()是初始化对象
# 2：__new__()返回对象引用，__init__()是定义实例属性
# 3：__new__()是类级别的方法，__init__()是实例级别的方法

# 2：单例模式
#2.1： 可以理解成一个特殊的类，这个类只有一个对象
# 优点：可以节省内存空间，减少了不必要的资源浪费
# 弊端：多线程访问的时候容易引发线程安全问题

# 2.2：方式
# 1：通过@classmethod方式来实现
# 2：通过装饰器来实现
# 3：通过重写__new__()方式来实现(***重点)
# 4：通过导入模块来实现

# 2.3：通过重写__new__()方法来实现单例模式
# 设计流程：
# 1：定义一个类属性，初始值为none，用来保存单例对象的引用（内存地址）
# 2：重写__new__()方法
# 3：判断类属性是不是none，如果是则把__new__()返回的对象引用保存进去
# 4：返回类属性中记录的对象引用
# class singleton(object):
#     obj = None
#     def __new__(cls,*args,**kwargs):
#         print('这是new方法')
#         if cls.obj == None:
#             cls.obj = super().__new__(cls)
#         else:
#             return cls.obj
#     def __init__(self):
#         print('这是init方法')
# s = singleton()
# print('s:',s)
# s2 = singleton()
# print('s2:',s2)
# s3 = singleton()
# print('s3:',s3)
# 单例模式：每一次实例化所创建的对象都是同一个，内存地址都一样

# 2.4：通过导入模块实现单例模式
# from mytest import te as te01
# from mytest import te as te02
# print(te01,id(te01))
# print(te02,id(te02))
# 模块就是天然的单例模式

# 3：魔法方法&魔法属性
# 3.1：__doc__：类\函数的描述信息
# ***（这是一种魔法属性，不是方法不能加小括号）
# class person(object):
#     """人类"""        #类的描述信息，只能使用多行注释
#     pass
# print(person.__doc__)

# 3.2：__module__:表示操作对象当前所在的模块
# 3.3：__class__:表示操作对象当前所在类
# import mytest
# b = mytest.B()
# print(b)
# b.func()
# print(b.__module__)
# print(b.__class__)

# 3.4：__str__():对象的描述信息
# 如果类中定义了此方法，则在打印对象时，默认输出的是该方法的返回值
# 注意：__str__()必须返回一个字符串
# class C(object):
#     def __str__(self):
#         return '这是str方法'
# c = C()
# print(c)

# 3.5：__del__():析构函数，在函数结束的时候会调用，或者要删除某个对象的时候也会调用
# 3.6：__call__():使一个实例对象变成一个可调用对象，就像一个函数一样可以调用
# 可调用对象：函数/内置函数/类都是可调用对象
# callable():判断一个对象是否是可调用对象
# class A(object):
#     def __call__(self, *args, **kwds):
#         print('这是call')
# a = A()
# a()                 ***调用一个可调用的实例化对象时，其实就是在调用它的__call__()方法
# print(callable(a))