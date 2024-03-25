class Rectangle(object):
    def __init__(self, h, v):
        self.h = h
        self.v = v

    def area(self):
        return self.h * self.v

r = Rectangle(10, 20)
a = r.area()
print(a)

print(r.h)
print(r.v)
print(r.area())

class Character(object):
    def __init__(self):
        self.life = 1000

    def attacked(self):
        self.life -= 10
        print("공격받음! 생명력 =", self.life)

    def attack(self):
        print("공격!")

a1 = Character()
b1 = Character()
c1 = Character()

print(a1.life)
print(b1.life)
print(c1.life)

a1.attacked()
b1.attacked()

print(a1.life)
print(b1.life)
print(c1.life)

a1.attacked()
a1.attacked()
a1.attacked()
a1.attacked()
a1.attacked()

print(a1.life, b1.life, c1.life)

class Warrior(Character):

    def __init__(self):
        super(Warrior, self).__init__()
        self.strength = 15
        self.intelligence = 5

    def attack(self):
        print("육탄 공격!")

class Wizard(Character):

    def __init__(self):
        super(Wizard, self).__init__()
        self.strength = 5
        self.intelligence = 15
    def attack(self):
        print("마법 공격!")

a2 = Warrior()
a3 = Wizard()

print(a2.life, a3.life)
print(a2.strength, a3.strength)
print(a2.intelligence, a3.intelligence)

a2.attacked()
a3.attacked()

print(a2.life, a3.life)

class Complex(object):

    def __init__(self, realpart, imagepart):
        self.r = realpart
        self.i = imagepart

g1 = Complex(1, 2)

print(g1, str(g1))

class Complex2(Complex):
    def __repr__(self):
        return "Complex: real = %f, image = %f" % (self.r, self.i)

    def __str__(self):
        return "[for str] " + self.__repr__()

g2 = Complex2(1, 1)

print(g2)

print(str(g2))

class Complex3(Complex2):
    def __getitem__(self, key):
        if key == "r":
            return self.r
        elif key == "i":
            return self.i

g3 = Complex3(1, 2)

print(g3)

print(g3["i"])









