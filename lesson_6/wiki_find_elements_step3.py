import time
from fileinput import close

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
wiki_icon = driver.find_element("class name", "wikipedia-icon")
driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element("id","Wikipedia1_wikipedia-search-input").click()
driver.find_element("class name","wikipedia-search-button").click()
driver.find_elements("tag name","button")[3].click()

