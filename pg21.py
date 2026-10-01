def convert_minutes(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    
    return hours, remaining_minutes

minutes = int(input("enter the number of minutes:"))  

hours, remaining_minutes = convert_minutes(minutes)

print(f"{minutes} minutes is equivalent to {hours} hour(s), {remaining_minutes} minutes.")