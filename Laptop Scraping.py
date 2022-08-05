from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

url = 'https://www.mytek.tn/informatique/ordinateurs-portables/pc-gamer.html?product_list_limit=all'

def get_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup

def  get_products(soup):
    products_list = []
    result = soup.find_all('tr', {'class' :'item product product-item product-item-info'})
    for item in result:
        products = {
            'name' : item.find('a', {'class' : 'product-item-link'}).text,
            'current_price' :float (item.find('span', {'class' : 'price-container price-final_price tax weee'}).find('span', {'class' : 'price'}).text.replace(' ', '').replace('TND', '').replace(',', '.').replace('\u202f',''). strip()),
            'link' : item.find('a', {'class' : 'product-item-link'}).get('href'),
        }
        products_list.append(products)
        
    return products_list

def create_dataframe(products_list):
    df = pd.DataFrame(products_list)
    df.to_csv('products.csv', index=False)
    print('File has been created')
    
    return 


soup = get_data(url)
products_list = get_products(soup)
create_dataframe (products_list)

