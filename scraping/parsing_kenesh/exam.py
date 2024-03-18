# from bs4 import BeautifulSoup 
# import requests
# import csv
# import pprint





# def parsing_data(url): 
#     response = requests.get(url) 
#     soup = BeautifulSoup(response.text, 'html.parser') 
#     container = soup.find('div', class_='product-index product-index oh') 
#     news = container.find_all('div', class_='item product_listbox oh') 
#     result = [] 

#     for t in news: 
#         name = t.find('div', class_ = 'listbox_title oh').text.strip() 
#         img = t.find('img').get('src')
#         price = t.find('div',class_='listbox_price text-center').find('strong').text
#         data = {'title': name, 'price': price, 'img': img} 
#         result.append(data) 

#     return result 

# def get_last_page(url): 
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser') 
#     pages = soup.find('li',class_='last').text
#     return int(pages)



    
     

# def prepare_csv(): 
#     with open('cars.csv','w') as file:  
#         fieldnames = ['№','name','desc','price','img'] 
#         writer = csv.DictWriter(file, fieldnames)
#         writer.writerow({  
#             '№':'№',
#             'name': 'Name:',
#             'price': 'Price:',
#             'img': 'Image Url:'

#         })

# count=1
# def write_to_csv(data: list): 
#         with open('cars.csv','a') as file: 
#             global count 
#             fieldnames = ['№','name','price','img']
#             writer = csv.DictWriter(file, fieldnames)  
#             for t in data:
#                 writer.writerow({
#                 '№':count,
#                 'name': t['title'],
#                 'price': t['price'],
#                 'img': t['img'],

#                 })
#                 count += 1
                 
# url = f'https://www.kivano.kg/mobilnye-telefony'  
# last_page = get_last_page(url) 
# print('Последняя страница:',last_page)
# prepare_csv()
# i = 1 

# while i <= last_page: 
#     page_url = f'https://www.kivano.kg/mobilnye-telefony?page={i}'
#     data = parsing_data(page_url)
#     write_to_csv(data)
#     print(f'Спарсили {i}/{last_page} страничку!')
#     i += 1


# data = parsing_data(url)
# write_to_csv(data) 

# __________________________________________________________________________________________

# from bs4 import BeautifulSoup 
# import requests
# import csv
# import pprint





# def parsing_data(url): 
#     response = requests.get(url) 
#     soup = BeautifulSoup(response.text, 'html.parser') 
#     container = soup.find('div', class_='result-block col-sm-8 js__listing') 
#     cars = container.find_all('div', class_='a-card a-card--pay-yellow js__a-card') 
#     result = [] 

#     for auto in cars: 
#         name = auto.find('div', class_ = 'a-card__link').text.strip() 
#         img = auto.find('img').get('src')
#         price = auto.find('div',class_='a-card__price').text
#         desc = auto.find('div',class_='a-card__main').text
#         data = {'title': name, 'price': price, 'img': img,'desc': desc} 
#         result.append(data) 

#     return result 



    
     

# def prepare_csv(): 
#     with open('deputy.csv','w') as file:  
#         fieldnames = ['№','name','desc','price','img'] 
#         writer = csv.DictWriter(file, fieldnames)
#         writer.writerow({  
#             '№':'№',
#             'name': 'Name:',
#             'price': 'Price:',
#             'img': 'Image Url:',
#             'desc':'Desc'

#         })
# prepare_csv()


# count=1
# def write_to_csv(data: list): 
#         with open('deputy.csv','a') as file: 
#             global count 
#             fieldnames = ['№','name','price','img','desc']
#             writer = csv.DictWriter(file, fieldnames)  
#             for auto in data:
#                 writer.writerow({
#                 '№':count,
#                 'name': auto['title'],
#                 'price': auto['price'],
#                 'img': auto['img'],
#                 'desc': auto['desc']

#                 })
#                 count += 1
                 
# url = f'https://kolesa.kz/cars/'  

# i = 1 

# while i <= 999: 
#     page_url = f'https://kolesa.kz/cars/?page={i}'
#     data = parsing_data(page_url)
#     write_to_csv(data)
#     print(f'Спарсили {i}/{1000} страничку!')
#     i += 1


# data = parsing_data(url)
# write_to_csv(data) 
# _______________________________________________________________________________________


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
import time
import pprint
import lxml

chromedriver_path = '/usr/bin/chromedriver'  # Замените на ваш путь к chromedriver
service = Service(executable_path=chromedriver_path)

# Настройки для WebDriver
options = webdriver.ChromeOptions()
options.headless = False # Установите True, если не нужно открывать окно браузера

