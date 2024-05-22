from tkinter import *

window = Tk()
window.geometry("393x852")
window.title("MRGSports")

w_width = 393
w_height = 852 #-whatever is the value for nav bar

#navigationBar = Frame(window, bg="Orange", width=393,height=103)
#navigationBar.grid(row=8, column=0)

logoFrame = Frame(window, background="Orange", width=w_width, height=100)
logoFrame.grid(row=0, column=0)

contentFrame = Frame(window, background="White", width=w_width, height=600)
contentFrame.grid(row=1, column=0)

navigationBar = Frame(window, bg="Orange", width=w_width, height=152)
navigationBar.grid(row=2, column=0)

navigationButtons = Frame(navigationBar, bg="Orange", width=w_width, height=152)
navigationBar.grid()

homeButton = Button(navigationButtons, text="Home", bg="White", bd=1, width=10)
homeButton.grid(row=0, column=0)

ResuButton = Button(navigationButtons, text="Resu", bg="White", bd=1, width=10)
ResuButton.grid(row=0, column=1)

StatButton = Button(navigationButtons, text="Stat", bg="White", bd=1, width=10)
StatButton.grid(row=0, column=3)

LeadButton = Button(navigationButtons, text="Lead", bg="White", bd=1, width=10)
LeadButton.grid(row=0, column=4)

window.mainloop()