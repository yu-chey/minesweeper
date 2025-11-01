import random

class Cell:
    def __init__(self, around_mines, mine, opened=False) -> None:
        self.around_mines = around_mines
        self.mine = mine
        self.opened = opened


class GamePole:
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
        self.__cells_to_open = n * n - m
        self.m = m
        self.init()
        self.__game_over = False
        self.__cells_to_open = 0
        self.__opened_count = 0

    def init(self) -> None:
        # create the field with mines
        self.__game_over = False
        self.__opened_count = 0
        n = self.n
        m = self.m
        mines_placed = 0
        while mines_placed < m:
            row, col = self.get_random(n)
            if not self.raw_list[row][col]:
                self.raw_list[row][col] = True
                mines_placed += 1

        # create a list with objects
        self.pole = [[Cell(self.get_around(self.raw_list, i, j), self.raw_list[i][j])
                    for j in range(n)]
                    for i in range(n)]

    def get_result_game(self) -> bool:
        if self.__game_over:
            return False
        else:
            return True

    def show(self) -> None:
        for i in range(self.n):
            data_list = list()
            for j in range(self.n):
                if self.pole[i][j].opened:
                    if self.pole[i][j].mine:
                        data_list.append("X")
                    else:
                        data_list.append(str(self.pole[i][j].around_mines))
                else:
                    data_list.append('#')
            print(" ".join(data_list))

    def open_neighbors(self, row, col):
        N = self.n

        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if 0 <= r < N and 0 <= c < N and (r != row or c != col):
                    if not self.pole[r][c].opened:
                        self.open(r, c)

    def open(self, row, col):
        if self.__game_over or self.pole[row][col].opened:
            return

        if self.pole[row][col].mine:
            self.__game_over = True
            print("You lost!")
            self.pole[row][col].opened = True
            return

        self.pole[row][col].opened = True
        self.__opened_count += 1

        if self.__cells_to_open == self.__opened_count:
            self.__game_over = True
            print("You won!")

        if self.pole[row][col].around_mines == 0:
            self.open_neighbors(row, col)