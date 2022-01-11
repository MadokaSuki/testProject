import time, functools


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        t_start = time.time() #取函数开始时间
        fn_return_value = fn(*args, **kw) #执行函数，并保存返回值
        t_end = time.time() #取函数结束时间
        print('func %s executed in %s ms. ReturnValue: %s' %(fn.__name__,(t_end-t_start)*1000,fn_return_value) )
        return fn_return_value #上面已经执行了一次原函数，这里不再执行原函数fn，只返回函数执行后的返回值
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
