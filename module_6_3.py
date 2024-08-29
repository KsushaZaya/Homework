class Horse:
    x_distance = 0
    sound_1 = 'Frrr'

    def run(self, dx):  # изменение дистанции
        self.x_distance += dx


class Eagle:
    y_distance = 0
    sound_2 = 'I train, eat, sleep, and repeat'

    def fly(self, dy):  # изменение дистанции
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        self.sound = super().sound_1
        self.sound = super().sound_2

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        pos_pegasus = (self.x_distance, self.y_distance)
        return pos_pegasus

    def voice(self):
        print(self.sound)


p1 = Pegasus()
print(Pegasus.mro())
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
