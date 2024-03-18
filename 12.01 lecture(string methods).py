# Методы строк это как инструмент 
#print(dir('123'))

#посчитать сколько буков е в тексте метод count кол во входящих
# text = 'hello ooo hello'
# print(text.count('o'))
# print(text.count('hello'))

# text = input('vvedite text: ')
# slovo = input('vvedite slovo: ')
# print(text.count(slovo))

# text = input('vvedite text: ')

# text = text.split(' ')
# print(text)
# print(len(text))


#Метод replace(old, new [count]) меняет в строке old символ на new, заменит count раз если переведете число 
#text = ' ahahahha'
#res = text.replace('a','v',2 )
#print(f'{res}')


#strip() убирает пробельные символы в начале и в конце строки 
#rstrip, lstrip убирает только спарва и слева 

#a = '   hello   '
#print(a, len(a), sep = '->')
#res = a.strip()
#print(res, len(res), sep = '->')
#print(a.lstrip(), '1')


#isdigit isnumeric isdecimal проверяет состоит ли наша строка из чисел 
#num = input ('введите число')
#print(f 'введено ли число: {num.isdigit()'})

#isalpha состоит ли наша строка из символов 
#print(txt.isaplpha())
#res = txt.replace(' ', '')
#print(res, res.isalpha())


# num = input('введиет число')
# if num.isdigit():
#    num = int(num)
#    print(f'{num}* 5 = {num * 5 }')
# else: 
#    print ('вы ввели не число')

#split дробит на несколько частей по разделителю 
#все части сохранятются в типе данныx list 

# text = 'let me speak in english'
# res = text.split(' ')
# print(res)

# a = '#hello#life#love#bishkek'
# res = a[1:].split('#') 
# print(res)

#'connector'.join(list) соединяет по connector строки которые были в list 
#ls =  ['aruuke', 'bakyt','altynai']
#print( ls)
#res = '-'.join(ls)
#print(res)


#swapcase переводит символы в противоположный регистр 
#upper переводит все в верхний регистр 
#lower переводит в нижний регистр 

##text = 'HELLO WORLD MY NAME IS CINNOMOROLL'
#print(text.swapcase())
#print(text.upper())
#print(text.lower())

#index(value) выводит индекс значения value внутри строки 
#find(value) выводит индекс значения value внутри строки но если не нашел вернется -1
#text = 'hello my nme is cinnomoroll' 
#print(text.find('a'))

