# controllers/user_controller.py
import requests
from fastapi import HTTPException
from bs4 import BeautifulSoup
import json
import re

# Example controller for user operations
async def fetch_details(event_id):
    # generate session at home page
    r = requests.Session()
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'dnt': '1',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }

    response = requests.get('https://viagogo.com/', headers=headers)
    r.cookies.update(response.cookies)
    r.headers.update(response.headers)
    response = r.get(f'https://www.viagogo.com/{event_id}')
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        event_name = soup.title.get_text(strip=True)
    except AttributeError:
        event_name = None
    try:
        event_time = soup.find('meta', {'name': 'robots'})['content'].replace('unavailable_after: ', '')
    except (AttributeError, TypeError):
        event_time = None
    try:
        event_place = soup.find('meta', {'property': 'og:description'})['content'].split(' at ')[1].split(' on ')[0]
    except (AttributeError, IndexError, TypeError):
        event_place = None
    try:
        price_match = re.search(r'"formattedMinPrice":"(.*?)"', response.text)
        lowest_listing = price_match.group(1) if price_match else None
    except AttributeError:
        lowest_listing = None
    try:
        event_image = soup.find('meta', {'property': 'og:image'})['content']
    except (AttributeError, TypeError):
        event_image = 'https://media.stubhubstatic.com/stubhub-v2-catalog/d_vgg-defaultLogo.jpg/q_auto:low,f_auto,c_fill,g_auto,w_280,h_180/categories/10671/6437768'
    event_details = {
        "EventName": event_name,
        "EventTime": event_time,
        "EventPlace": event_place,
        "LowestListing": lowest_listing,
        "EventImageURL": event_image
    }

    return event_details