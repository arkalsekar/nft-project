import requests
from parsel import Selector
import re
import lxml.html

cookies = {
    'isOpen': '1',
    '_ga': 'GA1.1.139025886.1718506172',
    '_fbp': 'fb.1.1718506175694.912323509995198930',
    '_ga_Z2YELMFYND': 'GS1.1.1718506172.1.1.1718506447.0.0.0',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'isOpen=1; _ga=GA1.1.139025886.1718506172; _fbp=fb.1.1718506175694.912323509995198930; _ga_Z2YELMFYND=GS1.1.1718506172.1.1.1718506447.0.0.0',
    'origin': 'https://upcomingnft.net',
    'priority': 'u=1, i',
    'referer': 'https://upcomingnft.net/upcoming-events/',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'action': 'movie_datatables',
}

data = {
    'draw': '4',
    'columns[0][data]': '0',
    'columns[0][name]': '',
    'columns[0][searchable]': 'true',
    'columns[0][orderable]': 'false',
    'columns[0][search][value]': '',
    'columns[0][search][regex]': 'false',
    'columns[1][data]': '1',
    'columns[1][name]': '',
    'columns[1][searchable]': 'true',
    'columns[1][orderable]': 'false',
    'columns[1][search][value]': '',
    'columns[1][search][regex]': 'false',
    'columns[2][data]': '2',
    'columns[2][name]': '',
    'columns[2][searchable]': 'true',
    'columns[2][orderable]': 'true',
    'columns[2][search][value]': '',
    'columns[2][search][regex]': 'false',
    'columns[3][data]': '3',
    'columns[3][name]': '',
    'columns[3][searchable]': 'true',
    'columns[3][orderable]': 'true',
    'columns[3][search][value]': '',
    'columns[3][search][regex]': 'false',
    'columns[4][data]': '4',
    'columns[4][name]': '',
    'columns[4][searchable]': 'true',
    'columns[4][orderable]': 'false',
    'columns[4][search][value]': '',
    'columns[4][search][regex]': 'false',
    'columns[5][data]': '5',
    'columns[5][name]': '',
    'columns[5][searchable]': 'true',
    'columns[5][orderable]': 'true',
    'columns[5][search][value]': '',
    'columns[5][search][regex]': 'false',
    'columns[6][data]': '6',
    'columns[6][name]': '',
    'columns[6][searchable]': 'true',
    'columns[6][orderable]': 'true',
    'columns[6][search][value]': '',
    'columns[6][search][regex]': 'false',
    'columns[7][data]': '7',
    'columns[7][name]': '',
    'columns[7][searchable]': 'true',
    'columns[7][orderable]': 'false',
    'columns[7][search][value]': '',
    'columns[7][search][regex]': 'false',
    'order[0][column]': '4',
    'order[0][dir]': 'desc',
    'start': '0',
    'length': '200',
    'search[value]': '',
    'search[regex]': 'false',
    'slug': '/upcoming-events/',
}

response = requests.post(
    'https://upcomingnft.net/wp-admin/admin-ajax.php',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
).json()

tables = response['data']
for i in range(len(tables)):
    # Extracting name of the NFT 
    name_selector = Selector(text=tables[i][1])
    name = name_selector.css("h6::text").get()
    print("Name : ", name)

    # Extracting the Pre Sale Date of the NFT
    pre_sale_selector = lxml.html.document_fromstring(tables[i][2])
    pre_sale = pre_sale_selector.text_content() + " " 
    print("Pre Sale : ", pre_sale)

    # Extracting the Pre Sale Date of the NFT
    public_sale_selector = lxml.html.document_fromstring(tables[i][3])
    public_sale = public_sale_selector.text_content() + " " 
    print("PUblic Sale : ", public_sale)

    # Extracting the Price of the NFT
    price_selector = lxml.html.document_fromstring(tables[i][4])
    price = price_selector.text_content()
    print("Price : ", price)    

    # Extracting the Price of the NFT
    register_selector = Selector(text=tables[i][7])
    register = register_selector.css("a::attr(href)").get()
    print("Register : ", register)
    