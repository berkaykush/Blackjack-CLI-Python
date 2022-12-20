class Balance:
    INITIAL_FUNDS = 1000

    def __init__(self, funds):
        self.__funds = funds

    @property
    def funds(self):
        return self.__funds

    def add_funds(self, money):
        self.__funds += money

    def remove_funds(self, money):
        self.__funds -= money

    def is_bankrupt(self):
        return self.__funds < 50
