import tkinter as tk
from tkinter import *
from tkinter import messagebox
import string
import random

FONT= ('Veranda', 12)
padding = 10
class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        # Ask user how long pthey want password to be
        tk.Label(self, text='How long should password be?', font=FONT).grid(row=0, sticky='nsew',pady=padding)
        self.lengthInput = tk.Entry(self, bg='light gray')
        self.lengthInput.grid(row=0,column=1, sticky='nsew',pady=padding)
        
        # Password generation
        generatePasswordButton = tk.Button(self, text='GENERATE PASSWORD', font=FONT, 
            command = self.generatePassword)\
            .grid(row=0, column=3, padx=padding, pady=padding)

        # Displaying password
        self.passwordDisplay = tk.Text(self, bg='light gray', width=50, height=1.5)
        self.passwordDisplay.grid(row=10,column=1,sticky='nsew', pady=50)
    
    def generatePassword(self):
        try:
            length = int(self.lengthInput.get())
            generate = True
        except ValueError:
            generate = False
            messagebox.showerror('Invalid Input!')

        if generate:
            if length <= 0:
                messagebox.showerror('Invalid Length!')
            else:
                lowerCase = string.ascii_lowercase
                upperCase = string.ascii_uppercase
                digits = string.digits
                specialChars = string.punctuation
                choice = [lowerCase,upperCase,digits,specialChars]

                password = ""
                for i in range(length):
                    randNum = random.randint(0,len(choice)-1)
                    character = choice[randNum]
                    randNum = random.randint(0,len(character)-1)
                    password += character[randNum]
                
                self.passwordDisplay.delete('1.0', tk.END)
                self.passwordDisplay.insert(tk.END,password)