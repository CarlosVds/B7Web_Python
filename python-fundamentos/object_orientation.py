# name = 'Carlos'
# age = 43

# def person():
#     print(f'My name is {name} and I am {age} years old')


# person()    

class Product:
    def description(data):
        print(f'{data.name} custs R$ {data.price}')


p1 = Product()
p1.name = 'CD Arlindo Cruz 2005'
p1.price = 50

p2 = Product()
p2.name = 'DVD Dudu nobre 2002'
p2.price = 40

p1.description()
p2.description()