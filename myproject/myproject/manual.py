import sqlite3


    
conn = sqlite3.connect("database.db")
conn.row_factory = sqlite3.Row 

import sqlite3

def get_db_connection():
     conn = sqlite3.connect("database.db") 
     conn.row_factory = sqlite3.Row 

     return conn

def initialize_db(): 
    conn = get_db_connection() 
    cursor = conn.cursor() 
    res = cursor.execute("""SELECT * FROM users""")
    print(res.fetchone()) 
    conn.commit() 
    conn.close()

if __name__ == "__main__": 
    initialize_db()

