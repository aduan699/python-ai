# a : int = 10
# print(a)

from __future__ import annotations
# 加上这一行，类型检查器就会在读完整个文件之后再解析里面的类型

from typing import Literal
# typing是一个专门做类型注解的类

from datetime import datetime 

from collections.abc import Iterable,Callable
# abc代表的是抽象基类，Iterable代表的是可迭代对象

from typing import TypeVar

# 抽象基类除了Iterable代表可迭代对象，还有mapping代表键值对，还有Callcble代表函数

# class student:
#     def __init__(self,name : str,birthdate : datetime|str,
#                  sex : Literal['male','female'],
#                  course : list[str],
#                  scores : dict[str,float],
#                  location : tuple[float,float]|None):
# # 1.这里定义的str，list，dict，tuple以及float都是自带的类型
# # 2.而datetime则是需要导入的类型
# # 3.值得注意的是，像是list，dict，tuple这类‘容器’也可以定义里面的内容的类型，tuple则必须定义里面所有元素的类型
# # 4.对于可以是多种类型的数据，可以在中间加一个|
# # 5.对于可选参数（可以不传值）可以在|后面写None
# # 6.想要某个参数的类型是某几个值之一，可以用Literal类来把这几个值放进去
#         self.name = name
#         self.birthdate = birthdate
#         self.sex = sex
#         self.course = course
#         self.scores = scores
#         self.location = location

#     def follow(self,other_student : student):
# # 1.如果不加from __future__ import annotations这里的student就会报错，因为这里的student还没定义完，不能作为一个类被定义
#         pass

# s = student(name = 'wen',birthdate = datetime(2006,11,8),sex = 'male',course = ['python'],scores = {'python':100},location = (66,99))
# print(s.name)

# def creat_student(name,birthdate,sex,course,scores,location) -> student :   
# # 1.自定义的类也可以作为类型，这里的代码的含义是最后返回的结果是student类型
#     return student(name,birthdate,sex,course,scores,location)

# def print_name(names : Iterable[str]):
#     for i in names:
#         print(i)
# print_name(('a','b','c'))   
# 1.代码健壮性原则：输入尽可能宽松，输出尽可能明确
# x : Callable[[int,int],str]
# 1.这是一个输入是整数，整数，输出的字符串的函数注解

# T = TypeVar('T',int,str)
# 这里的意思是指T是一个待定的类型
def add[T : (str,int)](a : T,b : T) -> T:
    return a + b
print(add(1,1))
print(add('a','b'))
# print(add(1,'b'))
# 1.这里用到了泛型：a和b的输入都必须是同一个类型，同时这个函数的输出也必须是这个类型
# 2.T = TypeVar('T',int,str)和def add[T : (str,int)](a : T,b : T) -> T:这两种写法完全是等价的