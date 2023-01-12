class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def name_hero(self):
        return f'Hero name ==> {self.name}'

    def extra_health(self):
        return f'Удвоенное здоровье нашего героя {self.health_points * self.health_points}'

    def __str__(self):
        return f'nickname: {self.nickname}, superpower: {self.superpower}, health {self.health_points}'

    def __len__(self):
        return f'Длина коронной фразы {len(self.catchphrase)}'


hero = SuperHero('Naruto', 'Kurama', 'rasengan', 100, 'dattebayo')


# print(hero.name_hero())
# print(hero.extra_health())
# print(hero.__len__())
# print(hero.__str__())
# print(hero.people)


class FriendHero(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def extra_health(self):
        self.fly = True
        return f'Удвоенное здоровье нашего героя {self.health_points * self.health_points}'

    def fly_sky(self):
        super().__str__()
        return f'fly in the {self.fly}_phrase'


friend = FriendHero('Sakura', 'haruno', 'bakugo', 100, 'Shinnarooo', damage=60)
print(friend.extra_health())
print(friend.fly_sky())


class BrotherHero(SuperHero):
    people = 'people'
    sword = True

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def extra_health(self):
        self.fly = True
        self.health_points **= 2
        return f'Удвоенное здоровье нашего героя {self.health_points}'

    def fly_sky(self):
        return f'fly in the {self.fly}_phrase'

    # def crit(self):
    #     return self.damage ** 2


bro = BrotherHero('Sasuke', 'uchiha', 'chidori', 100, 'usuratonkachi', damage=70)
print(bro.extra_health())
print(bro.fly_sky())


class Villain(BrotherHero, FriendHero):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(hero):
        return hero.damage ** 2


vil = Villain('Madara', 'Uchiha', 'susano', 120, 'Lets go dance')
print(Villain.crit(friend))
print(Villain.crit(bro))
print(Villain.crit(vil))
