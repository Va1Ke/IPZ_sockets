import datetime
import socket
from tkinter import *
import tkinter as tk
import sqlite3


sqlite_connection = sqlite3.connect("mydatabase.db")
cursor = sqlite_connection.cursor()

HOST = "127.0.0.1"
PORT = 65431

def add_admin(admin_name, admin_pass):
    try:

        cursor.execute("""INSERT INTO users
                            VALUES (?,?,?)
                            """, (admin_name, admin_pass, 1))
        sqlite_connection.commit()
    except Exception as ex:
        print("ex:", ex)

def add_user(user_name, user_password, admin_name, admin_pass):
    try:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        for row in users:
            if row[0] == admin_name and row[1] == admin_pass and row[2] == 1:
                cursor.execute("""INSERT INTO users
                                      VALUES (?,?,?)
                                       """, (user_name, user_password, 0))
                sqlite_connection.commit()
    except Exception as ex:
        print("ex:", ex)

def add_record(user_name, user_password, worked_hours):
    try:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        for row in users:
            if row[0] == user_name and row[1] == user_password:
                cursor.execute("""INSERT INTO workflow
                                      VALUES (?,?,?)
                                       """, (user_name, worked_hours, datetime.datetime.today().strftime('%Y-%m-%d')))
                sqlite_connection.commit()

    except Exception as ex:
        print("ex:", ex)

#add_admin("admin","12345")
s = socket.socket()
s.bind((HOST, PORT))
s.listen(50)
while True:
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            list = data.split(',')
            if list[0] == "log_in":
                add_record(list[1],list[2],list[3])
                conn.send("Success".encode())
            if list[0] == "add_user":
                bool = add_user(list[1],list[2],list[3],list[4])
                conn.send("Success".encode())
        conn.close()
