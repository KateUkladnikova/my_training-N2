# "Множественное наследование"
# Задача "Ошибка эволюции"
from random import randint
import winsound
class Animal():
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __new__(cls, *args):
        return object.__new__(cls)
    def __init__(self, speed, cords = [0, 0, 0]):
        self.speed = speed
        self._cords = cords
    def move(self, dx, dy, dz):
        if (self.speed * dz) < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords = [dx * self.speed, dy * self.speed, dz * self.speed]
    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")
    def speak(self):
        # Play Windows exit sound.
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        print(self.sound)
class Bird(Animal):
    beak = True
    def __new__(cls, *args):
        return object.__new__(cls)
    def lay_eggs(self):
        print(f"Here are(is) {randint(1, 4)} eggs for you")
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def __new__(cls, *args):
        return object.__new__(cls)
    def __init__(self, speed, cords = [0, 0, 0]):
        super().__init__(speed, cords = [0, 0, 0])
    def dive_in(self, dz):
        self._cords[2] = self._cords[2] - int(abs(dz/2 * self.speed))
        return self._cords[2]
class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8
    def __new__(cls, *args):
        return object.__new__(cls)
class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    def __new__(cls, *args):
        return object.__new__(cls)
    def __init__(self, speed, sound = "Click-click-click", cords = [0, 0, 0]):
        super().__init__(speed, cords = [0, 0, 0])
        self.sound = sound

print(Duckbill.mro())
db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()

