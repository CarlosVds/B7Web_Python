# #list
# list = ['rice', 'beans', 'flour', 'egg']

# #tupla
# list1 = ('rice','beans','flour','egg')

# #dictionary

# pessoa = {
#     'name':'Carlos',
#     'age': 99,
#     'city':'Brazil'
# }

# print(pessoa['name'])
# post = [
#     {'title': 'First title blog', 'author':'Carlos'},
#     {'title': 'Second title blog', 'author':'Enzo'},
#     {'title': 'Third title blog', 'author':'Marcella'}
# ]

# for item in post:
#     print(item['title'])
#     print(f'Author: {item['author']}')
#     print('--------------------')

list = [
    {'name':'Carlos', 'age': 99},
    {'name':'Enzo', 'age': 140}
]

def newName(name, age):
    list.append({'name': name, 'age':age})
    
newName('Marcella', 120)
newName('Erika', 40)
newName('Patricia', 60)

print(list)    