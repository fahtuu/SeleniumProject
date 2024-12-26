import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://demoqa.com/automation-practice-form")
wait = WebDriverWait(driver, 10)
firstNameInput = driver.find_element("xpath", "(//input[@id='firstName'])")
firstNameInput.clear()
firstNameInput.send_keys("Test")
assert firstNameInput.get_attribute("value") == "Test" , f"{firstNameInput.get_attribute("value")} не является Test."

lastNameInput = driver.find_element("xpath", "(//input[@id='lastName'])")
lastNameInput.clear()
lastNameInput.send_keys("Testovich")
assert lastNameInput.get_attribute("value") == "Testovich" , f"{lastNameInput.get_attribute("value")} не является Testovich."

emailInput = driver.find_element("xpath", "(//input[@id='userEmail'])")
emailInput.clear()
emailInput.send_keys("test@mail.ru")
assert emailInput.get_attribute("value") == "test@mail.ru" , f"{emailInput.get_attribute("value")} не является Testovich."


