from tkinter import *
from app_settings import *
from os import *

w_width = 400
w_height = 850 
margin_length = 30

class App():
    
    def __init__(self):
        self.window = Tk()
        self.window.geometry((str(w_width)) + "x" + (str(w_height)))
        self.window.title("MRGSports")

        #logo frame

        self.logoFrame = Frame(self.window, background="#FC6736", width=w_width, height=100)
        self.logoFrame.pack_propagate(False)
        self.logoFrame.grid(row=0, column=0)

        #logo text test
        
        self.logoText = Label(self.logoFrame, text="MRGSports", bg="#FC6736", fg="White")
        self.logoText.pack(pady=40)

        #content frame

        self.contentFrame = Frame(self.window, background="Black", width=w_width, height=600)
        self.contentFrame.grid_propagate(False)
        self.contentFrame.grid(row=1, column=0)
        
        #home page frame
        
        self.homePage = Frame(self.contentFrame, background="#EFECEC", width=w_width, height=600)
        self.homePage.pack_propagate(False)
        self.homePage.grid_propagate(False)
        self.homePage.grid(rowspan=TRUE, columnspan=TRUE)

        #upcomings
        
        self.upcomingMain = Frame(self.homePage, width=w_width - margin_length, height=350, bg='Blue')
        self.upcomingMain.pack_propagate(False)
        self.upcomingMain.pack()
        
        self.upcomingText = Label(self.upcomingMain, text="UPCOMING", bg="#EFECEC", fg="#0C2D57", font=("Cairo", 16, "bold"))
        self.upcomingText.pack(padx=20, pady=5)
        
        #box 1
        
        self.upcomingBox1 = Frame(self.upcomingMain, bg="White", width=185, height=50, bd=3, relief=GROOVE)
        self.upcomingBox1.pack_propagate(False)
        self.upcomingBox1.pack(side=LEFT, padx=2.5, pady=3)
        
        self.upcomingGame1 = Label(self.upcomingBox1, text="Football Game")
        self.upcomingGame1.pack(padx=5,pady=5)

        self.upcomingTime1 = Frame(self.upcomingMain, bg="White", width=95, height=50, bd=3, relief=GROOVE)
        self.upcomingTime1.pack(side=RIGHT, padx=2.5, pady=3)        

        #box 2
        
#        self.upcomingBox2 = Frame(self.homePage, bg="White", width=185, height=50, bd=3, relief=GROOVE)
 #       self.upcomingBox2.grid(row=2,column=0, padx=2.5, pady=3)
#
 #       self.upcomingTime2 = Frame(self.homePage, bg="White", width=95, height=50, bd=3, relief=GROOVE)
  #      self.upcomingTime2.grid(row=2,column=1, padx=2.5, pady=3)
#
 #       #box 3
#
 #       self.upcomingBox3 = Frame(self.homePage, bg="White", width=185, height=50, bd=3, relief=GROOVE)
  #      self.upcomingBox3.grid(row=3,column=0, padx=2.5, pady=3)
#
 #       self.upcomingTime3 = Frame(self.homePage, bg="White", width=95, height=50, bd=3, relief=GROOVE)
  #      self.upcomingTime3.grid(row=3,column=1, padx=2.5, pady=3)
#
 #       #box 4
#
 #       self.upcomingBox4 = Frame(self.homePage, bg="White", width=185, height=50, bd=3, relief=GROOVE)
  #      self.upcomingBox4.grid(row=4,column=0, padx=2.5, pady=3)
#
 #       self.upcomingTime4 = Frame(self.homePage, bg="White", width=95, height=50, bd=3, relief=GROOVE)
  #      self.upcomingTime4.grid(row=4,column=1, padx=2.5, pady=3)
        
        #results this week
        
#        self.homeLabel2 = Label(self.homePage, text="RESULTS THIS WEEK", bg="#EFECEC", fg="#0C2D57", font=("Cairo", 16, "bold"))
 #       self.homeLabel2.grid(row=5, columnspan=TRUE, sticky=W, padx=20, pady=6)
  #      
   #     self.hResuBox1 = Frame(self.homePage, bg="White", width=285, height=240, bd=3, relief=GROOVE)
    #    self.hResuBox1.grid(row=6,column=0, padx=2.5, pady=3)        
        
        #stat page frame
        
        self.statPage = Frame(self.contentFrame, background="Red", width=w_width, height=600)        
        self.statPage.grid_propagate(False)

        #resu page frame
        
        self.resuPage = Frame(self.contentFrame, background="Purple", width=w_width, height=600)
        self.resuPage.grid_propagate(False)
        #lead page frame
        
        self.leadPage = Frame(self.contentFrame, background="Green", width=w_width, height=600)        
        self.leadPage.grid_propagate(False)
        #navigation bar

        self.navigationBar = Frame(self.window, bg="#FC6736", width=w_width, height=150)
        self.navigationBar.grid_propagate(False)
        self.navigationBar.grid(row=2, column=0)

        #placing buttons on nav bar

        #self.exampleButton = Button(self.navigationBar, text="Example Button")
        #self.exampleButton.grid(row=0,column=0)
        
        self.homeButton = Button(self.navigationBar, text="Home", bg="White", width=7, command=self.goToHome)
        self.homeButton.grid(row=0,column=0,)

        self.ResuButton = Button(self.navigationBar, text="Resu", bg="White", width=7, command=self.goToResu)
        self.ResuButton.grid(row=0, column=1,padx=19,pady=65)

        self.StatButton = Button(self.navigationBar, text="Stat", bg="White", width=7, command=self.goToStat)
        self.StatButton.grid(row=0, column=2,padx=19,pady=65)

        self.LeadButton = Button(self.navigationBar, text="Lead", bg="White", width=7, command=self.goToLead)
        self.LeadButton.grid(row=0, column=3,padx=19,pady=65)
        
        self.window.mainloop()
        
    def goToHome(self):
        self.resuPage.grid_forget()
        self.statPage.grid_forget()
        self.leadPage.grid_forget()
        self.homePage.grid(rowspan=TRUE, columnspan=TRUE)
        
    def goToResu(self):
        self.statPage.grid_forget()
        self.leadPage.grid_forget()
        self.homePage.grid_forget()
        self.resuPage.grid(rowspan=TRUE, columnspan=TRUE)
 
    def goToStat(self):
        self.resuPage.grid_forget()
        self.leadPage.grid_forget()
        self.homePage.grid_forget()
        self.statPage.grid(rowspan=TRUE, columnspan=TRUE)       
        
    def goToLead(self):
        self.resuPage.grid_forget()
        self.statPage.grid_forget()
        self.homePage.grid_forget()
        self.leadPage.grid(rowspan=TRUE, columnspan=TRUE)       