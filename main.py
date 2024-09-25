# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import os
from dotenv import load_dotenv

load_dotenv()  # Ensure this is at the top of settings.py

# Print environment variables for testing
# print(f"DB Name: {os.getenv('db_name')}")
# print(f"DB User: {os.getenv('db_user')}")
# print(f"DB Password: {os.getenv('password')}")
# print(f"DB Host: {os.getenv('host')}")
# print(f"DB Port: {os.getenv('port')}")
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_phone_number(url):
    # WebDriver ni ishga tushirish
    driver = webdriver.Chrome(executable_path='"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"')  # ChromeDriver ning to'liq yo'lini kiriting
    driver.get(url)

    try:
        # "Pokazat telefon" tugmasini kutish va bosish
        show_phone_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'css-bq03zg'))
            # "Pokazat telefon" tugmasining to'g'ri klassini kiriting
        )
        show_phone_button.click()

        time.sleep(2)  # Telefon raqami yuklanishi uchun kutish

        # Telefon raqamini olish
        phone_number = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'css-1p1kj9u'))
            # Telefon raqami ko'rsatilgan element klassi
        ).text

        print("Telefon raqami:", phone_number)
    except Exception as e:
        print("Xatolik:", e)
    finally:
        driver.quit()


if __name__ == "__main__":
    url = 'https://www.olx.uz/d/obyavlenie/urban-samokat-ot-pervyh-ruk-postavschikov-ID3zK0n.html'
    get_phone_number(url)
