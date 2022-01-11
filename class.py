import math


class MyClass:

    def info(self):
        print('我定义的类！')

    def cal(self, x, y):
        return x + y


sc = MyClass()
print('调用info方法的结果')
sc.info()
print(sc.cal(3, 5))


def loca_change(x, y):
    return abs(x), abs(y)


class Ant:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.show_location()

    def show_location(self):
        print("当前位置：(%d,%d)" % (self.x, self.y))

    def move(self, x, y):
        x, y = loca_change(x, y)
        self.edit_point(x, y)
        self.show_location()

    def edit_point(self, x, y):
        self.x += x
        self.y += y


antA = Ant()
antA.move(1, 2)
antA.move(-1, -3)
print("")


class FlySpeed:
    def __init__(self, speed=0.5):
        self.fly_speed = speed

    def weather_influence(self, weather="sunny"):
        if weather == "rainy":
            self.fly_speed -= 0.3
        elif weather == "downwind":
            self.fly_speed *= 2
        elif weather == "upwind":
            self.fly_speed /= 2

        if self.fly_speed > 1:
            self.fly_speed = 1
        elif self.fly_speed < 0.1:
            self.fly_speed = 0.1

    def describe_speed(self):
        print("飞蚁速度：%.2f" % self.fly_speed)


class FlyAnt(Ant):

    def __init__(self, x, y):
        self.speed = FlySpeed()
        super().__init__(x, y)

    def show_location(self):
        print("飞蚁位置：(%d,%d)" % (self.x, self.y))

    def move(self, x, y):
        x, y = loca_change(x, y)
        self.edit_point(x, y)
        self.fly_away(x, y)

    def fly_away(self, x, y):
        print("飞蚁飞到位置：(%d,%d)" % (self.x, self.y))
        fly_length = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
        fly_time = fly_length / self.speed.fly_speed
        print("飞行距离 %.2f cm" % fly_length)
        print("飞行时间 %.2f s" % fly_time)


my_flyAnt = FlyAnt(4, 5)
my_flyAnt.speed.fly_speed = 0.5
my_flyAnt.speed.weather_influence("rainy")
my_flyAnt.speed.describe_speed()
my_flyAnt.move(3, -3)
# 在对象中运用实例 FlyAnt引用FlySpeed并且继承了Ant
# FlySpeed为创建的另一个对象
