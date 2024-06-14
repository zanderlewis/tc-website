import sqlite3


def delete_menu():
    # Connect to the SQLite database
    conn = sqlite3.connect("menu.db")
    c = conn.cursor()

    # Delete everything from the menu table
    c.execute("DELETE FROM ashevillenc")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
