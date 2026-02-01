# Recipe Scraper

A quick and dirty recipe scraper that uses [this](https://github.com/hhursev/recipe-scrapers) recipe scraper
to quickly convert recipes online to json format.

Attempted to use gemini but got pretty inaccurate results.

Simply put in a list of the recipes you want to the `main.py` file (which will be saved
 to `/recipes/`) and then run `uv run main.py`.

 You can then upload these recipes to google drive by running `uv run upload-to-drive.py`.