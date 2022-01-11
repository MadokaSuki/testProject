import itertools
import sys

for i in itertools.count(1, 3):
    print(i)
    if i >= 10:
        break

x = 0
for i in itertools.cycle(['a', 'b']):
    print(i)
    x += 1
    if x >= 6:
        break

print(list(itertools.repeat(3, 4)))
print(list(itertools.chain([1, 3], [2, 3])))
print(list(itertools.compress([1, 2, 3, 4], [1, [], True, 3])))
print(list(itertools.dropwhile(lambda x: x > 10, [18, 19, 2, 13, 1, 12])))
print(list(itertools.takewhile(lambda x: x > 10, [18, 19, 2, 13, 1, 12])))
for its in itertools.tee([0, 1.3], 3):
    for it in its:
        print(it)
print(list(itertools.permutations('abc', 2))) #排列
print(list(itertools.combinations('abc', 2))) #组合

list = [1, 2, 3, 4]
it = iter(list)
for x in it:
    print(x)

list = [1, 2, 3, 4]
it = iter(list)
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
