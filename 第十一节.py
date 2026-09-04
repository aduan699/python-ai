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