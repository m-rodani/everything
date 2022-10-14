car_mileage_previous = int(input("enter the mileage of the car the last time it was filled"))
car_mileage_now = int(input("enter the mileage of the car now"))
diff = car_mileage_now - car_mileage_previous
litres_to_fill_tank = int(input("enter the number of litres to fill the tank"))
gallons = litres_to_fill_tank * 0.22
print(gallons)
miles_per_gallon = diff/gallons
print(round(miles_per_gallon,2))
