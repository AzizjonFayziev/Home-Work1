class Dog:
    def __init__(self, name, age, bread):
        self.name = name
        self.age = age
        self.bread = bread
dog1 = Dog('Tommy', 2, 'labrador')
dog2 = Dog('Rex',2,'buldog')

print(dog1.name)
print(dog1.age)
print(dog1.bread)
print(dog2.name)
print(dog2.age)
print(dog2.bread)