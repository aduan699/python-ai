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
class person():
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height
    def play(self):
        print(f'{self.name}正在玩王者荣耀')
    def introduce(self):
        print(f'{self.name}的年纪是{self.age},身高是{self.height}')
pe = person('duan',20,180)
pe.play()
pe.introduce()