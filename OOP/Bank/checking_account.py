from account import Account


class Checking(Account):
    type = "checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self._fee = fee

    @property
    def fee(self):
        return self._fee

    def transfer(self, ammount):
        self.balance -= ammount + self.fee


checking = Checking("balance.txt", 1)
print(checking.balance)
checking.transfer(100)
checking.commit()
print(checking.balance)
