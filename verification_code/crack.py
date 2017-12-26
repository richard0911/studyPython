from PIL import Image

im = Image.open('captcha.gif', 'r')  # 以只读模式打开文件
im.convert("P")  # 将图片转换为8位像素模式

his = im.histogram()
values = dict()

for i in range(256):
    values[i] = his[i]


for j, k in sorted(values.items(), key=lambda x: x[1],
                   reverse=True)[:10]:
    print(j, k)

