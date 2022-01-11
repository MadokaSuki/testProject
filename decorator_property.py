class Rect:
    def __init__(self, area):
        self.__area = area
    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, value):
        self.__area = value

    @area.deleter
    def area(self):
        self.__area = 0

rect = Rect(30)
#直接通过方法名来访问 area 方法
print("矩形的面积是：", rect.area)
rect.area = 50
print("矩形的面积是：", rect.area)
del rect.area
print("矩形的面积是：", rect.area)
