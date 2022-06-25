#  元组，下标（从0开始编号）
#  a=()  # 空的元组
"""(
a=(1,2,3,4,"哈哈","嘻嘻",True,False)
a[0]  # 
print(a[4])
print(a[5])
a=("我","爱","中","国","你","好",)
print((a[0]+a[1]+a[4])*9)
print(a[0]*10)
print(a[1]*10)
print(a[4]*10)



#切片
a=("我","爱","中","国","国","国","国","国","国","国","国","国","你","好",)
print(a[0:4])  #左闭右开
print(a[4:9])
print(a[9:])
print(a)
print(a[:])
print(a[0]*10)
print(a[1]*10)
print(a[-2]*10)


a=("我","爱","中","国","国","国","国","国","国","国","国","国","你","好",)
#  a.index("国")   提取下标
print(a.index("国"))
#  a.count("国")   统计""的个数
print(a.count("国"))
# 二维元组
a=("我","爱","中","国","国","国","国","国","国","国","国","国","你","好",)
b=(a,"哈哈","嘻嘻")
print(b[0][3])
print(a[3])

#  数组
# a=["我","爱","中","国","国","国","国","国","国","国","国","国","你","好",]
#  print(a[4])
a.append("append1")
a.append("append2")
# 元组一旦写好不可以修改，数组可以修改
# a.index()
# a.count()
# a.insert(0,"insert")
# a.insert(-1,"insert-1")
# a.insert(99,"insert")
#  print(a)


a.pop(0) #  剪切
b = a.pop(0)
c = a.pop(0)

print(b+c)
print(c)


a=[1,2,3,4,5,"我","爱","中","国","国","国","国","国","国","国","国","国","你","好",]
#  a.clear()  清空
#  a.extend()  插入多个数据
xx=["你好","不好"]
# a.extend(xx)
print(a+xx)
a.remove(1)
print(a)
x=(0,1,True,False)
a=x.count(0)
print(a)
#  下标不要超出范围 = 越界
s=[1,2,3,4,5]
s[2]
"""

"""
这就是Python语法一部分
所有的方法都是()结尾。 比如 print(),input,len(),insert(),count(),index()
元组，数组，字典的取值，都用[]。比如 a[0]
元组，数组，字典的定义，分别是(),[],{}

"""
#  字典
"""
1 字典中的值没有顺序
2 字典的结构必须是 键值对的结构。  key：value
3 字典的取值，是通过key去取这个value
4 任何地方字符串都要加""



a={
     "name":"张三",
     "sex":"女",
     "age":"29"
     }
# 取值
print(a["name"])
# 新增
a["high"]="183cm"
print(a)
# 修改    
a["name"]="李四"
print(a)
print(a["name"])
print(a["sex"])
print(a["age"])
print(a["high"])
print(a["name"],a["sex"])
print(a["name"]+a["sex"])
a["interest"]="打篮球"
print(a)
a["interest"]="游泳"
print(a)
# get 取值
b=a.get("name")
print(b)
#  print(a.get("name11"))
#  print(a["name11"])

# pop 剪切
b=a.pop("name")
print(b)
print(a)
# update  更新
a.update(name=1111)
print(a)
a.update(name="哈哈")
print(a)
# value
#  数组和字典删除的通用方法
del a["name"]
print(a)
a=[1,2,3,4,5]
del a[0]
print(a)
"""
"""
练习：
获取用户的个人信息并存储到字典中
个人信息包括：age,sex,age,high,niterest,
"""
x={"name":"a","sex":"b","age":"c","high":"d","interest":"e"}
a=input("请输入你的名字:")
b=input("请输入你的性别:")
c=input("请输入你的年龄:")
d=input("请输入你的身高:")
e=input("请输入你的兴趣:")

print(x)