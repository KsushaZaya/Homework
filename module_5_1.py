class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        floor = 0
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f'{new_floor} - Такого этажа не существует')
        else:
            for floor in range(new_floor):
                print(floor + 1)


h1 = House('ЖК Адмиральский', 18)
parking = House('Парковка', 2)

h1.go_to(9)
print()
parking.go_to(-1)
