#numbers = [] # empty array
numbers = [34,2,3456,456] # populated array
for i in range(len(numbers)-1,-1,-1):
    print(numbers[i])
total = sum(numbers)
avg = total / 5
print(total)
print(avg)