#! python3

from tkinter import *
from tkinter import messagebox
import os

def menuWindow():
    pass

def checkPwd(pwd):
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'masterPwd.txt')
    f = open(my_file, "r")
    if f.mode == "r":
        masterPwd = f.read()
    
    if pwd == masterPwd:
        messagebox.showinfo("Password Input", "Correct!")
        menuWindow()        
    else:
        messagebox.showinfo("Password Input", "Incorrect!")
        return False        

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