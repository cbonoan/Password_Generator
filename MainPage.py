import tkinter as tk
from tkinter import *
from tkinter import messagebox
import string
import random
import database
from VaultPage import VaultPage
import os 

FONT= ('System', 12)
padding = 10

lowerCase = string.ascii_lowercase
upperCase = string.ascii_uppercase
digits = string.digits
specialChars =  '!@#$%^&*()'
class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        self.conn =database.createConnection() # Create sqlite3 db in order to save password

        tk.Frame.__init__(self,parent)

        # Ask user how long pthey want password to be
        tk.Label(self, text='How long should password be?', font=FONT).grid(row=0, sticky='nsw',pady=padding)
        self.lengthInput = tk.Spinbox(self, bg='light gray', from_=1, to=100)
        self.lengthInput.grid(row=1,column=0, sticky='nsew')
        tk.Label(self, text='Where will this password be used? (Optional)', font=FONT).grid(row=2, sticky='nsw',pady=padding)
        self.pwdDestUse = tk.Entry(self, bg='light gray')
        self.pwdDestUse.grid(row=3,column=0, sticky='nsew')
        
        # Check which symbols and characters to include into password
        Label(self, text='Check which symbols and charcters to include into your password:', font=FONT).grid(row=4,column=0)
        self.chars1 = tk.IntVar()
        self.chars2 = tk.IntVar()
        self.chars3 = tk.IntVar()
        self.chars4 = tk.IntVar()
        self.charactersToInsert = [] # Will use in generatePassword() 
        Checkbutton(self, text=lowerCase, variable=self.chars1).grid(row=5, column=0, sticky='nsw')
        Checkbutton(self, text=upperCase, variable=self.chars2).grid(row=6, column=0, sticky='nsw')
        Checkbutton(self, text=digits, variable=self.chars3).grid(row=7, column=0, sticky='nsw')
        Checkbutton(self, text=specialChars, variable=self.chars4).grid(row=8, column=0, sticky='nsw')

        # Password generation
        generatePasswordButton = tk.Button(self, text='GENERATE PASSWORD', font=FONT, 
            command = self.generatePassword)\
            .grid(row=9, column=0, padx=padding, pady=padding)

        # Displaying password
        self.passwordDisplay = tk.Text(self, bg='light gray', width=50, height=1.5)
        self.passwordDisplay.grid(row=10,column=0,sticky='nsew', pady=10)

        savePwd = tk.Button(self, text='Save Password', font=FONT, command= self.savePassword).grid(row=11, column=0, sticky='nsew', pady=padding)
        goToVaultPage = tk.Button(self, text='Password Vault', font=FONT, command=lambda: controller.show_frame(VaultPage)).grid(row=12, column=0, sticky='nsew', pady=padding)

    def savePassword():
        pass

    def generatePassword(self):
        try:
            length = int(self.lengthInput.get())
            generate = True
        except ValueError:
            generate = False
            messagebox.showerror('Value Error','Invalid Input!')

        if generate:
            if length <= 0:
                messagebox.showerror('Length Error','Invalid Length!')
            else:
                choice = []
                if self.chars1.get() == 1:
                    choice.append(lowerCase)
                if self.chars2.get() == 1:
                    choice.append(upperCase)
                if self.chars3.get() == 1:
                    choice.append(digits)
                if self.chars4.get() == 1:
                    choice.append(specialChars)

                password = ""
                for i in range(length):
                    randNum = random.randint(0,len(choice)-1)
                    character = choice[randNum]
                    randNum = random.randint(0,len(character)-1)
                    password += character[randNum]
                
                self.passwordDisplay.delete('1.0', tk.END)
                self.passwordDisplay.insert(tk.END,password)