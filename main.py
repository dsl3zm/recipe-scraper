import json
import os
from recipe_scrapers import scrape_me

def main():
    recipes = [
    "https://www.recipetineats.com/gyoza-japanese-dumplings-potstickers/",
    "https://www.recipetineats.com/mexican-shredded-beef-and-tacos/",
    "https://www.recipetineats.com/baked-sausage-breakfast-hash/",
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


if __name__ == "__main__":
    main()
