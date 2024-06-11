import requests
from bs4 import BeautifulSoup
import sqlite3
import delete

_debug_ = False

def debug(message):
    if _debug_:
        print(f"DEBUG: {message}")

# Connect to the SQLite database
conn = sqlite3.connect("menu.db")
c = conn.cursor()

delete.delete_menu()

# Get the HTML of the webpage
response = requests.get("https://thaichiliasianbistronc.kwickmenu.com/")
soup = BeautifulSoup(response.text, "html.parser")

# Find all categories that have a 'data-item' attribute
categories = soup.find_all("li", class_="cat", attrs={"data-item": True})

debug(f"Found {len(categories)} categories")

# Insert each menu item into the database
# Insert each menu item into the database
for category in categories:
    try:
        # Parse the HTML within the 'data-item' attribute
        category_html = BeautifulSoup(category["data-item"], "html.parser")

        # Find all menu items within the category
        menu_items = category_html.find_all("li", class_="item")

        debug(f"Found {len(menu_items)} items in category {category_html.find('h5').text}")

        for item in menu_items:
            name_element = item.find("b", class_="n") or item.find("b", class_="n2")
            description_element = item.find("p") if item.find("p") and item.find("p").text.strip() != "" else ""
            price_element = item.find("b", class_="p")
            section_element = category_html.find("h5")

            if (
                name_element is not None
                and price_element is not None
                and section_element is not None
            ):
                name = name_element.text
                description = description_element.text if description_element else ""
                price = price_element.text.replace("$", "")
                # Format the price to always have two decimal places
                price = f"{float(price):.2f}"
                section = section_element.text
                debug(f"Inserting {name}, {description}, {price}, {section}")
                c.execute(
                    "INSERT INTO menu VALUES (?, ?, ?, ?)",
                    (name, description, price, section),
                )
            else:
                debug(f"Skipping item due to missing data: {item}: {name_element}, {description_element}, {price_element}, {section_element}")
    except Exception as e:
        debug(f"Exception occurred: {e}")

# Commit the changes and close the connection
debug("Committing changes")
conn.commit()
debug("Closing connection")
conn.close()