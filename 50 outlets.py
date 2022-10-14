import random
total = [0,0,0,0]
outletSales = [[random.randint(10000,80000) for cols in range(4)] for rows in range(50)]


for quarter in range(4):
    for row in range(50):
        total[quarter] += outletSales[row][quarter]

    print(f"the total for quarter {quarter+1} is {total[quarter]}")



















#sum_of_quarter1 = (sum(outletSales[0][0],[49][0]))
#print(sum_of_quarter1)