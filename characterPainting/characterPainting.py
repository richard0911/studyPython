from PIL import Image
import argparse

#为命令行调用设定参数
parser = argparse.ArgumentParser()

parser.add_argument('file') #输入文件
parser.add_argument('-o', '--output') #输出文件
parser.add_argument('--width', type=int, default=80) #输出字符画宽度
parser.add_argument('--heigth', type=int, default=80) #输出字符画高度

#获取参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGTH = args.heigth
OUTPUT = args.output

#定义一个字符列表
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


'''通过公式来计算灰度，并在字符列表中找到想要的值来替换'''
def get_char(r, g, b, alpha =256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGTH), Image.NEAREST)#重定义图片大小

    txt = ""

    for i in range(HEIGTH):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    print(txt)

    #字符画输出到文件
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open('output.txt', 'w') as f:
            f.write(txt)
