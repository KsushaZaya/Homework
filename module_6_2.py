class Vehicle:  # Любой транспорт
    __COLOR_VARIANTS = ['pink', 'yellow', 'red', 'black', 'white']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)  # владелец транспорта (изменяемый атрибут)
        self.__model = str(__model)  # модель (марка) транспорта. (неизм. атр.)
        self.__engine_power = int(__engine_power)  # мощность двигателя (неизм. атр.)
        self.__color = str(__color)  # название цвета

    def get_model(self, __model):
        print(f'Модель: {self.__model}')

    def get_horsepower(self, __engine_power):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self, __color):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        print(f'{self.get_model(self.__model)}'
              f'{self.get_horsepower(self.__engine_power)}'
              f'{self.get_color(self.__color)}'
              f'Владелец: {self.owner}\n')

    def set_color(self, new_color):
        if new_color.lower() in Vehicle.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}\n')


class Sedan(Vehicle):  # Седан
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['pink', 'yellow', 'red', 'black', 'white']
avto_1 = Sedan('Vi', 'Mazda 323 BG', 88, 'Red')

# Изначальные свойства
avto_1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
avto_1.set_color('Green')
avto_1.set_color('PINK')
avto_1.owner = 'Ksusha'

# Проверяем что поменялось
avto_1.print_info()
