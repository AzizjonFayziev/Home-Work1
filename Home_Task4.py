class Furniture:
    def __init__(self, name,cost):
        self.name = name
        self.cost = cost
home1 = Furniture('Диван', 20000000)
home2 = Furniture('Телевизор',12000000)

print(home1.name)
print(home1.cost)
print(home2.name)
print(home2.cost)
