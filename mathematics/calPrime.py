#计算素数


prime = [] #使用List保存素数
prime1 = [1,]  # 1能整除所有数，特殊排除

for i in range(2,1000):
    for j in prime:#所有合数都能被一个素数整除
        if (i % j == 0):
            break
    else:
        prime.append(i)
print(prime)
print(len(prime))

'''关于循环else语句判断，
    else是在循环正常完成后才会被执行，
    正常完成时指系统判断循环停止时待循环项中是否还有待循环项，如果有就是非正常结束，else语句不会执行'''