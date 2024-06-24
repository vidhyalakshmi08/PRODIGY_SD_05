import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.amazon.in/gp/bestsellers/kitchen/ref=zg_bs_kitchen_sm"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results=soup.find_all('div',class_='zg-grid-general-faceout')


with open('ProductList.csv',mode='w',newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title','Product Link','Price','Rating'])

    for res in results:
        title = res.find('div', class_='_cDEzb_p13n-sc-css-line-clamp-3_g3dy1')
        link_tag = res.find('a', class_='a-link-normal')
        price = res.find('span', class_='p13n-sc-price')
        rating = res.find('span', class_='a-icon-alt')

        title_text = title.text.strip() if title else 'Title not found'
        product_link = "https://www.amazon.in" + link_tag.get('href') if link_tag else 'Link not found'
        price_text = price.text.strip() if price else 'Price not found'
        rating_text = rating.text.strip() if rating else 'Rating not found'

        writer.writerow([title_text, product_link, price_text, rating_text])

print("Data has been written to ProductList.csv")
