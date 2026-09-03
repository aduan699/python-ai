# 1：封装
# 面向对象的三大特性：封装，继承，多态
# 1.1：封装：指的是隐藏3对象中一些不希望被外部所访问到的属性或者方法

# 1.2：隐藏属性（私有权限），只允许在类的内部访问无法通过对象访问
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

# 1.3：私有属性/方法
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

# 1.4：隐藏方法
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

# 1.5：私有方法
class girl:
    def _buy(self):
        print('整天买买买')
gi = girl()
# gi.buy()      ***报错，调用时要通过对象名._私有方法名调用
gi._buy()