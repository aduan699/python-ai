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
# pe = person()
# del pe             #删除p这个对象
# del pe语句执行的时候，内存会被立刻回收，会调用对象本身的__del__()方法
# print('这是最后一行代码')
# 正常运行时，系统不会调用__del__，对象执行结束后，代码会自动调用__del__
# __del__()主要表示该程序块或者函数已经全部执行结束
