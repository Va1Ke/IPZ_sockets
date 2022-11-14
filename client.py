import socket
from tkinter import *
import tkinter as tk

window = tk.Tk()
window.title('Client')
window.geometry('230x130+800+100')
HOST = "127.0.0.1"
PORT = 65431


def log_in():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        sended_data = f"log_in,{e1.get()},{e2.get()},{e3.get()}"
        s.send(sended_data.encode())
        data = s.recv(1024).decode()
        message.config(text=f'Success',fg='#2c731a')

def add_new_user():
    def send():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            sended_data = f"add_user,{e1.get()},{e2.get()},{e3.get()},{e4.get()}"
            s.send(sended_data.encode())
            data = s.recv(1024).decode()
            message.config(text=f'Success',fg='#2c731a')

    admin_window = tk.Tk()
    admin_window.title('AddUser')
    admin_window.geometry('230x130+800+100')
    tk.Label(admin_window, text="User_name:").grid(row=0)
    tk.Label(admin_window, text="Password:").grid(row=1)
    tk.Label(admin_window, text="Admin_name:").grid(row=2)
    tk.Label(admin_window, text="Admin_Password:").grid(row=3)
    message = tk.Label(admin_window, text="")
    message.grid(row=4, column=0)
    e1 = tk.Entry(admin_window)
    e2 = tk.Entry(admin_window)
    e3 = tk.Entry(admin_window)
    e4 = tk.Entry(admin_window)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    btn2 = Button(admin_window, text='Send', command=send, pady=4, padx=10)
    btn2.grid(row=4, column=1, pady=4, padx=0)

    window.mainloop()

tk.Label(window, text="User_name:").grid(row=0)
tk.Label(window, text="Password:").grid(row=1)
tk.Label(window, text="WorkedHours:").grid(row=2)
message = tk.Label(window, text="")
message.grid(row=4, column=0)

e1 = tk.Entry(window)
e2 = tk.Entry(window)
e3 = tk.Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

btn1 = Button(window, text='Add user', command=add_new_user, pady=4, padx=10)
btn1.grid(row=3, column=0, pady=4, padx=0)

btn2 = Button(window, text='Send', command=log_in, pady=4, padx=10)
btn2.grid(row=3, column=1, pady=4, padx=0)


window.mainloop()