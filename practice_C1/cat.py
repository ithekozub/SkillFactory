class Cat:
    def __init__(self, name="", age=0, sex=None):
        self.name = name
        self.age = age
        self.sex = sex

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_sex(self):
        return self.sex

    def set_name(self, name):
        self.name = name

    def set_sex(self, sex):
        self.sex = sex

    def set_age(self, age):
        self.age = age

