# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options

# from selenium import webdriver

# options = webdriver.FirefoxOptions()

# # # Добавляем headless режим
# # options.add_argument("--headless")

# # Добавляем user-agent
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0'
# options.add_argument(f'user-agent={user_agent}')

# # Создаем драйвер с опциями
# driver = webdriver.Firefox(options=options)

# print("zapusheno")

# # while True:
# input("Нажмите Enter для закрытия браузера...")

#типо не работает прост
# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# import os

# options = Options()
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0'
# options.add_argument(f'user-agent={user_agent}')

# # Создаем профиль Firefox с пользовательскими настройками
# profile = webdriver.FirefoxProfile('C:\\Users\\You\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\something.default-release')

# # # Настраиваем прокси
# # PROXY_HOST = "12.12.12.123"
# # PROXY_PORT = "1234"
# # profile.set_preference("network.proxy.type", 1)
# # profile.set_preference("network.proxy.http", PROXY_HOST)
# # profile.set_preference("network.proxy.http_port", int(PROXY_PORT))

# # Устанавливаем navigator.webdriver в false
# profile.set_preference("dom.webdriver.enabled", False)
# profile.set_preference('useAutomationExtension', False)
# profile.update_preferences()

# desired = DesiredCapabilities.FIREFOX
# driver = webdriver.Firefox(firefox_profile=profile, desired_capabilities=desired)

#старый типо
# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# options = Options()
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0'
# options.add_argument(f'user-agent={user_agent}')

# # Создаем профиль Firefox с пользовательскими настройками
# profile = webdriver.FirefoxProfile()

# # Устанавливаем navigator.webdriver в false
# profile.set_preference("dom.webdriver.enabled", False)
# profile.set_preference('useAutomationExtension', False)
# profile.update_preferences()

# desired = DesiredCapabilities.FIREFOX
# driver = webdriver.Firefox(firefox_profile=profile, desired_capabilities=desired)

#тоже типо старый
# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# options = Options()
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0'
# options.add_argument(f'user-agent={user_agent}')

# # Создаем профиль Firefox с пользовательскими настройками
# profile = webdriver.FirefoxProfile()

# # Устанавливаем navigator.webdriver в false
# profile.set_preference("dom.webdriver.enabled", False)
# profile.set_preference('useAutomationExtension', False)
# profile.update_preferences()

# # Добавляем профиль в объект options
# options.profile = profile

# desired = DesiredCapabilities.FIREFOX
# driver = webdriver.Firefox(options=options, desired_capabilities=desired)

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0'
options.add_argument(f'user-agent={user_agent}')

# Создаем профиль Firefox с пользовательскими настройками
profile = webdriver.FirefoxProfile()

# Устанавливаем navigator.webdriver в false
profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference('useAutomationExtension', False)
profile.update_preferences()

# Добавляем профиль в объект options
options.profile = profile

driver = webdriver.Firefox(options=options)

