class Game:
    def __init__(self, name, category, size):
        self.name = name
        self.category = category
        self.size = size
game1 = Game('PUBG','Shooter', '1.6 gb')
game2 = Game('State of survival','Strategy','800 mb')

print(game1.name)
print(game1.category)
print(game1.size)
print(game2.name)
print(game2.category)
print(game2.size)
