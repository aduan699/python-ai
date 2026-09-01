#      1，while循环
# 基本语法
# while 条件：
#     循环体
#     改变变量
# i = 1
# while i<= 10:
#     print (i)
#     i += 1
# i = 1
# num = 0
# while i<= 100:
#     num += i
#     i += 1
# print(num)
#      2，for循环
# 基本格式
# for 临时变量 in 可迭代对象:
#     循环满足条件时执行的代码
# 可迭代对象就是要去遍历取值的整体，现在只需记住字符串就是可迭代对象
# str = "hello python"
# for i in str :
#     print(i)
# range()用来记录循环次数，相当于是一个计数器
# for i in range(1,6):    ***从1开始，从6-1结束，遵循包前不包后原则
# for i in range(5):      ***也可以用这种更加简便的写法，默认是从0开始的
#     print(i)
# num = 0
# for i in range(1,101):
#     num += i            ***不需要改变变量，他自己会添加
# print(num)
#     3，关键字break和continue
# i = 1
# while i <= 5:
#     print(f"我正在吃第{i}个苹果")
#     if i == 3:
#         print("吃饱了不吃了")
#         break
#     i += 1
# i = 1
# while i <= 5:
#     print(f"我正在吃第{i}个苹果")
#     if i == 3:
#         print("吃饱了不吃了")
#         i += 1               #***在continue之前一定要修改计数器，否则会陷入死循环
#         continue
#     i += 1
# for i in range(5):
#     if i == 3:
#         continue
#     print(i)

#    1,字符串编码
# 本质上就是二进制数据与语言文字的一一对应关系
# Unicode:所有字符都是两个字节，所以字符与数字之间的转换速度更快一些，但是相对占用空间大
# UTF-8:精准，对不同的字符用不同的长度表示，所以占用的空间更小，但是转换速度较慢
# 字符串编码转换：
# 1，编码：encode（），将其他类型的字符串转换成Unicode编码
# 2，解码：decode（），将Unicode编码转换成其他类型的字符串
# a = "hello"
# print(type(a))     ***str是以字符为单位进行处理
# a1 = a.encode()
# print(type(a1))    ***bytes是以字节为单位进行处理

# 2，字符串常见操作
# 2.1，+：字符串拼接
# 2.2，*：重复输出
# print("haha"*5)
# 成员运算符
# 作用：检查字符串中是否包含了某个子子字符串
# in ：如果包含则为真，不包含则为假
# not in ：如果不包含则为真，包含则为假
# name = "guli"
# print("b" not in name)
# 2.3，下标
# python中下标从0开始
# name = "123456"
# print(name[2])
# print(name[-1])      ***从右往左数，下标从-1开始
# 2.4，切片
# 含义：指对被操作的对象截取其中的一部分的操作
# 语法：[开始的位置：结束的位置：步长]     ***遵循包前不包后原则
# 从左往右
# st = "asdfg"
# print(st[0:3])
# print(st[ :2])
# 从右往左
# print(st[-1:])
# 步长：表示选取间隔，不写的话默认是1
# 步长的绝对值大小决定切取的间隔，正负号决定切取的方向
# st = "asdfgh"
# print(st[-1:-5:-1])

# 3，字符串常见操作
# 3.1，查找     ***全都遵循包前不包后原则
# 1，find（）：检测某个子字符串是否包含在字符串中，如果在就返回这个子字符串开始位置的下标，如果不在就返回-1
# find(子字符串，开始位置下标，结束位置下标)     ***开始和结束位置下标可以省略，此时表示在整个字符串中查找
# name = "yuewenduan"
# print(name.find("e"))   第一个e的下标为2
# print(name.find("y",1))
# 2，index（）：检测某个子字符串是否包含在字符串中，如果在就返回这个子字符串开始位置的下标，如果不在就会报错
# index(子字符串，开始位置下标，结束位置下标)     ***开始和结束位置下标可以省略，此时表示在整个字符串中查找
# name = "我命油我不油天"
# print(name.index("油",3))
# 3，count（）：返回某个子字符串在整个字符串中出现的次数，没有就返回0
# count(子字符串，开始位置下标，结束位置下标)     ***开始和结束位置下标可以省略，此时表示在整个字符串中查找
# name = "bingbing"
# print(name.count("b"))
# 3.2，判断
# 1，startswith()：是否是以某个子字符串开头，是的话返回True，否则返回False
# startswith(子字符串，开始位置下标，结束位置下标)
# st = "sixstar"
# print(st.startswith("s",1))
# 2，endswith（）：是否是以某个子字符串结尾，是的话返回True，否则返回False
# endswith(子字符串，开始位置下标，结束位置下标)
# st = "sixstar"
# print(st.endswith("a",0,6))     **包前不包后
# 3，isupper（）：检测字符串中的所有字母是否都为大写，是的话返回True,否则返回False
# st = "sixstar"
# print(st.isupper())
# print("ASD".isupper())
# 3.3，修改元素
# 1，replace（）：替换
# replace（旧内容，新内容，替换次数）     ***替换次数可以省略，默认全部替换
# name = "我的天哪，你的天哪"
# print(name.replace("天","地",1))
# 2，split（）：指定分隔符来切字符串
# st = "hello,python"
# print(st.split(","))   ['hello', 'python']---以列表的形式返回
# print(st.split("a"))   ***如果不包含分割内容，则不会分割
# 3，capitalize（）：第一个字母大写，其他都小写
# 4，lower（）：大写字母转为小写
# 5，upper（）：小写字母转为大写
# st = "six star"
# print(st.upper())
