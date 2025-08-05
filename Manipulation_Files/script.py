# file = open("Manipulation_Files_PEP8_Testing_Simple\lista.txt", "r")

# line = file.readlines()

# for itens in line:
#     print(f'Lines: {itens.strip()}')

# file = open('Manipulation_Files_PEP8_Testing_Simple\lista.txt', 'a')
# file.write('Mariana\n')
# file.close()

# with open('Manipulation_Files_PEP8_Testing_Simple\lista.txt', 'r') as file:
#     for itens in file:
#         print(itens.strip()) 
# file = open('Manipulation_Files/lista.txt', 'a')

# readFile = file.readlines()

# for line in readFile:
#     print(f'Lines: {line.strip()}')

# writeFile = file.write('Carlos\n')
# writeFile = file.write('Santos\n')
# file.close()

# with open('Manipulation_Files/lista.txt', 'r') as files:
#     for list in files:
#         print(f'-{list.strip()}')
# print('----------------------')    

# with open('Manipulation_Files/lista.txt', 'a') as files:
#     digitItem = input('Enter an item: ')
#     if digitItem != "":
#         files.write(f'{digitItem.strip()}\n')
#         print('Item added successfully')
#     else:
#         print("You didnt't type anything")          
# print("----------------------")          

class List:
    def __init__(self, name):
        self._fileName = f'{name}.txt'
    
    def get_file(self):
        list = []
        with open(self._fileName, 'r') as file:
            for item in file:
                list.append(item.strip())
        return list 
    
    def add_item(self, new_item):
        with open(self._fileName, 'a') as file:
            file.write(f'{new_item}\n')
            if new_item != "":
                return True
            else:
                return False            
            
list = List('Manipulation_Files/lista')
for item in list.get_file():
    print(f'-{item.strip()}')
 
print("----------------------")

enter = input('Enter new item: ')
added = list.add_item(enter)

if added == True:
    print('Item added succssfully')
else:
    print('Item dont type anything')    
     