# команда для входа 
# sude -u postgres qsql
# Анвар, [5/3/24 12:32]
# PostgreSQL - Система управления базами данных(СУБД/DBMS)
# Это ряд программ и инструментов позволяющих создавать БД, управлять ею и хранятся в виде таблиц, и таблицы имюет связи между собой

# SQL (Structured Query Language) - декларативный язык структурированных запросов, он применяется для создания и получения данных при помоши запросов в БД

##----------------##----------------##----------------##----------------##----------------

# команда для входа в бд через юзера postgres:
# sudo -u postgres psql

# команда для входа в своего юзера
# psql

# команда для выхода
# \q 
# exit

# создание суперюзера
# CREATE ROLE 'username' SUPERUSER LOGIN PASSWORD '1';

# изменение пароля
# ALTER USER 'username' WITH PASSWORD '1';

# создание БД
# CREATE DATABASE 'name';

# рекомендуют писать все команды sql большим регистром для удобства а все остальное маленькими по типу username



# \l - список всех БД

# \du - все юзеры

# \dt - все таблицы (нужно подключиться в БД заранее)

# \d 'name' - подробная информация про таблицу (нужно подключиться к бд заранее)

# \с 'name' - команда для подключения в бд

##-------------------------------##-------------------------------##-------------------------------##-------------------------------



# Типы полей в PostgreSQL
# Numeric Types(Числовые типы)
    # a. smallint(2 bytes) -> -32767 to 326767
    # b. integer(4 bytes) -> -2.147...to 2.147...
    # c. bigint(8 bytes) -> ...
    # d. real (4 bytes) -> число с плавающей точкой, вещественное
    # f. diuble precision (8 bytes) -> real но только с двойной точностью
    # e. serial(4 bytes) -> int, auto-increment

# Character types(Символьные типы(строковые)):
#     a. varchar(кол-во символов) -> если мы укажем 50 символов, а заполним только 10, то остальные будут свободныю Макс 255
#     b. char(кол-во символов)  ->  если укажем 50 символов, а заполним тоолько 10, то остальные будут заполнены пробелом. Макс 255
#     с. text() -> неограниченное количество символов



# Boolean types
    # a. boolean(1 bytes) - True/False
    
# date -> календарная дата (год.месяц.день)

# location -> координатная точка (x, y) - (245, -12)

# enumerate types:
#     ('a', 'b', 'c')
#     CREATE TYPE <any name> AS ENUM ('Happy', 'Sad', 'Mad')
##-----------------------##-----------------------##-----------------------##---------------------

# Ограничения:
#     1. NOT NULL -> обязательно к заполнению
#     2. UNIQUE -> то что будут харинться только уникальные данные
#     3. CHECK -> CHEK age -> -1 - ограничение проверки на условие
#     4. PRIMARY KEY -> для установки идентификатора данных в таблице
#     5. FOREIGN KEY -> для установки связей между таблицами
#     6. ON DELETE -> для установки поведения при удалении данных которые были связаны



##-----------------------##-----------------------##-----------------------##---------------------
# создание бд
# CREATE DATABASE 'name'; #recomended
# create database 'name';

# Команда для создания таблицы
# CREATE TABLE <tableName> (
#     <column> <type> [<constraint>]
#     <column> <type> [<constraint>]
# )

# CREATE TABLE films (
#     id serial,
#     code char(5), 
#     title varchar(100),
#     date date, 
#     genre varchar(50),
#     budget bigint, 
#     country varchar(50)
# );

##------------##------------##------------##------------##------------##------------

# DROP TABLE <name> - удаление таблицы

##------------##------------##------------##------------##------------##------------
# Команда для добавления данных в таблицу
# INSERT INTO <tableName> (column) VALUES (data), (data);

# INSERT INTO films (code, title, date, genre, budget, country) VALUES 
# ('AU56', 'Game test56', '2015-05-31', 'Fantasy', 100000, 'USA'),
# ('123', 'test123', '2001-06-12', 'Fantasy', 1200000, 'USA');


# Команда для обновления данных
# UPDATE <table> SET <column> = <new_value> WHERE <column> = <value>
# UPDATE films SET genre = 'Adventure'; WHERE code = 'het5';

# команда для удаления данных
# DELETE FROM <table> WHERE <column> = <value>;
##------------##------------##------------##------------##------------##------------

# Анвар, [5/3/24 12:32]
# ORDER BY: Позволяет нам сортировать выводящие данные по убыванию или возрастанию. ASC (по возрастанию) и DESC (по убыванию)
# Синтаксис: SELECT <row> FROM <tablename> ORDER BY <row> [ASC/DESC]
##------------##------------##------------##------------##------------##------------


# WHERE: ИСПОЛЬЗУЕТСЯ ДЛЯ ФИЛЬТРАЦИИ ПО ПОЛЯМ. будут выводиться только те данные которые соответствуют условию оператора WHERE
# Синтаксис: SELECT <row> FROM <tableName> WHERE <row> = 'чему либо';
##------------##------------##------------##------------##------------##------------

# BETWEEN: условие между
# SELECT * FROM films WHERE id BETWEEN 3 and 1

##------------##------------##------------##------------##------------##------------

# LIKE: Выводит результат который соответствует введенному шаблону дл строк, Чувствителен к регистру
# ILIKE: тоже самое только не зависит от регистра
# Синтаксис: SELECT <row> FROM <tableName> WHERE <row> LIKE/ILIKE 'чему либо';



##------------##------------##------------##------------##------------##------------
##------------##------------##------------##------------##------------##------------


# Экспорт бд(дамп):
# pg_dump -U <username> -d 'dbname' > 'file.sql'

# импорт:
# psql -U <username> -d 'dbname' -f <filename>


##---------------##---------------##---------------##---------------##---------------##---------------
                                    # Группировка

# SELECT count(product_name), c.category_name FROM products as p, categories as c WHERE p.category_id = c.category_id GROUP BY c.category_name;





# JOIN: выборка данных из двух таблицб соединение таблиц, соединение таблиц

# LEFT JOIN: выборка будет содержать все строки из левой таблицы

# RIGHT JOIN: выборка будет содержать все таблицы из правой таблицы

# SELECT p1.title, p1.price, o1.quality, p1.price * o1.quality as total_sum FROM product p1, orders o1 WHEREp1.id = o1.product_id; - Запрос сразу после в де таблицы

# SELECT p1.title, p1.price, o1.quality, p1.price * o1.quality as total_sum FROM product p1 JOIN orders ON p1.id = o1.product_id;









