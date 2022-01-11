import contextlib

class FileMgr:
    def __init__(self, filename):
        self.selfname = filename
        self.f = None

    def __enter__(self):
        self.f = open(self.selfname, encoding = 'utf-8')
        return self.f

    def __exit__(self, t, v, tb):
        if self.f:
            self.f.close()


@contextlib.contextmanager
def my_mgr(s, e):
    print(s)
    yield s + ' ' + e
    print(e)


if __name__ == '__main__':
    with FileMgr('chapter10_2.py') as f:
        for line in f.readlines():
            print(line, end = '')

    with my_mgr('start', 'end') as val:
        #进入时打印start
        print(val) #中间打印start end
    #退出后打印end


