from selenium import webdriver
import time 
import csv

chrome_options =webdriver.ChromeOptions()
chrome_options.add_argument('--disable-javascript')

def get_html_selennium(url):
    driver = webdriver.Chrome(options = chrome_options)
    driver.get(url)

    time.sleep(3)
    html = driver.page_source
    return html 

url = 'https://global.oliveyoung.com/display/page/best-seller?target=pillsTab1Nav1'
html_content = get_html_selennium(url)
from bs4 import BeautifulSoup
import requests

def parsing_data(url): 
    soup = BeautifulSoup(html_content,'html.parser')
    container = soup.find('div',class_='tab-pane fade active in')
    cosmetics = container.find_all('ul', class_='unit-list best-seller-list')
    
    result = []

    for i in cosmetics: 
        print(i)
        name = i.find('dl', class_='brand-info').find('dt').text
        price = i.find('strong',class_='point').text
        desc = i.find('dl',class_='brand-info').find('dd').text
       
        img = i.find('img').get('src')
        
        data = {'name':name,'price':price,'desc':desc,'img':img}
        result.append(data)
    return result
    
def prepare_csv():
    with open('olive_young.csv','w') as file: 
        fields = ['№','name','price','desc','img']
        writer = csv.DictWriter(file, fields)
        writer.writerow({
            '№':'№',
            'name':'name',
            'price':'price',
            'desc':'desc',
            'img':'img',
        })
count = 1
def write_csv(data):
     with open('olive_young.csv','a') as file: 
        global count 
        fields = ['№','name','price','desc','img']
        writer = csv.DictWriter(file, fields)
        for  i in data:
            writer.writerow({
                '№':count,
                'name':i['name'],
                'price':i['price'],
                'desc':i['desc'],
                'img':i['img'],
        })
        count += 1

res = parsing_data(url)
print(res)



    











