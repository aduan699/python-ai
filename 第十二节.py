# 1:文件
# 1.1：文件就是存储在一些长期存储设备上的一段数据

# 1.2：文件操作
# 打开文件 -> 读写文件 -> 关闭文件

# 1.3：文件对象的方法
# 1：open()：创建一个file对象，默认以只读模式打开
# 2：read(n):n表示从文件中读取数据的长度，如果没有写n，则默认一次性读取文件中的全部内容
# 3：write():将指定内容写入文件
# 4：close():关闭文件

# 1.4：属性
# 文件名.name:返回要打开的文件的文件名，可以包含文件的具体路径
# 文件名.mode:返回文件的访问格式
# 文件名.closed:检测文件是否被关闭，如果关闭就返回true
# 1：打开文件
# f = open('test.txt')
# print(f.name)
# print(f.mode)
# print(f.closed)
# # 2:关闭文件
# f.close()
# print(f.closed)

# 2：读写操作
# 2.1：read(n):n表示从文件中读取数据的长度，如果没有传n值或者传的是负数，则默认一次性读取文件中的全部内容
# f = open('test.txt')
# # print(f)
# print(f.read())
# f.close()

# 2.2：readline():一次读取一行内容，方法执行完，会把文件指针移到下一行，准备再次读取
# f = open('test.txt')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# while True:
#     text = f.readline
#     if text == None:
#         break
# print(text)
# for i in f:
#     print(i,end = '')
# f.close()

# 2.3：readlines():按照行的方式把文件中的内容一次性读取，返回值是一个列表，每一行的数据就是列表的一个元素

# 2.4：访问模式
# 2.4.1：r:只读模式（默认模式），文件必须存在，不存在就会报错
# 2.4.2：w:只写模式，文件存在就先清空文件内容，再写入新内容，不存在就创建新文件
# file = open('test01.txt','w')
# file.write('bingbing')
# file.close()

# 2.4.3：+表示可以同时读写某个文件
# 使用+会影响文件的读写效率，在开发过程中一般都是以只读，只写的方式来操作文件
# r+：可读写文件，如果文件不存在就会报错
# w+：先写再读，如果文件存在就覆盖，如果文件不存在就创建
# f = open('test.txt','w+')
# f.write('susu')
# f.close()

# 2.4.4:a:追加模式：如果不存在就创建新文件写入，如果存在就在原有的基础上追加新内容
# f = open('test.txt','a')
# f.write('\ntest is being written')
# f.close()
# 文件指针：标记从哪个位置开始读取数据

# 2.5：文件定位操作
# tell()和seek()
# tell()：显示文件内当前位置，即文件指针当前位置
# seek(offset,whence)：移动文件读取指针到指定位置
# offset:偏移量，表示文件指针要移动的字节数
# whence:起始位置，表示要移动字节的参考位置，默认是0，0代表文件的开头位置，1代表当前位置，2代表文件结尾位置
# seek(0,0)就会把文件指针移到文件开头
f = open('test.txt','w+')
f.write('hello python!')
pos = f.tell()
print('文件指针当前位置：',pos)
f.seek(0,0)
pos2 = f.tell()
print('移动后文件指针所在位置：',pos2)
print(f.read())
f.close()