from tkinter import *

class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.pack()
        self.master.title("Hello World")
        Label(self , text = "This is my first GUI").pack()
        self.master.geometry("200x200")
        self.master.resizable(False,False) # Do not allow to resize in X and Y axis



root = Tk()
app = Application(root)
app.mainloop()
