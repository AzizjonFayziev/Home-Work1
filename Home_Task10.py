class Student:
    def __init__(self, name, id, level):
        self.name = name
        self.id = id
        self.level = level
student1 = Student('Azizjon Fayziev','ACC20017', 2)
student2 = Student('Asadbek Oripov','BAN23933','3')

print(student1.name)
print(student1.id)
print(student1.level)
print(student2.name)
print(student2.id)
print(student2.level)