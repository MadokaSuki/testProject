class Book:

    def __init__(self, name = 'Python从入门到精通'):
        self.name = name

    def __add__(self, obj):
        return self.name + ' add ' + obj.name

    def __len__(self):
        return len(self.name)


if __name__  == '__main__':
    booka = Book()
    bookb = Book('Java从入门到精通')
    print('len(booka):', len(booka))
    print('len(bookb):', len(bookb))
    print(booka + bookb)
    