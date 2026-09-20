import re
# 第一小节
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

# 2.7：\w 匹配单词字符 a-z A-Z _ 汉字，数字都可以匹配   ----常用
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

# 第二小节
# 1：匹配分组
# 1.1：| 匹配左右任意一个表达式   ----常用
# res = re.match('abc|def','def')
# print(res.group())
# 匹配时会优先匹配左边的，如果左边匹配不到就匹配右边的

# 1.2：(ab) 将括号中的字符作为一个分组   ----常用
# res = re.match('\w*@(163|qq|155).com','123@155.com')
# print(res.group())

# 1.3：\num 匹配分组num匹配到的字符串   ----经常在匹配标签的时候被使用
# res = re.match(r'<(\w*)>\w*</\1>','<html>login</html>')
# res = re.match(r'<(\w*)><(\w*)>\w*</\2></\1>','<html><body>login</body></html>')
# print(res.group())
# 注意：从外到内排序，编号从1开始

# 1.4：(?P<name>) 分组起别名
# 1.5：(?P=name)  引用别名为name分组匹配到的字符串
# res = re.match(r'<(?P<l1>\w*)><(?P<l2>\w*)>\w*</(?P=l2)></(?P=l1)>','<html><body>login</body></html>')
# print(res.group())

# 综合举例：匹配网址   前缀一般是www,后缀一般是.com , .cn , .org
# li = ['www.baidu.com','www.python.org','http.jd.cn','www.py.en','www.abc.cn']
# res = re.match(r'www(\.)\w*\1(com|cn|org)','www.baidu.com')
# print(res.group())
# for i in li:
#     res = re.match(r'www(\.)\w*\1(com|cn|org)',i)
#     if res == None:
#         print(f'{i}这个网址不合规')
#     else:
#         print(res.group())

# 2：高级用法
# 2.1：search：扫描整个字符串并返回第一个匹配成功的对象，如果没有匹配成功，就返回None
# res = re.search('\d','pyth2on3')
# print(res.group())

# 2.2:findall：从头到尾匹配，返回所有匹配到的对象
# res = re.findall('\d','py123456thon')
# print(res)
# 注意：使用findall时不用group()取值，直接打印就可以了

# 总结
# match()：从头开始匹配，匹配成功返回match对象，通过group()进行提取，只匹配一次
# serach()：从头到尾进行匹配，匹配成功返回第一个匹配到的对象，通过group()进行提取，只匹配一次
# findall()：从头到尾匹配，匹配成功返回所有匹配到的对象，不需要通过group()的方法提取

# 2.3：sub(pattern,repl,string,count)
# pattern：正则表达式（需要被替换的内容，也就是字符串里面的旧内容）
# repl：   新内容
# string： 字符串
# count：  要替换的次数
# res = re.sub('bing','b','hellobingbing',1)
# print(res)
# res = re.sub('\d','2','这是这个月的第30天',1)
# print(res)

# 2.4:split(pattern,string,maxsplit)
# pattern：正则表达式
# string：字符串
# maxsplit：最大分割次数
# res = re.split('\D','123w456e789',1)
# print(res)

# 3：贪婪与非贪婪
# 3.1：贪婪匹配（默认）：在满足匹配时，尽可能匹配长的字符串
# res = re.match('em*','emmmmm')
# print(res.group())

# 3.2：非贪婪匹配：在满足匹配时，尽可能匹配短的字符串，使用？来表示非贪婪匹配
# res = re.match('em+?','emmmmm')
# print(res.group())
# res = re.match('m{1,5}?','mmmmm')
# print(res.group())

# 4：原生字符串
# print(r'sixs\tar')     r表示取消转义
# res = re.match(r'\\','\game')
# print(res.group())
# 正则表达式要匹配\字符时需要\\\\

# 练习题
# 1：提取手机号
# li = ['张三13812345678','李四15999001122','abc123456789','1388888']
# for i in li:
#     res = re.search('1\d{10}',i)
#     if res == None:
#         print(f'{i}中没有手机号码')
#     else:
#         print(res.group())
# 2：提取邮箱地址
# res = re.findall(r'\w+@\w+\.\w{2,6}','contact me at test123@qq.com or abc_xyz@school.cn')
# print(res)
# 注意：\w还可以匹配下划线
# 3：匹配简单日期
# str = '今天2026-09-16,昨天2026-09-15,2026/9/16 2026-9-5'
# res = re.findall(r'\d{4}-\d{2}-\d{2}',str)
# print(res)
# 4：去除掉文本里的<>
# str = '<p>这是<b>加粗</b>文字</p>'
# res = re.sub('<.*?>','',str)
# print(res)
# 注意：这里要用非贪婪匹配，不然会把整个字符串都吞掉
# 5：提取文本中的http://
# str = '访问https://www.baidu.com http://github.com'
# res = re.findall(r'https?://\S+',str)
# print(res)