alarm = False
lights = False
movement_Ground = False
movement_first = False
system  = "on"

if system == "on":
    print("system is on")
    if movement_Ground == True:
        alarm = True
        lights = True
        print("intruder on the ground floor")
    if movement_first == True:
        alarm = True
        lights = True
        print("intruder on the first floor")

if system == "on" and (movement_Ground == True or movement_first == True):
    alarm = True
    lights = True