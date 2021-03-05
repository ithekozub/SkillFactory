from volontier import Volontier

v1 = Volontier()
v1.set_name("Николаев Николай")
v1.set_city("Москва")
v1.set_state("Наставник")

v2 = Volontier()
v2.set_name("Петров Петр")
v2.set_city("Пермь")
v2.set_state("Ученик")


volontiers = [v1, v2]

for volontier in volontiers:
    print(volontier)

