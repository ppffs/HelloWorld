#!/usr/bin/python
# Filename : firstWindow.py

import Tkinter
from Tkinter import *
from multiprocessing import Process, Pipe

class Login:
    def __init__(self, master, con=""):
        self.con = con
        self.parent = master
        self.username = ""
        self.password = ""
        master.protocol("WM_DELETE_WINDOW", self.cancel)
        self.__layout__(master)

    def __layout__(self, master):
        master.geometry("320x150+400+100")
        master.title("Window")
        
        row1 = Frame(master)
        row1.pack(padx=10, pady=15)
        Label(row1, width=8, text="User:", anchor=W).pack(side=LEFT)
        self.en_user = Entry(row1)
        self.en_user.pack(side=LEFT)

        row2 = Frame(master)
        row2.pack(padx=10, pady=15)
        Label(row2, width=8, text="Password:", anchor=W).pack(side=LEFT)
        self.en_pswd = Entry(row2)
        self.en_pswd.pack(side=LEFT)

        row3 = Frame(master)
        row3.pack(padx=10, pady=15)
        Button(row3, text="Ok", width=10, command=self.ok).pack(side=LEFT,padx=5)
        Button(row3, text="Cancel", width=10, command=self.cancel).pack(side=LEFT,padx=5)

    def ok(self):
        pass

    def cancel(self):
        pass          

if __name__ == "__main__":
    root = Tk()
    main = Login(root)
    root.mainloop()


