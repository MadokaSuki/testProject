import pysnooper
import math


# @pysnooper.snoop("./log/debug.log")
print('a', 'b', 'c', sep=',', end=';')
# 分隔符休止符
math.pow(2, 4)
n = 5
t = 'pythonn '
print(t.capitalize() * t.count('n'))
f = t.isalpha()
# 操作字符串

print(f)
job = input('Please input your job:')
if job.isalpha():
    print('I am a %s.' % job)
elif job.isdigit():
    print('请不要输入数字')
else:
    print('请不要输入其他字符')
# 提取输入
k = [1, 5, 2] + [3, 4]
print(k)
k.sort()
print(k)
# 对列表操作

m = (2, 3)
print(m)
# 元组

classA = {1: 'Richard', 2: 'Nikki', 3: 'Jason'}
classB = ['BIOS', 'FIRMWARE', 'DRIVER', 'APP']
print(classA.get(1) + " " + classA[2])
print(classA.items())
print(classA.keys())
print(classA.values())
# 操作字典(dict) not in 检查key成员而不是value

numberList = list(map(int, input("请输入数字 用空格隔开：").split()))
print(min(numberList))
print(len(numberList))
print(sum(numberList))
print(sum(numberList) / len(numberList))

for key, value in classA.items():
    print(key, ":", value)
for i in range(0, 7, 2):
    print(i, "的平方是：", pow(i, 2))
else:
    print('计算完成')

for i, item in enumerate(classB):
    print('第%d种更新是:%s' % (i, item))
# 编号迭代 排序迭代 翻转迭代
#
# def(numberA, numberB)
#
square = [i**i for i in range(1, 4)]
square_even = [i**i for i in range(1, 11) if i**i % 2 == 0]


# append() pop() insert()
