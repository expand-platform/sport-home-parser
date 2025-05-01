from helpers.Dotenv import Dotenv
from parser.SitemapParser import SitemapParser
from parser.PageScrapper import PrestaShopScraper

# parser = SitemapParser(
#     "https://planeta-shop.com.ua/uploads/sitemaps/sitemap1.xml", ["/ganteli", "/gantel-"]
# )
# dumbbell_urls = parser.get_filtered_urls()

# Save in different formats
# parser.save_to_txt()
# parser.save_to_json()
# parser.save_to_csv()

# Load URLs from a file or list
# with open("dumbbells.txt", "r", encoding="utf-8") as f:
#     product_urls = [line.strip() for line in f.readlines()]

scraper = PrestaShopScraper()
product = scraper.scrape_product("https://zelart.com.ua/product/7212")
product_string_prettified = scraper.product_prettify(product)
print(product["id"]) # type: ignore
print(product_string_prettified)

# scraper.save_to_json()
# scraper.save_to_csv()