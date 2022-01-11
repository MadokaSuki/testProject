def is_odd_number(number):
    return number % 2 != 0


k = int(input("请输入数字k 即将排列0-k的奇数"))
new_list = filter(is_odd_number, range(k + 1))
print(list(new_list))


def find(item):
    score = int(item[1])
    return True if 550 <= score < 600 else False


list1 = [
    ("Richard", 460), ("Nikki", 575), ("Jason", 645), ("Wind", 580)
]
list2 = list(filter(find, list1))
print(f"600分以上：{len(list2)}人")
# 格式化输出

user_info1 = [{'name': 'John', 'password': '2332wkk', 'usertype': 'VIP1'},
              {'name': 'Mac', 'password': '521521', 'usertype': 'guest'},
              {'name': 'Madoka', 'password': '19971017', 'usertype': 'VIP2'}]
log_info1 = [{'name': 'John', 'password': 'node'}]
log_info2 = [{'name': 'John', 'password': '2332wkk'}]


def verity_password(login_info, user_info):
    login_name = login_info[0].get('name', '0')
    login_password = login_info[0].get('password', '0')
    for i in range(len(user_info)):
        if user_info[i].get('name') == login_name:
            if user_info[i].get('password') == login_password:
                return user_info[i].get('usertype')
            else:
                return 0
        else:
            return 0


print(verity_password(log_info1, user_info1))
print(verity_password(log_info2, user_info1))
# filter应用 filter的结果需要转换为list

str1 = input("计算字符中空格数量")


def count_blank(str):
    a = str1.split(" ")
    return len(a) - 1


print(count_blank(str1))
html1 = input("请输入html以获取超链接")


def get_href(html):
    list1 = html.split('"')
    x = []
    for i in range(len(list1)):
        if list1[i].count("href=") > 0:
            x.append(list1[i + 1])
    print(x)
# 获取超链接


get_href(html1)

seq = [3, 5, 6, 7, 8, 9]
seq = filter(lambda x: x % 3 and x % 2, seq)
print(list(seq))

a = ['Richard', 1, -3.5, None, False, -3, []]
b = ['d', 3, 4]
print(set(filter(lambda x: type(x) != str, b)))
print(list(filter(None, a)))
# 按条件过滤

temp = [('a', 1, 1.5),
        ('b', 2, 5.1),
        ('c', 9, 4.3)]
findindex = lambda self, i, value: sorted(self, key = lambda x: x[i] != value)[0]
print(findindex(temp, 0, 'b'))
# 索引

print((lambda x: x**2)(3))
print(list(map(lambda x, y: x * y, [1, 3, 5, 7, 9, 11, 13], [2, 4, 6, 8, 10, 12])))
a = [('b', 3), ('a', 2), ('d', 4), ('c', 1)]
print(sorted(a, key = lambda x: x[0]))
# map映射与lambda应用


Names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']
B_Name = filter(lambda x: x.startswith('B'), Names)
print(B_Name)


def increment(n):
    return lambda x: x+n


f = increment(4)
f(2)


def factorial(n):
    if n == 0:
        return 1
    elif n >= 1:
        return n * factorial(n - 1)
    else:
        print("不允许输入小于0的值！")
# lambda 函数 return


print(factorial(5))

stringA = " abc xyz "
print(stringA.rstrip())
print(stringA.lstrip())
print(stringA.strip())

# 去掉


a = ['dc', 'ed', '3s', '44f']
a.append('e323')
a.insert(3, 'fj;ie')
print(a)
