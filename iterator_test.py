class MyIterator:

    def __init__(self, x, xmax=100):
        self.__mul, self.__x = x, x
        self.__xmax = xmax

    def __iter__(self):
        return self

    def __next__(self):
        if self.__x and self.__x != 1:
            self.__mul *= self.__x
            if self.__mul <= self.__xmax:
                return self.__mul
            else:
                raise StopIteration
        else:
            raise StopIteration


if __name__ == '__main__':
    # 类似于main函数
    a = int(input("请输入被迭乘迭代的数字："))
    b = input("请输入被迭乘迭代到的最大值，默认为100：")
    if b:
        myiter = MyIterator(a, int(b))
    else:
        myiter = MyIterator(a)
    for i in myiter:
        print('迭代的数据元素为: ', i)
