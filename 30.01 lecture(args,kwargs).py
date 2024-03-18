# def sum_of_args (a,b,c=5,d=3): #параметры 
#     return a+b+c+d
# result = sum_of_args(1,2,3,4) #аргументы 
# print(result)
# print(sum_of_args(0,0))

# ________________________________________________________
# позиционные и именованные аргументы 
# def printParams(a,b,c):
#     print(a,'is stored in param a')
#     print(b,'is stored in param b')
#     print(c,'is stored in param c')

# # printParams(5,10,15)
# print()
# printParams(c=5,b=15,a=10)

# def sum_of_args(a,b,c,d):
#     return a+b+c+d
# print(sum_of_args(5,10,15,20)) #ARGUMENTS(позиционные аргументы)
# print(sum_of_args(a=5,b=15,c=23,d=13)) #KEYWORD ARGUMENTS (именованные аргументы)
# print(sum_of_args(5,10,d=20,c=15)) 

#_________________________________________________________________________

# оператор *(звездочка)

# a = [1,2,3]
# b = [4,5,6]
# c = [*a, *b] #соединение 

# print(c)

# __________________________________________________________________________
# ARGS, KWARGS 

# def func(*args,**kwargs):
#     print(args) #сохраняет в кортежи 
#     print(kwargs) #сохраняет в библиотеки

# func(1,2,3,5,45,a=3,b= 34)





# def printScores(student, *scores):
#     print(f'Name of Student: {student}')
#     print(f'AVR:{sum(scores)/ len(scores)}')
#     for x in scores:
#         print(f'Score: {x}')
# printScores('John Snow',100,90,90,100,100,95,98,93)






# def printPetNames(owner, **pets): #{'key': "value"}
#     print(f'owner name:{owner}')
#     # print(pets)
#     for pet,name in pets.items():
#         if type(name) == list:
#             print(f'{pet}:',*name)
#         else:
#             print(f'{pet}:{name}')
# printPetNames('Kim',dog = 'YeonTan',cat = 'Eshkeree',fish= ['Dori','Nemo','Fonk'])




# def get_some_data(a,b, *args,**kwargs):
#     print('параметры a и b:',a,b)
#     print('аргументы:',args)
#     print('именованные аргументы:', kwargs)

# get_some_data(1,2,3,4,5, lang = 'Python', car = 'Tesla')

#___________________________________________________________________________________________

# import string as s 
# from random import choice,shuffle 

# def generate_random_string(len_):
#     # print(s.ascii_letters, s.digits,s.punctuation)
#     symbols = s.ascii_letters + s.digits
#     res = [choice(symbols) for _ in range(1,len_)] + [choice(s.punctuation)]
#     print(res)

#     shuffle(res)
#     return ''.join(res)

# print(generate_random_string(15))
# print(generate_random_string(0))
# print(generate_random_string(10))
# print(generate_random_string(15))
# print(generate_random_string(333))

