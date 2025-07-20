from google import genai
import os

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-pro", contents="Scrape the recipe from https://www.allrecipes.com/recipe/60708/jagerschnitzel/"   
)

recipes_dir = os.path.join(os.path.dirname(__file__), "recipes")
os.makedirs(recipes_dir, exist_ok=True)
filename = "jagerschnitzel.txt"
filepath = os.path.join(recipes_dir, filename)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(response.text)