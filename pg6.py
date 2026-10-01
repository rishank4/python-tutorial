def celsius_to_kelvin(celsius):
    kelvin=celsius+273.15 #k=C+273.15
    return kelvin

celsius_temp=float(input("enter temperature in celsius:"))
kelvin_temp=celsius_to_kelvin(celsius_temp)
print(f"Tenperature in kelvin:{kelvin_temp}")