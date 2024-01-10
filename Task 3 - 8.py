import datetime

# Task 3 Реализуйте генераторную функцию, возвращающую по одному члену геометрической прогрессии.


def geometric_progression_generator(a, q):
    while True:
        yield a
        a *= q


generator = geometric_progression_generator(2, 3)
for i in range(5):
    print(next(generator))


# Task 4 Реализуй свой аналог генераторной функции range().

def my_range(start, stop, step=1):
    while start < stop:
        yield start
        start += step


for i in my_range(0, 10, 2):
    print(i)


# Task 5 Напишите генераторную функцию, которая возвращает простые числа.
# Верхний предел диапазона должен быть задан параметром этой функции.


def prime_numbers_generator(n):
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i


for i in prime_numbers_generator(100):
    print(i, end=" ")


# Task 6 Напишите генераторное выражение для заполнения списка.
# Список должен быть заполнен кубами чисел от 2 до указанной величины.

cubes_list = [x**3 for x in range(2, 10)]
print(cubes_list)


# Task 7 Реализуйте генераторную функцию, возвращающую элементы последовательности чисел Фибоначчи.

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


for i in fibonacci_generator(10):
    print(i, end=" ")


# Task 8 Реализуйте генераторную функцию для генерации последовательности дат.
# Начальная и конечная дата должны быть заданы параметрами этой функции.

def date_generator(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        yield current_date
        current_date += datetime.timedelta(days=1)


for date in date_generator(datetime.date(2023, 11, 1), datetime.date(2024, 1, 11)):
    print(date)

