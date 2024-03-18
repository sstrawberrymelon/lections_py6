#Операторы сравнения 
#Условные операторы
#Логические операторы 

# операторы сравнения <, >, ==(equal), !=(not equal), >=,<=
# 1>5 --> False 
# 7<9 --> True 
# print('ABC' > 'abc123')

# 1 2 4 8 16 32 64 128 256 512 1024 2048
#  1  0  1
# 44 --> 101100 
#джордж бул 
#ascii code 
# print(ord(a))
# num = 1100
# print(chr(num))


#Условные операторы 
#if 
#elif 
#else 


# string  = input('Enter something:').lower()
# if string == 'hello': 
#     print('hello, where is slash')
# elif string == 'john':
#     print('welcome back John snow, the king of North')
# else: 
#     print('no match found!')
    

# print('Regisration Form;:')
# email = input('Vvedite email:')
# if '@' not in email: 
#     raise ValueError('email is invailid!')

# password1 = input('Vvedite password:')

# if len(password1) < 8:
#     raise ValueError('Too short! At least 8 symbols!')
# elif password1.isdigit():
#     raise ValueError('Inavalid password')
# elif passwod1.idalpha():
#     raise ValueError



# password2 = input('Vvedite password:')

# if password != password1:
#     raise ValueError('Password did not match!')

# index = email.find('@')

# print(f'Successfully registered! Hello Mr/Mrs {emeil[:index]}!')


# age = input('enter your age:')
# if age.isdigit():
#     age = int(age)

# else:
#     raise ValueError('Invalid value for age!')


# if age< 18:
#     print('Access Denied! Come again after {18-age} year!')
# else: 
#     print('You can buy it!')
 

#логические операторы 
#and or not 
# money = 1_000_002 
# status = 'premium'

# if money > 1_000_000 and status == 'premium':
#     print('welcome our president!')
# elif money > 1_000_000 or status == ' premium': 
#     print('You are minister of our club!')
# else: 
#     print('You are horable member of our club!')
