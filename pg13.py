my_tuple =(1,2,3,4,3)
#1.access item
item = my_tuple[1]
print(item) #output:2
#2. count item
count=my_tuple.count(3)
print(count)#output:2
#3.find index of item
index = my_tuple.index(3)
print(index) #output:
#4.concatenate tuples
new_tuple = my_tuple+(4,5)
print(new_tuple) #output:(1,2,3,4,3,4,5)
#5.convert to list to modify
temp_list = list(my_tuple)
temp_list.append(6)
my_tuple = tuple(temp_list)
print(my_tuple) #output:(1,2,3,4,3,6)