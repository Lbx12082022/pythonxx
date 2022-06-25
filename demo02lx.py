# 元组下标从0开始编号
"""
a=(1,2,3,4,5,6)
print(a[1])
a=("我","爱","中","国","你","好")
print(a[0]+a[1]+a[4])
print(a[0],a[1],a[4])
print(a[0])
print(a[1])
print(a[4])
# 切片
a=("我","爱","中","国","你","好")
print(a[0:2])  #  左闭右开
print(a[2:3])
print(a[3:])
#  提取下标
b=a.index("国")
print(b)
print(a.index("国"))
#  统计个数
print(a.count("国"))

#   二维元组
a=("我","爱","中","国","你","好")
b=(a,"嘻嘻","哈哈")
# print(b[0],b[1])
# print(a[3])
# 数组
a=[1,2,3,4,5,"我","爱","中","国","国","国","国","国","国","你","好"]
# a.append("append1")
# a.append("append2")
#  元组一旦写好不可更改，数组可以修改
b=a.index("国")
c=a.count("国")
print(b,c)
#  插入
# a.insert(0,"insert1")
# a.insert(-1,"insert1")
# print(a)
# 剪切
b = a.pop(5)
c = a.pop(5)
print(b+c)
print(a)
a=[1,2,3,4,5,"我","爱","中","国","国","国","国","国","国","你","好"]
# clear  清空
# a.clear()
# print(a)
# a.extend() 合并多个数组
x=["嘻嘻","哈哈"]
a.extend(x)
# print(a+x) # 和a.extend()一样
# print(a)
# remove() 移除某个值
a.remove(a[8])
x=[0,1,True,False]
print(x.count(0))
# 下标不要超出范围= 越界
print(x[2])
"""
"""
这就是Python语法一部分：
1、所有的方法都是以0结尾 比如：print(),index(),count(),insert(),remove(),clear(),extend(),pop()
2、元组、数组、字典、的取值都用[] 比如：a[0]
3、数组、元组、字典的定义分别是[],(),{}
"""
"""
  字典
1、 字典的值没有顺序
2、 字典的结构必须是 键值对结构 key:value
3、 字典的取值都是通过key去取value
4、 所以字符串都要加""
a={
    "name":"张三",
    "sex":"女",
    "age":"29"
     }
#  取值    
print(a["name"])
#  新增
a["high"]="170cm"
#  修改
a["name"]="李四"
print(a)
print(a["name"])
print(a["name"],a["sex"])
print(a["name"]+a["sex"])
a["interest"]="游泳"
print(a)
# 取值
b=a.get("name")
print(b)
# print(a["name11"])
# print(a.get("name11"))
# 剪切 a.pop()
# b=a.pop("name")
# print(a)
# print(b)
# 更新 update()
a.update(name="哈哈")
print(a)
# 数组和字典的通用删除方法 del
del a["name"]
print(a)
a=[1,2,3,4,5,6]
print(a)
del (a[0],a[0])
print(a)
"""


"""
练习
获取用户的信息并储存到字典中，用户信息包括：姓名、性别、年龄、身高，兴趣爱好。
"""
a=input("请输入你的名字:")
b=input("请输入你的性别:")
c=input("请输入你的年龄:")
d=input("请输入你的身高:")
e=input("请输入你的兴趣:")
x={"name":a,"sex":b,"age":c,"high":d,"interest":e}

print(x)