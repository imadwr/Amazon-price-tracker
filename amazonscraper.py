from bs4 import BeautifulSoup
import requests
import os

URL = os.getenv("product_amazon_url")


class AmazonScraper:
    def __init__(self):
        self.product_price = None
        self.product_title = ""

    def get_product_price(self):

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
        }

        response = requests.get(url=URL, headers=headers)
        amazon_website = response.text

        amazon_soup = BeautifulSoup(amazon_website, "html.parser")

        product_price_tag = amazon_soup.find(name="span", id="priceblock_ourprice")
        price = float(product_price_tag.getText().split("$")[1])
        self.product_price = price
        title = amazon_soup.find(name="span", id="productTitle").getText()
        self.product_title = title
