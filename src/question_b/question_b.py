#write functions here, don't add input('') statements here!

def get_miles_per_hour(kilometers, minutes):
    if kilometers < 0 or minutes <= 0:
        return "Invalid arguments"
    
    hours = minutes / 60
    miles = kilometers * 0.621371
    mph = miles / hours
    return mph