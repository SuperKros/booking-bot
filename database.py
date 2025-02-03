import sqlite3
from datetime import datetime

# Створення бази даних (якщо вона не існує)
def create_db():
    conn = sqlite3.connect('bookings.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        date_time TEXT
    )
    ''')
    conn.commit()
    conn.close()

# Функція для збереження запису
def save_booking(user_id, date_time):
    conn = sqlite3.connect('bookings.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
        INSERT INTO bookings (user_id, date_time)
        VALUES (?, ?)
        ''', (user_id, date_time))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error inserting booking: {e}")
        conn.rollback()
    conn.close()

# Функція для отримання всіх записів користувача
def get_user_bookings(user_id):
    conn = sqlite3.connect('bookings.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM bookings WHERE user_id = ?
    ''', (user_id,))
    bookings = cursor.fetchall()
    conn.close()
    return bookings

# Функція для видалення запису
def delete_booking(booking_id):
    conn = sqlite3.connect('bookings.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
        DELETE FROM bookings WHERE id = ?
        ''', (booking_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error deleting booking: {e}")
        conn.rollback()
    conn.close()
