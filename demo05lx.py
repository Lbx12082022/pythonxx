
# def checkname(a,b):
#     """
#     自动判断账号必须以小写字母开头,账号5-8位;密码6-16位
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
# c=checkname(a,b)
# if c is True:
#     print({a:b})
# else:
#     print(c)


"""
class 声明类的名字
类的首字母必须大写
面向对象编程

"""
class Girlfriend():
    """
    女朋友
    """
    def __init__(self,sex,high,weight,hair,age):
        self.sex=sex
        self.high=high
        self.weight=weight
        self.hair=hair
        self.age=age
    def talentshow(self,num):
        """
        才艺表演
        """
        if num == 1:
            print("唱")
        elif num == 2:
            print("跳")
        elif num == 3 :
            print("rap")
        else:
            print("篮球")
    def cookingskill(self) :
        """
        厨艺
        """
        print("精通八大菜系！！！中外贯通！！！糕点大师！！！") 
    def work(self): 
        """
        工作挣钱
        """    
        print("按摩正骨")


# # 类的实例化
# a=Girlfriend("女","170cm","55kg","黑长直","18岁")
# a.talentshow(4)
# a.work()
# print(a.age)

class Car():
    def __init__(self,pinpai,yanse,neishi,mali):
        self.pinpai=pinpai
        self.yanse=yanse
        self.neishi=neishi
        self.mali=mali
    def bianxing(self):
        print("启动变形！！正在变形为霸天虎！！！")
    def fly(self):
        print("飞行模式开始！！！准备飞行！！！")

# a=Car("奔驰","五颜六色","真龙内饰","9.0T")
# a.bianxing()
# a.fly()
# print(a.pinpai)


class Nvpengyou(Girlfriend):
    def work(self):
        print("修电脑")
a=Nvpengyou("nv","180cm","70kg","hcz","18")
a.work()

# 父类
# 子类
# object 所有类的起点/祖宗

import time
now=time.strftime("%y-%m-%d %H:%M:%S")
print(now)
text= input("请输入今天的心情：")  # "w"写入；"a"追加
with open("日记.txt","a",encoding="utf8") as f : 
    f.write(now+"\n")
    f.write(text+"\n")
    f.write("----------\n")