# Переход на страницу
url = 'https://kaktus.media/?lable=8&date=2024-02-15&order=time'
def get_html_selenium(url):
    browser = webdriver.Chrome(service=service, options=options)
    browser.get(url)

    # Явные ожидания для загрузки элементов
    # WebDriverWait(browser, 30).until(
    #     EC.presence_of_all_elements_located((By.CLASS_NAME, 'card__link'))
    #     and EC.presence_of_all_elements_located((By.CLASS_NAME, 'main-img'))
    #     and EC.presence_of_all_elements_located((By.CLASS_NAME, 'price__lower'))
    #     and EC.presence_of_all_elements_located((By.CLASS_NAME, 'price__discount'))
    #     and EC.presence_of_all_elements_located((By.CLASS_NAME, 'b-card__name'))
    #     and EC.presence_of_all_elements_located((By.CLASS_NAME, 'b-card__reviews'))
    #     and EC.presence_of_all_elements_located((By.CLASS_NAME, 'b-card__rating'))
    # )
    time.sleep(2)
    # Получить HTML-код после выполнения JavaScript
    html = browser.page_source

    # Закрыть браузер
    browser.quit()

    return html

def parsing_data():
    html=get_html_selenium(url)
    soup = BeautifulSoup(html, 'lxml')
    
    container = soup.find('div', class_ = 'Tag--articles')
    news = container.find_all('div', class_ = 'Tag--article')
    result = []
    count = 0
    for i in news:
        count += 1
        name = i.find('a', class_ = 'ArticleItem--name').text.strip()
        img = i.find('img').get('src')
        link = i.find('a').get('href')
        desc = parsing_desc(link)
        data = {'count': count, 'name': name, 'img': img, 'link': link, 'desc': desc}
        result.append(data)
        if count == 30: #кол-во новостей (сильно нагружает)
            break
    if result == []:
        result.append({'count': 'Пока новостей нет', 'name': '.', 'img': 'https://risovach.ru/upload/2021/06/mem/da-kto-takoy_273422635_orig_.jpg', 'link': '.', 'desc': '.'})
        result.append({'count': 'Пока новостей нет', 'name': '.', 'img': 'https://risovach.ru/upload/2021/06/mem/da-kto-takoy_273422635_orig_.jpg', 'link': '.', 'desc': '.'})
        result.append({'count': 'Пока новостей нет', 'name': '.', 'img': 'https://risovach.ru/upload/2021/06/mem/da-kto-takoy_273422635_orig_.jpg', 'link': '.', 'desc': '.'})
        return 
    print(result)
    return result
def parsing_desc(url):
    html=get_html_selenium(url)
    soup = BeautifulSoup(html, 'lxml')
    desc = soup.find('div', class_ = 'BbCode').find_all('p')
    desc_text = []
    for i in desc:
        desc_text.append(i.text)
    desc_text = ''.join(desc_text)
    return desc_text


print('Парсируем там что то короче')
a = parsing_data()






import telebot
from telebot import types

token='6567901938:AAFLssCqrZKwBFMNSMwe8HlpjM9p5K_jQsc'
bot=telebot.TeleBot(token)
print('\nУра наконецто\n')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Здравствуй!\nВведите "/news"')
    

@bot.message_handler(commands=['news'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in a:
        bot.send_photo(message.chat.id, i['img'], caption=f"№{i['count']} {i['name']}")
    bot.send_message(message.chat.id,'Введите номер',reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    try:
        for x in a:
            if message.text == str(x['count']):
                global id
                id = x
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                desc_b=types.KeyboardButton("Description")
                photo_b=types.KeyboardButton("Photo")
                quit_b = types.KeyboardButton("Quit")
                markup.add(desc_b)
                markup.add(photo_b)
                markup.add(quit_b)
                bot.send_message(message.chat.id,'Вы выбрали:')
                bot.send_photo(message.chat.id, id['img'], caption=f"№{id['count']} {id['name']}")
                bot.send_message(message.chat.id,'Deistvie', reply_markup=markup)
                bot.send_message(message.chat.id,'после получения результата, ты можешь продолжить поиск по номерам')
                break
    except TypeError:
        bot.send_photo(message.chat.id, 'https://risovach.ru/upload/2021/06/mem/da-kto-takoy_273422635_orig_.jpg', caption="Новостей пока нет )':")
    if message.text=="Description":
        try:
            bot.send_message(message.chat.id,id['desc'])
        except telebot.apihelper.ApiTelegramException:
            i = 0
            while i < len(id['desc']):
                bot.send_message(message.chat.id,f"{id['desc'][i:i+1000:]}")
                i += 1000

        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)

    elif message.text == 'Photo':
        bot.send_photo(message.chat.id, id['img'], caption=f"№{id['count']} Источник:{id['link']}")

    elif message.text == 'Quit':
        bot.send_message(message.chat.id,"':")
        bot.stop_bot()
        print('STOP_BOT!')

    elif message.text.lower() == 'test':
        bot.send_message(message.chat.id,"""OK\n\n/start    /kaktus""")


bot.polling()





Class Communalka: 
    def