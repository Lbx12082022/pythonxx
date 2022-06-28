# 判断  缩进  代码块
# a=1
# b=2
# if a==1:     #  ==判断 = 赋值
#     print("哈哈哈")
# if a>b:
#     print("a>b")
# else:    
#     print("a<b")
# age=int(input("请输入你的年龄:"))
"""
if age>60:
    print("老了")
elif age>40:
    print("中年")
elif age>20:
    print("少壮")
else:
    print("青年")
"""
# if age<20 and age>0 :
#     print("青年")
# elif age<40:
#     print("少壮")
# elif age<60:
#     print("中年")
# else:
#     print("老了")
#  in

# a = input("请输入：")
# if a == "":
#     print("请重新输入")
#     exit()
# if a in "0123456789":  # in的用法
#     a =int(a)
# else:
#     print("请输入正确的年龄")
#     exit()
# if a > 5:
#     print("大")
# else:
#     print("不大")


# a="sdfggjkk"
# if type(a) is int:  #is是判断类型
#     print("是数字")
# elif type(a) is str:
#     print("是字符串")
# else:
#     print("其它类")

# a=1
# while a<10 :      # while循环
#     print("哈哈哈",a)
#     a = a+1
"""
练习:有10个学生成绩需要录入系统中(张三、李四、王五、浪晋、流云、希希、沧海、大狗、二狗、亚索);且>60和<60的需要分开存放

"""


"""
studentlist = ["张三","李四","王五","浪晋","流云","希希","沧海","大狗","二狗","亚索"]
h={} #成绩及格学生
d={} #成绩不及格学生
a=0     # 我自己写的
while a<10 :
    grade=int(input("请输入"+studentlist[a]+"的成绩"))
    if grade >=60.0:
        h[studentlist[a]]=grade
    else:
        d[studentlist[a]]=grade
    a=a+1
print("大于60的:",h)
print("小于60的:",d)
"""


"""
s= ["张三","李四","王五","浪晋","流云","希希","沧海","大狗","二狗","亚索"]
b={}
c={}
a=0
while a < len(s):
    grade = int(input("请输入"+s[a]+"的成绩"))
    if grade>=60:
        b[s[a]]=grade
        #b.update(s[a]=grade)
    else:
        c[s[a]]=grade
        # c.update(s[a]=grade)
    a=a+1
print("成绩大于等于60的学生:",b)
print("成绩小于60的学生:",c)

"""

"""
# for循环  遍历
s= ["张三","李四","王五","浪晋","流云","希希","沧海","大狗","二狗","亚索"]
# a="你好，今天你吃了吗？"
for i in s:
    print(i)
# range  数列生成器
b=list(range(0,100,3))  # 左闭右开 自动生成一个数列  步进/步长
print(b)
for i in range(10):
    print(i)
"""


"""
s= ["张三","李四","王五","浪晋","流云","希希","沧海","大狗","二狗","亚索"]
b={}
c={}
for i in s:
    grade = int(input("请输入"+i+"的成绩"))
    if grade>=60:
        b[i]=grade
        #b.update(s[a]=grade)
    else:
        c[i]=grade
        # c.update(s[a]=grade)
print("成绩大于等于60的学生:",b)
print("成绩小于60的学生:",c)

#  练习打印九九乘法表



for i in  range(1,10):
    for j in range(1,i+1):
        print(j,"x",i,"=",i*j,end=" ")
    print()
"""

"""
s= ["张三","李四","王五","浪晋","流云","希希","沧海","大狗","二狗","亚索"]
for i in s :
    print(i,end="||||")  # end禁止自动换行
    print()  # 自动换行的作用

"""
#  练习1：模拟红绿灯：红灯30秒 绿灯35秒 黄灯 3秒
#  练习2：使用代码实现一个注册的功能。用户输入账号与密码，账号5-8位，密码6-12位，并且账号必须小写字母开头。储存到字典中 {username,password}

# a=1
# while a<2:
#     for i in range(30):
#         print("红灯还有",30-i,"秒结束")
#     for j in range(35):
#         print("绿灯还有",35-j,"秒结束")
#     for k in range(3):
#         print("黄灯还有",3-k,"秒结束")
#         a=a+1


# a=input("请输入你的账号")
# b=input("请输入你的密码")
c="请重新输入账号，账号必须以小写字母开头,账号5-8位"
d="请重新输入你的密码,密码6-12位"
m="a,b,c,d,e,f,g,h,i,j,k,m,l,n,o,p,q,r,s,t,u,v,w,x,y,z"
e={}
i=0
while i < 1:
    a=input("请输入你的账号")
    b=input("请输入你的密码")
    if len(a)>=5 and len(a)<=8 and a[0] in m and len(b)>=6 and len(b)<=12:
        e[a]=b
        i=i+1
    elif len(a)>=5 and len(a)<=8 and a[0] in m :
        print(d)       
    elif len(b)>=6 and len(b)<=12:
        print(c)    
    else:
        print(c)
        print(d)
print(e)