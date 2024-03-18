# Задания по командной строке linux

# 1) Какая комбинация клавиш используется для открытия терминала в Linux?
# ctrl + alt + t 
# 2) Перейдите в свою домашнюю директорию
# cd ~, cd/home/user, cd
# 3) Создайте папку под названием codify
# cd Desktop
# mkdir codify 
# ls
# 4) Создайте внутри папки codify 3 папки c названиями: week1, week2, week3
# mkdir week1
# mkdir week2
# mkdir week3
# ls 
# cd week1 
# 5) Перейдите в папку week1 и создайте файл test.txt (одной командой)
# touch test.txt
# 6) Напишите внутри файла test.txt предложение Hello world!
# nano test.txt 
# Hello world!
# 7) Выведите содержимое файла test.txt на стандартное устройство вывода.
# cat test.txt
# 8 Перейдите в домашнюю папку.
# cd 
# 9) Перейдите в папку week1 находясь в домашней папке.
# cd codify/week1 
# 10) Создайте внутри папки week1 три файла под названием test1.txt, test2.txt, test3.txt
# touch test1.txt,test2.txt,test3.txt 
# 11) Скопируйте содержимое файла test.txt и скопируйте в файл под названием test1.txt
# cp test.txt test1.txt
# 12) Удалите файл test1.txt
# rm test1.txt 
# 13) Переместите файл test.txt в папку week2
# mv week1/test.txt week2
# 14) Удалите папку week1 с содержимым
# cd ..
# rm -rf week1  
# 15) Перейдите в домашнюю папку по абсолютному пути (не используя ~)
# cd
# cd home/user 
# 16) Введите команду, чтобы узнать путь до текущей директории
# pwd 