a = int(input('Введите трехзначное число:'))
a1 = a // 100
a2 = (a%100)//10
a3 = a % 10 
sum = a1 + a2 + a3
prod = a1 * a2 * a3
print('Сумма цифр:', sum,'Произведение цифр:', prod)
    

