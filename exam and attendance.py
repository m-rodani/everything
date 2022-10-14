import sys
attendance = int(input("enter the attendance"))
if attendance < 90:
  sys.exit()
exam = int(input("enter the score"))
if attendance >= 90:
    if exam > 90:
        print("grade A")
    elif exam > 80 and exam <= 90:
        print("B")
    elif exam > 70 and exam <= 80:
        print("c")
    elif exam > 60 and exam <= 70:
        print("D")


