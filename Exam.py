import string
import random
import os

print("猜数字游戏\n游戏开始时由电脑随机生成四位数字\n玩家需要对这个四位数字进行猜测\n每次猜测过后电脑都会给出猜测的结果")
print("A代表数字正确且位置正确\nB代表数字正确但位置错误\n游戏共有四个难度\neasy难度下电脑将生成四个不重复的数字")
print("normal难度下电脑将生成四个可重复的数字\nhard难度下电脑将生成四个不重复的字母\nhell难度下电脑将生成四个不重复的字母或数字")
print("从hard难度开始可解锁提示功能\n可提示谜底的其中一个数字是什么\n相信你已经明白怎么玩了\n现在就让我们开始吧!")
level = input("请选择难度:")
while level != "easy" and level != "normal" and level != "hard" and level != "hell":
    level = input("错误，请重新输入:")
if level == "easy":
    num = random.sample(range(1,10),4)#生成待猜测的不重复四位数
elif level == "normal":
    num = [random.randint(1,9) for i in range(4)]#生成可重复的四位数
elif level == "hard":
    num = []
    while len(num) < 4:
        letter = string.ascii_lowercase
        RandomLetter = random.choice(letter)
        if RandomLetter not in num:
            num.append(RandomLetter)
    hint = input("是否需要提示?(Y/N)")#生成四个不重复字母
    while hint != "Y" and hint != "N":
        hint = input("错误，请重新输入:")
elif level == "hell":
    num = []
    resource = ['1','2','3','4','5','6','7','8','9']
    while len(resource) < 35:
         letter = string.ascii_lowercase
         RandomLetter = random.choice(letter)
         if RandomLetter not in resource:
             resource.append(RandomLetter)
    while len(num) < 4:
        element = resource[random.randint(0,34)]
        if element not in num:
            num.append(element)
    hint = input("是否需要提示?(Y/N)")#生成四个不重复数字、字母
    while hint != "Y" and hint != "N":
        hint = input("错误，请重新输入:")


if level == "hard" and hint == "Y":
    print(num[random.randint(0,3)])
if level == "hell" and hint == "Y":
    print(num[random.randint(0,3)])
#提示判定

#print(num) #调试开关

A=0
B=0
#设定判断参数

def judge1(a,b):
    global A
    global B

    if int(a[0]) in b:
        if int(a[0]) == b[0]:
            A+=1
        else:
            B+=1
#判断第一位数为A或B，下同理
    if int(a[1]) in b:
        if int(a[1]) == b[1]:
            A+=1
        else:
            B+=1

    if int(a[2]) in b:
        if int(a[2]) == b[2]:
            A+=1
        else:
            B+=1

    if int(a[3]) in b:
        if int(a[3]) == b[3]:
            A+=1
        else:
            B+=1

    if A==4:
        print("right")
    elif A<4:
        print("%dA%dB"%(A,B))

def judge2(a,b):
    global A
    global B

    if a[0] in b:
        if a[0] == b[0]:
            A+=1
        else:
            B+=1
#判断第一位数为A或B，下同理
    if a[1] in b:
        if a[1] == b[1]:
            A+=1
        else:
            B+=1

    if a[2] in b:
        if a[2] == b[2]:
            A+=1
        else:
            B+=1

    if a[3] in b:
        if a[3] == b[3]:
            A+=1
        else:
            B+=1

    if A==4:
        print("right")
    elif A<4:
        print("%dA%dB"%(A,B))#判断猜中个数

while A<4 and level == "easy":
    guess = input("请输入猜测:")
    judge1(guess,num)
    if A == 4:
        break#胜利时跳出循环
    A=0
    B=0

while A<4 and level == "normal":
    guess = input("请输入猜测:")
    judge1(guess,num)
    if A == 4:
        break#胜利时跳出循环
    A=0
    B=0

while A<4 and level == "hard":
    guess = input("请输入猜测:")
    judge2(guess,num)
    if A == 4:
        break#胜利时跳出循环
    A=0
    B=0

while A<4 and level == "hell":
    guess = input("请输入猜测:")
    judge2(guess,num)
    if A == 4:
        break#胜利时跳出循环
    A=0
    B=0

os.system('pause')