import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3
'''
TODO
- Create sqlite3 database to store all passwords in MainPage
- This page will display the database neatly 
'''
class VaultPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        button = tk.Button(self, text='test').pack()