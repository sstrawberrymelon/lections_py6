# работа с файлами

# Каретка - указатель - курсор 


# open('путь до файла')
# относительный путь 
# ---> file = open('files.py')
# ~ working directory -> (pwd в терминале) 

# абслютный путь 
# path = '/home/aisha/Desktop/py.6/files/lections/files.py'
# file = open(path,'r') #read 
# data = file.read()
# print(data, type(data))
# file.close() #обязательно закрыть 

# Режимы работы с файлами 
# 1) r/r+/rb - read - для чтения файлов 
# 2) w/w+/wb - write - для записи данных
# 3) a/a+ - для добавления данных 
# b,x

# file = open('test.txt', 'r')
# print(file.read())
# file.close()


# file = open('test.txt', 'r')
# print(file.readlines())
# file.close()
# file.close()


# контекстный менеджер 
# with open('test.txt','r') as file:
#     print(file.readline()) #первая строка 
#     print(file.readline())  #вторая строка 
#     print(file.readline())
#     print(file.read() #каретка читает)



# file.tell() - Возвращает индекс где находится картека 
# file.seek( - Перемещает курсор на индекс который вы передали)
          
# with open('nums.txt','r') as file: 
#     print(file.tell()) 
#     data = file.read()
#     print(data,'!!')
#     print(file.tell())
#     file.seek(0)
#     data = file.read()
#     print(data, '!!')
#     print(file.tell())


# with open('test.txt','w') as file: 
#     file.write('Hello world!\n')
#     file.write('My name is John Snow!\n')
#     file.write('I\'m Need Stark bastard\n')
#     file.seek(0)
#     data = ['Test 1 stroka\n'
#             'Test 1 stroka\n']
#     file.writelines(data)

# with open('test.txt','a+') as f:
#           f.write('\nJohn Snow is a king od North!')
#           f.write('\nYou know nothing John Snow!')
#           f.seek(0)
#           print(f.read())

# _______________________________________________________________________________________

# дана картинка вытащить imei коды и сохраним в файле для дальнейшей работы 
# regex python patterns регулярные выражения для работы с текстом 
# w3school прикольный сайт для изучения 
from PIL import Image #чтоб питон распознавал картинку 
import pytesseract 
import re 

base_url = '/home/aisha/Desktop/py.6/files/lections/'

def get_imei_codes(image_path: str): 
    string = pytesseract.image_to_string(image_path)
    list_of_imei = re.findall(r'IMEI\d.\s\d+', string)
    print(list_of_imei)
    

    with open('imei_codes.txt','w') as file: 
        file.writelines(f'{x}\n' for x in list_of_imei)


image_path = base_url + 'imei.jpg'
get_imei_codes(image_path)





    




