#dictionary словарь упорядоченная коллекция элементов (python 3.7 -> ordered)
#  Каждый элемент внутри словаря хранится в виде пары --> {ключ:значение}
#ассоциативный массив, hash table, object(ts). structure == dictionary.py 
#ключи могут только неизменяемые типы данных и в словаре сохраняются только уникальные ключи 
# тогда как в значении могут выступать любые типы данных и любые значения

# thisdict = {
#     'brand': 'Ford',
#     'model':'Mustang',
#     'year': 1967,
# }
# ls = ['Ford', 'Mustang',1967]
# print(thisdict, type(thisdict))
# print(thisdict, ['brand'] , thisdict ['model'])
# print(thisdict['year'])

# thisdict['motor'] = 'GTI Turbo'
# thisdict['model'] = 'fiesta'
# print(thisdict) 


# print(dir(dict))
# items, keys , values 



# user_info = {
#     'first_name': 'John',
#     'last_name': 'Snow',
#     'age': 24,
#     'email': 'bastard123@gmail.com',
#     'role': 'admin', 
#     }
# ls = list(user_info.keys())
# ls1 = user_info.keys()
# ls2= user_info.items()
# ls3 = user_info.values()

# print(ls,ls2,ls3,ls1)


# for value in user_info.values():
#     print(value)

# for key, value in user_info.items():
#     print(f'keys:{key}, values: {value}')

#изменение словарей 
# dict_ = {'name': 'Jack', 'age': 17}
# print(dict_)
# dict_['name'] = 'John '
# dict_['adress'] = 'WinterFell'
# print(dict_)
# dict_.update(age=24,adress='Blackcastle')
# print(dict_)


# dict_ = {1: 'Pizza', 2: 'Burger', 3: 'Steak'}
# print(dict_[2], '!!!')
# print(dict_.get(3))

# #setdefault - работает так же как и get, но если нет такого ключа создает новую


# dict_ = {1: 'Pizza', 2: 'Burger', 3: 'Steak'}
# print(dict_.setdefault('6'))
# print(dict_)
 
# #создание fromkeys 
# ls = list(range(1,20))
# new_dict = dict.fromkeys(ls,'default')                        
# print(new_dict)



# #удаление эдементов 
# #pop, popitem 

# pop(<key>) - удаляет пару по ключу 
# popitem() - удаляет последнюю пару 

# dict = {'first_name': 'John',
#     'last_name': 'Snow',
#     'age': 24,
# }
# print (dict)
# removed = dict.pop('last_name')
# print (dict)
# print(removed)
# print('------------')
# removed = dict.popitem()
# print (dict)
# print (removed)

# roles = { 1: 'Admin',
#          2: 'Customer',
#          3:'Vendor',

# }

# users = {
#     55: {
#     'id': 55, 'role': roles [3], 'username' : 'Tirion'
# }, 
#     12: {
    
#     'id' :12, 'role': roles[1], 'username' : 'Tirion'
# },
#     4: {
#     'id' :4, 'role': roles[2], 'username' : 'Tirion'
 
#     }}

# print(users)

# product = {
#     'id': 1, 
#     'title': 'Samsung Galaxy S23 Ultra',
#     'description': 'lorem ipsum', 
#     'price': 1000
# }
# print(product)
# id_user = int(input('Vvedite id:'))
# if users[id_user]['role'] == roles[1]:
#     product['desription'] = input ('Vvedite opisaniye:')
# else: 
#     print('you dont have permission')
# print()
# print(product)

