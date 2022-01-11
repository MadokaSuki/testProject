names = list(input("请输入名字,并用空格隔开：").split(" "))
names.remove(input("请输入不能参会的嘉宾："))
names.append(input("请输入新来的嘉宾："))
names.insert(0, input("请输入贵宾："))
for name in names:
    print("dear %s, would you like to join the party on Friday evening?" % name)

for i in range(len(names) - 2):
    guestDeleted = names.pop();
    print("I am sorry for %s that I can't invite you to the party" % guestDeleted)

print(names)
del names[0]
del names[0]
print(names)
print(range(2, 11, 3))

# for i in range(1, 1000001):
#     print(i)
# print(sum(range(1, 1000001)))

listA = list(filter(lambda x: x % 3 == 0 or x % 2 == 0, range(3, 30)))
for k in listA:
    print(k)

series =[1, 3, 5, 0, 9]
print(sorted(series, reverse = True))
