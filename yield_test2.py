

def myYield(n):
    while n > 0:
        rcv = yield n
        n -= 1
        if rcv is not None:
            n = rcv



def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 使用 yield
        # print b
        a, b = b, a + b
        n = n + 1


for n in fab(5):
    print(n)


def consumer():
    print('等待接收处理任务...')
    while True:
        data = (yield)
        print("收到任务：", data)


def producer():
    c = consumer()
    c.__next__()
    for i in range(3):
        print('发送一个任务...', '任务%d' % i)
        c.send('任务 %d' % i)


if __name__ == '__main__':
    my_yield = myYield(3)
    print(my_yield.__next__())
    print(my_yield.__next__())
    print('传给生成器一个值，重新初始化生成器。')
    print(my_yield.send(10))
    print(my_yield.__next__())
    producer()