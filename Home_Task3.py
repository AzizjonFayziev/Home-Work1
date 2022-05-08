class Account:
    def __init__(self, login, password, credit):
        self.login = login
        self.password = password
        self.credit = credit
acc1 = Account('samurai', int(input('password:')), 'money,IQ')
acc2 = Account('Flash',int(input('password:')),'speed,intelect')

print(acc1.login)
print(acc1.password)
print(acc1.credit)
print(acc2.login)
print(acc2.password)
print(acc2.credit)