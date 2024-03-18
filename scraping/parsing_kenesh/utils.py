from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains 
from time import sleep


chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--disable-javascript")
service = Service('/usr/bin/chromedriver') #which chromedriver поиск в терминале путь до браузера 


def get_deps_html_selenium(url):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'card-title')))
    
    html = driver.page_source
    driver.quit() 
    return html 



def get_page_html_selenium(url):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    element = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'section-footer'))) #ждем пока наш элемент не высветится в браузере окна 
    
    i = 1
    res = {}
    while i <= 8:
        sleep(1.5)
        html = driver.page_source
        res[i] = html
        if i ==  8:
            break #закончить цикл и не нажимать на кнопку  после 8 стр 

        page_btn = driver.find_elements(By.CSS_SELECTOR,'.page-link')

        element = page_btn[-1]
        if page_btn:
            ActionChains(driver).move_to_element(element).perform() #скролит до кнопки 
            sleep(0.5)  
            element.click() #нажимает на кнопку 
        
        i+=1
    
    driver.quit() 
    return res

# res = get_page_html_selenium('https://kenesh.kg/ru/deputies')
# print(res)
