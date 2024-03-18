# JSON - JavaScript object Notation 
# единый язык для передачи данных между языыками 
# единый текстовый формат данных, был создан для хранения и передачи данных
# между сервисами, проектами 
# <filename>.json #file в формате json

# 
# Процесс сериализации и десериализации данных (конвертация), переделываем код из JS -> PY
# Сериализация - это перевод из PY в JSON

# dump - записывает данные в файл формат Jиз JSON
# dumpd - записывает данные в текст формата JSON

# Десериализация - это чтение данных из JSOM  -> Pyton 
# load - функция которая считывает даннфе из файла JSON 
# load - функция которая считывает даннфе из текста JSON
  
# _________________________________________________________________________________________
# процесс сериализация 

# import json 
# dict_ = {
#     'name': 'John Snow',
#     'age': 24,
#     'status': True,
#     'wife': False,
#     'children': None
# }

# print(dict_,type(dict_))

# json_text = json.dumps(dict_)
# print()
# print(json_text, type(json_text))



# import json 
# dict_ = {
#     'name': 'John Snow',
#     'age': 24,
#     'status': True,
#     'wife': False,
#     'children': None
# }

# print(dict_,type(dict_)) 
# with open('new.json','w') as file: 
#     json.dump(dict_,file,indent = 4)

# ______________________________________________________
# import json 
# процесс дессериализации 

# with open('new.json','r' ) as file: 
#     json_data = file.read()

# print(json_data, type(json_data))
# dict_ = json.loads(json_data)
# print()
# print(dict_, type(dict_))



# with open('new.json','r' ) as file: 
#     dict_ = json.load(file)
#     print(dict_, type(dict_))
    