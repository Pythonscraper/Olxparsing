from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
browser = webdriver.Chrome('chromedriver.exe', options=options)
url = 'https://www.olx.uz/d/obyavlenie/zhalyuzi-tashkent-jalyuzi-toshkent-ishlab-chqaruvchidan-yuvish-15000-som-ID2iQcL.html'
browser.get(url)


def getinformations():
    time.sleep(3)

    errors = []
    try:
        browser.find_element(By.XPATH, "//button[@data-cy='dismiss-cookies-overlay']").click()
    except NoSuchElementException as err:
        errors.append(err.msg)
        pass
    except ElementClickInterceptedException as err:
        errors.append(err.msg)
        pass


    try:
        name = browser.find_element(By.XPATH, "//h1[@class='css-r9zjja-Text eu5v0x0']").text.strip()
        print(f"1: ", name)
    except Exception:
        print('No project')
    time.sleep(1)
    
    try:
        price = browser.find_element(By.XPATH, "//p[@class='css-xl6fe0-Text eu5v0x0']").text.strip()
        print(f"2: ", price)
    except Exception:
        print('No project')
    time.sleep(1)
    
    try:
        address = browser.find_element(By.XPATH, "//p[@class='css-7xdcwc-Text eu5v0x0']").text.strip()
        print(f"3: ", address)
    except Exception:
        print('No project')
    time.sleep(1)
    
    try:
        user = browser.find_element(By.XPATH, "//h2[@class='css-u8mbra-Text eu5v0x0']").text.strip()
        print(f"4: ", user)
    except Exception:
        print('No project')
    time.sleep(1)
    
    try:
        text = browser.find_element(By.XPATH, "//div[@class='css-2t3g1w-Text']").text.strip()
        print(f"5: ", text)
    except Exception:
        print('No project')
    time.sleep(1)
    
    try:
        browser.find_element(By.XPATH, "//button[@data-testid='show-phone']").click()
        time.sleep(1)
        number = browser.find_element(By.XPATH, "//li[@class='css-11hr49z-Text eu5v0x0']").text.strip()
        print(f"6: ", number)
    except Exception:
        print('No project')
    time.sleep(1)

    browser.close()
    browser.quit()


getinformations()
