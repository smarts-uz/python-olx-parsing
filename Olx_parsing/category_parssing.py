import requests
from bs4 import BeautifulSoup
import os
from django.utils.dateparse import parse_datetime
from your_project.settings import BASE_PATH_PLAYER  # O'zingizning yo'lga moslashtiring
from your_app.models import Ayirboshlash, Bolalar_dunyosi, Elektr_jihozlari, Hayvonlar, Ish, Kochmas_mulk, Moda_Stil, \
    Sport, Tekin, Transport, Uy_Bog, Xizmatlar


def fetch_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.content
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def parse_category(category_name, url):
    response_content = fetch_content(url)
    if response_content is None:
        return

    soup = BeautifulSoup(response_content, 'html.parser')

    # Find products in the category page
    products = soup.find_all('a', class_='css-1ep67ka')
    for product in products:
        product_name = product.find('p', class_='css-g6otoa').get_text()
        product_image_url = product.find('img')['src']
        product_link = product['href']

        # Determine model based on category_name
        model_class = determine_model_class(category_name)
        if model_class:
            save_product(model_class, product_name, product_image_url, product_link)


def determine_model_class(category_name):
    # Map category names to model classes
    category_to_model = {
        'Ayirboshlash': Ayirboshlash,
        'Bolalar_dunyosi': Bolalar_dunyosi,
        'Elektr_jihozlari': Elektr_jihozlari,
        'Hayvonlar': Hayvonlar,
        'Ish': Ish,
        'Kochmas_mulk': Kochmas_mulk,
        'Moda_Stil': Moda_Stil,
        'Sport': Sport,
        'Tekin': Tekin,
        'Transport': Transport,
        'Uy_Bog': Uy_Bog,
        'Xizmatlar': Xizmatlar,
    }
    return category_to_model.get(category_name)


def save_product(model_class, product_name, product_image_url, product_link):
    # Fetch product page to get more details if needed
    product_content = fetch_content(product_link)
    if product_content is None:
        return

    product_soup = BeautifulSoup(product_content, 'html.parser')
    customer_name = product_soup.find('span', class_='customer-name-class').get_text()  # Adjust the selector as needed
    phone_number = product_soup.find('span', class_='phone-number-class').get_text()  # Adjust the selector as needed
    location = product_soup.find('span', class_='location-class').get_text()  # Adjust the selector as needed
    price = int(
        product_soup.find('span', class_='price-class').get_text().replace('USD', '').strip())  # Adjust as needed
    add_product_time = parse_datetime(product_soup.find('span', class_='date-class').get_text())  # Adjust as needed

    # Save the product
    try:
        model_class.objects.create(
            Costumer_name=customer_name,
            Product_name=product_name,
            Phone_number=phone_number,
            Location=location,
            Price=price,
            Product_image_url=product_image_url,
            Add_product_time=add_product_time,
            created_at=None,
            updated_at=None,
            deleted_at=None,
            created_by=None,
            updated_by=None,
            deleted_by=None
        )
        print(f"Product '{product_name}' saved successfully.")
    except Exception as e:
        print(f"Error saving product '{product_name}': {e}")


# Example usage
categories = {
    'detskiy-mir': 'Bolalar_dunyosi',
    'elektronika': 'Elektr_jihozlari',
    # Add other categories here
}

for path, model_name in categories.items():
    category_url = f'https://www.olx.uz/{path}/'
    parse_category(model_name, category_url)