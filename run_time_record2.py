import time


class Cache:
    __cache = {}

    def __init__(self, func):
        self.func = func

    def __call__(self):

        # 如果缓存字典中有这个方法的执行结果
        # 直接返回缓存的值
        if self.func.__name__ in Cache.__cache:
            return Cache.__cache[self.func.__name__]

        # 计算方法的执行结果
        value = self.func()
        # 将其添加到缓存
        Cache.__cache[self.func.__name__] = value
        # 返回计算结果
        return value


@Cache
def long_time_func():
    time.sleep(5)
    return '我是计算结果'


start = time.time()
print(long_time_func())
end = time.time()
print(f'计算耗时{end-start}秒')

start = time.time()
print(long_time_func())
end = time.time()
print(f'计算耗时{end-start}秒')