# PostgresSQL - Система управления базами данных(СУБД/DBMS)
# Это ряд программ и инструментов, позволяющих создавать БД, управлять ею и манипулировать данными внутри.

# Postgres - сама база данных, она обязательна реляционная, то есть данные хранятся в виде таблиц и таблицы имеют связи между собой.

# SQL (Structured Query language) - деклартивный язык структурированных запросов, он применяется для создания и получения данных при помощи запросов в БД.

# --------------------------------------------------------
# Команда для входа в бд через юзера postgres:
# sudo -u postgres psql

# Команда для входа в своего юзера
# psql

# создание суперюзера 
# CREATE ROLE 'username' SUPERUSER LOGIN PASSSWORD '1';
# # CREATE USER 'username' SUPERUSER LOGIN PASSWORD '1'; #create user

# изменение пароля 
# ALTER USER 'username' WITH PASSWORD '1';

# создание бд
# CREATE DATABASE 'name';

# DROP USER 'username'; # delete user
# CREATE USER 'username' SUPERUSER LOGIN PASSWORD '1'; #create user

# ---------------------------------
# diana=# \l #List of databases
# diana=# \du #List of roles
# ; - НЕ ЗАБЫВАЙ!!! Это конец команды 

# diana@MacBook-Pro-Diana DB % sudo -u postgres psql
# diana@MacBook-Pro-Diana DB % psql postgres # -> postgres=#
# postgres=# \q
# diana@MacBook-Pro-Diana DB % psql # -> diana=#
# diana=# \q
# diana@MacBook-Pro-Diana Desktop % psql -U diana -d northwind_db -f northwind.sql
# diana=# \c northwind_db #-> You are now connected to database "northwind_db" as user "diana".
# northwind_db=# SELECT * FROM us_states;
# ---------------------------------

# \du - все юзеры
# \c 'name' - команда для подключения к бд
# \dt - все таблицы (нужно подключиться к бд заранее)
# \d - 'name' - подробна информация про таблицу(нужно подключиться к бд заранее)
# psql -U <username> -d <dbname> - подключаемся под выбранным username к dbname
# \f - file xxx.sql

# -----------------------------------------
# Типы полей в Postgres

# Numeric Types(числовые типы)
    # a. smallint(2 bytes) -> -32767 to 32767
    # b. integer(4 bytes) -> -2.147... to 2.147...
    # c. bigint(8 bytes) -> ...
    # d. real (4bytes) -> число с плавающей точкой, вещественное
    # f. serial (4bytes) -> integer, auto-increment

# Character types(Символьные типы(строковые)):
    # a. varchar(кол -во символов) -> если мы укаже 50 символов, а заполим тольок 10, остальные будут свободны. Макс 255
    # b. char(кол -во символов) -> если мы укаже 50 символов, а заполим тольок 10, остальные будут заполнены пробелами. Макс 255
    # c. text() -> неогр кол - во символов

# Boolean Type
    # a. boolean(1 bytes) -> True/False

# date -> календарная дата(год.месяц.день)
# location -> координатная точка (x, y) - (245, -12)

# Enumerate types:
    # ('a', 'b', 'c')
    # CREATE TYPE <any name> AS ENUM('Happy', 'Sad', 'Mad');

# ---------------------------------------------

# Команда для добавления данных в таблицу 
# INSERT INTO <tablename> [(columns)] VALUES (data), (data);

# Команда для обновления данных 
# UPDATE <tablename> SET <column> = <new_value> WHERE <column> = <value>;

# Команда для удаления данных 
# DELETE FROM <table> WHERE <column> = <value>; 



# Команда для получения данных
# SELECT (columns) * FROM <table>; # все колоны высвечивает
# SELECT column_name, column_name FROM <table>; # только те колоны, которые нужны

# ORDER BY: Позволяет нам сортировать выводящие данные по убыванию или возрастанию. ASC(по возрастанию) и DESC(по убыв) 
# Синтаксис: SELECT <row> FROM <tablename> ORDER BY <row> [ASC/DESC]

# WHERE: используется для фильтрации по полям. будут выводится только те данные которые соответсвуют условию оператора WHERE

# Синтаксис: SELECT <row> FROW <tablename> WHERE <row> = 'чему либо';

# BETWEEN: условие между 
# SELECT * FROM products WHERE id BETWEEN 3 and 8 

# AND оператор и, для множественных условий 
# IN: WHERE <row> in (1,2,3,4);
# LIMIT: ставит ограничение в кол-во получаемых данных 


# LIKE: Выводит результат который соответсвует введенному шаблону для строк. Чувствителен к регистру 
# ILIKE: тоже самое только не зависит от регистра 
# Синтаксис: SELECT <row> FROM <tablename> WHERE <row> LIKE/ILIKE 'чему либо';

# GROUP BY: разделяет данные которые мы получаем в SELECT, при этом группируя их по определенному признаку.
# И теперь для каждой группы можно использовать функцию
# HAVING: ставит условие при помощи которого данные отбираются в группировке 
# # ____в тондеме(работают вместе в group by)
# Агрегатные функции: AVG COUNT SUM MAX MIN 

# Экспорт бд(дамп):
# pg_dump -U <username> -d 'dbname' > 'file.sql'

# Испорт:
# psql -U<username> -d 'dbname' > <filename>

# Ограничения:
# 1. NOT NULL - обязательно к заполнению
# 2. UNIQUE -будут хранится только уникальные данные
# 3. CHECK -> CHECK age > -1 - ограничение проверки на условие
# 4.PRIMARY KEY(для установки идентификатора данных в таблице)
# 5. FOREIGHN KEY(для установки связей между таблицами )
# 6. ON DELETE - для установки поведения при удалении данных которые были связаны 

# ________________________________________________
# jOIN: выборка данных из двух таблиц, соединение таблиц

# LEFT JOIN: выюорка будет сожержать все строки из левой таюлицы 

# RIGHT JOIN: выюорка будет сожержатьб все строки из первой таблицы

# SELECT p1.title, p1.price, o1.quantity, p1.price * o1. quantity as total_sum FROM products p1, orders o1 WHERE p1.id = o1.product_id 

# - Запрос сразу в две таблицы 

# SELECT p1.title, p1.price, o1.quantity, p1.price * o1.quantity as total_sum FROM products p1 JOIN orders o1 ON p1.id - o1.product_id;



