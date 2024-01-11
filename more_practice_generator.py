# Task Напишите генераторную функцию, которая возвращает части списка.

names = ['John', 'Paul', 'George', 'Ringo', 'Atahan', 'Mehmet', 'Ali', 'Veli', 'Ayşe', 'Fatma', 'Hayriye', 'Ahmet']


def get_name_part(name, n):
    index = 0
    while index < len(name):
        temp_names = []
        for i in range(index, index + n):
            if i > len(name):
                yield temp_names
                break
            else:
                temp_names.append(name[i])
            index += 1
        yield temp_names


res = get_name_part(names, 3)
print(next(res))
print(next(res))


# Task Метод send генератора позволяет передать значение в генератор.

def square_gen(n):
    i = 0
    exponent = 2
    while i < n:
        total = yield i ** exponent
        if total is not None:
            exponent = total
        i += 1


g = square_gen(5)
next(g)
print(g.send(3))
print(next(g))
print(next(g))
print(next(g))

# Task Метод throw генератора позволяет передать исключение в генератор.


def square_gen(n):
    i = 0
    exponent = 2
    while i < n:
        try:
            total = yield i ** exponent
        except StopIteration:
            raise StopIteration
        if total is not None:
            exponent = total
        i += 1


g = square_gen(10)
next(g)
print(next(g))
print(next(g))
print(g.send(3))
print(next(g))
print(next(g))
print(g.throw(StopIteration))
print(next(g))


# Task Метод close генератора позволяет закрыть генератор.

def square_gen(n):
    i = 0
    exponent = 2
    while i < n:
        total = yield i ** exponent
        if total is not None:
            exponent = total
        i += 1


for i in square_gen(10):
    if i >= 25:
        i.close()
    print(i)




