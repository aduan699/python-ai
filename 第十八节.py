import re
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
li = ['www.baidu.com','www.python.org','http.jd.cn','www.py.en','www.abc.cn']
# res = re.match(r'www(\.)\w*\1(com|cn|org)','www.baidu.com')
# print(res.group())
for i in li:
    res = re.match(r'www(\.)\w*\1(com|cn|org)',i)
    if res == None:
        print(f'{i}这个网址不合规')
    else:
        print(res.group())