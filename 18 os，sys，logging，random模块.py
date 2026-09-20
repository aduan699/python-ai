# 导入os模块
import os
# 导入sys模块
import sys 
# 导入time模块
import time 
# 导入logging模块
import logging 
# 导入random模块
import random 
# 1：os模块
# 作用：用于和操作系统进行交互
# 1.1：os.name   #指示正在使用的工作平台（操作系统的类型）
# print(os.name)
# 对于windows,返回nt;对于linux,返回posix

# 1.2：os.getenv(环境变量名称)   #读取环境变量
# print(os.getenv('path'))

# 1.3：os.path.split()   #把目录名和文件名分离，以元组的形式接收，第一个元素是目录路径，第二个元素是文件名
# print(os.path.split(r'C:\Users\28455\OneDrive\Desktop\python-ai\第十八节.py'))

# 1.4：os.path.dirnamm   #显示split分割的第一个元素，即目录
# print(os.path.dirname(r'C:\Users\28455\OneDrive\Desktop\python-ai\第十八节.py'))

# 1.5：os.path.basename  #显示split分割的第二个元素，即文件名
# print(os.path.basename(r'C:\Users\28455\OneDrive\Desktop\python-ai\第十八节.py'))

# 1.6：os.path.exists()   #判断路径（文件或目录）是否存在，存在就返回True,不存在就返回False
# print(os.path.exists(r'C:\Users\28455\OneDrive\Desktop\python-ai\第十八节.py'))

# 1.7：os.path.isfile()   #判断文件是否存在
# print(os.path.isfile(r'C:\Users\28455\OneDrive\Desktop\python-ai\第十八节.py'))   #True
# print(os.path.isfile(r'C:\Users\28455\OneDrive\Desktop\python-ai'))              #False

# 1.8：os.path.isdir()    #判断目录是否存在
# print(os.path.isdir(r'C:\Users\28455\OneDrive\Desktop\python-ai\第十八节.py'))   #False
# print(os.path.isdir(r'C:\Users\28455\OneDrive\Desktop\python-ai'))              #True

# 1.9：os.path.abspath()  #获取当前路径下的绝对路径
# print(os.path.abspath('第十八节.py'))   

# 1.10：os.path.isabs()   #判断是否是绝对路径
# print(os.path.isabs(r'C:\Users\28455\OneDrive\Desktop\python-ai\第十八节.py'))

# 2：sys模块
# 作用：负责程序跟python解释器的交互
# 2.1：sys.getdefaultencoding()   #获取系统默认的编码格式
# print(sys.getdefaultencoding())

# 2.2：sys.path：获取环境变量的路径，跟解释器相关
# print(sys.path)   #以列表的形式返回，第一项为当前所在的工作目录

# 2.3：sys.platform   #获取操作系统平台名称
# print(sys.platform)

# 2.4：sys.version   #获取python解释器的版本信息
# print(sys.version)

# 3：time模块
# 三种时间表示
# 1：时间戳（timestamp）
# 2：格式化的时间字符串（format time）
# 3：时间元组（struct_time）
# 3.1：time.sleep()   #延时操作，以秒为单位
# print(12)
# time.sleep(2)
# print(123)

# 3.2:time.time()   #获取当前的时间戳，以秒计算，计算的是从1970年1月1日00：00：00到现在的时间差
# print(time.time())   #返回的是浮点型

# 3.3：time.localtime()   #将一个时间戳转换为当前时区的time_struct
# print(time.localtime())

# 3.4：time.asctime()   #获取当前系统时间，把struct_time换成固定的字符串表达式
# print(time.asctime())
# t = time.localtime()
# print(t)
# print(time.asctime(t))

# 3.5：time.ctime()   #获取当前系统时间，把时间戳换成固定的字符串表达式
# print(time.ctime())
# t = time.time()
# print(t)
# print(time.ctime(t))

# 3.6：time.strftime(格式化字符串，struct_time)   #将struct_time转换成格式化字符串
# print(time.strftime(r'%Y-%m-%d',time.localtime()))

# 3.7：time.strptime(时间字符串，格式化字符串)     #将格式化字符串转换成struct_time（时间元组）
# print(time.strptime('2026-9-15',r'%Y-%m-%d'))

# 4：logging模块
# 4.1：作用：用于记录日志信息
# 4.2：日志的作用：
    #  1：程序调试
    #  2：了解软件程序运行情况是否正常
    #  3：软件程序故障分析与异常定位

# 4.3：级别排序（从高到低）
# CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTEST
# 注意：前两个程序根本无法运行，后面四个都还可以运行
# logging.debug('我是debug')
# logging.info('我是info')
# logging.warning('我是warning')
# logging.error('我是error')
# logging.critical('我是critical')
# 注意：logging默认的level就是warning，也就是说它只会显示等级大于等于warning的日志信息

# 4.4：logging.basicConfig()   #配置root,logger的参数
#    1：filename：指定日志文件的文件名，所有记录的日志都会放到这个文件中去
# logging.basicConfig(filename = 'log.log')
# logging.debug('debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')
#    2：filemode：文件的打开方式，默认是a，追加模式
# logging.basicConfig(filename = 'log.log',filemode = 'w')
# logging.debug('debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')
#    3：level指定日志显示的级别，默认是warning
# logging.basicConfig(filename = 'log.log',filemode = 'w',level = logging.NOTSET)
# logging.debug('debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')
#    4：format：指定日志的输出格式
# logging.basicConfig(filename = 'log.log',filemode = 'w',level = logging.NOTSET,format = '%(levelname)s')
# logging.debug('debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')

# 5：random模块
# 作用：用于实现各种分布的伪随机数生成，可以根据不同的实数分布来随机生成值
# 5.1：random.random()   #产生大于零小于一的小数
# print(random.random())

# 5.2：random.uniform()  #产生指定范围内的随机小数
# print(random.uniform(1,3))

# 5.3：random.randint()  #产生指定范围内的整型，包括开头和结尾
# print(random.randint(1,5))

# 5.4：random.randrange(start,stop,[step])   #产生start到stop范围内的随机整数，包含开头但是不包含结尾
# step   指定随机产生的步长
# print(random.randrange(2,7,2))