# 1，面向对象
# 面向对象和面向过程的区别：一个是手洗，一个是机洗

# 2，类和对象
# 在开发过程中，是先有类才有对象
# 2.1：类的三要素
# 1：类名
# 2：属性：是对象的特征描述，用来说明是什么样子的
# 3：方法：对象具有功能（行为），用来说明能够做什么
# 2.2：定义类
# 基本格式
# class 类名：     ***类名必须遵守标识符规定，采用大驼峰命名法，见名知义
#      代码块
# class washer:
#     height = 800
# # 查看类属性：类名.属性名
# print(washer.height)
# # 新增类属性：类名.属性名=值
# washer.wideth = 450
# print(washer.wideth)
# 2.3：创建对象
# 创建对象的过程也叫做实例化对象
# 2.3.1：实例化对象的基本格式：对象名 = 类名（）
# wa = washer()
# print(wa)     #显示的是对象的内存地址
# wa2 = washer()
# print(wa2)    #内存地址不一样，说明可以实例化多个对象
# 2.4：实例方法和实例属性
# 2.4.1：实例方法
# 由对象调用，至少有一个self参数，执行实例方法的时候，自动将调用该方法的对象赋值给self
# class washer:
#     height = 800
#     def wash(self):     #self参数是类中的实例方法必须具备的
#         print('我会洗衣服')
#         print('方法中的self',self)   #self表示当前调用方法的对象
# wa = washer()
# # 对象调用类中的方法
# print(wa)
# wa.wash()
# ***self代表对象本身，当对象调用实例方法时，python会自动将对象本身的引用作为参数
# 传递到实例方法的第一个参数self里面
# 2.4.2：实例属性
# 格式：self.属性名
# class person:
#     name = 'aduan'
#     def introduce(self):
#         print('我是实例属性')
#         print(f'{person.name}的年龄是{self.age}')
# pe = person()
# pe.age = 20
# pe.introduce()
# pe.sex = '男'
# print(pe.sex)     #新增实例属性
# # print(person.sex)   ***实例属性只能由对象名访问到，类名访问不到
# print(person.name)
# print(pe.name)       #***类属性由类名和对象名都可以访问到
# # ***类属性和实例属性的区别：类属性是公共的，大家都能访问，而实例属性是属于对象的，是私有的
# # 只能由对象名访问，不能由类名访问
# pe2 = person()
# pe2.age = 30
# pe2.introduce()
# print(pe2.sex)     #***sex这个实例属性是属于pe的，其他对象仍然是没有这个属性的
# 每实例化一次就需要添加一次属性，效率不高，可以使用构造函数
# 2.4.3：构造函数__init__（）
# 作用：通常会用来做属性的初始化或者赋值
# 注意：在类实例化对象的时候，会被自动调用
# class test:
#     def __init__(self):
#         print('这是__init__()函数')
# te = test()
# class person:
#     def __init__(self,name,age,height):
#         self.name = name
#         self.age = age
#         self.height = height
#     def play(self):
#         print(f'{self.name}正在玩王者荣耀')
#     def introduce(self):
#         print(f'{self.name}的年龄是{self.age}，身高是{self.height}cm')
# pe = person('aduan',20,180)
# pe.play()
# pe.introduce()
# pe2 = person('atuan',30,173)
# pe2.introduce()

# 3：析构函数__del__()
# 删除对象的时候，解释器会默认调用__del__()方法
# class person:
#     def __init__(self):
#         print('这里是__init__')
#     def __del__(self):
#         print('被销毁了')
# pe = person() 删除对象的时候，解释器会默认调用__del__()方法
# class person:
#     def __init__(self):
#
# del pe             #删除p这个对象
# del pe语句执行的时候，内存会被立刻回收，会调用对象本身的__del__()方法
# print('这是最后一行代码')
# 正常运行时，系统不会调用__del__，对象执行结束后，代码会自动调用__del__
# __del__()主要表示该程序块或者函数已经全部执行结束

# 4：封装
# 面向对象的三大特性：封装，继承，多态
# 4.1：封装：指的是隐藏3对象中一些不希望被外部所访问到的属性或者方法

# 4.2：隐藏属性（私有权限），只允许在类的内部访问无法通过对象访问
# 在属性或者方法前面加上__两个下划线
# class person:
#     name = 'duan'
#     __height = 180
#     def introduce(self):
#         print(f'{person.name}的身高是{person.__height}')   
#第一种可以在类外访问到隐藏属性的方法：在实例方法中访问类属性和隐藏属性
# pe = person()
# print(pe.name)
# # print(person.__height)
# 第二种可以在类外访问到隐藏属性的方法：隐藏属性实际上是将名字修改为了_类名__属性名
# # print(pe._person__height)
# pe.introduce()

# 4.3：私有属性/方法
# 1：xxx：普通属性/方法，如果是类中定义的，则可以在任何地方使用
# 2：_xxx：单下划线开头，声明私有属性/方法，如果定义在类中，外部也可以使用，子类也可以继承
#         但是在另一个py文件中通过from xxx import *导入时，无法导入
# 3：__xxx：双下划线开头，隐藏属性，如果定义在类中，外部无法直接访问，子类也不会继承，并且在另一个
#         py文件中通过from xxx import *导入时也无法导入
# class person:
#     name = 'wen'
#     __height = 180
#     _sex = '男'
# pe = person()
# # print(pe.sex)   ***报错，调用时要用对象名._属性名调用
# print(pe._sex)

# 4.4：隐藏方法
# class man:
#     def __funa(self):
#         print('我是隐藏方法')
#     def func(self):
#         print('我是普通的实例方法')
#         # man.__funa(self) ***不推荐，比较繁琐
#         self.__funa()      ***推荐，更加简便
# # 第一种可以调用隐藏方法的方法：在普通实例方法中调用隐藏方法
# ma = man()
# ma.func()
# 第二种可以调用隐藏方法的方法：对象名._类名__隐藏方法名
# ma._man__funa()

# 4.5：私有方法
# class girl:
#     def _buy(self):
#         print('整天买买买')
# gi = girl()
# # gi.buy()      ***报错，调用时要通过对象名._私有方法名调用
# gi._buy()