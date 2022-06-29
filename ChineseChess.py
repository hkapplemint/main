#Red goes first
import copy

class ChineseChess:

    def __init__(self):
        self.board = []

    def create_board(self):
        board = self.board
        for i in range(5):
            row = []
            for j in range(9):
                row.append(" -  ")
            board.append(row)

        #black
        board[0][0] = "b車1"
        board[0][8] = "b車2"
        board[0][1] = " - " #"b馬1"
        board[0][7] = "b馬2"
        board[0][2] = "b象1"
        board[0][6] = "b象2"
        board[0][3] = "b士1"
        board[0][5] = "b士2"
        board[0][4] = "b將 "
        board[2][1] = "b砲1"
        board[2][7] = "b砲2"
        board[3][0] = "b卒1"
        board[3][2] = "b卒2"
        board[3][4] = "b卒3"
        board[3][6] = "b卒4"
        board[3][8] = "b卒5"

        board_r = board[::-1]
        board_r_n = copy.deepcopy(board_r)

        for i in range(5):
            for j in board_r_n[i]:
                if j[0] == "b":
                    k = j.replace("b","r")
                    board_r_n[i][board_r_n[i].index(j)] = k

        column_header = []
        row_c = []
        for i in range(9):
            row_c.append("  " + str(i + 1) + " ")
        column_header.append(row_c)

        self.board = column_header + board + board_r_n

        temp_count = 0
        for i in " ABCDEFGHIJ":
            self.board[temp_count].append(i)
            self.board[temp_count] = self.board[temp_count][-1:] + self.board[temp_count][:-1]
            temp_count += 1

        return self.board

    def Chariot(self, player, number, row, column):
        peg = player + "車"  + str(number)

        for i in range(len(self.board)):
            if row == self.board[i][0]:
                row = i

        def Chariot_collision(original_row, original_column, target_row, target_column):
            if original_row == target_row and original_column < target_column:
                for i in range(self.board[original_row].index(peg),target_column):
                    print(i)
                    if self.board[original_row][target_column] == None or self.board[original_row][target_column] == "-":
                        print("You can move~")
                        break
                        return True
                    else:
                        print("You are blocked")
                        break
                        return False
        Chariot_collision(row,1,row,2)

        for og_row in range(11):
            for peg_name in self.board[og_row]:
                if peg_name == peg:
                    print("hi")
                    print(self.board[og_row][0])
                    print(self.board[og_row].index(peg_name))

                    if (row == self.board[og_row] and
                            self.board[og_row][column][0] != player):
                        self.board[og_row][column] = self.board[og_row][self.board[og_row].index(peg_name)]
                        self.board[og_row][self.board[og_row].index(peg_name)] = " - "
                        break
                    elif column == self.board[og_row].index(peg_name) and self.board[row][self.board[og_row].index(peg_name)][0] != player:
                        self.board[row][self.board[og_row].index(peg_name)] = self.board[og_row][self.board[og_row].index(peg_name)]
                        self.board[og_row][self.board[og_row].index(peg_name)] = " - "
                        break
                    else:
                        print("You can't move in that way!")

    def start(self):

        self.create_board()

        print("\n")
        print(*self.board, sep = "\n")
        self.Chariot("r",1,"J",1)
        print(*self.board, sep = "\n")

chinese_chess = ChineseChess()
chinese_chess.start()
