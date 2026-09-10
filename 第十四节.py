# 导入线程模块
import threading
# 导入时间模块
import time

# def sing():
#     print('我在唱歌')
#     time.sleep(2)          #睡眠，以秒为单位，代码执行到这里会停顿2秒
#     print('唱完歌了')
# def dance():
#     print('我在跳舞')
#     time.sleep(2)
#     print('跳完舞了')
# sing()
# dance()

# 2：多线程
# 2.1：线程和进程
# 进程：是操作系统进行资源分配的基本单位，每打开一个程序都至少会有一个进程
# 线程：是cpu调度的基本单位，每一个进程都至少会有一个线程，这个线程就是我们通常所说的主线程
# 一个进程默认有一个线程，一个进程可以有多个线程，线程是依附在进程里面的，没有进程就没有线程

# 2.2:多线程
# Thread线程类的参数
# target：执行的任务名(不要加小括号)
# args：以元组的形式给任务传参
# kwargs：以字典的形式给任务传参
# def sing(name):
#     print(f'{name}在唱歌')
#     time.sleep(2)          
#     print('唱完歌了')
# def dance(name2):
#     print(f'{name2}在跳舞')
#     time.sleep(2)
#     print('跳完舞了')
# # 主程序入口
# if __name__ == '__main__':
#     # 1:创建子线程
#     t1 = threading.Thread(target = sing,args = ('wen',))     
# *******元组中只有一个元素时，必须要加上逗号
#     # print(t1)
#     t2 = threading.Thread(target = dance,args = ('wen',))
#     # 3：守护线程，必须放在start()前面，主线程结束，子线程也会跟着结束
#     t1.setDaemon(True)
#     t2.setDaemon(True)
#     # 2:开启子线程
#     t1.start()
#     t2.start()
#     # 4：阻塞主线程join()：必须放在start()后面，暂停的作用，等子线程执行结束后，主线程才会继续执行
#     t1.join()
#     t2.join() 
#     # 5：获取线程名
#     print(t1.getName())
#     print(t2.getName())
#     # 6：更改线程名
#     t1.setName('子线程一')
#     t2.setName('子线程二')
#     print('表演结束，完美谢幕')

# 2.3：线程之间执行是无序的
# 线程执行是根据cpu调度决定的
# def task():
#     time.sleep(1)
#     print('当前线程是：',threading.current_thread().name)     #显示当前线程名
# if __name__ == '__main__':
#     for i in range(5):
#         # 每循环一次就创建一个子线程
#         t = threading.Thread(target = task)
#         # 启动子线程
#         t.start()

# 2.4：线程之间共享资源
# li = []
# def wdata():
#     for i in range(5):
#         li.append(i)
#         time.sleep(1)
#         print('写入的数据是：',li)
# def rdata():
#     print('读取的数据是：',li)
# if __name__ == '__main__':
#     # 创建子线程
#     wd = threading.Thread(target = wdata)
#     rd = threading.Thread(target = rdata)
#     # 开启子线程
#     wd.start()
#     wd.join()
#     rd.start()
#     rd.join()

# 2.5：资源竞争
# a = 0
# b = 1000000
# def add():
#     for i in range(b):
#         global a
#         a += 1
#     print('第一次累加的结果：',a)
# def add2():
#     for i in range(b):
#         global a
#         a += 1
#     print('第二次累加的结果：',a)
# # add()
# # add2()
# if __name__ == '__main__':
#     a1 = threading.Thread(target = add)
#     a2 = threading.Thread(target = add2)
#     a1.start()
#     a2.start()

# 3：线程同步
# 主线程和创建的子线程之间各自执行完自己的代码直至结束
# a = 0
# b = 1000000
# def add():
#     for i in range(b):
#         global a
#         a += 1
#     print('第一次累加的结果：',a)
# def add2():
#     for i in range(b):
#         global a
#         a += 1
#     print('第二次累加的结果：',a)
# # add()
# # add2()
# if __name__ == '__main__':
#     a1 = threading.Thread(target = add)
#     a2 = threading.Thread(target = add2)
#     a1.start()
#     a1.join()
#     a2.start()
#     a2.join()
# 可以通过join()来阻塞主线程来保证不会出现资源竞争

# 4：互斥锁
# 4.1:对共享数据进行锁定，保证多个线程访问共享数据时不会出现数错误问题；保证同一时刻只能有一个线程操作
# 导入模块
# from threading  import Lock
# # 1:创建全局互斥锁
# lock = Lock()
# a = 0
# b = 1000000
# def add():
#     # 2:上锁
#     lock.acquire()
#     for i in range(b):
#         global a
#         a += 1
#     print('第一次累加的结果：',a)
#     # 3:释放锁
#     lock.release()
# def add2():
#     lock.acquire()
#     for i in range(b):
#         global a
#         a += 1
#     print('第二次累加的结果：',a)
#     lock.release()
# # add()
# # add2()
# if __name__ == '__main__':
#     a1 = threading.Thread(target = add)
#     a2 = threading.Thread(target = add2)
#     a1.start()
#     # a1.join()
#     a2.start()
#     # a2.join()

# 4.2：总结
# 互斥锁的作用：保证线程同步
# 1：上锁和释放锁必须成对出现，不然就会造成死锁
# 2：死锁：一直在等待对方释放锁的情景就叫做死锁
#      死锁会造成应用程序停止响应，不能再处理其他任务
# 3：互斥锁的缺点：会影响代码的执行效率
