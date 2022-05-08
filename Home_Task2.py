class Hero:
    def __init__(self, name, age, skills):
        self.name = name
        self.age = age
        self.skills = skills
hero1 = Hero('Batman', 42, 'money,IQ')
hero2 = Hero('Flash',23,'speed,intelect')

print(hero1.name)
print(hero1.age)
print(hero1.skills)
print(hero2.name)
print(hero2.age)
print(hero2.skills)