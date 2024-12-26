import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://demoqa.com/automation-practice-form")
firstNameInput = driver.find_element("xpath", "(//input[@id='firstName'])")
firstNameInput.clear()
time.sleep(1)
firstNameInput.send_keys("Test")
time.sleep(5)
assert firstNameInput.get_attribute("value") == "Test" , f"{firstNameInput.get_attribute("value")} не является Test."
time.sleep(5)
