from client import Client

class Volontier(Client):
    def __init__(self, name="", city="", state="", balance=0):
        self.name = name
        self.city = city
        self.state = state
        self.balance = balance

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def set_city(self, city):
        self.city = city

    def set_state(self, state):
        self.state = state

    def __str__(self):
        return (f'«{self.name}, г. {self.city}, статус "{self.state}"»')



