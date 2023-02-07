# http://quotes.toscrape.com
# http://flibusta.is/b/440093/read

import requests
from bs4 import BeautifulSoup
import csv

# self decision

response = requests.get('http://quotes.toscrape.com')
html_data = BeautifulSoup(response.text)
quotes = html_data.find_all(class_='quote')

# with open('quotes.csv', 'w') as file:
#     headers_list = ['Author', 'Quote', 'Tags']
#     csv_writer = csv.DictWriter(file, fieldnames=headers_list)
#     csv_writer.writeheader()
#     for quote in quotes:
#         quote_text = quote.find(class_='text').get_text()
#         quote_author = quote.find(class_='author').get_text()
#         quote_tags = quote.find(class_='keywords')['content']
#         csv_writer.writerow({
#             'Author': quote_author,
#             'Quote': quote_text,
#             'Tags': quote_tags
#         })


# lector decision

with open('quotes_lector.csv', 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Text', 'Author', 'Tags'])
    for quote in quotes:
        quote_text = quote.find(class_='text').get_text()
        quote_author = quote.find(class_='author').get_text()
        quote_tags = quote.find(class_='keywords')['content']
        csv_writer.writerow([quote_text,quote_author,quote_tags])