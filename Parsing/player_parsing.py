import sys
sys.dont_write_bytecode = True

# Django specific settings
import os
from dotenv import load_dotenv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')
import django
django.setup()
import requests
load_dotenv()
base_path = os.getenv('base_path_player')
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
from orm.db.models import Player
from orm.db.models import Club
from orm.db.models import Competition

def get_position_code(player_position):
    switcher = {
        'вратарь': 'GOA',
        'защитник': 'DEF',
        'полузащитник': 'MID',
        'нападающий': 'STR'
    }
    return switcher.get(player_position, 'Unknown')

def fetch_content(url, retries=3, timeout=10):
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            return response.content
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            if attempt < retries - 1:
                print(f"Retrying ({attempt + 1}/{retries})...")
    return None

a = Club.objects.all()
competition = Competition.objects.all()

for club in a:
    url = f'https://www.sports.ru/football/club/{club.slug}/team/'
    b = club.id
    c = club.country_id
    response_content = fetch_content(url)
    if response_content is None:
        print(f"Failed to fetch {url} after retries.")
        continue

    soup = BeautifulSoup(response_content, 'html.parser')
    table = soup.find('div', class_='stat mB15')
    if table is None:
        print(f"No table found for {club.name}")
        continue

    table_body = table.find('tbody')
    if table_body is None:
        print(f"No tbody found for {club.name}")
        continue

    table_row = table_body.find_all('tr')
    if not table_row:
        print(f"No table rows found for {club.name}")
        continue


    for com in competition:
        if c == com.country_id:
            d = com.id
            break



    i = 0
    for row in table_row:
        name = row.find('a').get_text()
        player_link = row.find('a')['href']
        slug = player_link.split('/')[-2]

        name_ru = row.find('a').get_text()
        number = row.find('td').get_text(strip=True)
        if not number:
            number = '0'
        name = GoogleTranslator(source='auto', target='en').translate(name)
        player_position = row.find_all('td')[-1].get_text(strip=True)
        position_code = get_position_code(player_position)

        club_link = row.find('a')['href']
        club_response_content = fetch_content(club_link)

        if club_response_content is None:
            print(f"Failed to fetch {club_link} after retries.")
            continue

        club_soup = BeautifulSoup(club_response_content, 'html.parser')
        descr = club_soup.find('div',class_="descr").text
        club_logo_box = club_soup.find('div', class_="img-box")
        if club_logo_box is None:
            print(f"No logo box found for {name}")
            continue

        club_logo = club_logo_box.find('img')['src']
        if not club_logo:
            print(f"No logo found for {name}")
            continue

        logo_response_content = fetch_content(club_logo)
        if logo_response_content is None:
            print(f"Failed to fetch logo for {name}")
            continue



        type = club_logo.split('.')[-1]
        club_path = os.path.join(base_path,club.name)
        player_path = os.path.join(club_path,name)
        os.makedirs(player_path, exist_ok=True)

        logo_path = os.path.join(player_path, f'{name}.{type}')
        relative_logo_path = logo_path.split('C:/Users/user/Desktop/Parser/Proliga')[-1].replace('\\', '/')
        with open(logo_path, 'wb') as f:
            f.write(logo_response_content)
        print(f'{name} Saved photo! ')

        try:
            Player.objects.get(name=name)
            print('Already Exists: ', name)
        except Player.DoesNotExist:
            Player.objects.create(name=name,slug=slug, shirt_number=number,image=relative_logo_path,club_id=b,position=position_code,name_ru=name_ru,player_link=player_link,native=descr)
            i += 1
            print(i, 'created: ', name)

    print(f"\n{club.name} Player finished\n")
