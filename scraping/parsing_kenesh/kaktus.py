from bs4 import BeautifulSoup 
import requests
import csv
import pprint 





def parsing_data(url): 
    response = requests.get(url) #используется библиотека requests для того чтоб получать данные из определенной ссылки 
    soup = BeautifulSoup(response.text, 'html.parser') #библиотека beautifulSoup использует данные HTML из сайта 
    # print(soup)
    
    result = [] 
    
    container = soup.find('div', class_='Dashboard--group') 
    news = container.find_all('div', class_='Dashboard-Content-Card') 

    for a in news: #цикл для получения названия картинки цены описания 
        name = a.find('a', class_ = 'Dashboard-Content-Card--name').text.strip() 
        img = a.find('img', class_ = 'Dashboard-Content-Card--image-img lazyloaded').get('src') 
        data = {'title': name,'img': img} 
        result.append(data) 

    container2 = soup.find('div', class_='CompanyArticles--content') 
    news2 = container2.find_all('div', class_='CompanyArticles--article') 

    for a in news: #цикл для получения названия картинки цены описания 
        name = a.find('a', class_ = 'CompanyArticles--article-name').text.strip() 
        img = a.find('img', class_ = 'CompanyArticles--article-image-img lazyloaded').get('src') 
        data = {'title': name,'img': img} 
        result.append(data) 

    return result 











def get_last_page(url): #функ для получения последней страницы 
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser') 
    pages = soup.find_all('a',class_="page-link")[-1] 
    return int(pages.get('data-page')) #возвращает и показывет сколько страниц на сайте
    
     

def prepare_csv(): #функция для выведения в виде таблицы csv на ubuntu нет excel 
    with open('cars.csv','w') as file: #w в режиме записи 
        fieldnames = ['№','name','desc','price','img'] #ячейки для талицы 
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({  
            '№':'№',
            'name': 'Name:',
            'desc': 'Description:',
            'price': 'Price:',
            'img': 'Image Url:'

        })
def write_to_csv(data: list): # фукнция чтоб добавить это все в таблицу csv 
        with open('cars.csv','a') as file: #a в режиме добавления 
            global count 
            fieldnames = ['№','name','desc','price','img']
            writer = csv.DictWriter(file, fieldnames)  
            for car in data:
                writer.writerow({
                '№':count,
                'name': car['title'],
                'desc': car['desc'],
                'price': car['price'],
                'img': car['img'],

                 })
                count += 1
                 
url = f'https://kaktus.media/'  #ссылка на сайт 
# last_page = get_last_page(url) 
# print('Последняя страница:',last_page)
prepare_csv()
count=1
i = 1 

# while i<= last_page: #цикл для парсинга всех страниц (если нужно остановить написть в терминал ctrl+c)
#     page_url = f'https://www.mashina.kg/search/all/?page={i}'
#     data = parsing_data(page_url)
#     write_to_csv(data)
#     print(f'Спарсили {i}/{last_page} страничку!')
#     i += 1


#SELENIUM ДЛЯ ПАРСИНГА 


# while i<= last_page:
#     page_url = f'https://www.mashina.kg/search/all/?page={i}'
#     i += 1




data = parsing_data(url)
write_to_csv(data) 