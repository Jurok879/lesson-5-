class House:                                                    # создаем класс
    def __init__(self, name, number_of_floors):                 # создаем функцию для характеристики объекта
        self.name = name                                        # название
        self.number_of_floors = number_of_floors                # количество этажей

    def go_to(self, new_floor):                                 # создаем функцию для удовлетворения условий задачи
        if self.number_of_floors < new_floor or new_floor < 1:  # условие
            print("Такого зтажа не существует")                 # выводим на консоль
        elif self.number_of_floors >= new_floor:                # условие
            new_floor = range(1, new_floor+1)                   # диапазон для переменной
            print('\n'.join(map(str,new_floor)))                # выводим диапазон строки в столбец на консоль

    def __len__(self):                                          # создаем функцию согласно условию задачи
        return self.number_of_floors                            # возвращаем переменную в функцию

    def __str__(self):                                          # создаем функцию согласно условию задачи
        return f"Название: {self.name}, количество этажей: {self.number_of_floors}"

    # перегрузка операторов сравнения

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors != other

    # перегрузка арифметических операторов

    def __add__(self, other):
        if isinstance(other, House):
            self.number_of_floors += other.number_of_floors
        elif isinstance(other, int):
            self.number_of_floors += other
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

# условия

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # _eq_

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
