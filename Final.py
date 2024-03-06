from graphics import *

def draw_board(win):
    for i in range(1, 3):
        line = Line(Point(i * 100, 0), Point(i * 100, 300))
        line.draw(win)
        line = Line(Point(0, i * 100), Point(300, i * 100))
        line.draw(win)

def get_square_clicked(pt):
    col = pt.getX() // 100
    row = pt.getY() // 100
    return int(row), int(col)

def draw_move(win, row, col, player):
    center = Point(col * 100 + 50, row * 100 + 50)
    if player == "X":
        x1 = Line(Point(center.getX() - 40, center.getY() - 40), Point(center.getX() + 40, center.getY() + 40))
        x2 = Line(Point(center.getX() + 40, center.getY() - 40), Point(center.getX() - 40, center.getY() + 40))
        x1.draw(win)
        x2.draw(win)
    else:
        o = Circle(center, 40)
        o.draw(win)

def check_win(board):
    for row in board:
        if len(set(row)) == 1 and row[0] is not None:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != None:
            return True
    if board[0][0] == board[1][1] == board[2][2] != None or board[0][2] == board[1][1] == board[2][0] != None:
        return True
    return False

def game_over(win, player):
    message = Text(Point(150, 150), f"Player {player} wins!")
    message.setSize(24)
    message.setStyle("bold")
    message.draw(win)
    win.getMouse()
    win.close()



def board_full(board):
    for row in board:
        if None in row:
            return False
    return True

def game_over_draw(win):
    message = Text(Point(150, 150), "It's a draw!")
    message.setSize(24)
    message.setStyle("bold")
    message.draw(win)
    win.getMouse()
    win.close()

def main():
    win = GraphWin("Tic Tac Toe", 300, 300)
    win.setBackground("light grey")

    draw_board(win)
    board = [[None for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    currentPlayer = 0
    while True:
        pt = win.getMouse()
        row, col = get_square_clicked(pt)

        if board[row][col] is None:
            draw_move(win, row, col, players[currentPlayer])
            board[row][col] = players[currentPlayer]

            if check_win(board):
                game_over(win, players[currentPlayer])
                return

            # Check for a draw after each move
            if board_full(board) and not check_win(board):
                game_over_draw(win)
                return

            currentPlayer = (currentPlayer + 1)%2



main()
