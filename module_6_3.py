class Horse:

    x_distance = 0
    sound = 'Frrr'

    def run(self, dx):
        Horse.x_distance = dx + Horse.x_distance

class Eagle:

    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        Eagle.y_distance = dy + Eagle.y_distance

class Pegasus(Horse, Eagle):

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        a = (super().x_distance, super().y_distance)
        return a

    def voice(self):
        print(super().sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()