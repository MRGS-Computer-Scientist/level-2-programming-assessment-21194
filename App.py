from tkinter import *
from app_settings import *
from os import *

w_width = 400
w_height = 850 
margin_length = 30



#leftarrow = PhotoImage(file = "C:\Users\21194\Downloads\683398_arrows_512x512.png")

class App():
    
    
    
    def __init__(self):
        self.window = Tk()
        self.window.geometry((str(w_width)) + "x" + (str(w_height)))
        self.window.title("MRGSports")
        
        self.page_number = 1
        self.max_page_numbers = 4

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
        self.upcomingTime1.pack_propagate(False)
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
        self.upcomingTime2.pack_propagate(False)
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
        self.upcomingTime3.pack_propagate(False)
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
        self.upcomingTime4.pack_propagate(False)
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
        self.upcomingTime5.pack_propagate(False)
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
        
        # First page (no L/R button press)
        # Top
        
        self.homeresuL1 = Frame(self.homeresuBox, width=305, height=29, bg="Blue")
        self.homeresuL1.pack_propagate(False)
        self.homeresuL1.grid_propagate(False)
        self.homeresuL1.grid(row=0,column=0)
        
        self.homeresuLL = Frame(self.homeresuL1, width=152.5, height=29, bg="Grey")
        self.homeresuLL.pack_propagate(False)        
        self.homeresuLL.pack(side=LEFT)
        
        self.homeresuTEST = Label(self.homeresuLL, text="Basketball")
        self.homeresuTEST.pack()
        
        # code for which page is shown on the top right, 
        
        self.homeresuLR = Frame(self.homeresuL1, width=152.5, height=29, bg="Black")
        self.homeresuLR.pack_propagate(False)        
        self.homeresuLR.pack(side=RIGHT)
        
        self.leftarrowbutton = Button(self.homeresuLR, text="Left", command=lambda: self.go_to_next_page("left"))
        self.leftarrowbutton.pack(side=LEFT)
        
        self.rightarrowbutton = Button(self.homeresuLR, text="Right", command=lambda: self.go_to_next_page("right"))
        self.rightarrowbutton.pack(side=LEFT)
        
        self.pagenumber = Label(self.homeresuLR, text=self.page_number)
        self.pagenumber.pack(side=RIGHT)

        

        
        # Middle
        
        self.homeresuB1 = Frame(self.homeresuBox, bg="Cyan", width=305, height=135)
        self.homeresuB1.pack_propagate(False)
        self.homeresuB1.grid_propagate(False)        
        self.homeresuB1.grid(row=1, columnspan=TRUE)

                                
        self.homeresuB1L2 = Frame(self.homeresuB1, width=305, height=45, bg="Green")
        self.homeresuB1L2.pack_propagate(False)
        self.homeresuB1L2.pack()
        
        # sub the First XI for first_team and second which is a string variable decided by the user input on teacher page
        
        self.resuTeam1 = Label(self.homeresuB1L2, text="First XI")
        self.resuTeam1.pack(side=LEFT, padx=25)
        
        self.resuScore1 = Label(self.homeresuB1L2, text="160")
        self.resuScore1.pack(side=LEFT, padx=5)
        
        self.resuTeam2 = Label(self.homeresuB1L2, text="First XI")
        self.resuTeam2.pack(side=RIGHT, padx=25)
        
        self.resuScore2 = Label(self.homeresuB1L2, text="70")
        self.resuScore2.pack(side=RIGHT, padx=5)
    
    
        self.homeresuB1L3 = Frame(self.homeresuB1, width=305, height=45, bg="Yellow")
        self.homeresuB1L3.pack_propagate(False)
        self.homeresuB1L3.pack()
        
        self.resuTeam3 = Label(self.homeresuB1L3, text="Second XI")
        self.resuTeam3.pack(side=LEFT, padx=25)
        
        self.resuScore3 = Label(self.homeresuB1L3, text="160")
        self.resuScore3.pack(side=LEFT, padx=5)
        
        self.resuTeam4 = Label(self.homeresuB1L3, text="Second XI")
        self.resuTeam4.pack(side=RIGHT, padx=25)
        
        self.resuScore4 = Label(self.homeresuB1L3, text="70")
        self.resuScore4.pack(side=RIGHT, padx=5)
        
        
        self.homeresuB1L4 = Frame(self.homeresuB1, width=305, height=45, bg="Red")
        self.homeresuB1L4.pack_propagate(False)
        self.homeresuB1L4.pack()
        
        self.resuTeam5 = Label(self.homeresuB1L4, text="Junior")
        self.resuTeam5.pack(side=LEFT, padx=25)
        
        self.resuScore5 = Label(self.homeresuB1L4, text="160")
        self.resuScore5.pack(side=LEFT, padx=5)
        
        self.resuTeam6 = Label(self.homeresuB1L4, text="Junior")
        self.resuTeam6.pack(side=RIGHT, padx=25)
        
        self.resuScore6 = Label(self.homeresuB1L4, text="70")
        self.resuScore6.pack(side=RIGHT, padx=5)
        
        # Second page (1st R button press)
        
        self.homeresuB2 = Frame(self.homeresuBox, bg="Cyan", width=305, height=135)
        self.homeresuB2.pack_propagate(False)
        self.homeresuB2.grid_propagate(False)
        # This needs to be said on the button press somehow == self.homeresuB2.grid(row=1,columnspan=TRUE)
        
        self.homeresuB3 = Frame(self.homeresuBox, bg="Blue", width=305, height=135)
        self.homeresuB3.pack_propagate(False)
        self.homeresuB3.grid_propagate(False)

        self.homeresuB4 = Frame(self.homeresuBox, bg="Red", width=305, height=135)
        self.homeresuB4.pack_propagate(False)
        self.homeresuB4.grid_propagate(False)

        # Home resu page indicator
        
        self.homeresuL5 = Frame(self.homeresuBox, width=305, height=26, bg="Orange")  
        self.homeresuL5.pack_propagate(False)
        self.homeresuL5.grid_propagate(False)
        self.homeresuL5.grid(row=2,columnspan=TRUE)
        
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
     
     
    def go_to_next_page(self, direction):
        if direction == "left":
            if self.page_number > 1:
                 self.page_number -= 1
            elif self.page_number <= 1:
                self.page_number = self.max_page_numbers
        elif direction == "right":
            if self.page_number < self.max_page_numbers:
                 self.page_number += 1
            elif self.page_number >= self.max_page_numbers:
                self.page_number = 1
                
        self.pagenumber.config(text=self.page_number)
        
        self.change_resu_page()
        
    def goToHome(self):
        self.resuPage.grid_remove()
        self.statPage.grid_remove()
        self.leadPage.grid_remove()
        self.homePage.grid(rowspan=TRUE, columnspan=TRUE)
        
    def goToResu(self):
        self.statPage.grid_remove()
        self.leadPage.grid_remove()
        self.homePage.grid_remove()
        self.resuPage.grid(rowspan=TRUE, columnspan=TRUE)
 
    def goToStat(self):
        self.resuPage.grid_remove()
        self.leadPage.grid_remove()
        self.homePage.grid_remove()
        self.statPage.grid(rowspan=TRUE, columnspan=TRUE)       
        
    def goToLead(self):
        self.resuPage.grid_remove()
        self.statPage.grid_remove()
        self.homePage.grid_remove()
        self.leadPage.grid(rowspan=TRUE, columnspan=TRUE)
           
    def change_resu_page(self):
        # Update visibility of each page
        self.homeresuB1.grid_remove()
        self.homeresuB2.grid_remove()
        self.homeresuB3.grid_remove()
        self.homeresuB4.grid_remove()

        if self.page_number == 1:
            self.homeresuB1.grid(row=1, columnspan=TRUE)
        elif self.page_number == 2:
            self.homeresuB2.grid(row=1, columnspan=TRUE)
        elif self.page_number == 3:
            self.homeresuB3.grid(row=1, columnspan=TRUE)
        elif self.page_number == 4:
            self.homeresuB4.grid(row=1, columnspan=TRUE)