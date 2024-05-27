from tkinter import *
from app_settings import *
from os import *

class App():
    
    
    
    def __init__(self):
        
        
        self.window = Tk()
        self.window.geometry("393x852")
        self.window.title("MRGSports")

        #logo frame

        self.logoFrame = Frame(self.window, background="Orange", width=393, height=100)
        
        self.logoFrame.grid(row=0, column=0)

        #content frame

        self.contentFrame = Frame(self.window, background="White", width=393, height=600)
        
        self.contentFrame.grid(row=1, column=0)

        #navigation bar

        self.navigationBar = Frame(self.window, bg="Orange", width=393, height=152)
        
        self.navigationBar.grid(row=2, column=0)

        #placing buttons on nav bar

        self.exampleButton = Button(self.navigationBar, text="Example Button")
        
        self.exampleButton.grid(row=0, column=0)
        
           
        self.window.mainloop()
        
        
        
        
        
        #self.homeButton = Button(self.navigationBar, text="Home", bg="White")
        #self.homeButton.grid(row=0,column=0)

        #self.ResuButton = Button(self.navigationBar, text="Resu", bg="White", )
        #self.ResuButton.grid(row=0, column=1)

        #self.StatButton = Button(self.navigationBar, text="Stat", bg="White", )
        #self.StatButton.grid(row=0, column=2)

        #self.LeadButton = Button(self.navigationBar, text="Lead", bg="White", )
        #self.LeadButton.grid(row=0, column=3)