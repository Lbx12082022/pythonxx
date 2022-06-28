import time
now= time.strftime("%y-%m-%d %H:%M:%S")
text = input("请输入你此时的心情：")
with open("C:\workhome\zhangsan\日记.txt","a",encoding="utf8") as f :
    f.write(now+"\n")
    f.write(text+"\n")
    f.write("----------------\n")