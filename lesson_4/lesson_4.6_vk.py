import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("https://vk.com/")
PAGE_TITLE = driver.title
print(PAGE_TITLE)
driver.get("https://www.google.com/")
PAGE_TITLE = driver.title
print(PAGE_TITLE)
driver.back()
PAGE_TITLE = driver.title
print(PAGE_TITLE)
time.sleep(2)
assert PAGE_TITLE == "ВКонтакте | Добро пожаловать", "Неверный заголовок страницы"
driver.refresh()
PAGE_URL = driver.current_url
print(PAGE_URL)
driver.forward()
PAGE_URL = driver.current_url
assert PAGE_URL == "https://www.google.com/", "Неправильный URL"
