class Account:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, "r") as file:
            self._balance = float(file.read())

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, balance):
        self._balance = balance

    def withdraw(self, amount):
        self._balance -= amount

    def deposit(self, amount):
        self._balance += amount

    def commit(self):
        with open(self.filepath, "w") as file:
            file.write(str(self._balance))
