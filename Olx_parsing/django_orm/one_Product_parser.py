import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from dotenv import load_dotenv

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
        except requests.RequestException:
            return 'No Image'
    return image_path

def get_product_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    product = {}

    # Product name
    product_name_tag = soup.find('div', {'data-cy': 'ad_title'})
    product['Product_name'] = product_name_tag.find('h4').text.strip() if product_name_tag else 'No Product Name'

    # Customer name
    customer_name_tag = soup.find('h4', class_='css-1lcz6o7')
    product['Customer_name'] = customer_name_tag.text.strip() if customer_name_tag else 'No Customer Name'

    # Phone number
    phone_tag = soup.find('a', {'data-testid': 'contact-phone'})
    product['Phone_number'] = phone_tag.text.strip() if phone_tag else 'No Phone Number'

    # Location
    location_div = soup.find('div', {'class': 'css-1dp6pbg'})
    if location_div:
        location_p_tags = location_div.find_all('p')
        location = ''
        if location_p_tags:
            location = location_p_tags[0].text.strip()
            if len(location_p_tags) > 1:
                location += f", {location_p_tags[1].text.strip()}"
        product['Location'] = location if location else 'No Location Info'

    # Add product time
    add_product_time_tag = soup.find('span', {'data-cy': 'ad-posted-at'})
    product['Add_product_time'] = add_product_time_tag.text.strip() if add_product_time_tag else 'No Time Info'

    # Price
    price_tag = soup.find('div', {'data-testid': 'ad-price-container'})
    product['Price'] = price_tag.find('h3', class_='css-90xrc0').text.strip() if price_tag else 'No Price Info'

    # Product image
    image_tag = soup.find('img', {'data-testid': 'swiper-image-lazy'})
    image_url = urljoin(base_url, image_tag['src']) if image_tag else None
    product['Product_image_path'] = download_image(image_url, 1) if image_url else 'No Image'

    # Product link
    product['Product_link'] = url

    return product

# Mahsulot ma'lumotlarini olish
url = "https://www.olx.uz/d/obyavlenie/odnorazovye-meditsinskie-shapochki-sharlotta-shapki-ID3IIbw.html"
product_details = get_product_details(url)

# Natijani chiqarish
print(product_details)