choice1 = "economy car"
choice2 = "saloon car"
choice3 = "sports car"
user_choice = input("enter your preferred car")
invalid = False
while invalid == False:
 if user_choice != choice1 or choice2 or choice3:
    invalid = True
    break
if user_choice == choice1:
     print("economy car")
elif user_choice == choice2:
     print("saloon car")
elif user_choice == choice3:
     print("sports car")
     print("have a nice day")