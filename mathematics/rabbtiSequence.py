#斐波那契数列 又称 兔子数列
#这个数列从第3项开始，每一项都等于前两项之和。


count = 0
seqList = [1, 1, ]
num1 = num2 = 1

while 1:
    num1, num2 = num2, num1 + num2
    seqList.append(num2)
    count += 1
    if count == 100:
        break

print(seqList)
