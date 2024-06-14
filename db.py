import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("menu.db")
c = conn.cursor()

# Create the table if it doesn't exist
c.execute(
    """CREATE TABLE IF NOT EXISTS ashevillenc
             (name text, item text, price real, section text)"""
)

c.execute(
    """CREATE TABLE IF NOT EXISTS ooltewahtn
                (name text, item text, price real, section text)"""
)

# Fetch all menu items
ashevillenc = c.execute("SELECT * FROM ashevillenc").fetchall()
ooltewahtn = c.execute("SELECT * FROM ooltewahtn").fetchall()

# Generate the HTML for the Asheville, NC menu
menu_html = '<details class="menu">\n<summary><h1 class="center">Asheville, NC Menu</h1></summary>\n<p class="center">Most things are vegetarian and can be made gluten free and/or vegan.</p>'
current_section = None
for name, item, price, section in ashevillenc:
    if section != current_section:
        if current_section is not None:
            menu_html += "</ul></details>\n"  # Close previous section
        # Start new section
        menu_html += (
            f'<details>\n<summary><h2 class="center">{section}</h2></summary>\n<ul>\n'
        )
        current_section = section
    # Format the price to always have two decimal places
    price = f"{price:.2f}"
    menu_html += f'  <li><div class="menu-item">{name}: {item} - ${price}</div></li>\n'
if current_section is not None:
    menu_html += "</ul></details>\n"  # Close last section
menu_html += "</details>\n"  # Close Asheville, NC menu

# Generate the HTML for the Ooltewah, TN menu
menu_html += '<details class="menu">\n<summary><h1 class="center">Ooltewah, TN Menu</h1></summary>\n'
current_section = None
for name, item, price, section in ooltewahtn:
    if section != current_section:
        if current_section is not None:
            menu_html += "</ul></details>\n"  # Close previous section
        # Start new section
        menu_html += (
            f'<details>\n<summary><h2 class="center">{section}</h2></summary>\n<ul>\n'
        )
        current_section = section
    # Format the price to always have two decimal places
    price = f"{price:.2f}"
    menu_html += f'  <li><div class="menu-item">{name}: {item} - ${price}</div></li>\n'
if current_section is not None:
    menu_html += "</ul></details>\n"  # Close last section
menu_html += "</details>\n"  # Close Ooltewah, TN menu

# Read the existing HTML
with open("menu_temp.html", "r") as file:
    html = file.read()

# Replace the placeholder with the menu HTML
html = html.replace("-*-*-menu-*-*-", menu_html)

# Write the new HTML
with open("menu.html", "w") as file:
    file.write(html)

# Close the database connection
conn.close()
