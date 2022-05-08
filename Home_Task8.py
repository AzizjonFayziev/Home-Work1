class Shop:
    def __init__(self, name, quality, cost):
        self.name = name
        self.quality = quality
        self.cost = cost
product1 = Shop('iphone 7 plus','original', '500 usd')
product2 = Shop('iphone 11 pro max','copy', '300 usd')

print(product1.name)
print(product1.quality)
print(product1.cost)
print(product2.name)
print(product2.quality)
print(product2.cost)