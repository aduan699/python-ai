import re
# 1：正则表达式
# 字符串处理工具
# 注意：需要导入re模块

# 1.2：特点
# 优点：正则表达式通用性很强，多种编程语言都可以使用
# 缺点：语法比较复杂，可读性较差

# 1.3：步骤
# 1：导入re模块
# 2：使用match方法进行匹配
#    re.match()能匹配以xxx开头的字符串
#    如果起始位置没有匹配成功，返回None
# re.match(pattern,string)
# pattern：要匹配的正则表达式是
# string：要匹配的字符串
# res = re.match('冰','冰冰永远十八')
# print(res)
# 3：如果上一步匹配成功，使用group()提取数据
# print(res.group())

# 2：匹配单个字符
# 2.1：. 匹配任意一个字符，\n除外 ----常用
# res = re.match('..','hello')
# print(res.group()) 

# 2.2：[]匹配[]中列举的字符  ----常用
# 匹配的字符串的开头在[]中有就算匹配成功
# res = re.match('[he]','hello')
# res = re.match('[1234]','4321')
# 第一种匹配0-9的写法
# res = re.match('[0123456789]','654321')
# 第二种匹配0-9的写法
# res = re.match('[0-9]','666')
# res = re.match('[a-zA-Z]','hello')
# a-zA-Z代表列举出所有大小写的字母
# print(res.group())

# 2.3：\d 匹配数字0-9   ----常用
# res = re.match('\d\d','630')
# print(res.group())

# 2.4：\D 匹配非数字    ----常用
# res = re.match('\D\D','s.66')
# \D只要不是数字就都能匹配
# print(res.group())

# 2.5：\s 匹配空白，即空格和tab键
# tab键是两个空格
# res = re.match('\s.',' 6991')
# print(res.group())

# 2.6：\S 匹配非空白
# 只要不是空白就都可以匹配
# res = re.match('\S',',6991')
# print(res.group())

# 2.7：\w 匹配单词字符 a-z A-Z _ 汉字都可以匹配   ----常用
# res = re.match('\w','我了我了')
# print(res.group())

# 2.8：\W 匹配非单词字符
# res = re.match('\W',',BING')
# print(res.group())

# 3：匹配多个字符
# 3.1：* 匹配前一个字符出现0次或者无限次，即可有可无   ----常用
# res = re.match('\d*','bingbing')
# print(res.group())
# print(res)

# 3.2：+ 匹配前一个字符出现1次或者无限次，即至少一次   ----常用
# res = re.match('\d+','12hello')
# print(res.group())

# 3.3：？匹配前一个字符出现一次或者0次                ----常用
# res = re.match('\w?','地主家的傻儿子')
# print(res.group())

# 3.4：{m} 匹配前一个字符出现m次
# res = re.match('\w{3}','python')
# print(res.group())

# 3.5：{m,n} 匹配前一个字符出现m次到n次
# 注意：必须满足m<n的条件
# res = re.match('\w{1,3}','嘿,,..')
# print(res.group())

# 4：匹配开头和结尾
# 4.1：^ 表示匹配以xxx开头或者表示取反
# res = re.match('^py','python')
# print(res.group())
# ^ 第二个作用：在[]里面则表示匹配不到
# res = re.match('[^py]','python')
# [^py]表示可以匹配到除了p,y之外的字符
# print(res.group())

# 4.2：$ 表示匹配字符串结尾
# res = re.match('.{7}\w$','bingbing')
# print(res.group())