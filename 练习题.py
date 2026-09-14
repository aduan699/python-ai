import threading
import time
from threading import Lock
from multiprocessing import Process,Queue 
# 第一题
# li = []
# [li.append(i) for i in range(2000,3201) if i%7==0 and i%5!=0]
# print(li,sep = ',',end = '')

# 第二题
# li =list(map(int,input().split()))
# res = []
# for n in li:
#     result =1
#     for i in range(1,n+1):
#         result *= i
#     res.append(result)
# for i in res:
#     print(i,sep = ',',end = '')

# # 第三题
# dic = {}
# n = int(input())
# for i in range(1,n+1):
#     dic[i] = i*i
# print(dic)

# #用q队列实现进程间的通信的案例
# def  producer(q):
#     for i in range(5):
#         q.put(i)
#         print(f'{i}已经放入队列')
# def consumer(q):
#     while True:
#         if q.empty():
#             break
#         else:
#             for i in range(5):
#                 print(f'从队列里面取出了{q.get()}')
# if __name__ == '__main__':
#     q = Queue()
#     p1 = Process(target = producer,args = (q,))
#     p2 = Process(target = consumer,args = (q,))
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()

# 第五题
# def getSpring():
#     global t1
#     t1 = str(input('请输入：'))
# def printSpring():
#     global t2
#     t2 = t1.upper()
#     print('大写的字符串是：',t2)
# # if __name__ == '__main__':
# #     x1 = threading.Thread(target = getSpring)
# #     x2 = threading.Thread(target = printSpring)
# #     x1.start()
# #     x1.join()
# #     x2.start()
# #     x2.join()
# def test():
#     getSpring()
#     printSpring()
# test()

# 第六题
