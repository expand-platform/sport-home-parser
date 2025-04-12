import requests
from bs4 import BeautifulSoup
import json
import csv
import time


class PrestaShopScraper:
    def __init__(self, urls, limit=3):
        self.urls = urls[:limit]  # Limit the number of URLs to scrape
        self.products = []

    def fetch_page(self, url):
        """Fetch the HTML content of a product page."""
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch {url} - Status Code: {response.status_code}")
            return None

    def parse_product(self, url):
        """Extract title, price, and description from a product page."""
        html = self.fetch_page(url)
        if not html:
            return

        soup = BeautifulSoup(html, "html.parser")

        # Extract title
        title = soup.find("h1")
        title = title.text.strip() if title else "No title found"

        # Extract price
        price = soup.find(class_="product-price__main-value")  # Adjust the class name if needed
        price = price.text.strip() if price else "No price found"

        # Extract description
        description = soup.find(
            "div", class_="accordion-tabs__content"
        )  # Adjust class if needed
        description = (
            description.text.strip() if description else "No description found"
        )

        # Store product data
        self.products.append(
            {"title": title, "price": price, "description": description, "url": url}
        )
        print(f"Scraped: {title}")

    def scrape_all_products(self):
        """Scrape all product pages."""
        for url in self.urls:
            self.parse_product(url)
            time.sleep(1)  # Be polite and avoid getting blocked

    def save_to_json(self, filename="products.json"):
        """Save data to JSON."""
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.products, f, indent=4, ensure_ascii=False)
        print(f"Saved {len(self.products)} products to {filename}")

    def save_to_csv(self, filename="products.csv"):
        """Save data to CSV."""
        with open(filename, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(
                f, fieldnames=["title", "price", "description", "url"]
            )
            writer.writeheader()
            writer.writerows(self.products)
        print(f"Saved {len(self.products)} products to {filename}")


# Load URLs from a file or list
with open("dumbbells.txt", "r", encoding="utf-8") as f:
    product_urls = [line.strip() for line in f.readlines()]

# Run the scraper (limit to 3 products)
