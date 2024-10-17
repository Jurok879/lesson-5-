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


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
