name = ["aishah", "iman", "mohammed", "ku","jess","declan"]
searchItem = input("enter student name")
recordNumber = 0
for i in range(0,len(name)):
        if name[i] == searchItem:
         recordNumber = i + 1
         print( searchItem, "record number is" , recordNumber)
        elif name[i] != searchItem:
            print( searchItem , " is not in the list")