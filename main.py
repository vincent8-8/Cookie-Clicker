from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

def check_store():
    money = int(driver.find_element(By.ID, "money").text.replace(",", ""))
    cursor_price = int(driver.find_element(By.CSS_SELECTOR, "#buyCursor b").text.split(" ")[-1].replace(",", ""))
    grandma_price = int(driver.find_element(By.CSS_SELECTOR, "#buyGrandma b").text.split(" ")[-1].replace(",", ""))
    factory_price = int(driver.find_element(By.CSS_SELECTOR, "#buyFactory b").text.split(" ")[-1].replace(",", ""))
    mine_price = int(driver.find_element(By.CSS_SELECTOR, "#buyMine b").text.split(" ")[-1].replace(",", ""))
    shipment_price = int(driver.find_element(By.CSS_SELECTOR, "#buyShipment b").text.split(" ")[-1].replace(",", ""))
    lab_price = int(driver.find_element(By.CSS_SELECTOR, "[id='buyAlchemy lab'] b").text.split(" ")[-1].replace(",", ""))
    portal_price = int(driver.find_element(By.CSS_SELECTOR, "#buyPortal b").text.split(" ")[-1].replace(",", ""))
    time_machine_price = int(driver.find_element(By.CSS_SELECTOR, "[id='buyTime machine'] b").text.split(" ")[-1].replace(",", ""))

    if money >= time_machine_price:
        purchase = driver.find_element(By.ID, "buyTime machine")
        purchase.click()
    elif money >= portal_price:
        purchase = driver.find_element(By.ID, "buyPortal")
        purchase.click()
    elif money >= lab_price:
        purchase = driver.find_element(By.ID, "buyAlchemy lab")
        purchase.click()
    elif money >= shipment_price:
        purchase = driver.find_element(By.ID, "buyShipment")
        purchase.click()
    elif money >= mine_price:
        purchase = driver.find_element(By.ID, "buyMine")
        purchase.click()
    elif money >= factory_price:
        purchase = driver.find_element(By.ID, "buyFactory")
        purchase.click()
    elif money >= grandma_price:
        purchase = driver.find_element(By.ID, "buyGrandma")
        purchase.click()
    elif money >= cursor_price:
        purchase = driver.find_element(By.ID, "buyCursor")
        purchase.click()

clicker = driver.find_element(By.ID, "cookie")

while True:
    clicker.click()
    if int(time.time()) % 5 == 0:
        check_store()




# driver.quit()