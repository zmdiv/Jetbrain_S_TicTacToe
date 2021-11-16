board = ["X", " ", "X", "X", "O", "X", "X", "X", "X"]
rows = [board[0], board[1], board[2]], [board[3], board[4], board[5]], [board[6], board[7], board[8]]

if (all(item != " " for item in rows[0]) and
        all(item != " " for item in rows[1]) and
        all(item != " " for item in rows[2])):
    print("Draw")
else:
    print("play")