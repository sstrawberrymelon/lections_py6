# list comprehencions - генераторы списков 
# list comprehensions - упрощенный подхот к созданию списков, котрый задействует в 
# себе цикл for, а также конструкцию if для определения того, ч
# то в итоге попадает в наш список

# list -> 0 - 200 -> четные

# ls = []
# for i in range(0, 201):
#     if i % 2 ==0:
#         ls.append(i)
# print(ls)
# ls = []
# ls = list(range(0, 201, 2))
# print(ls)

# ls = [x for x in range(0, 201, 2)]
# ls = [x for x in range(0, 201) if x % 2 == 0]
# print(ls)

# list: 0 - 300, dealyatsa na 3 i na 2 bez ostatka

# ls = []
# for x in range(0, 301):
#     if x % 2 == 0 and x % 3 == 0:
#         ls.append(x)
# print(ls)


# ls = [x for x in range(0, 301) if x % 2 == 0 and x % 3 == 0] # самый первый x с ним атоматически есть .append
# print(ls)

# list: 0 - 100 -> x % 2 == 0: x  2, x % 3 == 0: x  3

# ls = []
# for x in range(0, 101):
#     if x % 2 == 0:
#         ls.append(x  2)
#     elif x % 3 == 0:
#         ls.append(x  3)
# print(ls)




# ls = [x   2 if x  2 == 0 else x ** 3
#     for x in range(0, 101) if x % 2 == 0 or x % 3 == 0
# ]
# print(ls)

# ------------------------------------------------------------------

# newlist = [expression for item in iterable <if condition == True>]

# ls = [str(i * 2) for i in range(0, 11)]
# print(ls)

# ls = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# res = []
# for x in ls:
#     for num in x:
#         res.append(num)
# print(res)


# ls = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# res = [num for x in ls for num in x]
# print(res)

# -----------------------------------------------------------

# from datetime import datetime

# start = datetime.now()
# ls = []
# for x in range(0, 100_000_000):
#     ls.append(x)
# finish = datetime.now()
# print(finish - start)



# start = datetime.now()
# ls = [x for x in range(0, 100_000_000)]
# finish = datetime.now()
# print(finish - start)