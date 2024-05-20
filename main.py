from tkinter import *

window = Tk()
window.geometry("393x852")
window.title("MRGSports")

#navigationBar = Frame(window, bg="Orange", width=393,height=103)
#navigationBar.grid(row=8, column=0)

navigationBar = Frame(window, bg="Orange")
navigationBar.grid(row=8, columnexpand=)

homeButton = Button(navigationBar, width=46, height=46, bg="White", bd=10)
homeButton.grid(row=8, column=0, padx=40, pady=20)


window.mainloop()