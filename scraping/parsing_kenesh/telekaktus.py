from bs4 import BeautifulSoup
import requests
import csv
import pprint
import telebot
from telebot import types

url = f'https://kaktus.media/?lable=8&date=2024-02-15&order=time'  


def parsing_data(url): 
    response = requests.get(url) 
    soup = BeautifulSoup(response.text, 'html.parser') 
    container = soup.find('div', class_='Tag--articles') 
    news = container.find_all('div', class_='ArticleItem--data ArticleItem--data--withImage') 
    result = []

    for t in news: 
        name = t.find('a', class_ = 'ArticleItem--name').text.strip() 
        img = t.find('a',class_= 'ArticleItem--image').find('img').get('src')
        time = t.find('div',class_='ArticleItem--time').text.strip()
        data = {'title': name, 'time': time, 'img': img} 
        result.append(data) 

    

def prepare_csv(): 
    with open('cars.csv','w') as file:  
        fieldnames = ['№','name','time','img'] 
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({  
            '№':'count',
            'name': 'Name:',
            'time': 'Time:',
            'img': 'Image Url:'

        })

count=1
prepare_csv()
def write_to_csv(data: list): 
        with open('cars.csv','a') as file: 
            global count 
            fieldnames = ['№','name','time','img']
            writer = csv.DictWriter(file, fieldnames)  
            for t in data:
                writer.writerow({
                '№':count,
                'name': t['title'],
                'time': t['time'],
                'img': t['img'],
                })
                count += 1
                 
url = f'https://kaktus.media/?lable=8&date=2024-02-15&order=time'   

a = parsing_data(url)
write_to_csv(a) 



token=''
bot=telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Здравствуй!\nВведите "/kaktus"')
    

@bot.message_handler(commands=['kaktus'])
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