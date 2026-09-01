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
li = [1,2,3,4,5]
print(id(li))
li.append(6)
print(li,id(li))