#1. Переписать вычисление n-ного члена последовательности Фибоначчи с помощью рекурсии.

def fibonacci(n):
    if n == 0:
        return 0
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

x = int(input("fibonacci num"))
print(fibonacci(x))

##############         GAME    #############################################

import math
from abc import ABC, abstractmethod


class Location:
    def __init__(self, name: str, width: int, height: int, length: int):
        self.name = name
        self._width = width
        self._height = height
        self._length = length
        self._objs = []

    def addObject(self, obj):
        if obj not in self._objs:
            self._objs.append(obj)

    def clear(self):
        self._objs = None

    def isInside(self, x, y, z) -> bool:
        return ((x > 0 and x < self._length)
                and (y > 0 and y < self._width)
                and (z > 0 and z < self._height))

    @property
    def width(self):
        return self._width

    @property
    def length(self) -> int:
        return self._length

    @property
    def height(self):
        return self._height

    @property
    def volume(self):
        return self.height * self.length * self.width


class GameObject:
    def __init__(self, name: str, loc: Location, x, y, z):
        self.name = name
        self._loc = loc
        self._loc.addObject(self)
        self.x, self.y, self.z = x, y, z

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if x < 0:
            self._x = 0
        elif self._loc.length < x:
            self._x = self._loc.length
        else:
            self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        if y < 0:
            self._y = 0
        elif self._loc.width < y:
            self._y = self._loc.width
        else:
            self._y = y

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, z):
        if z < 0:
            self._z = 0
        elif self._loc.height < z:
            self._z = self._loc.height
        else:
            self._z = z

    def move(self, x, y, z):
        self.x += x
        self.y += y
        self.z += z

    def distance(self, obj):
        dx = self.x - obj.x
        dy = self.y - obj.y
        dz = self.z - obj.z
        r2 = dx ** 2 + dy ** 2 + dz ** 2
        return int(math.sqrt(r2))

class LivingObject(GameObject):
    def __init__(self, name: str, loc: Location, x, y, z, hp: int):
        super().__init__(name, loc, x, y, z)
        self._max_hp = hp
        self._hp = hp

    @property
    def maxHP(self):
        return self._max_hp

    @property
    def hp(self):
        return self._hp

    def changeHP(self, change):
        if not self.alive:
            return
        self._hp += change
        if self._hp < 0:
            self._hp = 0
        if self._hp > self._max_hp:
            self._hp = self._max_hp

    @property
    def alive(self):
        return self._hp > 0

    def eat(self, obj):
        if self.distance(obj) > 1:
            return
        self.changeHP(obj.eatMe())

class Weapon(GameObject):
    def __init__(self, name: str, loc: Location, x, y, z, damage, radius):
        super().__init__(name, loc, x, y, z)
        self._damage = damage
        self._radius = radius

    @property
    def damage(self):
        return self._damage

    @property
    def radius(self):
        return self._radius

    def attack(self, obj: LivingObject):
        d = self.distance(obj)
        if d > self.radius:
            return
        obj.changeHP(-self.damage)

######################## Добавить в игру разные типы оружия: холодное и метательное
class ColdArms(Weapon):
    def __init__(self, name: str, loc: Location, x, y, z, damage, radius, cold_damage: float):
        super().__init__(name, loc, x, y, z, damage, radius)
        self.cold_damage = cold_damage
    def attack(self, obj: LivingObject):
        d = self.distance(obj)
        if d > self.radius:
            return
        obj.changeHP(-self.damage - self.cold_damage)

#3. Реализовать выстрел в направлении ################################################
class ThrowWeapon(ColdArms):
    def throw(self, destruction_x: int, destruction_y: int, destruction_z: int):
        object_destruction = GameObject('object', self._loc, x=destruction_x, y=destruction_y, z=destruction_z)

        d = self.distance(object_destruction)
        if d > self.radius:
            return
        else:
            self.x = destruction_x
            self.y = destruction_y
            self.z = destruction_z


# 4. Добавить использование предметов персонажами ######################################
class Player(LivingObject):
    def __init__(self, name: str, loc: Location, x, y, z, hp: int, pick_up_distance: int):
        super().__init__(name, loc, x, y, z, hp)
        self.pick_up_distance = pick_up_distance
        self.weapon = None

    def pick_up_weapon(self, weapon: Weapon):
        if self.pick_up_distance >= self.distance(weapon):
            weapon.x, weapon.y, weapon.z = self.x, self.y, self.z
            self.weapon = weapon
        else:
            return


    def attack(self, obj: LivingObject):
        if not self.weapon:
            return
        self.weapon.attack(obj)



class Eatable(ABC):
    def __init__(self, hp: int):
        self._hp = hp
        self._eaten = False

    @property
    def eaten(self):
        return self._eaten

    @abstractmethod
    def eatMe(self):
        if not self.eaten:
            self._eaten = True
            return self._hp
        else:
            return 0

class Food(GameObject, Eatable):
    def __init__(self, name, loc, x, y, z, hp):
        GameObject.__init__(self, name, loc, x, y, z)
        Eatable.__init__(self, hp)

    def eatMe(self):
        Food.eatMe(self)


class Poison(GameObject, Eatable):
    def __init__(self, name, loc, x, y, z, hp):
        GameObject.__init__(self, name, loc, x, y, z)
        Eatable.__init__(self, hp)

    def eatMe(self):
        return -Eatable.eatMe(self)


class Burnable(ABC):
    def __init__(self):
        self._burned = False

    @property
    def burned(self):
        return self._burned

    @abstractmethod
    def burnMe(self):
        self._burned = True

class Cookable(GameObject, Eatable, Burnable):
    def __init__(self, name, loc, x, y, z, hp):
        GameObject.__init__(self, name, loc, x, y, z)
        Eatable.__init__(self, hp)
        Burnable.__init__(self)

    @classmethod
    def growMushroom(cls, loc, x, y, z):
        return cls('mushroom', loc, x, y, z, 20)

    def burnMe(self):
        Burnable.burnMe(self)

    def eatMe(self):
        hp = Eatable.eatMe(self)
        return hp if self.burned else -hp

if __name__ == '__main__':
    pole = Location('pole', 100,100,100)
    siryukens = ThrowWeapon('siryukens', pole, 1,3,4,55,10,77)

    hero = Player('Nana', pole, 1, 1, 1, 1000, 10)
    villain = Player('Fan', pole, 10, 10, 10, 10, 1)
    print(hero.hp)

    hero.pick_up_weapon(siryukens)
    hero.attack(villain)

    print(villain.hp)

