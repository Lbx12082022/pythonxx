"""
class  声明类的名字
类的名字首字母必须大写
面对对象编程
类里面所以的方法,都必须要传一个参数self。
"""


class Girlfriend():
    """
    女朋友
    """
    def __init__(self,sex,high,weight,hair,age):
        self.sex = sex
        self.high = high
        self.weight = weight
        self.hair = hair
        self.age = age
    def talentshow(self,num) :
        """
        才艺表演
        """
        print("你的"+self.age+"身高"+self.high+"体重"+self.weight+"发型"+self.hair+"年龄"+self.age+"的"+self.sex+"朋友开始了")
        if num == 1:
            print("唱歌")
        elif num == 2:
            print("跳舞")
        elif num == 3:
            print("rap")
        else:
            print("篮球")
    def cookingskill(self):
        """
        厨艺持家
        """
        print("你的"+self.age+"身高"+self.high+"体重"+self.weight+"发型"+self.hair+"年龄"+self.age+"的"+self.sex+"朋友开始了")
        print("精通八大菜系！中外融合！糕点大师！！！")
    def work(self):
        """
        工作挣钱
        """
        print("你的身高"+self.high+"体重"+self.weight+"发型"+self.hair+"年龄"+self.age+"的"+self.sex+"朋友开始了")
        print("按摩正骨")



# #  类的实例化
# a = Girlfriend("女","180cm","60","黑长直","18")
# a.talentshow(3)
# a.work()
# a.cookingskill()
# a.talentshow(1)
# print(a.high)

# class Car():
#     def __init__(self,pinpai,yanse,neishi,dongli):
#         self.pinpai=pinpai
#         self.yanse=yanse
#         self.neishi=neishi
#         self.dongli=dongli
#     def bianxing(self):
#         print("启动变形！正在变身为霸天虎！！！")
#     def fly(self):
#         print("正在开始起飞！！！")

# a=Car("奔驰","灰黑色","龙皮内饰","3.0T")
# a.bianxing()

# class nvpengyou(Girlfriend):
#     pass
# a = nvpengyou("女","180cm","60kg","黑长直","18岁")
# a.work()
# Girlfriend  父类
# nvpengyou   子类  继承了父类所有的参数
# object      总类

# class nvpengyou(Girlfriend):
#     def work(self):
#         print("修电脑")  # 重写/多态
# a = nvpengyou("女","180cm","60kg","黑长直","18岁")
# a.work()


#   python文件的读写
# text= input("请输入今天的心情：")
# with open("日记.txt","a",encoding="utf8") as f : # "w" 写入 "a"  追加
#     f.write(text)

import time
now= time.strftime("%y-%m-%d %H:%M:%S")
text = input("请输入你此时的心情：")
with open("C:\workhome\zhangsan\日记.txt","a",encoding="utf8") as f :
    f.write(now+"\n")
    f.write(text+"\n")
    f.write("----------------\n")
