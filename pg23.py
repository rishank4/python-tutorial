#class definition
class person:
    def __init__(self,name,age,id):
          #constructor
        self.name = name
        self.age = age
        self.id= id
        
    def greet(self): 
            return f"My name is {self.name} and i am {self.age}years old  my id is {self.id}"
        
        #Object creation
p1=person ("rishan",25,5)
p2=person("hanan",21,2)

#inheritence
class Employee(person): #Inherits from person
    def __init__(self, name, age,id, emp_id):
        super().__init__(name, age,id)
        self.emp_id = emp_id
        
    def show_id(self):
        return f"Employee ID: {self.emp_id} emp name is  {self.name} "
    
e1 = Employee("Bob", 30,14, "E123")

print(e1.show_id())

