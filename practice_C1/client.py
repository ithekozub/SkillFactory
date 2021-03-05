class Client:
    def __init__(self, name="", balance=0):
        self.name = name
        self.balance = balance

    def get_name(self):
        return self.name

    def get_balance(self):
        return  self.balance

    def set_name(self, name):
        self.name = name

    def set_balance(self, balance):
        self.balance = balance

    def __str__(self):
        return (f"Клиент «{self.name}». Баланс: {self.balance} руб.")
