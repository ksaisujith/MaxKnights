import random

class nKnights:

    __slots__ = "n" , "board", "max_knights", "knights_placed"

    def __init__(self,board_size):
        """

        :param board_size:
        """
        self.n = int(board_size)
        self.start()

    def start(self):
        """

        :return:
        """
        self.board = [[ 0 for r in range(self.n)] for c in range(self.n)]
        self.max_knights = 0
        self.knights_placed = 0

    def possible_positions(self,current_position):
        """

        :param current_position:
        :return:
        """
        x = int(current_position[0])
        y = int(current_position[1])
        moves = []

        if x+2 < self.n:
            if y-1 >= 0:
                moves.append((x+2, y-1))
            if y+1 < self.n:
                moves.append((x+2 , y+1))

        if x + 1 < self.n:
            if y - 2 >= 0:
                moves.append((x + 1, y - 2))
            if y + 2 < self.n:
                moves.append((x + 1, y + 2))

        if x - 1>= 0:
            if y - 2 >= 0:
                moves.append((x - 1, y - 2))
            if y + 2 < self.n:
                moves.append((x - 1, y + 2))

        if x - 2>= 0:
            if y - 1 >= 0:
                moves.append((x - 2, y - 1))
            if y + 1 < self.n:
                moves.append((x - 2, y + 1))

        return moves

    def random(self):
        """
        Places the knights randomly

        :return:
        """
        while self.knights_placed <= self.max_knights:
            x_position = random.randint(0,self.n -1)
            y_position = random.randint(0,self.n -1)
            if self.board[x_position][y_position] != "k" and self.check_safety((x_position,y_position)):
                self.board[x_position][y_position] = "k"
                self.knights_placed += 1

    def knight_canAdd(self):
        """

        :return:
        """
        for row in range(self.n):
            for column in range(self.n):

                if self.board[row][column] != "k":
                    safe_space_available = True

                    for move in self.possible_positions((row,column)):
                        if self.board[move[0]][move[1]] == "k":
                            safe_space_available = False
                    if safe_space_available:
                        return True
        return False

    def check_safety(self, position):
        """

        :param position:
        :return:
        """

        for move in self.possible_positions((position[0], position[1])):
            if self.board[move[0]][move[1]] == "k":
                return False
        return True

    def place_knights(self):
        """

        :return:
        """
        max_acheived = 0
        knights_placed = []

        for iteration in range(self.n ** 2):
            while self.knight_canAdd():
                self.random()
                self.max_knights += 1

            if max_acheived < self.max_knights:
                max_acheived = self.max_knights
                knights_placed = self.board.copy()

            # reset everything
            self.start()

        self.board = knights_placed.copy()
        self.max_knights = max_acheived


    def print_board(self):
        """

        :return:
        """
        for row in self.board:
            for e in row:
                print(e ,"\t", end=" ")
            print("\n")

def main():
    k = nKnights(input("Please enter the board size(n)"))
    k.place_knights()
    k.print_board()
    print("Maximum knights that can be placed:",k.max_knights)

if __name__ == '__main__':
    main()