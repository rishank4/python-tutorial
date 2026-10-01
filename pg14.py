my_dict ={"name":"Alice","age": 25}
print(my_dict) 

my_dict["city"] ="New York"
print(my_dict)
 
my_dict["age"] =26
print(my_dict)

del my_dict["name"]
print(my_dict)

print(my_dict.get("city"))
print(my_dict.get("country","Not Found"))
                   
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())