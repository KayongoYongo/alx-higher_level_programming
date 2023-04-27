#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

# Make a GET request to the website
url = "https://swapi.co/api/films/"
response = requests.get(url)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the links on the page and print their URLs
for link in soup.find_all("a"):
    href = link.get("href")
    if href:
        print(href)

