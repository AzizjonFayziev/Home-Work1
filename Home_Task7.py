class Ufc:
    def __init__(self, name, weight, scores):
        self.name = name
        self.weight = weight
        self.scores = scores
fighter1 = Ufc('Dana White ','95 kg', '45 points')
fighter2 = Ufc('Khabib Nurmagomedov', '70 kg','52 points')

print(fighter1.name)
print(fighter1.weight)
print(fighter1.scores)
print(fighter2.name)
print(fighter2.weight)
print(fighter2.scores)