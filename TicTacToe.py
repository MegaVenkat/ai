def check(arr, ch):
    if(arr[0][0] == ch and arr[0][1] == ch and arr[0][2] == ch or arr[0][0] == ch and arr[1][0] == ch and arr[2][0] == ch or arr[0][0] == ch and arr[1][1] == ch and arr[2][2] == ch or arr[0][1] == ch and arr[1][1] == ch and arr[2][1] == ch or arr[0][2] == ch and arr[1][2] == ch and arr[2][2] == ch or arr[0][2] == ch and arr[1][1] == ch and arr[2][0] == ch or arr[1][0] == ch and arr[1][1] == ch and arr[1][2] == ch or arr[2][0] == ch and arr[2][1] == ch and arr[2][2] == ch):
        return True
    return False


def allOcupied(arr):
    for i in range(0, 3):
        for j in range(0, 3):
            if arr[i][j] == ".":
                return False
    return True


def display(arr):
    for i in range(0, 3):
        for j in range(0, 3):
            print(arr[i][j]+"\t", end="")
        print()


arr = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
for i in range(0, 3):
    for j in range(0, 3):
        print(arr[i][j]+"\t", end="")
    print()
player1 = str(input("Enter player 1 name :"))
player2 = str(input("Enter player 2 name :"))
print("X is the symbol for "+player1+" and O for "+player2)


while(True):
    while(True):
        row1 = int(input(player1+" ,plz enter your cell row number : "))
        col1 = int(input(player1+" ,plz enter your cell column number : "))
        if row1 < 0 or row1 > 2 or col1 < 0 or col1 > 2:
            print("Invalid move! Plz enter correct cell number.")
        elif arr[row1][col1] == ".":
            arr[row1][col1] = "X"
            print("\033[H\033[J")
            display(arr)
            break
        else:
            print(player1+" plz enter cell number which are unoccupied.")

    if check(arr, "X"):
        print("Game Over! "+player1+" wins the game.")
        break
    if allOcupied(arr):
        print("Game Drawn")
        break
    while True:
        row2 = int(input(player2+" ,plz enter your cell row number : "))
        col2 = int(input(player2+" ,plz enter your cell column number : "))
        if row2 < 0 or row2 > 2 or col2 < 0 or col2 > 2:
            print("Invalid move! Plz enter correct cell number.")
        elif arr[row2][col2] == ".":
            arr[row2][col2] = "O"
            print("\033[H\033[J")
            display(arr)
            break
        else:
            print(player2+" plz enter cell number which are unoccupied.")

    if check(arr, "O"):
        print("Game Over!"+player2+" wins the game.")
        break
