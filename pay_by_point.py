# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

get_money = input().split()
#print(get_money)

money = int(get_money[0])
point = int(0)
loop = int(get_money[1])

import sys
line = sys.stdin.readlines()
#print(line)

for i in range(loop):
    use = int(line[i])
    if use <= point:
        point -= use
    else:
        money -= use
        point += int(use/10)
    print(money,point)
    i += 1
