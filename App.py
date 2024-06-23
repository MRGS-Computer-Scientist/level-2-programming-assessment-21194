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
        
        self.upcomingMain = Frame(self.homePage, width=w_width - margin_length, height=330, bg='Blue')
        self.upcomingMain.pack_propagate(False)
        self.upcomingMain.pack()
        
        self.upcomingText = Label(self.upcomingMain, text="UPCOMING", bg="#EFECEC", fg="#0C2D57", font=("Cairo", 16, "bold"))
        self.upcomingText.pack(padx=20, pady=5)
        
        # First upcoming display
        
        self.upcomingOne = Frame(self.upcomingMain, bg="Cyan", width=w_width - margin_length, height=70)
        self.upcomingOne.pack()
        
        self.upcomingBox1 = Frame(self.upcomingOne, bg="White", width=200, height=50, bd=3, relief=GROOVE)
        self.upcomingBox1.pack_propagate(False)
        self.upcomingBox1.pack(side=LEFT, padx=2.5, pady=3)
        
        self.upcomingGame1 = Label(self.upcomingBox1, text="Football Game")
        self.upcomingGame1.pack(padx=5,pady=5)

        self.upcomingTime1 = Frame(self.upcomingOne, bg="White", width=100, height=50, bd=3, relief=GROOVE)
        self.upcomingTime1.pack(side=RIGHT, padx=2.5, pady=3)        
        
        # Second upcoming display
        
        self.upcomingTwo = Frame(self.upcomingMain, bg="Green", width=w_width - margin_length, height=70)
        self.upcomingTwo.pack()
        
        self.upcomingBox2 = Frame(self.upcomingTwo, bg="White", width=200, height=50, bd=3, relief=GROOVE)
        self.upcomingBox2.pack_propagate(False)
        self.upcomingBox2.pack(side=LEFT, padx=2.5, pady=3)
        
        self.upcomingGame2 = Label(self.upcomingBox2, text="Basketball Game")
        self.upcomingGame2.pack(padx=5,pady=5)

        self.upcomingTime2 = Frame(self.upcomingTwo, bg="White", width=100, height=50, bd=3, relief=GROOVE)
        self.upcomingTime2.pack(side=RIGHT, padx=2.5, pady=3)      
        
        # Third upcoming display
        
        self.upcomingThree = Frame(self.upcomingMain, bg="Red", width=w_width - margin_length, height=70)
        self.upcomingThree.pack()
        
        self.upcomingBox3 = Frame(self.upcomingThree, bg="White", width=200, height=50, bd=3, relief=GROOVE)
        self.upcomingBox3.pack_propagate(False)
        self.upcomingBox3.pack(side=LEFT, padx=2.5, pady=3)
        
        self.upcomingGame3 = Label(self.upcomingBox3, text="Hockey Game")
        self.upcomingGame3.pack(padx=5,pady=5)

        self.upcomingTime3 = Frame(self.upcomingThree, bg="White", width=100, height=50, bd=3, relief=GROOVE)
        self.upcomingTime3.pack(side=RIGHT, padx=2.5, pady=3)

        # Fourth upcoming display
        
        self.upcomingFour = Frame(self.upcomingMain, bg="Brown", width=w_width - margin_length, height=70)
        self.upcomingFour.pack()
        
        self.upcomingBox4 = Frame(self.upcomingFour, bg="White", width=200, height=50, bd=3, relief=GROOVE)
        self.upcomingBox4.pack_propagate(False)
        self.upcomingBox4.pack(side=LEFT, padx=2.5, pady=3)
        
        self.upcomingGame4 = Label(self.upcomingBox4, text="Hockey Game")
        self.upcomingGame4.pack(padx=5,pady=5)

        self.upcomingTime4 = Frame(self.upcomingFour, bg="White", width=100, height=50, bd=3, relief=GROOVE)
        self.upcomingTime4.pack(side=RIGHT, padx=2.5, pady=3)

        # Fifth upcoming display
        
        self.upcomingFive = Frame(self.upcomingMain, bg="Brown", width=w_width - margin_length, height=70)
        self.upcomingFive.pack()
        
        self.upcomingBox5 = Frame(self.upcomingFive, bg="White", width=200, height=50, bd=3, relief=GROOVE)
        self.upcomingBox5.pack_propagate(False)
        self.upcomingBox5.pack(side=LEFT, padx=2.5, pady=3)
        
        self.upcomingGame5 = Label(self.upcomingBox5, text="Waterpolo Game")
        self.upcomingGame5.pack(padx=5,pady=5)

        self.upcomingTime5 = Frame(self.upcomingFive, bg="White", width=100, height=50, bd=3, relief=GROOVE)
        self.upcomingTime5.pack(side=RIGHT, padx=2.5, pady=3)
                            
        # End of upcoming/Start of res-this-week
        
        self.homeresuMain = Frame(self.homePage, width=w_width - margin_length, height=270, bg='Pink')
        self.homeresuMain.pack_propagate(False)
        self.homeresuMain.pack()
        
        self.homeresuText = Label(self.homeresuMain, text="RESULTS THIS WEEK", bg="#EFECEC", fg="#0C2D57", font=("Cairo", 16, "bold"))
        self.homeresuText.pack(padx=20, pady=5)
        
        self.homeresuBox = Frame(self.homeresuMain, bg="White", width=305, height=190, bd=3, relief=GROOVE)
        self.homeresuBox.pack_propagate(False)
        self.homeresuBox.pack(padx=5, pady=3)        
        
        self.homeresuB1 = Frame(self.homeresuBox, width=305, height=26, bg="Blue")
        self.homeresuB1.pack_propagate(False)
        self.homeresuB1.pack()
        
        self.homeresuB2 = Frame(self.homeresuBox, width=305, height=46, bg="Green")
        self.homeresuB2.pack_propagate(False)
        self.homeresuB2.pack()
        
        self.homeresuB3 = Frame(self.homeresuBox, width=305, height=46, bg="Yellow")
        self.homeresuB3.pack_propagate(False)
        self.homeresuB3.pack()
        
        self.homeresuB4 = Frame(self.homeresuBox, width=305, height=46, bg="Red")
        self.homeresuB4.pack_propagate(False)
        self.homeresuB4.pack()
        
        self.homeresuB5 = Frame(self.homeresuBox, width=305, height=26, bg="Orange")
        self.homeresuB5.pack_propagate(False)
        self.homeresuB5.pack()
        
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