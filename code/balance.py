class Balance:

    def __init__(self, balance):
        self.__balance = balance

    def add_balance(self, money):
        self.__balance += money

    def remove_balance(self, money):
        self.__balance -= money

    def is_bankrupt(self):
        return self.__balance < 50

    @property
    def get_balance(self):
        return self.__balance
