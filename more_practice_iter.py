# Напишите класс Garage, который хранит список машин.
# В классе должны быть реализованы методы для добавления машин в гараж и вывода списка машин.
# Также реализуйте возможность вывода машин по индексу и срезу.
# А также возможность итерации по объекту Garage.
class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.name} {self.model} {self.year}y."


class CarIterator:
    def __init__(self, car_list):
        self.car_list = car_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.car_list):
            current_car = self.car_list[self.index]
            self.index += 1
            return current_car
        else:
            raise StopIteration


class Garage:
    def __init__(self):
        self.car_list = []

    def add_car(self, car_add):
        self.car_list.append(car_add)

    def __str__(self):
        result = "Garage: [ "
        for i in self.car_list:
            result += f"{i} "
        result += "]"
        return result

    def __getitem__(self, index):
        if isinstance(index, int):
            if 0 >= index < len(self.car_list):
                return self.car_list[index]
            else:
                raise IndexError("Index out of range")

        if isinstance(index, slice):
            start = 0 if index.start is None else index.start
            stop = len(self.car_list) if index.stop is None else index.stop
            step = 1 if index.step is None else index.step
            self.temp_car_list = []
            if step < 0 and stop >= len(self.temp_car_list):
                raise IndexError("Index out of range")
            else:
                for i in range(start, stop, step):
                    self.temp_car_list.append(self.car_list[i])
                return self.temp_car_list
        raise TypeError()

    def __len__(self):
        return len(self.car_list)

    def __iter__(self):
        return CarIterator(self.car_list)


car_1 = Car("Audi", "A4", 2019)
car_2 = Car("BMW", "X5", 2018)
car_3 = Car("Mercedes", "C", 2017)
car_4 = Car("Mercedes", "M", 2021)
car_5 = Car("Mercedes", "E", 2019)

garage = Garage()
garage.add_car(car_1)
garage.add_car(car_2)
garage.add_car(car_3)
garage.add_car(car_4)
garage.add_car(car_5)

print(f'{garage}\n')
print(f'{garage[0]}\n')

cars = garage[0:3]

for car in cars:
    print(f'{car}')

print()

for car in garage:
    print(f'{car}')