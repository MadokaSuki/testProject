import math

collectedList = list(map(int, input('请输入20个数字').split()))
listA = [k for k in sorted(collectedList) if k > 0]
listB = [k for k in sorted(collectedList) if k < 0]
for i in listA:
    print(i)

print('\n')
for m in listB:
    print(m)


def tpl_sum(t):
    result = 0
    for x in t:
        result += x
    return result


a = [3, 5, 2]

print(tpl_sum(a))


def hello(m):
    print('hello!,', m)


def multitest(a, b, c):
    return a * b * c


print(multitest(2, c=1, b=3))


def change_para_num(*tql, a, b=3.1):
    print(type(tql))
    print('tql:', tql)
    print('a:', a)
    print('b:', b)


change_para_num(1, 3, 4, a=1, b=0)
change_para_num(1, 3, 4, a=1)


# change_para_num(1, 3, 4, a = 1, 0)
# 拆解元组 *  拆解字典 **


def cube(name, **nature):
    all_nature = {'x': 5,
                  'y': 5,
                  'z': 4,
                  'color': 'white',
                  'weight': 1
                  }
    all_nature.update(nature)
    print(name, "立方体的属性:")
    print('体积:', all_nature['x'] * all_nature['y'] * all_nature['z'])
    print('颜色:', all_nature['color'])
    print('重量:', all_nature['weight'])


cube('top', **{'x': 2, 'color': 'black'})


# 函数退出以后：list dict改变 但是字符串不变

def myfun(lst=None):
    lst = [] if lst is None else lst
    lst.append('abc')
    print(lst)


myfun()
myfun()
myfun(['3'])


def test():
    global a
    a = 0
    a += 3
    print('函数内a:', a)


a = 'external'
print('全局作用域a:', a)
test()
print('全局作用域a:', a)

s = lambda x1, y1, x2, y2: math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(s(1, 1, -3, 4))
