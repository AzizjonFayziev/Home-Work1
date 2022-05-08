class Scores:
    def __init__(self, name, hero, damage):
        self.name = name
        self.hero = hero
        self.damage = damage
player1 = Scores('Bob','Eydora', 2478)
player2 = Scores('Aziz','Balmond',9780)

print(player1.name)
print(player1.hero)
print(player1.damage)
print(player2.name)
print(player2.hero)
print(player2.damage)