import math

for i in range(1, 20, 2):
    print(i)

testList = [ i**3 for i in range(3, 30) if i % 3 == 0]
print(testList)

print(testList[:3])

a = []
if a:
    print('not None')
else:
    print('Is None or []')

current_users = ['a', 'b', 'c', 'd', 'e']
new_users = list(input('请输入待创建用户组 空格隔开：').split())

if new_users:
    for new_user in new_users:
        if new_user in current_users:
            print("%s用户已存在" % new_user)
        else:
            print("可以创建用户%s" % new_user)
else:
    print('待创建用户组不得为空')
