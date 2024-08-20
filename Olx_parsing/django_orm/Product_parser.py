import requests
from bs4 import BeautifulSoup
import os
import time

url = "https://www.olx.uz/moda-i-stil/"
base_url = "https://www.olx.uz"
image_dir = os.getenv('image_file_path')

# Fayl katalogini yaratish
if not os.path.exists(image_dir):
    os.makedirs(image_dir)


def download_image(image_url, product_id):
    try:
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            image_path = os.path.join(image_dir, f"product_{product_id}.jpg")
            with open(image_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            return image_path
        else:
            return "No Image Downloaded"
    except Exception as e:
        return f"Error: {str(e)}"


def get_products(url):
    products = []
    product_id = 1

    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract product items
        items = soup.find_all('div', class_='offer-wrapper')

        for item in items:
            title_tag = item.find('a', class_='marginright5 link linkWithHash detailsLink')
            if title_tag:
                product_name = title_tag.get_text(strip=True)
                link = title_tag['href']
                link = base_url + link if link.startswith('/') else link
            else:
                product_name = "No Product Name"
                link = "No Link"

            price_tag = item.find('p', class_='price')
            price = price_tag.get_text(strip=True) if price_tag else "No Price"

            location_tag = item.find('small', class_='breadcrumb x-normal')
            location = location_tag.get_text(strip=True) if location_tag else "No Location"

            customer_name = "No Customer Name"
            phone_number = "No Phone Number"

            # Extract image path
            image_tag = item.find('img', class_='fleft')
            image_url = image_tag['src'] if image_tag else None
            image_path = download_image(image_url, product_id) if image_url else "No Image"

            time_tag = item.find('td', class_='bottom-cell')
            add_product_time = time_tag.get_text(strip=True) if time_tag else "No Time Info"

            product = {
                'ID': product_id,
                'Customer_name': customer_name,
                'Product_name': product_name,
                'Phone_number': phone_number,
                'Location': location,
                'Product_image_path': image_path,
                'Add_product_time': add_product_time,
                'Price': price,
                'Product_link': link
            }
            products.append(product)
            product_id += 1

        # Find next page URL
        next_page = soup.find('a', {'data-cy': 'pagination-forward'})
        url = next_page['href'] if next_page else None
        if url and not url.startswith("http"):
            url = base_url + url

        # 1-soniyalik pauza
        time.sleep(1)

    return products


# Ma'lumotlarni parsing qilish
products = get_products(url)

# Natijani ko'rish
for product in products:
    print(product)