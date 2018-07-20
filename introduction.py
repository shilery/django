import sys
import math
import time


def frange(start, end, step=1.0):
    if step > 0:
        while start < end:
            yield start
            start += step
    elif step < 0:
        while start > end:
            yield start
            start += step
    else:
        raise ValueError('range() step must not be zero')


def f(x, y, z):
    a = x * x + 9.0 / 4 * y * y + z * z - 1
    return a * a * a - x * x * z * z * z - 9.0 / 80 * y * y * z * z * z


def h(x, z):
    for y in frange(1.0, 0.0, -0.001):
        if f(x, y, z) <= 0:
            return y
    return 0.0


def writefrang():
    for z in frange(1.5, -1.5, -0.1):
        for x in frange(-1.5, 1.5, 0.05):
            v = f(x, 0, z)
            if v <= 0:
                y0 = h(x, z)
                ny = 0.01
                nx = h(x + ny, z) - y0
                nz = h(x, z + ny) - y0
                nd = 1.0 / math.sqrt(nx * nx + ny * ny + nz * nz)
                d = (nx + ny - nz) * nd * 0.5 + 0.5
                sys.stdout.write('.:-=+*#%@'[int(d * 5)])
            else:
                sys.stdout.write(' ')
        sys.stdout.write('\n')


def writefrange1():
    for y in frange(1.5, -1.5, -0.1):
        for x in frange(-1.5, 1.5, 0.05):
            z = x * x + y * y - 1
            f = z * z * z - x * x * y * y * y
            if f <= 0:
                sys.stdout.write('*')
            else:
                sys.stdout.write(' ')
        sys.stdout.write('\n')


def start():
    print("*" * 80)



def dee():
    print("-" * 80)

introduce_list = [
    "陈嘻嘻！！！！！",
    "首先很高心认识你",
    "很高兴能在深圳这个年轻的城市认识你",
    "这座城市具有活力与包容 能相对公平的得到你付出的相应回报",
    "我热爱这座城市 热爱现在的生活 欣赏我遇到的人",
    "不慕大富贵，但求小清新",
    "我相信 无论生活多艰难 我们最终还是会珍爱生活 珍爱每一个新来的早晨 并且对未来的日子充满信心和希冀",
    "送你一首诗：",
    "  《热爱生命》 汪国真",
    "我不去想是否能够成功",
    "既然选择了远方",
    "便只顾风雨兼程",

    "我不去想能否赢得爱情",
    "既然钟情于玫瑰",
    "就勇敢地吐露真诚",
    "我不去想身后会不会袭来寒风冷雨",
    "既然目标是地平线",
    "留给世界的只能是背影",
    "我不去想未来是平坦还是泥泞",
    "只要热爱生命",
    "一切，都在意料之中"
]

i = 0
for line in introduce_list:
    print(line)
    time.sleep(1)
    i += 1
    if i > 6:
        break
dee()
writefrange1()
# writefrang()
time.sleep(1)
dee()
for j in range(7, len(introduce_list)):
    print(''.join((introduce_list[j:j+1])))
    # dee()
    print()
    time.sleep(1)

writefrang()
n = input("输入任意关闭此窗口：")
