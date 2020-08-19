import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
from MainPage import MainPage
from VaultPage import VaultPage
class Window(tk.Tk):
    # Credits to sentdex on Youtube for implementation of 
    # frame switching in Tkinter
    '''
    Create all needed pages for application, and the one that needs 
    to be shown will "raise" to the top of all the other frames
    '''
    def __init__(self):
        
        tk.Tk.__init__(self)
        container = tk.Frame(self)
        
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        '''
        frame = MainPage(container,self)
        self.frames[MainPage] = frame
        frame.grid(row=0,column=0, sticky="nsew")
        '''
        
        for F in (MainPage, VaultPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class GeneratorPage():
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
    gui = Window()
    gui.geometry('+500+200')
    gui.mainloop()
    