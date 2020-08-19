import sqlite3
from tkinter import messagebox
import tkinter as tk 
import os 

def createConnection():
    if os.path.isdir('./db') == False:
        messagebox.showinfo('Directory Missing', 'Creating database folder to store database')
        os.mkdir('./db')

    conn = None
    currDir = os.getcwd()+'\db\password.db'
    try:
        conn = sqlite3.connect(currDir)
    except:
        messagebox.showerror('Error', 'Error connecting to database.')

    if conn:
        return conn