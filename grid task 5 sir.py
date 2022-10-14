grid = [["x" for cols in range(4)] for rows in range(6)]
grid [0][0] = "o"
for row in grid:
    print(row)


while True:
    while True:
        row = int(input("enter row"))
        col = int(input("enter column"))
        if (col >= 1 and col <=4) and (row >= 1 and row <=6):
            col -= 1
            row -= 1
            break
        else:
            print("error try again")
    grid = [["x" for cols in range(4)] for rows in range(6)]
    grid[row][col] = "o"
    for row in grid:
        print(row)
