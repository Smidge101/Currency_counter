https://www.exchangerate-api.com/docs/python-currency-api


https://www.datacamp.com/tutorial/python-backend-development

https://www.google.com/search?q=building+a+python+django+database&sca_esv=b40ec5302c58a810&rlz=1C1GCEB_enUS1097US1126&sxsrf=AHTn8zomeoEpkamAcsGU0gT-zOR0kfYxcA%3A1741449041846&ei=UWfMZ7SrM4vtptQPg4aNqQE&ved=0ahUKEwj0l6Kc6_qLAxWLtokEHQNDIxUQ4dUDCBI&uact=5&oq=building+a+python+django+database&gs_lp=Egxnd3Mtd2l6LXNlcnAiIWJ1aWxkaW5nIGEgcHl0aG9uIGRqYW5nbyBkYXRhYmFzZTIFECEYqwIyBRAhGKsCSM8PUPoDWMEMcAF4AZABAJgBcKABsgSqAQM2LjG4AQPIAQD4AQGYAgigAuIEwgIKEAAYsAMY1gQYR8ICBhAAGA0YHsICCxAAGIAEGIYDGIoFwgIKECEYoAEYwwQYCpgDAIgGAZAGCJIHAzcuMaAH8hs&sclient=gws-wiz-serp



import sqlite3

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row  # Access columns by name
    return conn

def initialize_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)
    conn.commit()
    conn.close()

if name == "main":
    initialize_db()
