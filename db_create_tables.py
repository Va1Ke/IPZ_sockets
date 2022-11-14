import sqlite3
import datetime

sqlite_connection = sqlite3.connect("mydatabase.db")
cursor = sqlite_connection.cursor()

# USERS
cursor.execute("""CREATE TABLE users(
                    user_name text PRIMARY KEY,
                    user_password text,
                    is_admin INTEGER)
               """)
sqlite_connection.commit()

# WORK_TIME
cursor.execute("""CREATE TABLE workflow(
                user_name text,
                worked_hours REAL,
                date datetime,
                FOREIGN KEY(user_name) REFERENCES users(user_name)
                )
               """)
sqlite_connection.commit()

cursor.close()