# 1：继承
# 就是让类和类之间变成父子关系，子类默认继承父类的属性和方法
# 1.1：语法
# class 类名（父类名）：
    # 代码块

# 1.2：单继承
# class person:
#     def eat(self):
#         print('我会吃饭饭')
#     def sing(self):
#         print('我是唱歌小能手')
# class girl(person):
#     pass                   #***占位符，不写这个的话会缩进报错
# gi = girl()
# gi.eat()
# 总结：子类可以继承父类的属性和方法，就算自己没有，也可以使用父类的

# 1.3：继承的传递（多重继承）
# 子类拥有父类的父类的属性和方法
# class father:
#     def eat(self):
#         print('吃饭饭')
#     def sleep(self):
#         print('睡觉觉')
# class son(father):
#     def drink(self):
#         print('喝水水')
# class grandson(son):
#     pass
# pe1 = grandson()
# pe1.eat()
# pe1.sleep()
# pe1.drink()

# 1.4：重写是指在子类中定义与父类相同名称的方法
# 1.4.1：覆盖父类的方法
# class person:
#     def money(self):
#         print('有一百万可以被继承')
# class son(person):
#     def money(self):
#         print('我自己赚了一千万')
# pe = son()
# pe.money()
# 1.4.2：对父类方法进行扩展：继承父类的方法，子类也可以增加自己的功能
# 1：父类名.方法名(self)
# 2：super().方法名()            ***推荐使用
# 3：super(子类名,self).方法名()
# super是python里面的一个特殊的类，super()是使用super类创建出来的对象，可以使用父类中的方法
# class person:
#     def money(self):
#         print('有一百万可以被继承')
# class son(person):
#     def money(self):
#         # person.money(self)
#         super().money()
#         print('我自己赚了一千万')
# pe = son()
# pe.money()

# 2：新式类写法
# 2.1：class A :经典类，不由任意内置类型派生出的类
# ***派生类：拥有与父类不同的属性或者方法，就称这个子类为派生类
# 2.2：class A()
# 2.3：class A(object):继承了object类   ---推荐使用
# object--对象，python为所有对象提供的基类（顶级父亲），提供了一些内置的属性和方法，可以使用dir()查看
# python3中一个类如果没有继承任何类，则默认继承object类，因此python3中都是新式类

# 3：多继承
#3.1：子类可以拥有多个父类，并且拥有所有父类的属性和方法
# class father(object):
#     def func(self):
#         print('这是第一个父类：爸爸')
# class mother(object):
#     def funa(self):
#         print('这是第二个父类：妈妈')
# class son(father,mother):
#     pass
# pe = son()
# pe.func()
# pe.funa()

# 3.2：不同的父类有同名的方法
# 多个父类具有同名的方法的时候，调用时就近原则（哪一个写在前面，就先调用哪一个类的方法）

# 3.3：方法的搜索顺序
# 如果在当前类中找到了方法，就会直接执行，不会搜索（子类和父类中有同名的方法会调用子类的方法）

# 3.4：多继承的弊端
# 多继承会引发冲突，导致代码设计的复杂度增加

# 4：多态
# 指的是同一种行为具有不同的表现形式
# 4.1：多态的前提
# 继承
# 重写
# class animal(object):
#     def shout(self):
#         print('动物会叫')
# class cat(animal):
#     def shout(self):
#         print('小猫哈不哈')
# class dog(animal):
#     def shout(self):
#         print('大狗叫不叫')
# ca = cat()
# ca.shout()
# do = dog()
# do.shout()

# 4.2：多态性；一种调用方式，不同的调用结果
# class animal(object):
#     def eat(self):
#         print('我会干饭')
# class pig(animal):
#     def eat(self):
#         print('猪吃糠糠')
# class dog(animal):
#     def eat(self):
#         print('狗吃狗粮')
# # 多态性：定义一个统一接口，一个接口多种实现
# def test(obj):
#     obj.eat()
# an = animal()
# pi = pig()
# test(an)
# test(pi)
# test函数传入不同的对象，执行不同的对象的方法

# 5：静态方法
# 使用@staticmethod来修饰，静态方法没有self，cls参数的限制
# 静态方法与类无关，他可以被转换成函数使用
# class person(object):
#     @staticmethod
#     def study(name):
#         print(f'{name}会学习')
# 静态方法既可以用类名调用，也可以用对象名调用
# person.study('wen')
# pe = person()
# pe.study('wen')
# 静态方法的使用场景：取消不必要的参数传递，有利于减少内存占用和性能消耗

# 6：类方法
# 使用装饰器@classmethod来标识为类方法，对于类方法，第一个参数必须是类对象，一般是以cls作为第一个参数
# class person(object):
#     name = 'wen'
#     @classmethod
#     def test(cls):
#         print('cls:',cls)     #***cls代表类对象本身，类本质上也是一个对象
#         print(cls.name)
# print(person)
# person.test()
# ***1：需要读取/修改实例属性（self.xxx）时使用实例方法
#    2：需要读取/修改类属性时使用类方法
#    3：既不用实例数据，也不用类数据时使用静态方法
# class person(object):
#     name = 'wen'             #类属性
#     def __init__(self):
#         self.age = 20        #实例属性
#     # def play(self):
#     #     print(f'{person.name}正在玩游戏')
#     #     print(self.age)
#     # @staticmethod
#     # def introduce():
#     #     print(f'我的名字是{person.name}')
#     #     print(self.age)
#     @classmethod
#     def introduce(cls):
#         print(f'我的名字是{person.name}')
#         print(self.age)
# pe = person()
# # pe.play()
# pe.introduce()
# 总结：类属性是公有的，三种方法都可以访问到，实例属性是私有的，只有实例方法能访问到