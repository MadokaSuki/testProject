class DemoClass:
    class_val = 3

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.info()

    def info(self):
        print('类属性class_val: ', DemoClass.class_val)
        print('实例属性x: ', self.x)
        print('实例属性y: ', self.y)


if __name__ == '__main__':
    dc = DemoClass()
    if hasattr(DemoClass, 'class_val'):
        setattr(DemoClass, 'class_val', 1000)
    if hasattr(dc, 'x'):
        setattr(dc, 'x', 'xxxxxxxx')
    if hasattr(dc, 'y'):
        setattr(dc, 'y', 'yyyyyyyy')
    dc.info()
    setattr(dc, 'z', 'zzzzzzzz')
    print('添加的属性z', dc.z)

# 设置对象属性