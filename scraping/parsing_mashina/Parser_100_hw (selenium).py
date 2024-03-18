# Parser 100 баллов дз

# Необходимые инструменты:
# 1)bs4
# 2)requests
# 3)csv
# 4)lxml
# 5)selenium webdriver

# Техническое задание

# Необходимо вытянуть данные с сайта
# url = 'https://global.wildberries.ru/catalog?category=9492';
# Парсинг сайтов – это новый метод ввода данных, который не требует повторного
# ввода или копипастинга. Такого рода программное обеспечение ищет информацию под
# контролем пользователя или автоматически, выбирая новые или обновленные данные
# и сохраняя их в таком виде, чтобы у пользователя был к ним быстрый доступ.
# Что нужно сделать?
# 1) Спарсить наименование товара;
# 2) Спарсить цену товара;
# 4) Спарсить линк картинки этого товара

# Полезные ссылки:

# 1) https://google.com/
# 2) https://youtube.com/
# 3) https://leftjoin.ru/all/parsim-dannye-kataloga-sayta-ispolzuya-beautiful-soup-i-selenium/
# 4) https://www.dataquest.io/blog/web-scraping-tutorial-python/
# 5) https://devman.org/encyclopedia/modules/bs4-tutorial/
# 6) https://www.crummy.com/software/BeautifulSoup/bs4/doc.ru/bs4ru.html
# 7) https://www.youtube.com/watch?v=ykjBVT57r68
# 8) https://www.youtube.com/watch?v=3hgkiDAaSQs
# 9) https://habr.com/ru/companies/selectel/articles/754674/





# browser = wd.Chrome("/usr/bin/chromedriver/") 
# import requests
# import csv
# from bs4 import BeautifulSoup
# url = 'https://global.wildberries.ru/catalog?category=9492'

# open_search = browser.find_element_by_class_name('header search')
# open_search.click()
# search = browser.find_element_by_class_name('search modal input')
# search.send_keys('Ноутбуки')


from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.support.ui import WebDriverWait #импортируем класс для работы с ожиданиями 
import time 
import csv




chrome_path = "/usr/bin/chromedriver" #путь к нашемк браузеру хрому 

service = Service(executable_path=chrome_path) #к какому серверу подключится или чрезе какой ему открыть 
url = 'https://global.wildberries.ru/catalog?category=9492' #ссылка на страницу которую нужно запарсить 
options =  webdriver.ChromeOptions()
options.headless = False 
browser = webdriver.Chrome(service=service,options=options)
browser.get(url) 
wait = WebDriverWait(browser, 10) #создать объект webdriverwait, 10 сек это время ожидания 



time.sleep(5) #задержка 5 сек 

product_names = browser.find_elements(By.CLASS_NAME, 'card__link')
result = []

for i in product_names:
    title = i.find_element(By.CLASS_NAME,'b-card__info-row').text
    price = i.find_element(By.CLASS_NAME,'price__lower').text
    picture = i.find_element(By.CLASS_NAME,"main-img").get_attribute('src')
    print(f"Название: {title}")
    print(f"Цена: {price}")
    print(f"Ссылка на картинку: {picture}")
    result.append({
        "title": title,
        "price": price,
        "picture": picture,
    })
# for i in result: #цикл для того чтоб он список вывел каждую с новой строки 
#     print(i)

def prepare_csv(): #функция для выведения в виде таблицы csv на ubuntu нет excel 
    with open('wildberries.csv','w') as file: #w в режиме записи редактирования 
        fieldnames = ['№','title','price','picture'] #ячейки для талицы 
        writer = csv.DictWriter(file, fieldnames) #нашу переменную file добавляет в столбцы fieldnames
        writer.writerow({  
            '№':'№',
            'title': 'Name:',
            'price': 'Price:',
            'picture': 'picture:'

        })
prepare_csv()

count = 1
def write_to_csv(result: list): # фукнция чтоб добавить это все в таблицу csv 
    with open('wildberries.csv','a') as file: #a в режиме добавления 
        global count 
        fieldnames = ['№','title','price','picture']
        writer = csv.DictWriter(file, fieldnames)  
        for note in result:
                writer.writerow({
            '№':count,
            'title': note['title'],
            'price': note['price'],
            'picture': note['picture'],

                })
                count += 1

write_to_csv(result)




browser.quit()









# html_code = driver.page_source
# soup = BeautifulSoup(html_code,'lmxl')


# product_names = soup.find_all('div',class_='product-card__name').text

# product_prices = soup.find_all('span', class_='price-block__final-price').text

# product_images = soup.find_all('img', class_='product-card__image').text


# for name, price, image in zip(product_names, product_prices, product_images):
#     print(f"Наименование: {name.text}")
#     print(f"Цена: {price.text}")
#     print(f"Ссылка картинки: {image['src']}")
#     print()





