import random

# 1. 生成随机数
answer = random.randint(1, 10)

print("🎮 猜数字游戏开始！")
print("我已经想好了一个1-10之间的数字")

# 2. 循环猜
while True:
    guess = int(input("请输入你的猜测："))

    if guess > answer:
        print("📉 太大了")
    elif guess < answer:
        print("📈 太小了")
    else:
        print("🎉 猜对了！")
        break
