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
        self.logoFrame.grid_propagate(False)
        self.logoFrame.grid(row=0, column=0)

        #logo text test
        
        self.logoText = Label(self.logoFrame, text="MRGSports")
        self.logoText.grid(row=0, column=0, pady=40, rowspan=1)
        #self.logoText.pack()

        #content frame

        self.contentFrame = Frame(self.window, background="White", width=393, height=600)
        
        self.contentFrame.grid(row=1, column=0)
        
        #home page frame
        
        self.homePage = Frame(self.contentFrame, background="White", width=393, height=600)
        
        #stat page frame
        
        self.homePage = Frame(self.contentFrame, background="White", width=393, height=600)        
        
        #resu page frame
        
        self.homePage = Frame(self.contentFrame, background="White", width=393, height=600)
        
        #navigation bar

        self.navigationBar = Frame(self.window, bg="Orange", width=393, height=152)
        self.navigationBar.grid_propagate(False)
        self.navigationBar.grid(row=2, column=0)

        #placing buttons on nav bar

        #self.exampleButton = Button(self.navigationBar, text="Example Button")
        #self.exampleButton.grid(row=0,column=0)
        
        self.homeButton = Button(self.navigationBar, text="Home", bg="White", width=7, command=self.goToHome)
        self.homeButton.grid(row=0,column=0,)

        self.ResuButton = Button(self.navigationBar, text="Resu", bg="White", width=7)
        self.ResuButton.grid(row=0, column=1,padx=19,pady=65)

        self.StatButton = Button(self.navigationBar, text="Stat", bg="White", width=7)
        self.StatButton.grid(row=0, column=2,padx=19,pady=65)

        self.LeadButton = Button(self.navigationBar, text="Lead", bg="White", width=7)
        self.LeadButton.grid(row=0, column=3,padx=19,pady=65)
        
        self.window.mainloop()
        
    def goToHome(self):
            