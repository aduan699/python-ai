# 1，抛出异常 raise
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

# 2，模块
# 2.1：含义：一个py文件本质上就是一个模块，即导入一个模块等同于运行了一个py文件
# 2.2：分类
# 2.2.1：内置模块
# 如：random、time、os、logging，直接导入就可以使用
# 2.2.2：第三方模块（第三方库）
# 下载：cmd窗口输入pip install 模块名
# 2.2.3：自定义模块
# 即自己在项目中定义的模块
# 注意：命名要遵循标识符规定以及变量的命名规范，并且不要与内置模块起冲突，否则将导致模块功能无法使用
# 2.3：导入模块
# 2.3.1：方式一：import 模块名
# 语法：
# 导入模块：import 模块名   ***注意：可以一个import导入多个模块，但是最好是一个模块单独用一个import导入
# 调用功能：模块名.功能名
# import pytest
# print(pytest.name)
# pytest.func()
# 2.3.2：方式二：from...import...
# 语法：
# 从模块中导入指定的部分：
# from 模块名 import 功能1，功能2...
# 调用功能：
# 直接输入功能即可，不需要添加模块名
# from pytest import func，name   ***import后面写需要导入的功能
# func（）                        ***导入函数只需要写函数名，不需要加小括号
# print(name)
# 2.3.3：方式三：from...import*
# 语法：from 模块名 import *
# from pytest import *     ***含义：把模块中的内容全部导入
# 注意：不建议过多使用from...import...声明，有时候命名冲突会造成一些错误
# 2.3.4：as起别名
# 1：as给模块起别名
# 语法：import 模块名 as 别名
# 2：as给功能起别名
# 语法：from 模块名 import 功能 as 别名
# 2.4：内置全局变量__name__
# 2.4.1：语法：
# if __name__ == '__main__':
# 2.4.2：作用
# 用来控制py文件在不同的应用场景执行不同的逻辑
# 2.4.3__name__
# 1：文件在当前程序执行（即自己执行自己）：__name__=='__main__'
# 2：文件被当作模块被其他文件导入：__name__==模块名
# 注意：__name__=='__main__'被当作模块导入时，下面的代码不会显示

# 3，包
# 3.1：含义：就是项目结构中的文件夹/目录
# 3.2：与普通文件夹的区别：包是含有__init__.py的文件夹
# 3.3：作用：包就是将有联系的模块放到同一个文件夹中，有效避免模块名称冲突问题，让结构更清晰
# 3.4：新建包
# 3.5：import导入包时，首先执行__init__.py的代码
# 导包方式一：
# import pack1
# 导包方式二：
# from pack1 import register
# 3.6：不建议在init文件中编写过多代码，尽量保证init文件内容简单
# 3.7：__all__：本质上是一个列表，列表里面的元素就代表了要导入的模块
# 作用：可以控制要引入的东西
# 语法：__all__ = ['register','login']   ***相当于导入[]里面定义的模块
# from pack1 import *
# register.reg()
# login.log()
# 3.8：包的本质又是一个模块，包又可以包含包