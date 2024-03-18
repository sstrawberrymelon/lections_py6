# 1) Напишите функцию, которая принимает строку и 
# вычисляет количество букв верхнего и нижнего регистра.

# def countLet(text):
#     count_upper = 0 
#     count_lower = 0 
#     for let in text:
#         if let == let.upper():
#             count_upper += 1
#         elif let == let.lower():
#             count_lower += 1 
#     print(count_lower,'- колво букв нижнего регистра')
#     print(count_upper,'- колво букв вверхнего регистра')

#     count = 0 
#     for i in range(start,end+1):
#         count += i
#         if start > end: 
#             end == start 
#             start == end
#     print(count)

# sum_range((int(input('Введите начало:'))),(int(input('Введите начало:'))))

# countLet(input('Введите текст:'))
             
# ________________________________________________________________________________

# 2) Напишите функцию, которая принимает число n и генерирует словарь, 
# чьи ключи состоят из чисел от 1 до n, а их значения -- куб ключей. 
# Пример: передано число 5. В результате должны получить словарь {1: 1, 2: 8, 3: 27, 4: 64}

# def func(n): 
#     dict_ = {}
#     for i in range(1,n+1):
#         dict_[i] = i**3
#     return dict_ 
        
# print(func(int(input('Введите число:'))))
      

#______________________________________________________________________________________

# 3) Напишите функцию sum_range(start, end), которая суммирует все целые числа
#     от значения «start» до величины «end» включительно. Если пользователь задаст
#     первое число большее чем второе, просто поменяйте их местами.


# def sum_range(start,end): 
#     count = 0 
#     for i in range(start,end+1):
#         count += i
#         if start > end: 
#             end == start 
#             start == end
#     print(count)

# sum_range((int(input('Введите начало:'))),(int(input('Введите начало:'))))




