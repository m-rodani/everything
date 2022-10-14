grid = [["x" for cols in range(4)] for rows in range(6)]
grid[0][0] = "o"
for list in grid:
    print(list)
row_value = int(input("enter the row"))
column_value = int(input("enter the column value"))
if row_value > 5:
    row_value = int(input("row value  is out of range try again"))
if column_value > 3:
    column_value = int(input("column value  is out of range please try again"))
grid[row_value][column_value] = "O"
grid[0][0] = "x"
for list in grid:
    print(list)
