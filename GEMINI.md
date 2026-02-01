# Recipe Scraper

## Project Overview
This project is a Python-based utility designed to scrape recipe data from various websites and save it in JSON format. It utilizes the `recipe-scrapers` library to parse recipe content. It also includes functionality (currently in development) to upload these recipes to Google Drive.

## Technologies & Dependencies
*   **Language:** Python (>=3.14)
*   **Package Manager:** [uv](https://github.com/astral-sh/uv)
*   **Key Libraries:**
    *   `recipe-scrapers`: For extracting recipe data from websites.
    *   `google-api-python-client`: For Google Drive API interaction.
    *   `google-genai`: Included in dependencies, possibly for future AI enhancements (referenced in README as an attempted approach).

## Setup & Installation
1.  Ensure you have `uv` installed.
2.  Install dependencies:
    ```bash
    uv sync
    ```

## Usage

### Scraping Recipes
1.  Open `main.py`.
2.  Modify the `recipes` list with the URLs you want to scrape:
    ```python
    recipes = [
        "https://www.recipetineats.com/gyoza-japanese-dumplings-potstickers/",
        # Add your URLs here
    ]
    ```
3.  Run the scraper:
    ```bash
    uv run main.py
    ```
    This will generate JSON files in the `recipes/` directory.

### Uploading to Drive
To upload files to Google Drive, run:
```bash
uv run upload-to-drive.py
```
*Note: This script appears to be a work-in-progress and relies on Google Application Default Credentials.*

## Key Files
*   **`main.py`**: The primary entry point. Iterates through a list of URLs, scrapes them, and saves the output as JSON in the `recipes/` folder.
*   **`upload-to-drive.py`**: Script intended to upload scraped files to Google Drive.
*   **`pyproject.toml`**: Project configuration and dependency definition.
*   **`recipes/`**: Output directory for the scraped JSON files.
