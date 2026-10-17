import sys
# 所谓的异常处理就是把发现错误与处理错误进行一个分离
#   编写者是发现错误，报告错误
#   使用者是接收错误，处理错误
#  1，抛出异常 raise
# 步骤：
# 1，创建一个Exception('xxx')对象，xxx就是异常提示信息
# 2，raise抛出这个异常（异常对象）
# def func():
#     raise Exception('来个异常')
#     print('现在呢老弟')      ***执行了raise语法后面的代码不会执行
# func()
# # 案例：用户输入密码，判断密码长度，如果密码长度不足就会报错
# def login():
#     key = input('请输入密码：')
#     if len(key) >= 6:
#         print(f'您的密码是：{key}')
#     else:
#         raise Exception('密码长度不足六位，请重新输入')
    # *** 以下内容是捕获异常的代码
# try:
#     login()
# except Exception as e:
#     print(e)
#捕获异常是为了让代码遇到异常时不会终止，能够继续运行

# 以下是不做异常捕获的情况
def xxx():
    sex = input('请输入性别：')
    if sex == 'boy':
        print('性别为男')
    elif sex == 'girl':
        print('性别为女')
    else:
        raise Exception('您的输入有误，请检查后重新输入')
# xxx()
# print('捕获后的代码')
# 可以看到捕获后的代码并没有打印，因为raise执行后就不会执行后面的代码了

# 以下是做异常捕获的情况
# try:
#     xxx()
# except:
#     print('出错了')
#     raise         
#     sys.exit()   #当这里的错误非常严重你想要立刻停止这段代码的执行时，可以导入sys模块并且调用sys的exit方法       
#这里加一个raise代表此处也不知道如何处理这个错误，选择继续往上报，这里如果加了raise，那么后面的代码就不会执行了
# print('捕获后的代码')
# 可以看到这次捕获后的代码打印出来了