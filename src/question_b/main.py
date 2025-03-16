#add import

def get_miles_per_hour(kilometers, minutes):
    if kilometers < 0 or minutes <= 0:
        return "Invalid arguments"
    
    hours = minutes / 60
    miles = kilometers * 0.621371
    mph = miles / hours
    return mph

kilometers = int(input("Enter the number of kilometers: "))
minutes = int(input("Enter the number of minutes: "))

result = get_miles_per_hour(kilometers, minutes)
print(f"The speed is {result:.6f} miles per hour")