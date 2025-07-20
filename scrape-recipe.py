import json
import os
from recipe_scrapers import scrape_me

recipes = [
    "https://www.recipetineats.com/peach-cobbler/",
    "https://www.recipetineats.com/sausage-ragu/",
    "https://www.recipetineats.com/potatoes-au-gratin/",
    "https://www.recipetineats.com/cheeseburger-casserole-homemade-hamburger-helper/",
    "https://www.recipetineats.com/salsa-super-easy-restaurant-style/",
    "https://www.recipetineats.com/chicken-fajitas/"


]

for i in range(0, len(recipes)):

    scraper = scrape_me(recipes[i])
    scraper.title()
    scraper.instructions()

    recipes_dir = os.path.join(os.path.dirname(__file__), "recipes")
    os.makedirs(recipes_dir, exist_ok=True)
    filename = scraper.title() + ".json"
    filepath = os.path.join(recipes_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(scraper.to_json(), f, indent=2)