# my_list = [1, 'string', False, None]
# print (my_list, type(my_list))

# numbers = range (1,101)
# print(numbers)
# ls = list(numbers)  в список 
# print(ls, type(ls))

# ls = list ('hello world')
# print(ls) #каждую букву закинет как отдельный элемент

# Индексация в списках 
# ls = [1,2,3,4,5,'string', [True, False, None], 5]
# print(ls, len(ls))
# print(ls[5], ls[-1])
# print (ls[6][0])
# print(ls[3:6])

# #Циклы 
# # while i < 5: 
#     print(i)
#     i+= 1 

# ls = range(1,11)
# for num in ls:
#     print(num)

# ls = ['john', 'sansa', 'tirion','jamie']
# for x in ls:
#      print(f'hello mr/mrs {x}! Welcome to club!')

# for num in range(1,20):
#     if num % 2 == 0:
#         print(f'chislo {num} chetnoe, kvadrat: {num ** 2 }')
#     else: 
#         print(f'chislo {num} nechetnoe, kub: {num ** 3 }')

#----------------------------------------------------

#Методы списков 
# print(dir(list))

# append(element) - добавляет элемент в конец списка
# ls = [1,2,3]
# print(ls)
# ls.append(4)
# ls.append(5)
# ls.append('hello')
# ls.append([True, False])
# print(ls)

#extend(container) - расширяет список
# ls = [1,2,3]
# ls.extend([True, False])
# print(ls)

# ls = [1,2,3]
# ls1 = [4,5,6]
# print(ls + ls1)

#sort - сортирует, если передать reverse=true, то список отсортируется в убывающем порядкке
# from random import randint 
# ls = []
# for x in range (1,100):
#     num = randint(1,100)
#     ls.append(num)

# print(ls)
# ls = list(set(ls)) #для того чтоб не было повторений
# ls.sort(reverse=True)
# print('after:', ls, len(ls))

# insert (index, element) - добавляет элемент по указанному индексу 
# ls = ['string', 2,3,False]
# ls.insert(1,1)
# ls.insert(4, 'hello world')
# print(ls)

#remove(element) - удаляет элемент из списка если такого нет то выводится ошибка 
#pop([index]) - удаляет или возвращает элемент из списка по индексу но если индекс 
# не передать то удаляет последний элемент 

# ls = [5,1,2,4,4,5,5,5]
# print(ls)

# # ls.remove(5)
# # print(ls)
# while 5 in ls:
#     ls.remove(5)

# # print(ls)

# ls.pop()
# ls.pop(0)
# print(ls)

# ls = [1,2,3]
# deleted  = ls.pop()
# print(ls)
# print(deleted)


#update ---------------------------------

# ls = [1,2,'t',4,5,6,None,8]
# ls[2]=3
# print(ls)
# i = ls.index(None)
# print(i)
# ls[i] = 7 
# print (ls)



