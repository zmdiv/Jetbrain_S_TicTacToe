turn = "X"
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
rows = [board[0], board[1], board[2]], [board[3], board[4], board[5]], [board[6], board[7], board[8]]
cols = [[rows[0][0], rows[1][0], rows[2][0]], [rows[0][1], rows[1][1], rows[2][1]],
        [rows[0][2], rows[1][2], rows[2][2]]]
diag = [rows[0][0], rows[1][1], rows[2][2]], [rows[0][2], rows[1][1], rows[2][0]]


def print_grid():
    print(f'---------\n| {rows[0][0]} {rows[0][1]} {rows[0][2]} |'
          f'\n| {rows[1][0]} {rows[1][1]} {rows[1][2]} |'
          f'\n| {rows[2][0]} {rows[2][1]} {rows[2][2]} |'
          f'\n---------')


def positions():
    global turn
    while True:
        try:
            pos = [int(x) for x in input("Enter the coordinates: ").split()]
            if pos[0] > 3 or pos[1] > 3:
                print("Coordinates should be from 1 to 3!")
            else:
                if (all(item != " " for item in rows[0]) and
                        all(item != " " for item in rows[1]) and
                        all(item != " " for item in rows[2])):
                    print("Draw")
                    break
                elif rows[pos[0] - 1][pos[1] - 1] == "X" or rows[pos[0] - 1][pos[1] - 1] == "O":
                    print("This cell is occupied! Choose another one!")
                else:
                    if turn == "X":
                        rows[pos[0] - 1][pos[1] - 1] = "X"
                        print_grid()
                        turn = "O"
                        if (all(item == "X" for item in rows[0]) or
                                all(item == "X" for item in rows[1]) or
                                all(item == "X" for item in rows[2]) or
                                all(item == "X" for item in [rows[0][0], rows[1][0], rows[2][0]]) or
                                all(item == "X" for item in [rows[0][1], rows[1][1], rows[2][1]]) or
                                all(item == "X" for item in [rows[0][2], rows[1][2], rows[2][2]]) or
                                all(item == "X" for item in [rows[0][0], rows[1][1], rows[2][2]]) or
                                all(item == "X" for item in [rows[0][2], rows[1][1], rows[2][0]])):
                            print("X wins")
                            break
                        elif (all(item != " " for item in rows[0]) and
                              all(item != " " for item in rows[1]) and
                              all(item != " " for item in rows[2])):
                            print("Draw")
                            break

                    elif turn == "O":
                        rows[pos[0] - 1][pos[1] - 1] = "O"
                        print_grid()
                        turn = "X"
                        if (all(item == "O" for item in rows[0]) or
                                all(item == "O" for item in rows[1]) or
                                all(item == "O" for item in rows[2]) or
                                all(item == "O" for item in [rows[0][0], rows[1][0], rows[2][0]]) or
                                all(item == "O" for item in [rows[0][1], rows[1][1], rows[2][1]]) or
                                all(item == "O" for item in [rows[0][2], rows[1][2], rows[2][2]]) or
                                all(item == "O" for item in [rows[0][0], rows[1][1], rows[2][2]]) or
                                all(item == "O" for item in [rows[0][2], rows[1][1], rows[2][0]])):
                            print("O wins")
                            break
                        elif (all(item != " " for item in rows[0]) and
                              all(item != " " for item in rows[1]) and
                              all(item != " " for item in rows[2])):
                            print("Draw")
                            break
                    else:
                        positions()
        except ValueError:
            print("You should enter numbers!")


print_grid()
positions()
