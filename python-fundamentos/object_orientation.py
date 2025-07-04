# name = 'Carlos'
# age = 43

# def person():
#     print(f'My name is {name} and I am {age} years old')


# person()    

# class Product:
#     def description(data):
#         print(f'{data.name} custs R$ {data.price}')


# p1 = Product()
# p1.name = 'CD Arlindo Cruz 2005'
# p1.price = 50

# p2 = Product()
# p2.name = 'DVD Dudu nobre 2002'
# p2.price = 40

# p1.description()
# p2.description()

#Constructor

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
        
#     def description(data):
#         print(f'{data.name} custs R$ {data.price}')


# p1 = Product('CD Arlindo Cruz 2005', 50)
# p2 = Product('DVD Dudu nobre 2002', 40)

# p1.description()
# p2.description()

#Encapsulation

# class Product:
#     def __init__(self, name, price):
#         self._name = name
#         self._price = price
        
#     def get_name(self):
#         return self._name
    
#     def get_price(self):
#         return self._price
    
#     def set_price(self, new_price):
#         self._price = float(new_price)

# p1 = Product('CD Arlindo Cruz 2005', 50)
# p2 = Product('DVD Dudu nobre 2002', 40)

# print(f"{p1.get_name()} custa ${p1.get_price()} dolar")
# p1.set_price(60)
# print(f"Agora o {p1.get_name()} custa ${p1.get_price()} dolar")

#Heritage

# class Person:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#     def get_name(self):
#         return self._name 
#     def get_age(self):
#         return self._age
#     def set_age(self, new_age):
#         self._age = int(new_age) 
             
# class Fucinay(Person):
#     def __init__(self, name, age, salary):
#         super().__init__(name, age)
#         self._salary = salary
        
#     def get_salary(self):
#         return self._salary
#     def set_salary(self, new_salary):
#         self._salary = float(new_salary)
        
#     def display_info(self):
#          print(f"Hello, my name is {self.get_name()} and I am {self.get_age()} years old, my salary a ${self.get_salary()} dolars")
         
# f1 = Fucinay("Carlos", 99, 7000)

# f1.display_info()

#Client Project

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    def get_name(self):
        return self._name
    def get_age(self):
        return self._age
    def set_age(self, new_age):
        self._age = new_age
    
class Client(Person):
    def __init__(self, name, age, email, ltv):
        super().__init__(name, age)
        self._email = email               
        self._ltv = ltv
        
    def get_email(self):
        return self._email
    
    def set_email(self, new_email):
        self._email = new_email
        
    def get_ltv(self):
        return self._ltv
    
    def set_ltv(self, new_ltv):
        self._ltv = new_ltv            

list = []            
            
list.append(Client("Carlos", 99, "carlos@carlos.com", 500))                           
list.append(Client("Marcella", 120, "marcella@marcella.com", 2000))

sum = 0

for itens in list:
    print(f'Client {itens.get_name()} -- LTV: ${itens.get_ltv()}')
    sum += itens.get_ltv()                         

print('------------------')
print(f'Total LTV: {sum}')    