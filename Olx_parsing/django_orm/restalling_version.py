import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import django
import argparse
from one_Product_parser import get_product_details, download_image
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()  # Load environment variables from .env file

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')  # Ensure this is correct
django.setup()

from parserapp.models import Category, Moda_stil, Bolalar_dunyosi, Kochmas_mulk, Transport, Ish, Hayvonlar, Uy_va_Bog, Elektronika, Biznes_va_Xizmatlar, Xobbi_va_Sport, Tekinga_berish, Ayirboshlash

def get_product_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    items = soup.find_all('div', class_='css-1ut25fa')

    if not items:
        print("No items found. Please check the class names or the HTML structure.")
        return []

    product_links = []
    for item in items:
        link_tag = item.find('a', class_='css-z3gu2d')
        if link_tag and 'href' in link_tag.attrs:
            product_link = urljoin(url, link_tag['href'])
            product_links.append(product_link)

    return product_links

def get_all_product_links(start_url):
    all_product_links = []
    url = start_url

    while url:
        product_links = get_product_links(url)
        all_product_links.extend(product_links)

        # Find next page URL
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        next_page_tag = soup.find('a', {'data-cy': 'pagination-forward'})

        if next_page_tag and 'href' in next_page_tag.attrs:
            url = urljoin(start_url, next_page_tag['href'])
        else:
            url = None

        # 1-soniyalik pauza
        time.sleep(1)

    return all_product_links

def get_model_class(model_name):
    model_mapping = {
        'Moda_stil': Moda_stil,
        'Bolalar_dunyosi': Bolalar_dunyosi,
        'Kochmas_mulk': Kochmas_mulk,
        'Transport': Transport,
        'Ish': Ish,
        'Hayvonlar': Hayvonlar,
        'Uy_va_Bog': Uy_va_Bog,
        'Elektronika': Elektronika,
        'Biznes_va_Xizmatlar': Biznes_va_Xizmatlar,
        'Xobbi_va_Sport': Xobbi_va_Sport,
        'Tekinga_berish': Tekinga_berish,
        'Ayirboshlash': Ayirboshlash,
    }
    return model_mapping.get(model_name)

def get_phone_number(product_url):
    # Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no UI)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Create a new Chrome session
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        driver.get(product_url)

        # Find and click the "Show Phone" button
        show_phone_button = driver.find_element(By.XPATH, '//button[text()="Pokazat telefon"]')
        show_phone_button.click()

        time.sleep(2)  # Wait for the phone number to appear

        # Extract the phone number
        phone_number = driver.find_element(By.CLASS_NAME, 'css-1c4v0an').text  # Adjust this class name as needed
        return phone_number

    except Exception as e:
        print(f"Error occurred while fetching phone number: {e}")
        return None
    finally:
        driver.quit()

def main(category_id):
    try:
        category = Category.objects.get(id=category_id)
        start_url = category.category_url
        model_name = category.model_name
    except Category.DoesNotExist:
        print(f"Category with ID {category_id} does not exist.")
        return

    category_model = get_model_class(model_name)
    if not category_model:
        print(f"Model with name {model_name} does not exist.")
        return

    all_product_links = get_all_product_links(start_url)

    if all_product_links:
        for link in all_product_links:
            print(link)
            product_details = get_product_details(link, category_model)
            print(product_details)

            # Get phone number from the product page
            phone_number = get_phone_number(link)
            print(f"Phone Number: {phone_number}")

            # download_image(product_details['product_image_path'], product_details['product_name'])

    else:
        print("No product links found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch product links from a category URL.")
    parser.add_argument('category_id', type=int, help="ID of the category")
    args = parser.parse_args()
    main(args.category_id)