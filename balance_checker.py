from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime
import pygame

driver = webdriver.Firefox()
driver.get('https://example.com')
wait = WebDriverWait(driver, 15)
url = driver.current_url
print(f'Logged in {url}')
if url in url:
    print('Logged successfully')

target_user = 'example'
target_pass = 'example'

def balance_checker(user,passw):
    try:
        username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'your-target-ID'))
        )
        password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'your-target-ID'))
        )
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'your-target-CSS_SELECTOR'))
        )
    except Exception as e:
        print(f'Error with {e}')

    username.send_keys(user)
    password.send_keys(passw)
    driver.execute_script('arguments[0].click();', button)
    sleep(3)
    balance = driver.find_element(By.CLASS_NAME, 'your-target-CLASS_NAME')
    start_balance = balance.text
    print(f'Current balance is {start_balance}')

    while True:
        driver.refresh()
        sleep(60)
        try:
            balance_again = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'your-target-CLASS_NAME'))
            )
            current_balance = balance_again.text
        except Exception as b:
            print(f'Error with updated balance {b}')

        if current_balance != start_balance:
            start_balance = current_balance
            now = datetime.now().strftime('%H:%M:%S')
            print(f'Balance was changed\nOld Balance {start_balance}\nNew Balance {current_balance}')
            pygame.mixer.init()
            pygame.mixer.music.load('example.mp3')
            pygame.mixer.music.play()
        else:
            print('Same balance')

balance_checker(target_user,target_pass)

