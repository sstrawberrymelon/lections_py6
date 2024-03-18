ls = [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,23]
left = 0  
right = len(ls) - 1 #получить крайнее число 
mid = len(ls) // 2 #получить середину
# print(len(ls))
# print(ls.index(right))
value = int(input('number:'))

i =0
while ls[mid] != value and left <= right: 
    if value < ls[mid]: 
        right = mid - 1 
    else: 
        left = mid + 1

    mid = (left + right) // 2
    i+=1

print(i)
if left > right: 
    print('not found')
else:
    print(f'{value} = {ls[mid]} id {mid}')






