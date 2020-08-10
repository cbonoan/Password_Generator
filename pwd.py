import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os

class SeaofBTCapp(tk.Tk):
    def __init__(self):
        
        tk.Tk.__init__(self)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (PasswordPage, GeneratorPage, VaultPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class PasswordPage():
    pass
class GeneratorPage():
    pass
class VaultPage():
    pass

def checkPwd(pwd):
    # Grabbing the last line of file which contains master password. 
    with open('masterPwd.txt', 'r') as file:
        for masterPwd in file:
            pass  

    if pwd == masterPwd:
        messagebox.showinfo("Password Input", "Correct!")
        menuFrame()
    else:
        messagebox.showinfo("Password Input", "Incorrect!")

if __name__ == "__main__":

    gui = Tk()
    gui.geometry('500x500')
    gui.title('Password Vault')
    gui.iconbitmap()
    gui.configure(bg='#81c6e3')

    '''
    field =  Entry(gui, bg='white', show="*")
    field.pack()
    field.focus_set()
   
    buttonEnter = Button(gui, text='Submit', command = lambda: checkPwd(field.get()))
    buttonEnter.pack()
    buttonEnter.focus_set()
    '''

    gui.mainloop()
    