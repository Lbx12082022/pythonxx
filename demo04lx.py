#  练习1：模拟红绿灯：红灯30秒 绿灯35秒 黄灯 3秒
#  练习2：使用代码实现一个注册的功能。用户输入账号与密码，账号5-8位，密码6-12位，并且账号必须小写字母开头。储存到字典中 {username,password}

# a={"红灯":30,"绿灯":35,"黄灯":3}
# while True :
#     for i in a :
#         for j in range(a[i]) :
#             print(i,"还有",a[i]-j,"秒结束")

# a=input("请输入你的账号：")
# b=input("请输入你的密码：")
# m="a,b,c,d,e,f,g,h,i,j,k,m,l,n,o,p,q,r,s,t,u,v,w,x,y,z"
# if len(a) >= 5 and len(a) <=8 :
#     if a[0] in m :
#         if len(b) >=6 and len(b) <=12 :
#             print("注册成功",{a:b})
#         else:
#             print("密码不符合规范,密码必须6-12位!")
#     else:
#         print("账号首字母必须小写字母开头")
# else:
#     print("账号长度不符合规范,账号长度5-8位")

# 跳出循环
# for i in range(10):
#     if i == 4:
#         # continue   # continue 跳过本次循环
#         break        # break 终止循环
#     print(i)

# for i in  range(1,10):
#     for j in range(1,i+1):
#         if i ==3 :
#             break
#         print(j,"x",i,"=",i*j,end=" ")
#     print()


#  函数/方法

# def checkname(a,b) :
#     """
#     自动判断账号必须以小写字母开头,账号5-8位,密码必须6-12位
#     """
#     m="a,b,c,d,e,f,g,h,i,j,k,m,l,n,o,p,q,r,s,t,u,v,w,x,y,z"
#     if len(a)>=5 and len(a)<=8 :
#         if a[0] in m:
#             if len(b)>=6 and len(b)<=12:
#                 return True
#             else:
#                 return "密码必须6-12位!"
#         else:
#             return "账号首字母必须小写字母开头！"
#     else:
#         return "账号的长度不符合规范,请输入5-8位账号"

# a=input("请输入你的账号：")
# b=input("请输入你的密码：")
# if checkname(a,b)==True:
#     print("注册成功!",{a:b})
# else:
#     print(checkname(a,b))

# def 方法的声明
# checkname 方法的名字
# a，b 方法的参数
# 方法的逻辑代码
# a=checkname("lbx123","2222222")
# print(a)


# def jiafa(a,b):
#     """
#     俩个数字之和
#     """
#     if type(a) is int and type(b) is int :
#         return a+b
#     else:
#         return "输入数据类型不正确!"
# # jiafa("333",444)


# 返回值返回后我们可以对它做其它操作，print没有返回值
# print(jiafa(1,1))
# a=[1,2,3,4,5,6]
# b=a.index(2)
# print(a[b])

# def checkname(a):
#     """
#     自动判断账号必须以小写字母开头,账号5-8位
#     """
#     m="a,b,c,d,e,f,g,h,i,j,k,m,l,n,o,p,q,r,s,t,u,v,w,x,y,z"
#     if len(a)>=5 and len(a)<=8 :
#         if a[0] in m:
#             return True
#         else:
#             return "账号首字母必须小写字母开头！"
#     else:
#         return "账号的长度不符合规范,请输入5-8位账号"
# a=input("请输入你的账号：")
# b=input("请输入你的密码：")
# if checkname(a)== True :
#     if len(b)>=6 and len(b)<=12:
#         print("注册成功！",{a:b})
#     else:
#         print("密码必须6-12位!")
# else:
#     print(checkname(a))

# def jiafa(a,b):
#     """
#     俩个数字之和
#     """
#     if type(a) is int and type(b) is int :
#         return a+b
#     else:
#         return "输入数据类型不正确!"
# a=jiafa(1,2)
# print(a+3)

#  异常捕获 异常类
# try:
#     print(a+1)
# except Exception as e:  #  异常类
#     print("写错了",e)

# a=input("请输入你的名字")
# b=input("请输入你的年龄")
# try:
#     if int(b)>=18:
#         print(a,"成年了")
#     else:
#         print(b,"未成年")
# except:
#     print("请输入正确的年龄")
# 处理用户输入的数据


import time    #  时间包
import random  #  生成随机数
import pymysql
# for i in range(10)
#     time.sleep(1)
#     print(i)


# a=random.randint(0,100)
# print(a)


# db=pymysql.connect(host="127.0.0.1",user="root",password="123456",db="testdb")
# cur=db.cursor()
# try:
#     cur.execute("select*from t_class;")
#     res=cur.fetchall()
#     print(res)
# except:
#     print("spl语句错误")