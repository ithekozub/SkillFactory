class Pet:
    def __init__(self, name, age, sex):
        self.__name = name
        self.__age = age
        self.__sex = sex

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_sex(self):
        return self.__sex