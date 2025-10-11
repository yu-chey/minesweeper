import random

class Cell:
    def __init__(self, around_mines, mine, fl_open=False) -> None:
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open


class GamePole:
    __lose = False

    @staticmethod
    def get_around(array, i, j) -> int:
        bounds, count = 0, 0
        for row in range(i - 1, i + 2):
            for col in range(j - 1, j + 2):
                bounds = 0 <= row <= len(array) - 1 and 0 <= col <= len(array[0]) - 1
                if i == row and j == col:
                    continue
                if bounds and array[row][col] == True:
                    count += 1
        return count

    @staticmethod
    def get_random(n) -> tuple:
        return random.randint(0, n - 1), random.randint(0, n - 1)

    def __init__(self, n, m) -> None:
        self.pole = None
        self.raw_list = [[False for _ in range(n)] for _ in range(n)]
        self.n = n
        self.m = m
        self.init()

    def init(self) -> None:
        # create the field with mines
        n = self.n
        m = self.m
        mines_placed = 0
        while mines_placed < m:
            row, col = self.get_random(n)
            if not self.raw_list[row][col]:
                self.raw_list[row][col] = True
                mines_placed += 1

        # create a list with objects
        self.pole = [[Cell(self.get_around(self.raw_list, i, j), self.raw_list[i][j]) for j in range(n)] for i in
                     range(n)]

    def show(self) -> None:
        for i in range(self.n):
            data_list = list()
            for j in range(self.n):
                if self.pole[i][j].fl_open:
                    if self.pole[i][j].mine:
                        data_list.append("X")
                    else:
                        data_list.append(str(self.pole[i][j].around_mines))
                else:
                    data_list.append('#')
            print(" ".join(data_list))

    def open(self, row, col) -> None:
        if self.__lose or self.pole[row][col].fl_open:
            return

        if self.pole[row][col].mine:
            self.__lose = True
            print("------------------Вы проиграли!--------------------")
            self.pole[row][col].fl_open = True
            self.show()
            return

        if not self.__lose:
            self.pole[row][col].fl_open = True


pole_game = GamePole(10, 12)
pole_game.show()