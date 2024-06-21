from selenium import webdriver

# Укажите путь к драйверу Chrome
driver_path = "C:/Users/slava/Desktop/list_of_prices/geckodriver.exe"

# Инициализируйте веб-драйвер
driver = webdriver.Firefox() 

url = 'https://soundcloud.com/koffeika_let/likes'  # Замените на нужный URL
driver.get(url)

def scroll_to_end():
    # Прокрутите страницу вниз до конца
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Прокручивайте страницу, пока не достигнете конца
while True:
    prev_height = driver.execute_script("return document.body.scrollHeight")
    scroll_to_end()
    time.sleep(2)  # Пауза между прокрутками

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == prev_height:
        break  # Достигли конца страницы


driver.quit()

# from bs4 import BeautifulSoup

# # Получите HTML-код страницы
# page_source = driver.page_source

# # Создайте объект BeautifulSoup
# soup = BeautifulSoup(page_source, 'html.parser')

# # Извлеките данные, которые вас интересуют
# # Например:
# # data = soup.find_all('div', class_='your-data-class')




