class Counter:
    def __init__(self, x = 0):
        self.x = x


counter = Counter()


def used_iter():
    counter.x += 2
    return counter.x


for i in iter(used_iter, 8):
    print("本次遍历的数值：", i)