from multiprocessing import Process,Queue
import os
import time 
# from queue import Queue 
# 1：进程
# 1.1：含义
# 是操作系统进行资源分配和调度的基本单位，是操作系统结构的基础
# 一个正在运行的程序或者软件就是一个进程
# 程序跑起来就成了进程
# 注意：进程里面可以创建多个线程，多进程也可以完成多任务

# 1.2：进程的状态
# 1：就绪状态：运行的条件都已经满足，等待cpu执行
# 2：执行状态：cpu正在执行其功能
# 3：等待（阻塞状态）：等待某些条件满足，如一个程序sleep了，此时就处于等待状态

# 2：进程语法结构
# multiprocessing模块提供了process类代表了进程对象
# 2.1：process类参数
# 1：target：要执行的目标任务名，即子进程要执行的任务
# 2：args：以元组的形式传参
# 3：kwargs：以字典的形式传参

# 2.2：常用的方法
# 1：start()：开启子进程
# 2：is_alive()：判断子进程是否还活着，存活返回True，否则返回False
# 3：join()：阻塞主进程，主进程等待子进程执行完才会继续执行

# 2.3：常用的属性
# 1：name：当前进程的别名，一般的process-N
# 2：pid：当前进程的编号
# def sing():
#     # os.getpid()：获取当前进程编号
#     # os.getppid()：获取父进程的进程编号
#     # 父进程的pid就是py文件主进程的pid
#     print(f'sing子进程的进程编号：{os.getpid()},父进程的进程编号：{os.getppid()}')
#     print('唱歌')
# def dance():
#     print(f'dance子进程的进程编号：{os.getpid()},父进程的进程编号：{os.getppid()}')
#     print('跳舞')
# if __name__ == '__main__':
#     # 创建子进程
#     # 修改子进程名字的第一种方式
#     p1 = Process(target = sing,name = '子进程一')
#     p2 = Process(target = dance,name = '子进程二')
#     # 开启子进程
#     p1.start()
#     p2.start()
#     # 修改子进程名字的第二种方式
#     p1.name = '子进程1'
#     p2.name = '子进程2'
#     # 访问子进程名字
#     print(p1.name)
#     print(p2.name)
#     # 查看子进程的进程编号
#     print(p1.pid)
#     print(p2.pid)
#     print(f'主进程的pid：{os.getpid()},主进程的父进程的pid：{os.getppid()}')
# 当前软件的pid就是主进程的父进程的pid
# def eat(name):
#     print(f'{name}会干饭')
# def sleep(name):
#     print(f'{name}会睡觉')
# if __name__ == '__main__':
#     p1 = Process(target = eat,args = ('wen',))
#     p2 = Process(target = sleep,args = ('yucheng',))
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()
#     print('p1的存活状态：',p1.is_alive())
#     print('p2的存活状态：',p2.is_alive())
# 写在主进程中判断子进程存活状态的时候需要加入join()阻塞一下

# 2.4：进程间不共享全局变量
# li = []
# def wdata():
#     for i in range(5):
#         li.append(i)
#         time.sleep(0.5)
#     print('写入的数据是：',li)
# def rdata():
#     print('读取的数据是：',li)
# if __name__ == '__main__':
#     p1 = Process(target = wdata)
#     p2 = Process(target = rdata)
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()
# 读取的数据一直为空，因为进程之间不共享全局变量

# 3：进程之间的通信
# Queue（q队列）
# q.put()：放入数据
# q.get()：取出数据
# q.empty()：判断队列是否为空
# q.full()：判断队列是否已满
# q.qsize()：返回当前队列包含的信息数量
# 初始化一个队列对象
# q = Queue(3)     #表示最多可以接收3条消息，没写或者是负值就代表没有上限
# q.put('爱你到老')
# q.put('你在做梦')
# print(q.full())
# q.put('年轻人不讲武德')
# print(q.full())
# # print(q.qsize())
# print(q.get())     #获取队列的一条消息，然后将其从队列中移除
# print(q.get())
# # print(q.empty())
# print(q.get())
# # print(q.empty())
# # print(q.qsize())

# li = ['张三','李四','王麻子','赵六']
# def wdata(q1):
#     for i in range(5):
#         print(f'{i}已经被放到q队列里面了')
#         q1.put(i)
#         time.sleep(0.5)
#     print('写入的数据是：',li)
# def rdata(q2):
#     while True:
#         if q2.empty():
#             break
#         else:
#             q2.get()
#     print('读取的数据是：',li)
# if __name__ == '__main__':
#     # 创建队列对象
#     q = Queue()
#     p1 = Process(target = wdata,args = (q,))
#     p2 = Process(target = rdata,args = (q,))
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()