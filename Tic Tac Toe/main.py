def sum(a, b, c):
    return a+b+c


def printBoard(xstate, zero_state):
    # condition for each matrix element
    zero = 'X' if xstate[0] else ('O' if z_state[0] else ' ')
    one = 'X' if xstate[1] else ('O' if z_state[1] else ' ')
    two = 'X' if xstate[2] else ('O' if z_state[2] else ' ')
    three = 'X' if xstate[3] else ('O' if z_state[3] else ' ')
    four = 'X' if xstate[4] else ('O' if z_state[4] else ' ')
    five = 'X' if xstate[5] else ('O' if z_state[5] else ' ')
    six = 'X' if xstate[6] else ('O' if z_state[6] else ' ')
    seven = 'X' if xstate[7] else ('O' if z_state[7] else ' ')
    eight = 'X' if xstate[8] else ('O' if z_state[8] else ' ')

    # printing
    print(f"    {zero} | {one} | {two}")
    print(f"    --|---|---")
    print(f"    {three} | {four} | {five}")
    print(f"    --|---|---")
    print(f"    {six} | {seven} | {eight}", end="\n\n")


def checkWin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
            [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if (sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            printBoard(x_state,z_state)
            print()
            print("X Won the match, Wooohooo !!", end="\n\n")
            return 1
        if (sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            printBoard(x_state,z_state)
            print()
            print("O Won the match, Wooohooo !!", end="\n\n")
            return 0
    return -1


if __name__ == "__main__":
    x_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    z_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  # 1 for X and 0 for zero
    print()
    print("--------------------------")
    print("| Welcome to Tic-Tac-Toe |")
    print("--------------------------", end="\n\n")

    # While loop
    ct=0
    while (True):
        printBoard(x_state, z_state)
        if (turn == 1):
            print("X's Chance", end="\n\n")
            value = int(input("Please enter a value : "))
            value = value-1
            print()
            x_state[value] = 1
            ct=ct+1
        else:
            print("O's Chance", end="\n\n")
            value = int(input("Please enter a value : "))
            value = value-1
            print()
            z_state[value] = 1
            ct=ct+1
        cwin = checkWin(x_state, z_state)
        if cwin != -1:
            print("Match over",end="\n\n")
            break
        if ct==9 and cwin==-1:
            printBoard(x_state,z_state)
            print()
            print("Nobody won",end="\n\n")
            break
        turn = 1-turn
