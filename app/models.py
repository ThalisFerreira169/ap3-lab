import sqlite3
from datetime import date

DATABASE_PATH = 'instance/app.db'

def get_db_connection():
  conn = sqlite3.connect(DATABASE_PATH)
  conn.row_factory = sqlite3.Row
  return conn

def create_tables():
  conn = get_db_connection()
  cursor = conn.cursor()
    
  cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL UNIQUE, email TEXT NOT NULL UNIQUE,password TEXT NOT NULL)''')

  cursor.execute('''CREATE TABLE IF NOT EXISTS meal_plans (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL, date TEXT NOT NULL, calories INTEGER, FOREIGN KEY (user_id) REFERENCES users (id))''')
    
  conn.commit()
  conn.close()

def insert_user(username, email, password):
  conn = get_db_connection()
  cursor = conn.cursor()
  cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
  conn.commit()
  conn.close()

def get_user_by_email(email):
  conn = get_db_connection()
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
  user = cursor.fetchone()
  conn.close()
  return user

def insert_meal_plan(user_id, meal_date, calories):
  conn = get_db_connection()
  cursor = conn.cursor()
  cursor.execute('INSERT INTO meal_plans (user_id, date, calories) VALUES (?, ?, ?)', (user_id, meal_date, calories))
  conn.commit()
  conn.close()
