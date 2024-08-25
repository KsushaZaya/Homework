class Animal:
    alive = True  # живой
    fed = False  # накормленный

    def __init__(self, name):
        self.name = name


class Plant:
    edible = False  # съедобность

    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Flower(Plant):
    pass  # edible = True


class Fruit(Plant):
    edible = True


a1 = Predator('Питон')
a2 = Mammal('Сурок')
p1 = Flower('Цветок')
p2 = Fruit('Банан')

print(a1.name)
print(p1.name)

print(a1.alive, f'- {a1.name} Жив')
print(a2.fed, f'- {a2.name} Не насытился')
a1.eat(p1)
a2.eat(p2)
print(a1.alive, f'- {a1.name} Погиб')
print(a2.fed, f'- {a2.name} Насытился')
