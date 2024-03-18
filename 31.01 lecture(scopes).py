# Области видимости и пространства имен (scopes)
# спец технология которая определяет контекст имени в рамках которого мы модем ее использовать 
# a = 5
# def func():
#     b = 10
#     print(a)
#     print(b)


# func()
# print(b)

# biult-ins(встроенная область видимости) - print(), len()
# global(глобальная) - область одного файла 
# <enclosed>(замкнутая(не локальная, non local))
# local(локальная) -> внутри одной функции 


# a = 10 #global 
# print #build-in 
# len = 10 

# def hello(): #global 
#     a = 'hello' #local 
#     print(a, 'local, inside in func!')

# hello()
# print(a, 'global')
# print(len)

# LEGB - local enclosed global build-in
            # ----------->>>>>>>>>

# ____________________________________________________________________

# enclosed - замкнутое пространство имен - это локальное пространство у которого есть внутреннее
# (вложенное) локальное пространство 

# x = 'global'
# print(x,'1')

# def enclosed(): #enclosed
#     x = 'enclosed'
#     print(x,'3') #local

#     def local():   #eclosed
#         x ='local'
#         print(x,'2')    #enclosed 
#         local()
#         print(x,'4') #enclosed 
#     enclosed()
    
# print(x,'2')




# var = 0 

# def increment(): #LEGB
#     global var
#     var += 1

# increment()
# print(var)

# ФУНКЦИИ:
# global -> позволяет изменять значение глобальной переменной внутри локальной области 
# nonlocal -> позволяет изменить значение не локальной (замкнутой) 
# переменной находясь внутри локальной области 


def counter():     #ВЕРНУТЬСЯ И ПОНЯТЬ КАК РАБОТАЕТ НУЖНО 
    num = 0 
    def increment():
        nonlocal num 
        num +=1
        return num 
    return increment 







# c_steps = counter()
# c_jumps = counter()

# print(c_steps)
# for _ in range(1,10000):
#     c_steps()
    
    
# print(с_steps(),'steps')
# print(c_jumps(),'jump')
      


