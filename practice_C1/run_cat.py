from cat import Cat

c1 = Cat()
c2 = Cat()

c1.set_name("Барон")
c1.set_age("2 года")
c1.set_sex("мальчик")

c2.set_name("Сэм")
c2.set_age("2 года")
c2.set_sex("мальчик")


print(c1.get_name(), c1.get_age(), c1.get_sex())
print(c2.get_name(), c2.get_age(), c2.get_sex())
