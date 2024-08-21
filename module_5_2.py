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

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, Количество этажей: {self.number_of_floors}')



h1 = House('ЖК Адмиральский', 18)
h2 = House('Парковка', 2)

# h1.go_to(9)
# print()
# h2.go_to(-1)
print()
# __str__
print(h1)
print(h2)
print()
# __len__
print(len(h1))
print(len(h2))
