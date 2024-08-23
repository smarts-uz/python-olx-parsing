import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from dotenv import load_dotenv
from django.utils.dateparse import parse_datetime

# .env faylni yuklash
load_dotenv()

base_url = "https://www.olx.uz"

# .env fayldan image_dir o'qish
image_dir = os.getenv('image_file_path')

# Fayl katalogini yaratish
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

def download_image(image_url, product_id):
    image_path = os.path.join(image_dir, f"product_{product_id}.jpg")
    if image_url:
        try:
            response = requests.get(image_url)
            response.raise_for_status()
            with open(image_path, 'wb') as file:
                file.write(response.content)
        except requests.RequestException as e:
            print(f"Error downloading image: {e}")
            return 'No Image'
    return image_path

def get_product_details(url, category_model):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    product = {}

    # Product name
    try:
        product_name_tag = soup.find('div', {'data-cy': 'ad_title'})
        product['product_name'] = product_name_tag.find('h4').text.strip() if product_name_tag else 'No Product Name'
    except AttributeError:
        product['product_name'] = 'No Product Name'

    # Customer name
    try:
        customer_name_tag = soup.find('h4', class_='css-1lcz6o7')
        product['customer_name'] = customer_name_tag.text.strip() if customer_name_tag else 'No Customer Name'
    except AttributeError:
        product['customer_name'] = 'No Customer Name'

    # Phone number
    try:
        phone_tag = soup.find('a', {'data-testid': 'contact-phone'})
        product['phone_number'] = phone_tag.text.strip() if phone_tag else 'No Phone Number'
    except AttributeError:
        product['phone_number'] = 'No Phone Number'

    # Location
    try:
        location_div = soup.find('div', {'class': 'css-1dp6pbg'})
        if location_div:
            location_p_tags = location_div.find_all('p')
            location = ''
            if location_p_tags:
                location = location_p_tags[0].text.strip()
                if len(location_p_tags) > 1:
                    location += f", {location_p_tags[1].text.strip()}"
            product['location'] = location if location else 'No Location Info'
        else:
            product['location'] = 'No Location Info'
    except AttributeError:
        product['location'] = 'No Location Info'

    # Add product time
    try:
        add_product_time_tag = soup.find('span', {'data-cy': 'ad-posted-at'})
        product['add_product_time'] = parse_datetime(add_product_time_tag.text.strip()) if add_product_time_tag else None
    except (AttributeError, ValueError):
        product['add_product_time'] = None

    # Price
    try:
        price_tag = soup.find('div', {'data-testid': 'ad-price-container'})
        product['price'] = price_tag.find('h3', class_='css-90xrc0').text.strip() if price_tag else 'No Price Info'
    except AttributeError:
        product['price'] = 'No Price Info'

    # Product image
    try:
        image_tag = soup.find('img', {'data-testid': 'swiper-image-lazy'})
        image_url = urljoin(base_url, image_tag['src']) if image_tag else None
        download_image(image_url, 1)
        product['product_image_path'] = download_image(image_url, 1) if image_url else 'No Image'
    except AttributeError:
        product['product_image_path'] = 'No Image'

    # Check if the product already exists in the database
    try:
        existing_product = category_model.objects.filter(
            customer_name=product['customer_name'],
            product_name=product['product_name'],
            phone_number=product['phone_number'],
            location=product['location'],
            product_image_path=product['product_image_path'],
            add_product_time=product['add_product_time'],
            product_url=url,
            price=product['price']
        ).first()

        if existing_product:
            # Update the existing record
            existing_product.product_image_path = product['product_image_path']
            existing_product.price = product['price']
            existing_product.save()
            return existing_product
        else:
            # Create a new record
            new_product = category_model.objects.create(
                customer_name=product['customer_name'],
                product_name=product['product_name'],
                phone_number=product['phone_number'],
                location=product['location'],
                product_image_path=product['product_image_path'],
                add_product_time=product['add_product_time'],
                product_url=url,
                price=product['price']
            )
            return new_product
    except Exception as e:
        print(f"Error saving product to database: {e}")

    return product