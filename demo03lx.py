"""
练习
获取用户的信息并储存到字典中，用户信息包括：姓名、性别、年龄、身高，兴趣爱好。
"""
# a=input("请输入你的姓名：")
# b=input("请输入你的性别：")
# e=input("请输入你的年龄：")
# c=input("请输入你的身高：")
# d=input("请输入你的兴趣爱好：")
# x={"name":a,"sex":b,"age":e,"high":c,"interest":d}
# x={}
# x.update(name=a,sex=b,age=e,high=c,interest=d)
# print(x)


# 判断    判断条件：==,!=,>,<,in,is,not in,not is
# a=1    # == 判断是否相等 ；= 是赋值
# b=2
# if a>b :     #  缩进 代码块
#     print("a>b")
# elif a<b :
#     print("a<b")
# else:
#     print("a=b")
#a=1
# if a ==1:
#     print("ok")
# else:
#     print("no")


# a=input("请输入：")
# if a == "":
#     print("不能为空")
#     exit()
# if a in "0123456789":
#     a=int(a)
# else:
#     print("请输入正确的数字")
#     exit()
# if a> 5:
#     print("大")
# else:
#     print("小")


# a=10
# if type(a) is int :
#     print("是数字")
# elif type(a) is str:
#     print("是字符串")
# else:
#     print("其它")

# 循环 while
# a=1
# while a <  10:
#     print("哈哈哈",a)
#     a=a+1

"""
练习：有十个学生成绩需要录入系统中（张三、李四、王五、浪晋、流云、希希、璐璐、沧海、大狗、二狗）；并且>=60和<60的需要分开存放。

"""
# a=("张三","李四","王五","浪晋","流云","希希","璐璐","沧海","大狗","二狗")
# b={} # 定义一个空字典用来存储大于等于60学生的成绩
# c={} # 定义一个空字典用来存储小于60学生的成绩
# d=0  # 定义了一个变量，用来控制下标的变化
# while d< len(a): #定义了循环的次数，便于录入所有学生的成绩  input
#     i=int(input("请输入"+a[d]+"的成绩"))  # 录入信息，为了判断更改了格式
#     if i>= 60: # 判断分数
#         b[a[d]]=i  #存到字典中
#     else:
#         c[a[d]]=i  #存到字典中
#     d=d+1  # 控制循环次数 每次循环都+1
# print("成绩大于等于60的信息:",b)
# print("成绩小于60的信息:",c)

# for 循环 遍历
# a="你好，今天你吃了吗？"
# for i in a :
#     print(i,end=" ") # end 禁止自动换行
#     print(i)

# range 数列生成器  range(0,100,3) # 步进/步长
# b=list(range(100)) # range左闭右开
# print(b)
# for i in range(10):
#     print(i,end="   ")


"""
a=("张三","李四","王五","浪晋","流云","希希","璐璐","沧海","大狗","二狗")
b={} # 定义一个空字典用来存储大于等于60学生的成绩
c={} # 定义一个空字典用来存储小于60学生的成绩
# d=0  # 定义了一个变量，用来控制下标的变化
for e in a : #定义了循环的次数，便于录入所有学生的成绩  input
    i=int(input("请输入"+e+"的成绩"))  # 录入信息，为了判断更改了格式
    if i>= 60: # 判断分数
        b[e]=i  #存到字典中
    else:
        c[e]=i  #存到字典中
    # d=d+1  # 控制循环次数 每次循环都+1
print("成绩大于等于60的信息:",b)
print("成绩小于60的信息:",c)

"""

# 练习打印九九乘法表

# for i in range(1,10) :
#     for j in range(1,i+1) :
#         print(j,"x",i,"=",i*j,end=" ") # end 禁止自动换行
#     print() # 起到自动换行作用


#  练习1：模拟红绿灯：红灯30秒 绿灯35秒 黄灯 3秒
#  练习2：使用代码实现一个注册的功能。用户输入账号与密码，账号5-8位，密码6-12位，并且账号必须小写字母开头。储存到字典中 {username,password}

# a={"红灯":30,"绿灯":35,"黄灯":3}
# while True:
#     for i in a:
#         for j in range(a[i]):
#             print(i,"还有",a[i]-j,"秒结束")

# c="请重新输入账号，账号必须以小写字母开头,账号5-8位"
# d="请重新输入你的密码,密码6-12位"
# m="a,b,c,d,e,f,g,h,i,j,k,m,l,n,o,p,q,r,s,t,u,v,w,x,y,z"
# e={}
# i=0
# while i < 1:
#     a=input("请输入你的账号")
#     b=input("请输入你的密码")
#     if len(a)>=5 and len(a)<=8 and a[0] in m and len(b)>=6 and len(b)<=12:
#         e[a]=b
#         i=i+1
#     elif len(a)>=5 and len(a)<=8 and a[0] in m :
#         print(d)
        
#     elif len(b)>=6 and len(b)<=12:
#         print(c)
        
#     else:
#         print(c)
#         print(d)

# print(e)




a=input("请输入账号：")
b=input("请输入密码：")
m="a,b,c,d,e,f,g,h,i,j,k,m,l,n,o,p,q,r,s,t,u,v,w,x,y,z"
if len(a)>=5 and len(a)<=8 :
    if a[0] in m:
        if len(b)>=6 and len(b)<=12:
            print("注册成功！",{a:b})
        else:
            print("密码必须6-12位!")
    else:
        print("账号首字母必须小写字母开头！")
else:
    print("账号的长度不符合规范,请输入5-8位账号")