from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-javascript")

def get_html_selenium(url):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    time.sleep(7)
    
    html = driver.page_source
    driver.quit() 
    return html


url = "https://www.wildberries.ru/catalog/elektronika/noutbuki-pereferiya/noutbuki-ultrabuki"
html_content = get_html_selenium(url)

from bs4 import BeautifulSoup
import requests
import csv
import pprint 


def parsing_data(url): 
    
    soup = BeautifulSoup(html_content,'html.parser')
    container = soup.find('div',class_='product-card-list')
    berries = container.find_all('div', class_= 'product-card__wrapper')
    result = []

    for i in berries: 
        title = i.find('h2',class_= 'product-card__brand-wrap').text
        price = i.find('p',class_= 'product-card__price price').text
        try:
            img = i.find('img',class_ ='j-thumbnail').get('src')
        except Exception as e: 
            img = f'Image not found {e}'
        data = {'title':title,
                'price':price,
                'img':img}
        
        result.append(data)

    return result 

def prepare_csv():
    with open('wildberries2.csv','w') as file:
        fields = ['№','title','price','picture']
        writer = csv.DictWriter(file,fields)
        writer.writerow({
            '№':'№',
            'title':'title',
            'price':'price',
            'picture':'picture'
        })
count=1
def write_to_csv(data:list):
    with open('wildberries2.csv','a') as file:
        global count 
        fields = ['№','title','price','picture']
        writer = csv.DictWriter(file,fields)
        for i in data: 
            writer.writerow({
                '№': count,
                'title': i['title'],
                'price':i['price'],
                'picture':i['img'],
                })
            count+=1


data = parsing_data(url)
prepare_csv()

write_to_csv(data)



