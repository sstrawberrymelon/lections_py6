from bs4 import BeautifulSoup 
import requests
import csv
import pprint 





def parsing_data(url): 
    response = requests.get(url) #используется библиотека requests для того чтоб получать данные из определенной ссылки 
    soup = BeautifulSoup(response.text, 'html.parser') #библиотека beautifulSoup использует данные HTML из сайта 
    # print(soup)
    container = soup.find('div', class_='table-view-list') 
    cars = container.find_all('div', class_='list-item') # ищем названия машин по определенном у тегу 
    result = [] 

    for car in cars: #цикл для получения названия картинки цены описания 
        name = car.find('h2', class_ = 'name').text.strip() #text выведит только текст без тега
        try: 
            img = car.find('img', class_ = 'lazy-image-attr').get('src') #получить только ссылку на картинку, обращаемся по тегу img 'scc'
        except Exception as e: 
            img = f'No Image {e}!'
        price = car.find('div',class_='block price').find('strong').text
        desc = ''.join(car.find('div',class_ = 'item-info-wrapper').text.spl.textit())
        data = {'title': name, 'desc': desc, 'price': price, 'img': img} #все это получаем в виде списка 
        result.append(data) #возвращаем в результат 

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
                 
url = f'https://www.mashina.kg/search/all/'  #ссылка на сайт 
last_page = get_last_page(url) 
print('Последняя страница:',last_page)
prepare_csv()
count=1
i = 1 

while i<= last_page: #цикл для парсинга всех страниц (если нужно остановить написть в терминал ctrl+c)
    page_url = f'https://www.mashina.kg/search/all/?page={i}'
    data = parsing_data(page_url)
    write_to_csv(data)
    print(f'Спарсили {i}/{last_page} страничку!')
    i += 1


#SELENIUM ДЛЯ ПАРСИНГА 


# while i<= last_page:
#     page_url = f'https://www.mashina.kg/search/all/?page={i}'
#     i += 1




data = parsing_data(url)
write_to_csv(data) 




        # print(img)
        # print()
        # print(name)
        # print()
        # print(price)
        # print()
        # print(desc)


    # print(response.text)
    # print(len(response.text))
#     print(response, type(response))
#     print()
#     print(dir(response))

# print(parsing_data(url))


