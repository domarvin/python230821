# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name 
        self.balance = balance 
    def deposit(self, amount):
        self.balance += amount 
    def withdraw(self, amount):
        self.balance -= amount
    def __str__(self):
        return "{0} , {1} , {2}".format(self.id, \
            self.name, self.balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(3000)
account1.withdraw(3000)
account1.balance = 15000
print(account1) # 클래서에서 __str__ 구현을 안하면 클래스 이름을 찍는다

#멤버변수 숨기기(__넣기)
class BankAccount1:
    def __init__(self, id, name, balance):
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account2 = BankAccount1(100, "전우치", 15000)
account2.deposit(3000)
account2.withdraw(3000)
account2.balance = 15000 #이것은 클래스에 없는데, 신규로 변수를 만들어서 저장하니 에러안남
account2.__balance = 30000 #이것은 클래스에 없는데, 신규로 변수를 만들어서 저장하니 에러안남
#이름변경(_BankAccount__balance)로 접근가능
print(account2) # 클래서에서 __str__ 구현을 안하면 클래스 이름을 찍는다
print(account2.balance) #이것은 클래스에 없는데, 신규로 변수를 만들어서 저장하니 에러안남
print(account2.__balance) #이것은 클래스에 없는데, 신규로 변수를 만들어서 저장하니 에러안남
print(account2._BankAccount1__balance)
