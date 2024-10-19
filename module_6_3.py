class Horse:
    def __init__(self, distance=0):
        self.distance = distance
        self.sound = 'Frrr'

    def run(self,  dx):
        self.distance += dx


class Eagle:
    def __init__(self, y_distance=0):
        self.y_distance = y_distance
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self, distance=0, y_distance=0):
        Horse.__init__(self, distance)
        Eagle.__init__(self, y_distance)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.distance, self.y_distance

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
