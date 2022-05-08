class Car:
    def __init__(self, model, complect, cost):
        self.model = model
        self.complect = complect
        self.cost = cost
product1 = Car('Lacetti','full', '17000 usd')
product2 = Car('Spark','half-full', '8000 usd')

print(product1.model)
print(product1.complect)
print(product1.cost)
print(product2.model)
print(product2.complect)
print(product2.cost)