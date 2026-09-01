# 4，列表 list
# li = [1,2,"a",4]
# print(li[0:3])     ***列表也可以进行切片
# ***列表也是可迭代对象，可以用for循环进行遍历

# 5，列表的常见操作
# 5.1：添加元素
# append() extend() insert()
# li = ["one","two","three"]
# li.append("four")     ***append：整体添加
# li.extend("four")     ***extend:分散添加，将另一个类型中的元素逐一添加
# li.insert(3,"four")   ***insert:在指定位置添加，如果指定位置已经有元素，原有元素就会后移
# print(li)
# 5.2：修改
# 直接通过下标就可以进行修改
# li = [1,2,3]
# li[1]="a"
# print(li)
# 5.3：查找元素
# in和not in:用法和字符串中的一致
# li = [1,2,3]
# print(1 in li）
# 案例：输入昵称时判断是否重复，若不重复则将昵称添加到列表中
# name_list=["张","王",'李','赵']
# while True:
#     name = input("请输入您的昵称：")
#     if name in name_list:
#         print(f"您输入的昵称{name}已经存在了呦")
#     else:
#         print(f"您输入的昵称{name}可以使用")
#         name_list.append(name)
#         print(name_list)
#         break
# index和count：和字符串中的用法相同
# 5.4：删除元素
# del:根据下标进行删除
# li = [1,2,3,4]
# del li[0]
# print(li)
# pop：删除指定下标位置的元素，python3版本默认删除最后一个位置的元素，下标超出范围会报错
# li = [1,2,3,4]
# li.pop(0)
# print(li)
# remove：根据元素的值进行删除，默认删除最先出现的指定元素
# li = ["a",'b','c','d']
# li.remove('d')
# print(li)
# 5.5：排序
# # sort：将列表按照特定的顺序排序，默认是从小到大
# li = [2,5,4,6,1,3]
# li.sort()
# print(li)
# reverse：倒序，将列表倒过来
# li.reverse()
# print(li)
# 5.6：列表推导式
# 格式一：[表达式 for 变量 in 列表]     ***注意：in后面不仅可以放列表，还可以放range（）、可迭代对象
# li = [1,2,3,4,5,6]
# [print(i) for i in li]
# li = []
# [li.append(i) for i in range(1,6)]
# print (li)
# 格式二：[表达式 for 变量 in 列表 if 条件]
# li = []
# [li.append(i) for i in range(1,7) if i%2==1]
# print(li)
# 5.7：列表嵌套
# 含义：一个列表里面又有一个列表
# li = [1,2,3,[4,5,6]]
# print(li[3])
# print(li[3][0])     ***取出内列表中的元素

# 6，元组 tuple
# 6.1：元组（tuple）
# 基本格式：元组名 = （元素1，元素2，元素3）
# tup = ()       ***定义空元组
# tup = (3,)     ***只有一个元素的时候，末尾一定要加上，
# 6.2：元组与列表的区别
# 1，元组中只有一个元素时末尾必须加上，而列表则不用
# 2，元组只支持查询操作，不支持增删改操作（元组也支持切片操作）
# count（）、index（）、len（）的用法和列表用法相同
# 6.3：元组的应用场景
# 1，函数的参数和返回值
# 2，格式化输出后面的（）本质上就是一个元组
# name = "bingbing"
# age = 18
# print("%s的年龄是%d"%(name,age))
# 3，数据不可以被修改，保护数据的安全

# 7，字典 dict
# 7.1：基本格式：字典名 = {键1：值1，键2：值2，.....}
# 以键值对的形式保存，键和值之间用：隔开，每个键值对之间用，隔开
# 字典中的键具有唯一性，但是值可以重复
# dic = {"name":"bingbing","name":"susu"}     ***不会报错，键名重复后面的值将会覆盖前面的值
# print(dic)
# dic2 = {"name1":"bingbing","name2":'bingbing'}
# print(dic2)
# 7.2：字典的常见操作一
# 7.2.1：查看元素
# 变量名[键名]（查找的键名不存在时会报错）
# dic = {'name':'bingbing','age':18}
# print(dic[2])     ***不可以使用下标，字典中没有下标，查找元素需要根据键名
# print(dic['age'])
# 变量名.get(键名)(查找的键名不存在时返回None)
# dic = {'name':'bingbing','age':18}
# print(dic.get('age'))
# 7.2.2：修改元素
# dic = {'name':'bingbing','age':18}
# dic['age'] = 20     ***列表通过下标修改，字典通过键修改
# print(dic)
# 7.2.3：添加元素
# 键名存在时则修改，键名不存在时则添加
# dic = {'name':'bingbing','age':18}
# dic['grade'] = 100
# print(dic)
# 7.2.4：删除元素
# del
# 删除整个字典：del 字典名
# 删除指定键值对：del 字典名[键名]，键名不存在就会报错
# dic = {'name':'bingbing','age':18}
# del dic['age']
# print(dic)
# clear（）：清空整个字典，但是保留了这个字典
# dic = {'name':'bingbing','age':18}
# dic.clear()
# print(dic)
# pop()：删除指定键值对，键不存在就会报错
# dic = {'name':'bingbing','age':18}
# dic.pop('age')
# dic.pop()       ***报错，没有指定键名
# dic.popitem()   ***python3.7之前的版本是随机删除一对键值对，3.7之后的版本默认删除最后一对键值对
# print(dic)
# 7.3：字典的常见操作二
# 7.3.1：len（）：求长度
# dic = {'name':'bingbing','age':18,'tel':'123'}
# print (len(dic))
# 7.3.2：keys（）：返回字典里所有的键名
# dic = {'name':'bingbing','age':18,'tel':'123'}
# print(dic.keys())
# for i in dic.keys():
#     print(i)
# 7.3.3：values：返回字典里包含的值
# dic = {'name':'bingbing','age':18,'tel':'123'}
# print(dic.values())
# 7.3.4：items：返回字典里包含的键值对，键值对是以元组的形式
# dic = {'name':'bingbing','age':18,'tel':'123'}
# print(dic.items())
# for i in dic.items():
#     print(i)
# 7.4：字典的应用场景
# 使用键值对，存储描述一个物体的信息