class Balance:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def get(self):
        return self.__balance

    def add(self, money):
        self.__balance += money

    def remove(self, money):
        self.__balance -= money

    def is_bankrupt(self):
        return self.__balance < 50
