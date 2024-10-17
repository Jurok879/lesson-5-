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
       return self.number_of_floors                             # возвращаем переменную в функцию

    def __str__(self):                                          # создаем функцию согласно условию задачи
       name_ = f"Название: {self.name}, количество этажей: {self.number_of_floors}"
       return name_                                             # возвращаем переменную в функцию

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# _str_
print(h1)
print(h2)

# _len_
print(len(h1))
print(len(h2))

