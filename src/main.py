from helpers.Dotenv import Dotenv
from parser.SitemapParser import SitemapParser
from parser.PageScrapper import PrestaShopScraper

# Dotenv()

parser = SitemapParser(
    "https://planeta-shop.com.ua/uploads/sitemaps/sitemap1.xml", ["/ganteli", "/gantel-"]
)
dumbbell_urls = parser.get_filtered_urls()

# Save in different formats
parser.save_to_txt()
# parser.save_to_json()
# parser.save_to_csv()

# Load URLs from a file or list
# with open("dumbbells.txt", "r", encoding="utf-8") as f:
#     product_urls = [line.strip() for line in f.readlines()]

# scraper = PrestaShopScraper(product_urls, limit=3)
# scraper.scrape_all_products()
# scraper.save_to_json()
# scraper.save_to_csv()
