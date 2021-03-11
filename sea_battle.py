from random import randint

class BoardException(Exception):
    pass

class BoardOutException(BoardException):
    def __str__(self):
        return "Вы пытаетесь выстрелить за доску!"

class BoardUsedException(BoardException):
    def __str__(self):
        return "Вы уже стреляли в эту клетку"

class BoardWrongShipException(BoardException):
    pass


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Dot) and \
            self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Dot({self.x}, {self.y})"

class Ship:
    def __init__(self, bow, d, l):
        self.l = l
        self.bow = bow
        self.d = d
        self.lives = l

    @property
    def dots(self):

        ship_dots = []

        for i in range(self.l):

            now_x = self.bow.x
            now_y = self.bow.y

            if self.d:
                now_y += i
            else:
                now_x += i

            ship_dots.append(Dot(now_x, now_y))

        return ship_dots

    def shooten(self, shot):
        return shot in self.dots

class Board:
    def __init__(self, hid = False, size = 6):
        self.size = size
        self.hid = hid
        self.dead = 0
        self.field = [ ["O"]*size for _ in range(size) ]
        self.occupy = []
        self.ships = []

    def add_ship(self, ship):
        for d in ship.dots:
            if self.out(d) or d in self.occupy:
                raise BoardWrongShipException()

        for d in ship.dots:
            self.field[d.x][d.y] = "■"
            self.occupy.append(d)

            self.ships.append(ship)
            self.contour(ship)

    def contour(self, ship, verb=False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        for d in ship.dots:
            for dx, dy in near:
                now = Dot(d.x + dx, d.y + dy)

                if not (self.out(now)) and now not in self.occupy:
                    if verb:
                        self.field[now.x][now.y] = "."
                    self.occupy.append(now)


    def out(self, d):
        return not((0 <= d.x < self.size) and (0 <= d.y < self.size))

    def shot(self, d):
        if self.out(d):
            raise BoardOutException()

        if d in self.occupy:
            raise BoardUsedException()

        self.occupy.append(d)

        for ship in self.ships:
            if d in ship.dots:
                ship.lives -= 1
                self.field[d.x][d.y] = "X"
                if ship.lives == 0:
                    self.dead += 1
                    self.contour(ship, verb=True)
                    print("Корабль убит!")
                    return False
                else:
                    print("Корабль ранен!")
                    return True
        self.field[d.x][d.y] = "."
        print("Промах!")
        return False

    def start(self):
        self.occupy = []

    def win(self):
        return self.dead == len(self.ships)

    def __str__(self):
        res = ""
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.field):
            res += f"\n{i + 1} | " + " | ".join(row) + " |"

        if self.hid:
            res = res.replace("■", "O")
        return res

class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        pass

    def move(self):
        while True:
            try:
                aim = self.ask()
                repeat = self.enemy.shot(aim)
                return repeat
            except BoardException as e:
                print(e)


class AI(Player):
    def ask(self):
        d = Dot(randint(0, 5), randint(0, 5))
        print((f"Выстрел АИ: {d.x +1} {d.y +1}"))
        return d

class User(Player):
    def ask(self):
        while True:
            cords = input(f"Введите координаты    ").split()

            if len(cords) != 2:
                print(" Введите 2 координаты! ")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print(" Нужно вводить числа! ")
                continue

            x, y = int(x), int(y)

            return Dot(x-1, y-1)

class Game:
    def __init__(self, size=6):
        self.size = size
        pl_board = self.rnd_board()
        ai_board = self.rnd_board()
        ai_board.hid = False

        self.ai = AI(ai_board, pl_board)
        self.us = User(pl_board, ai_board)

    def rnd_board(self):
        board = None
        while board is None:
            board = self.rnd_place()
        return board

    def rnd_place(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attempts = 0
        for l in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), randint(0, 1), l)
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.start()

        return board

    def greet(self):
        print("-------------------")
        print("  Приветсвую вас  ")
        print("      в игре       ")
        print("    морской бой    ")
        print("-------------------")
        print(" формат ввода: x y ")
        print(" x - номер строки  ")
        print(" y - номер столбца ")

    def print_head(self):
        print("-" * 20)
        print("Доска человека:")
        print(self.us.board)
        print("-" * 20)
        print("Доска компьютера:")
        print(self.ai.board)
        print("-" * 20)

    def loop(self):
        num = 0
        while True:
            self.print_head()

            if num % 2 == 0:
                print("-" * 20)
                print("Ходит человек!")
                repeat = self.us.move()
            else:
                print("-" * 20)
                print("Ходит компьютер!")
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.us.board.dead == 7:
                self.print_head()
                print("Компьютер выиграл!")
                break

            if self.ai.board.dead == 7:
                self.print_head()
                print("Человек выиграл!")
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()


g = Game()
g.start()
