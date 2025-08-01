with open('Manipulation_Files_PEP8_Testing_Simple\lista.txt', 'r') as list:
    for itens in list:
        print(f"- {itens.strip()}")
        
        
print('----------------------')        

with open('Manipulation_Files_PEP8_Testing_Simple\lista.txt', 'a') as list:
    new_list = input('Enter new item: ')
    if new_list != '':
        list.write(f'{new_list}\n')
        print('Item added successfully ')
    else:
        print('Item not added')    
        
print("--------------------------------")  