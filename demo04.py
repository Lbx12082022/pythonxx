# for i in range(10):
#     if i==4:
#         #continue  # 跳过本次循环
#         break  # 终止循环 跳出循环
#     print(i)

# for i in range(1,10) :
#     for j in range(1,i+1) :
#         if i ==9:
#             break  # 跳出一层循环
#         print(j,"x",i,"=",i*j,end=" ") # end 禁止自动换行
#     print() # 起到自动换行作用

#  函数/方法

# def checkname(a):
#     """
#     自动判断账号必须以小写字母开头,账号5-8位
#     """
#     m="a,b,c,d,e,f,g,h,i,j,k,m,l,n,o,p,q,r,s,t,u,v,w,x,y,z"
#     if len(a)>=5 and len(a)<=8 :
#         if a[0] in m:
#             print("ok")
#         else:
#             print("账号首字母必须小写字母开头！")
#     else:
#         print("账号的长度不符合规范,请输入5-8位账号")
# def       方法的声明
# checkname 方法的名字
# a         方法的参数
# """ """   方法的说明
#           方法的逻辑代码
# a="QWER"
# checkname("a")


# def jiafa(a,b):
#     """
#     实现俩个数字相加
#     """
#     if type(a) is int and type(b) is int :
#         return  a+b
#     else:
#         return  "输入的数据类型不正确"
        

# jiafa("3",55)
"""
返回值，返回后我们可以做其它的工作，而print不能
"""

# a=[]
# print(a.append("哈哈")) None
# print(a.count("哈哈")) 1
# print(jiafa(1,1))
# a=[1,2,3,4,5,6,7]
# x=a.index(2)
# print(a[x])


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
#     实现俩个数字相加
#     """
#     if type(a) is int and type(b) is int :
#         return  a+b
#     else:
#         return  "输入的数据类型不正确"
# a= jiafa(1,2)
# print(a+2)


#  异常捕获
# try:
#     print(2+1)
# except:
#     print("代码写错了")

# 异常类  包->类->方法->变量 (包含并列的关系)
# try:
#     print("2"+1)
# except Exception as e:
#     print("代码写错了",e)

# a=input("请输入你的名字：")
# b=input("请输入你的年龄：")
# try:
#     if int(b)>=18:
#         print(a,"成年了")
#     else:
#         print(a,"未成年")
# except:
#     print("请输入正确的年龄")
# 处理用户输入的数据


import time  #  时间包   一般写在代码开头
import random # 生成随机数
import pymysql # 连接数据库
# for i in range(10):
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

"""
练习：
定义一个方法用来判断用户输入的账号密码是否符合规范

"""

def checkname(a,b):
    """
    自动判断账号必须以小写字母开头,账号5-8位;密码6-16位
    """
    m="a,b,c,d,e,f,g,h,i,j,k,m,l,n,o,p,q,r,s,t,u,v,w,x,y,z"
    if len(a)>=5 and len(a)<=8 :
        if a[0] in m:
            if len(b)>=6 and len(b)<=12:
                return True
            else:
                return "密码必须6-12位!"
        else:
            return "账号首字母必须小写字母开头！"
    else:
        return "账号的长度不符合规范,请输入5-8位账号"


checkname("zhangsan","1234567")