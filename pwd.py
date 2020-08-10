#! python3

from tkinter import *
from tkinter import messagebox
import os

def menuWindow():
    pass

def checkPwd(pwd):
    # Grabbing the last line of file which contains master password. 
    with open('masterPwd.txt', 'r') as file:
        for masterPwd in file:
            pass  

    if pwd == masterPwd:
        messagebox.showinfo("Password Input", "Correct!")
        menuWindow()
    else:
        messagebox.showinfo("Password Input", "Incorrect!")
          

if __name__ == "__main__":
    
    gui = Tk()
    gui.geometry('500x500')
    gui.title('Password Vault')
    gui.configure(bg='#81c6e3')
    

    field =  Entry(gui, bg='white', show="*")
    field.pack()
    field.focus_set()
   
    buttonEnter = Button(gui, text='Submit', command = lambda: checkPwd(field.get()))
    buttonEnter.pack()
    buttonEnter.focus_set()
    

    gui.mainloop()