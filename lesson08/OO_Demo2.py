class Account:
    name = '' # 公有屬性
    __balance = 0 # 私有屬性

    def setBalance(self, balance): # 物件方法，需含 self 參數
        self.__balance = balance

    def getBalance(self):
        return self.__balance


account = Account()
account.name = 'Vincent'
account.setBalance(30000)
print(account.name)
print(account.getBalance())