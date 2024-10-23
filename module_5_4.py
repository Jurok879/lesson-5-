# class Example:
#     def __new__(cls, *args, **kwargs):
#         print(args)
#         print(kwargs)
#         return object.__new__(cls)
#
#     def __init__(self, first, second, third):
#         print(first)
#         print(second)
#         print(third)
#
# ex = Example('data', second=25, third=3.14)

class House:                                                    # создаем класс

    houses_history = []                                         # создаем атрибут с пустым списком

    def __new__(cls, *args, **kwargs):                          # создаем метод "new"
        cls.houses_history.append(args[0])                      # добавляем в список объекта аргумент
        return super().__new__(cls)                             # возвращаем метод ч/з функцию "super()"

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

    # переопределяем метод

    def __del__(self):
        print(f'  {self.name} снесён, но он останется в истории')



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
