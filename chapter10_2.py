x = 14


def foo():
    x = 3

    def bar():
        print('x is %d' % x)

    bar()


def delay_fun(x, y):

    def calculator():
        return x + y
    return calculator #返回了函数本身 并不是返回函数的调用 类似于装饰器


def line(a, b):

    def aline(x):
        return a * x + b
    return aline


if __name__ == '__main__':
    foo()
    print('返回一个求和函数，并不求和')
    msum = delay_fun(3, 4)
    print()
    print('调用并求和：')
    print(msum())

    line23 = line(2, 3)
    line50 = line(5, 0)
    print(line23(4))
    print(line50(3))
