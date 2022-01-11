class Duck:
    def __init__(self, name = 'duck'):
        self.name = name

    def quack(self):
        print('嘎嘎嘎...')


class Cat:
    def __init__(self, name = 'cat'):
        self.name = name

    def quack(self):
        print('喵喵喵...')


class Tree:
    def __init__(self, name = 'tree'):
        self.name = name

    def quack(self):
        pass


def duck_demo(obj):
    obj.quack()


if __name__ == '__main__':
    duck = Duck()
    cat = Cat()
    tree = Tree()
    duck_demo(duck)
    duck_demo(cat)
    duck_demo(tree)
