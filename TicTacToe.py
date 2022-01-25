from dis import dis


def check(arr, ch):
    if(arr[0][0] == ch and arr[0][1] == ch and arr[0][2] == ch or arr[0][0] == ch and arr[1][0] == ch and arr[2][0] == ch or arr[0][0] == ch and arr[1][1] == ch and arr[2][2] == ch or arr[0][1] == ch and arr[1][1] == ch and arr[2][1] == ch or arr[0][2] == ch and arr[1][2] == ch and arr[2][2] == ch or arr[0][2] == ch and arr[1][1] == ch and arr[2][0] == ch or arr[1][0] == ch and arr[1][1] == ch and arr[1][2] == ch or arr[2][0] == ch and arr[2][1] == ch and arr[2][2] == ch):
        return True
    return False


def allOcupied(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if arr[i][j] == ".":
                return False
    return True

def display(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            print(arr[i][j]+"\t",end="")
        print()
    
    

rows, cols = (3, 3)
arr = [['.']*cols]*rows
for i in range(0, len(arr)):
    for j in range(0, len(arr)):
        print(arr[i][j]+"\t", end="")
    print()
player1 = str(input("Enter player 1 name :"))
player2 = str(input("Enter player 2 name :"))
print("X is the symbol for "+player1+" and O for "+player2)


while(True):
    row, col = input(player1+" ,plz enter your cell coordinates.").split()
    row=int(row)
    col=int(col)
    if(arr[row][col] == "."):
        arr[row][col] = "X"
        display(arr)
    else:
        print(player1+" plz enter cell number which are unoccupied.")
    if(check(arr, "X")):
        print("Game Over! "+player1+" wins the game.")
        break
    row, col = input(player2+" ,plz enter your cell coordinates.").split()
    row=int(row)
    col=int(col)
    if(arr[row][col] == "."):
        arr[row][col] = "O"
        display(arr)
    else:
        print(player2+" plz enter cell number which are unoccupied.")
    if(check(arr, "O")):
        print("Game Over !"+player2+" wins the game.")
        display(arr)
        break
    if(allOcupied(arr)):
        print("Game Drawn")
        break
