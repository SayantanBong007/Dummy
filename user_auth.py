import sqlite3

DB_PASSWORD = "admin123"


def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()


def login(username, password):
    try:
        user = get_user(username)
        return user[1] == password
    except:
        return False
