import json

import requests
from bs4 import BeautifulSoup

# Send an HTTP GET request to the website
url = "https://books.toscrape.com/"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the book containers on the page
books = soup.find_all('article', class_='product_pod')

# Create a list to store book data
book_data = []

# Iterate through the book containers and extract information
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    link = book.h3.a['href']
    book_url = url.rsplit('/', 2)[0] + '/' + link
    
    book_info = {
        "Title": title,
        "Price": price,
        "Link": book_url
    }
    
    book_data.append(book_info)

# Save the data to a JSON file
with open('books_data.json', 'w') as json_file:
    json.dump(book_data, json_file, indent=4)

print("Data exported to 'books_data.json'")
