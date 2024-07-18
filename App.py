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

        self.logo_frame = Frame(self.window, background="#FC6736", width=w_width, height=100)
        self.logo_frame.pack_propagate(False)
        self.logo_frame.grid(row=0, column=0)

        #logo text test
        
        self.logo_text = Label(self.logo_frame, text="MRGSports", bg="#FC6736", fg="White")
        self.logo_text.pack(pady=40)

        #content frame

        self.content_frame = Frame(self.window, background="Black", width=w_width, height=600)
        self.content_frame.grid_propagate(False)
        self.content_frame.grid(row=1, column=0)
        
        #home page frame
        
        self.home_page = Frame(self.content_frame, background="#EFECEC", width=w_width, height=600)
        self.home_page.pack_propagate(False)
        self.home_page.grid_propagate(False)
        self.home_page.grid(rowspan=TRUE, columnspan=TRUE)

        #upcomings
        
        self.upcoming_main = Frame(self.home_page, width=w_width - margin_length, height=330, bg='Blue')
        self.upcoming_main.pack_propagate(False)
        self.upcoming_main.pack()
        
        self.home_header_one = Label(self.upcoming_main, text="UPCOMING", bg="#EFECEC", fg="#0C2D57", font=("Cairo", 16, "bold"))
        self.home_header_one.pack(padx=20, pady=5)
        
        # First upcoming display, it is split up into 5 rows called one, two, three, four, and five which show the most relevant and most imminent sport match for the school (the dictionary created for upcoming matches will be here and separate to results)
        
        self.upcoming_row_one = Frame(self.upcoming_main, bg="Cyan", width=w_width - margin_length, height=70)
        self.upcoming_row_one.pack()
        
        self.upcoming_box_game = Frame(self.upcoming_row_one, bg="White", width=200, height=50, bd=3, relief=GROOVE)
        self.upcoming_box_game.pack_propagate(False)
        self.upcoming_box_game.pack(side=LEFT, padx=2.5, pady=3)
        
        self.upcoming_game_one = Label(self.upcoming_box_game, text="Football Game")
        self.upcoming_game_one.pack(padx=5,pady=5)

        self.upcoming_box_time = Frame(self.upcoming_row_one, bg="White", width=100, height=50, bd=3, relief=GROOVE)
        self.upcoming_box_time.pack_propagate(False)
        self.upcoming_box_time.pack(side=RIGHT, padx=2.5, pady=3)        
        
        self.upcoming_day_one = Label(self.upcoming_box_time, text="Wednesday")
        self.upcoming_day_one.pack()
        
        self.upcoming_time_one = Label(self.upcoming_box_time, text="15:30")
        self.upcoming_time_one.pack()
        
        # Second upcoming display
        
        self.upcoming_row_two = Frame(self.upcoming_main, bg="Green", width=w_width - margin_length, height=70)
        self.upcoming_row_two.pack()
        
        self.upcoming_box_game2 = Frame(self.upcoming_row_two, bg="White", width=200, height=50, bd=3, relief=GROOVE)
        self.upcoming_box_game2.pack_propagate(False)
        self.upcoming_box_game2.pack(side=LEFT, padx=2.5, pady=3)
        
        self.upcoming_game_two = Label(self.upcoming_box_game2, text="Basketball Game")
        self.upcoming_game_two.pack(padx=5,pady=5)

        self.upcoming_box_time2 = Frame(self.upcoming_row_two, bg="White", width=100, height=50, bd=3, relief=GROOVE)
        self.upcoming_box_time2.pack_propagate(False)
        self.upcoming_box_time2.pack(side=RIGHT, padx=2.5, pady=3)      

        self.upcoming_day_two = Label(self.upcoming_box_time2, text="Tuesday")
        self.upcoming_day_two.pack()
        
        self.upcoming_time_two = Label(self.upcoming_box_time2, text="11:56")
        self.upcoming_time_two.pack()
                
        # Third upcoming display
        
        self.upcoming_row_three = Frame(self.upcoming_main, bg="Red", width=w_width - margin_length, height=70)
        self.upcoming_row_three.pack()
        
        self.upcoming_box_game3 = Frame(self.upcoming_row_three, bg="White", width=200, height=50, bd=3, relief=GROOVE)
        self.upcoming_box_game3.pack_propagate(False)
        self.upcoming_box_game3.pack(side=LEFT, padx=2.5, pady=3)
        
        self.upcoming_game_three = Label(self.upcoming_box_game3, text="Volleyball Game")
        self.upcoming_game_three.pack(padx=5,pady=5)

        self.upcoming_box_time3 = Frame(self.upcoming_row_three, bg="White", width=100, height=50, bd=3, relief=GROOVE)
        self.upcoming_box_time3.pack_propagate(False)
        self.upcoming_box_time3.pack(side=RIGHT, padx=2.5, pady=3)

        self.upcoming_day_three = Label(self.upcoming_box_time3, text="Monday")
        self.upcoming_day_three.pack()
        
        self.upcoming_time_three = Label(self.upcoming_box_time3, text="8:17")
        self.upcoming_time_three.pack()
                
        # Fourth upcoming display
        
        self.upcoming_row_four = Frame(self.upcoming_main, bg="Brown", width=w_width - margin_length, height=70)
        self.upcoming_row_four.pack()
        
        self.upcoming_box_game4 = Frame(self.upcoming_row_four, bg="White", width=200, height=50, bd=3, relief=GROOVE)
        self.upcoming_box_game4.pack_propagate(False)
        self.upcoming_box_game4.pack(side=LEFT, padx=2.5, pady=3)
        
        self.upcoming_game_four = Label(self.upcoming_box_game4, text="Hockey Game")
        self.upcoming_game_four.pack(padx=5,pady=5)

        self.upcoming_box_time4 = Frame(self.upcoming_row_four, bg="White", width=100, height=50, bd=3, relief=GROOVE)
        self.upcoming_box_time4.pack_propagate(False)
        self.upcoming_box_time4.pack(side=RIGHT, padx=2.5, pady=3)

        self.upcoming_day_four = Label(self.upcoming_box_time4, text="Friday")
        self.upcoming_day_four.pack()
        
        self.upcoming_time_four = Label(self.upcoming_box_time4, text="19:20")
        self.upcoming_time_four.pack()
                
        # Fifth upcoming display
        
        self.upcoming_row_five = Frame(self.upcoming_main, bg="Brown", width=w_width - margin_length, height=70)
        self.upcoming_row_five.pack()
        
        self.upcoming_box_game5 = Frame(self.upcoming_row_five, bg="White", width=200, height=50, bd=3, relief=GROOVE)
        self.upcoming_box_game5.pack_propagate(False)
        self.upcoming_box_game5.pack(side=LEFT, padx=2.5, pady=3)
        
        self.upcoming_game_five = Label(self.upcoming_box_game5, text="Waterpolo Game")
        self.upcoming_game_five.pack(padx=5,pady=5)

        self.upcoming_box_time5 = Frame(self.upcoming_row_five, bg="White", width=100, height=50, bd=3, relief=GROOVE)
        self.upcoming_box_time5.pack_propagate(False)
        self.upcoming_box_time5.pack(side=RIGHT, padx=2.5, pady=3)

        self.upcoming_day_five = Label(self.upcoming_box_time5, text="Thursday")
        self.upcoming_day_five.pack()
        
        self.upcoming_time_five = Label(self.upcoming_box_time5, text="14:15")
        self.upcoming_time_five.pack()
                                            
        # End of upcoming/Start of res-this-week
        
        self.homeresu_main = Frame(self.home_page, width=w_width - margin_length, height=270, bg='Pink')
        self.homeresu_main.pack_propagate(False)
        self.homeresu_main.pack()
        
        self.home_header_two = Label(self.homeresu_main, text="LATEST RESULTS", bg="#EFECEC", fg="#0C2D57", font=("Cairo", 16, "bold"))
        self.home_header_two.pack(padx=20, pady=5)
        
        self.homeresu_box = Frame(self.homeresu_main, bg="White", width=305, height=190, bd=3, relief=GROOVE)
        self.homeresu_box.pack_propagate(False)
        self.homeresu_box.pack(padx=5, pady=3)        
        
        # First resu page (no L/R button press)
        # Top is split into two parts "Left top" and "Right top"
        
        self.homeresu_top = Frame(self.homeresu_box, width=305, height=29, bg="Blue")
        self.homeresu_top.pack_propagate(False)
        self.homeresu_top.grid_propagate(False)
        self.homeresu_top.grid(row=0,column=0)
        
        self.homeresu_topLeft = Frame(self.homeresu_top, width=152.5, height=29, bg="Grey")
        self.homeresu_topLeft.pack_propagate(False)        
        self.homeresu_topLeft.pack(side=LEFT)
        
        self.homeresu_sportname = Label(self.homeresu_topLeft, text="Football")
        self.homeresu_sportname.pack(side=LEFT, padx=10, pady=5)
        
        self.homeresu_topRight = Frame(self.homeresu_top, width=152.5, height=29, bg="Black")
        self.homeresu_topRight.pack_propagate(False)        
        self.homeresu_topRight.pack(side=RIGHT)
         
        self.home_right_button = Button(self.homeresu_topRight, text="Right", command=lambda: self.go_to_next_page("right"))
        self.home_right_button.pack(side=RIGHT, padx=1, pady=1)
       
        self.home_left_button = Button(self.homeresu_topRight, text="Left", command=lambda: self.go_to_next_page("left"))
        self.home_left_button.pack(side=RIGHT, padx=1, pady=1)
        
        # Middle of homeresu, this is what changes on the button press containing the actual results
        # Home results page one
        
        self.homeresu_pageOne = Frame(self.homeresu_box, bg="Cyan", width=305, height=135)
        self.homeresu_pageOne.pack_propagate(False)
        self.homeresu_pageOne.grid_propagate(False)        
        self.homeresu_pageOne.grid(row=1, columnspan=TRUE)

        # Divide the pages into 3 lines with each match
                                
        self.homeresu_pageOne_L1 = Frame(self.homeresu_pageOne, width=305, height=45, bg="Green")
        self.homeresu_pageOne_L1.pack_propagate(False)
        self.homeresu_pageOne_L1.pack()
        
        # Sub the First XI for first_team and second which is a string variable decided by the user input on teacher page
        
        # Divide the lines into 4 sections, 1 = MRGS TEAM, 2 = MRGS SCORE, 3 = OTHER SCORE, 4 = OTHER TEAM
        
        self.homeresu_pageOne_L1S1 = Frame(self.homeresu_pageOne_L1, width=100, height=45, bg="Yellow")
        self.homeresu_pageOne_L1S1.pack_propagate(False)
        self.homeresu_pageOne_L1S1.pack(side=LEFT)
        
        self.homeresu_pageOne_L1Team1 = Label(self.homeresu_pageOne_L1S1, text="First XI")
        self.homeresu_pageOne_L1Team1.pack(pady=12)
        
        
        self.homeresu_pageOne_L1S2 = Frame(self.homeresu_pageOne_L1, width=52.5, height=45, bg="Green")
        self.homeresu_pageOne_L1S2.pack_propagate(False)
        self.homeresu_pageOne_L1S2.pack(side=LEFT)
        
        self.homeresu_pageOne_L1Score1 = Label(self.homeresu_pageOne_L1S2, text="160")
        self.homeresu_pageOne_L1Score1.pack(pady=12)
        
        
        self.homeresu_pageOne_L1S4 = Frame(self.homeresu_pageOne_L1, width=100, height=45, bg="Blue")
        self.homeresu_pageOne_L1S4.pack_propagate(False)
        self.homeresu_pageOne_L1S4.pack(side=RIGHT)        
        
        self.homeresu_pageOne_L1Team2 = Label(self.homeresu_pageOne_L1S4, text="First XI")
        self.homeresu_pageOne_L1Team2.pack(pady=12)
        
        
        self.homeresu_pageOne_L1S3 = Frame(self.homeresu_pageOne_L1, width=52.5, height=45, bg="Red")
        self.homeresu_pageOne_L1S3.pack_propagate(False)
        self.homeresu_pageOne_L1S3.pack(side=RIGHT)
        
        self.homeresu_pageOne_L1Score2 = Label(self.homeresu_pageOne_L1S3, text="70")
        self.homeresu_pageOne_L1Score2.pack(pady=12)
    
        # Line 2 of the latest results
    
        self.homeresu_pageOne_L2 = Frame(self.homeresu_pageOne, width=305, height=45, bg="Yellow")
        self.homeresu_pageOne_L2.pack_propagate(False)
        self.homeresu_pageOne_L2.pack()

        # Line subdivisions
        
        self.homeresu_pageOne_L2S1 = Frame(self.homeresu_pageOne_L2, width=100, height=45, bg="Yellow")
        self.homeresu_pageOne_L2S1.pack_propagate(False)
        self.homeresu_pageOne_L2S1.pack(side=LEFT)
        
        self.homeresu_pageOne_L2Team1 = Label(self.homeresu_pageOne_L2S1, text="Second XI")
        self.homeresu_pageOne_L2Team1.pack(pady=12)
        
        
        self.homeresu_pageOne_L2S2 = Frame(self.homeresu_pageOne_L2, width=52.5, height=45, bg="Green")
        self.homeresu_pageOne_L2S2.pack_propagate(False)
        self.homeresu_pageOne_L2S2.pack(side=LEFT)
        
        self.homeresu_pageOne_L2Score1 = Label(self.homeresu_pageOne_L2S2, text="40")
        self.homeresu_pageOne_L2Score1.pack(pady=12)
        
        
        self.homeresu_pageOne_L2S4 = Frame(self.homeresu_pageOne_L2, width=100, height=45, bg="Blue")
        self.homeresu_pageOne_L2S4.pack_propagate(False)
        self.homeresu_pageOne_L2S4.pack(side=RIGHT)        
        
        self.homeresu_pageOne_L2Team2 = Label(self.homeresu_pageOne_L2S4, text="Second XI")
        self.homeresu_pageOne_L2Team2.pack(pady=12)
        
        
        self.homeresu_pageOne_L2S3 = Frame(self.homeresu_pageOne_L2, width=52.5, height=45, bg="Red")
        self.homeresu_pageOne_L2S3.pack_propagate(False)
        self.homeresu_pageOne_L2S3.pack(side=RIGHT)
        
        self.homeresu_pageOne_L2Score2 = Label(self.homeresu_pageOne_L2S3, text="2")
        self.homeresu_pageOne_L2Score2.pack(pady=12)
        
        # Line 3 of the latest results
        
        self.homeresu_pageOne_L3 = Frame(self.homeresu_pageOne, width=305, height=45, bg="Red")
        self.homeresu_pageOne_L3.pack_propagate(False)
        self.homeresu_pageOne_L3.pack()
        
        # Line subdivisions
        
        self.homeresu_pageOne_L3S1 = Frame(self.homeresu_pageOne_L3, width=100, height=45, bg="Yellow")
        self.homeresu_pageOne_L3S1.pack_propagate(False)
        self.homeresu_pageOne_L3S1.pack(side=LEFT)
        
        self.homeresu_pageOne_L3Team1 = Label(self.homeresu_pageOne_L3S1, text="Junior")
        self.homeresu_pageOne_L3Team1.pack(pady=12)
        
        
        self.homeresu_pageOne_L3S2 = Frame(self.homeresu_pageOne_L3, width=52.5, height=45, bg="Green")
        self.homeresu_pageOne_L3S2.pack_propagate(False)
        self.homeresu_pageOne_L3S2.pack(side=LEFT)
        
        self.homeresu_pageOne_L3Score1 = Label(self.homeresu_pageOne_L3S2, text="23")
        self.homeresu_pageOne_L3Score1.pack(pady=12)
        
        
        self.homeresu_pageOne_L3S4 = Frame(self.homeresu_pageOne_L3, width=100, height=45, bg="Blue")
        self.homeresu_pageOne_L3S4.pack_propagate(False)
        self.homeresu_pageOne_L3S4.pack(side=RIGHT)        
        
        self.homeresu_pageOne_L3Team2 = Label(self.homeresu_pageOne_L3S4, text="Junior")
        self.homeresu_pageOne_L3Team2.pack(pady=12)
        
        
        self.homeresu_pageOne_L3S3 = Frame(self.homeresu_pageOne_L3, width=52.5, height=45, bg="Red")
        self.homeresu_pageOne_L3S3.pack_propagate(False)
        self.homeresu_pageOne_L3S3.pack(side=RIGHT)
        
        self.homeresu_pageOne_L3Score2 = Label(self.homeresu_pageOne_L3S3, text="203")
        self.homeresu_pageOne_L3Score2.pack(pady=12)
        
        # Second resu page (page_number = 2), exactly the same as the first page but the numbers must change
        
        self.homeresu_pageTwo = Frame(self.homeresu_box, bg="Cyan", width=305, height=135)
        self.homeresu_pageTwo.pack_propagate(False)
        self.homeresu_pageTwo.grid_propagate(False)
        
        # Divide the pages into 3 lines with each match
                                
        self.homeresu_pageTwo_L1 = Frame(self.homeresu_pageTwo, width=305, height=45, bg="Green")
        self.homeresu_pageTwo_L1.pack_propagate(False)
        self.homeresu_pageTwo_L1.pack()

        # Divide the lines into 4 sections, 1 = MRGS TEAM, 2 = MRGS SCORE, 3 = OTHER SCORE, 4 = OTHER TEAM
        
        self.homeresu_pageTwo_L1S1 = Frame(self.homeresu_pageTwo_L1, width=100, height=45, bg="Yellow")
        self.homeresu_pageTwo_L1S1.pack_propagate(False)
        self.homeresu_pageTwo_L1S1.pack(side=LEFT)
        
        self.homeresu_pageTwo_L1Team1 = Label(self.homeresu_pageTwo_L1S1, text="First XI")
        self.homeresu_pageTwo_L1Team1.pack(pady=12)
        
        
        self.homeresu_pageTwo_L1S2 = Frame(self.homeresu_pageTwo_L1, width=52.5, height=45, bg="Green")
        self.homeresu_pageTwo_L1S2.pack_propagate(False)
        self.homeresu_pageTwo_L1S2.pack(side=LEFT)
        
        self.homeresu_pageTwo_L1Score1 = Label(self.homeresu_pageTwo_L1S2, text="472")
        self.homeresu_pageTwo_L1Score1.pack(pady=12)
        
        
        self.homeresu_pageTwo_L1S4 = Frame(self.homeresu_pageTwo_L1, width=100, height=45, bg="Blue")
        self.homeresu_pageTwo_L1S4.pack_propagate(False)
        self.homeresu_pageTwo_L1S4.pack(side=RIGHT)        
        
        self.homeresu_pageTwo_L1Team2 = Label(self.homeresu_pageTwo_L1S4, text="First XI")
        self.homeresu_pageTwo_L1Team2.pack(pady=12)
        
        
        self.homeresu_pageTwo_L1S3 = Frame(self.homeresu_pageTwo_L1, width=52.5, height=45, bg="Red")
        self.homeresu_pageTwo_L1S3.pack_propagate(False)
        self.homeresu_pageTwo_L1S3.pack(side=RIGHT)
        
        self.homeresu_pageTwo_L1Score2 = Label(self.homeresu_pageTwo_L1S3, text="143")
        self.homeresu_pageTwo_L1Score2.pack(pady=12)
    
        # Line 2 of the latest results
    
        self.homeresu_pageTwo_L2 = Frame(self.homeresu_pageTwo, width=305, height=45, bg="Yellow")
        self.homeresu_pageTwo_L2.pack_propagate(False)
        self.homeresu_pageTwo_L2.pack()

        # Line subdivisions
        
        self.homeresu_pageTwo_L2S1 = Frame(self.homeresu_pageTwo_L2, width=100, height=45, bg="Yellow")
        self.homeresu_pageTwo_L2S1.pack_propagate(False)
        self.homeresu_pageTwo_L2S1.pack(side=LEFT)
        
        self.homeresu_pageTwo_L2Team1 = Label(self.homeresu_pageTwo_L2S1, text="Second XI")
        self.homeresu_pageTwo_L2Team1.pack(pady=12)
        
        
        self.homeresu_pageTwo_L2S2 = Frame(self.homeresu_pageTwo_L2, width=52.5, height=45, bg="Green")
        self.homeresu_pageTwo_L2S2.pack_propagate(False)
        self.homeresu_pageTwo_L2S2.pack(side=LEFT)
        
        self.homeresu_pageTwo_L2Score1 = Label(self.homeresu_pageTwo_L2S2, text="52")
        self.homeresu_pageTwo_L2Score1.pack(pady=12)
        
        
        self.homeresu_pageTwo_L2S4 = Frame(self.homeresu_pageTwo_L2, width=100, height=45, bg="Blue")
        self.homeresu_pageTwo_L2S4.pack_propagate(False)
        self.homeresu_pageTwo_L2S4.pack(side=RIGHT)        
        
        self.homeresu_pageTwo_L2Team2 = Label(self.homeresu_pageTwo_L2S4, text="Second XI")
        self.homeresu_pageTwo_L2Team2.pack(pady=12)
        
        
        self.homeresu_pageTwo_L2S3 = Frame(self.homeresu_pageTwo_L2, width=52.5, height=45, bg="Red")
        self.homeresu_pageTwo_L2S3.pack_propagate(False)
        self.homeresu_pageTwo_L2S3.pack(side=RIGHT)
        
        self.homeresu_pageTwo_L2Score2 = Label(self.homeresu_pageTwo_L2S3, text="214")
        self.homeresu_pageTwo_L2Score2.pack(pady=12)
        
        # Line 3 of the latest results
        
        self.homeresu_pageTwo_L3 = Frame(self.homeresu_pageTwo, width=305, height=45, bg="Red")
        self.homeresu_pageTwo_L3.pack_propagate(False)
        self.homeresu_pageTwo_L3.pack()
        
        # Line subdivisions
        
        self.homeresu_pageTwo_L3S1 = Frame(self.homeresu_pageTwo_L3, width=100, height=45, bg="Yellow")
        self.homeresu_pageTwo_L3S1.pack_propagate(False)
        self.homeresu_pageTwo_L3S1.pack(side=LEFT)
        
        self.homeresu_pageTwo_L3Team1 = Label(self.homeresu_pageTwo_L3S1, text="Junior")
        self.homeresu_pageTwo_L3Team1.pack(pady=12)
        
        
        self.homeresu_pageTwo_L3S2 = Frame(self.homeresu_pageTwo_L3, width=52.5, height=45, bg="Green")
        self.homeresu_pageTwo_L3S2.pack_propagate(False)
        self.homeresu_pageTwo_L3S2.pack(side=LEFT)
        
        self.homeresu_pageTwo_L3Score1 = Label(self.homeresu_pageTwo_L3S2, text="35")
        self.homeresu_pageTwo_L3Score1.pack(pady=12)
        
        
        self.homeresu_pageTwo_L3S4 = Frame(self.homeresu_pageTwo_L3, width=100, height=45, bg="Blue")
        self.homeresu_pageTwo_L3S4.pack_propagate(False)
        self.homeresu_pageTwo_L3S4.pack(side=RIGHT)        
        
        self.homeresu_pageTwo_L3Team2 = Label(self.homeresu_pageTwo_L3S4, text="Junior")
        self.homeresu_pageTwo_L3Team2.pack(pady=12)
        
        
        self.homeresu_pageTwo_L3S3 = Frame(self.homeresu_pageTwo_L3, width=52.5, height=45, bg="Red")
        self.homeresu_pageTwo_L3S3.pack_propagate(False)
        self.homeresu_pageTwo_L3S3.pack(side=RIGHT)
        
        self.homeresu_pageTwo_L3Score2 = Label(self.homeresu_pageTwo_L3S3, text="17")
        self.homeresu_pageTwo_L3Score2.pack(pady=12)
        
        # Third resu page (page_number = 3)
        
        self.homeresu_pageThree = Frame(self.homeresu_box, bg="Blue", width=305, height=135)
        self.homeresu_pageThree.pack_propagate(False)
        self.homeresu_pageThree.grid_propagate(False)
        
        # Divide the pages into 3 lines with each match
                                
        self.homeresu_pageThree_L1 = Frame(self.homeresu_pageThree, width=305, height=45, bg="Green")
        self.homeresu_pageThree_L1.pack_propagate(False)
        self.homeresu_pageThree_L1.pack()

        # Divide the lines into 4 sections, 1 = MRGS TEAM, 2 = MRGS SCORE, 3 = OTHER SCORE, 4 = OTHER TEAM
        
        self.homeresu_pageThree_L1S1 = Frame(self.homeresu_pageThree_L1, width=100, height=45, bg="Yellow")
        self.homeresu_pageThree_L1S1.pack_propagate(False)
        self.homeresu_pageThree_L1S1.pack(side=LEFT)
        
        self.homeresu_pageThree_L1Team1 = Label(self.homeresu_pageThree_L1S1, text="First XI")
        self.homeresu_pageThree_L1Team1.pack(pady=12)
        
        
        self.homeresu_pageThree_L1S2 = Frame(self.homeresu_pageThree_L1, width=52.5, height=45, bg="Green")
        self.homeresu_pageThree_L1S2.pack_propagate(False)
        self.homeresu_pageThree_L1S2.pack(side=LEFT)
        
        self.homeresu_pageThree_L1Score1 = Label(self.homeresu_pageThree_L1S2, text="12")
        self.homeresu_pageThree_L1Score1.pack(pady=12)
        
        
        self.homeresu_pageThree_L1S4 = Frame(self.homeresu_pageThree_L1, width=100, height=45, bg="Blue")
        self.homeresu_pageThree_L1S4.pack_propagate(False)
        self.homeresu_pageThree_L1S4.pack(side=RIGHT)        
        
        self.homeresu_pageThree_L1Team2 = Label(self.homeresu_pageThree_L1S4, text="First XI")
        self.homeresu_pageThree_L1Team2.pack(pady=12)
        
        
        self.homeresu_pageThree_L1S3 = Frame(self.homeresu_pageThree_L1, width=52.5, height=45, bg="Red")
        self.homeresu_pageThree_L1S3.pack_propagate(False)
        self.homeresu_pageThree_L1S3.pack(side=RIGHT)
        
        self.homeresu_pageThree_L1Score2 = Label(self.homeresu_pageThree_L1S3, text="63")
        self.homeresu_pageThree_L1Score2.pack(pady=12)
    
        # Line 2 of the latest results
    
        self.homeresu_pageThree_L2 = Frame(self.homeresu_pageThree, width=305, height=45, bg="Yellow")
        self.homeresu_pageThree_L2.pack_propagate(False)
        self.homeresu_pageThree_L2.pack()

        # Line subdivisions
        
        self.homeresu_pageThree_L2S1 = Frame(self.homeresu_pageThree_L2, width=100, height=45, bg="Yellow")
        self.homeresu_pageThree_L2S1.pack_propagate(False)
        self.homeresu_pageThree_L2S1.pack(side=LEFT)
        
        self.homeresu_pageThree_L2Team1 = Label(self.homeresu_pageThree_L2S1, text="Second XI")
        self.homeresu_pageThree_L2Team1.pack(pady=12)
        
        
        self.homeresu_pageThree_L2S2 = Frame(self.homeresu_pageThree_L2, width=52.5, height=45, bg="Green")
        self.homeresu_pageThree_L2S2.pack_propagate(False)
        self.homeresu_pageThree_L2S2.pack(side=LEFT)
        
        self.homeresu_pageThree_L2Score1 = Label(self.homeresu_pageThree_L2S2, text="2645")
        self.homeresu_pageThree_L2Score1.pack(pady=12)
        
        
        self.homeresu_pageThree_L2S4 = Frame(self.homeresu_pageThree_L2, width=100, height=45, bg="Blue")
        self.homeresu_pageThree_L2S4.pack_propagate(False)
        self.homeresu_pageThree_L2S4.pack(side=RIGHT)        
        
        self.homeresu_pageThree_L2Team2 = Label(self.homeresu_pageThree_L2S4, text="Second XI")
        self.homeresu_pageThree_L2Team2.pack(pady=12)
        
        
        self.homeresu_pageThree_L2S3 = Frame(self.homeresu_pageThree_L2, width=52.5, height=45, bg="Red")
        self.homeresu_pageThree_L2S3.pack_propagate(False)
        self.homeresu_pageThree_L2S3.pack(side=RIGHT)
        
        self.homeresu_pageThree_L2Score2 = Label(self.homeresu_pageThree_L2S3, text="1")
        self.homeresu_pageThree_L2Score2.pack(pady=12)
        
        # Line 3 of the latest results
        
        self.homeresu_pageThree_L3 = Frame(self.homeresu_pageThree, width=305, height=45, bg="Red")
        self.homeresu_pageThree_L3.pack_propagate(False)
        self.homeresu_pageThree_L3.pack()
        
        # Line subdivisions
        
        self.homeresu_pageThree_L3S1 = Frame(self.homeresu_pageThree_L3, width=100, height=45, bg="Yellow")
        self.homeresu_pageThree_L3S1.pack_propagate(False)
        self.homeresu_pageThree_L3S1.pack(side=LEFT)
        
        self.homeresu_pageThree_L3Team1 = Label(self.homeresu_pageThree_L3S1, text="Junior")
        self.homeresu_pageThree_L3Team1.pack(pady=12)
        
        
        self.homeresu_pageThree_L3S2 = Frame(self.homeresu_pageThree_L3, width=52.5, height=45, bg="Green")
        self.homeresu_pageThree_L3S2.pack_propagate(False)
        self.homeresu_pageThree_L3S2.pack(side=LEFT)
        
        self.homeresu_pageThree_L3Score1 = Label(self.homeresu_pageThree_L3S2, text="753")
        self.homeresu_pageThree_L3Score1.pack(pady=12)
        
        
        self.homeresu_pageThree_L3S4 = Frame(self.homeresu_pageThree_L3, width=100, height=45, bg="Blue")
        self.homeresu_pageThree_L3S4.pack_propagate(False)
        self.homeresu_pageThree_L3S4.pack(side=RIGHT)        
        
        self.homeresu_pageThree_L3Team2 = Label(self.homeresu_pageThree_L3S4, text="Junior")
        self.homeresu_pageThree_L3Team2.pack(pady=12)
        
        
        self.homeresu_pageThree_L3S3 = Frame(self.homeresu_pageThree_L3, width=52.5, height=45, bg="Red")
        self.homeresu_pageThree_L3S3.pack_propagate(False)
        self.homeresu_pageThree_L3S3.pack(side=RIGHT)
        
        self.homeresu_pageThree_L3Score2 = Label(self.homeresu_pageThree_L3S3, text="4")
        self.homeresu_pageThree_L3Score2.pack(pady=12)
        
        # Fourth resu page (page_number = 4)

        self.homeresu_pageFour = Frame(self.homeresu_box, bg="Red", width=305, height=135)
        self.homeresu_pageFour.pack_propagate(False)
        self.homeresu_pageFour.grid_propagate(False)
        
        # Divide the pages into 3 lines with each match
                                
        self.homeresu_pageFour_L1 = Frame(self.homeresu_pageFour, width=305, height=45, bg="Green")
        self.homeresu_pageFour_L1.pack_propagate(False)
        self.homeresu_pageFour_L1.pack()

        # Divide the lines into 4 sections, 1 = MRGS TEAM, 2 = MRGS SCORE, 3 = OTHER SCORE, 4 = OTHER TEAM
        
        self.homeresu_pageFour_L1S1 = Frame(self.homeresu_pageFour_L1, width=100, height=45, bg="Yellow")
        self.homeresu_pageFour_L1S1.pack_propagate(False)
        self.homeresu_pageFour_L1S1.pack(side=LEFT)
        
        self.homeresu_pageFour_L1Team1 = Label(self.homeresu_pageFour_L1S1, text="First XI")
        self.homeresu_pageFour_L1Team1.pack(pady=12)
        
        
        self.homeresu_pageFour_L1S2 = Frame(self.homeresu_pageFour_L1, width=52.5, height=45, bg="Green")
        self.homeresu_pageFour_L1S2.pack_propagate(False)
        self.homeresu_pageFour_L1S2.pack(side=LEFT)
        
        self.homeresu_pageFour_L1Score1 = Label(self.homeresu_pageFour_L1S2, text="3")
        self.homeresu_pageFour_L1Score1.pack(pady=12)
        
        
        self.homeresu_pageFour_L1S4 = Frame(self.homeresu_pageFour_L1, width=100, height=45, bg="Blue")
        self.homeresu_pageFour_L1S4.pack_propagate(False)
        self.homeresu_pageFour_L1S4.pack(side=RIGHT)        
        
        self.homeresu_pageFour_L1Team2 = Label(self.homeresu_pageFour_L1S4, text="First XI")
        self.homeresu_pageFour_L1Team2.pack(pady=12)
        
        
        self.homeresu_pageFour_L1S3 = Frame(self.homeresu_pageFour_L1, width=52.5, height=45, bg="Red")
        self.homeresu_pageFour_L1S3.pack_propagate(False)
        self.homeresu_pageFour_L1S3.pack(side=RIGHT)
        
        self.homeresu_pageFour_L1Score2 = Label(self.homeresu_pageFour_L1S3, text="5")
        self.homeresu_pageFour_L1Score2.pack(pady=12)
    
        # Line 2 of the latest results
    
        self.homeresu_pageFour_L2 = Frame(self.homeresu_pageFour, width=305, height=45, bg="Yellow")
        self.homeresu_pageFour_L2.pack_propagate(False)
        self.homeresu_pageFour_L2.pack()

        # Line subdivisions
        
        self.homeresu_pageFour_L2S1 = Frame(self.homeresu_pageFour_L2, width=100, height=45, bg="Yellow")
        self.homeresu_pageFour_L2S1.pack_propagate(False)
        self.homeresu_pageFour_L2S1.pack(side=LEFT)
        
        self.homeresu_pageFour_L2Team1 = Label(self.homeresu_pageFour_L2S1, text="Second XI")
        self.homeresu_pageFour_L2Team1.pack(pady=12)
        
        
        self.homeresu_pageFour_L2S2 = Frame(self.homeresu_pageFour_L2, width=52.5, height=45, bg="Green")
        self.homeresu_pageFour_L2S2.pack_propagate(False)
        self.homeresu_pageFour_L2S2.pack(side=LEFT)
        
        self.homeresu_pageFour_L2Score1 = Label(self.homeresu_pageFour_L2S2, text="193")
        self.homeresu_pageFour_L2Score1.pack(pady=12)
        
        
        self.homeresu_pageFour_L2S4 = Frame(self.homeresu_pageFour_L2, width=100, height=45, bg="Blue")
        self.homeresu_pageFour_L2S4.pack_propagate(False)
        self.homeresu_pageFour_L2S4.pack(side=RIGHT)        
        
        self.homeresu_pageFour_L2Team2 = Label(self.homeresu_pageFour_L2S4, text="Second XI")
        self.homeresu_pageFour_L2Team2.pack(pady=12)
        
        
        self.homeresu_pageFour_L2S3 = Frame(self.homeresu_pageFour_L2, width=52.5, height=45, bg="Red")
        self.homeresu_pageFour_L2S3.pack_propagate(False)
        self.homeresu_pageFour_L2S3.pack(side=RIGHT)
        
        self.homeresu_pageFour_L2Score2 = Label(self.homeresu_pageFour_L2S3, text="645")
        self.homeresu_pageFour_L2Score2.pack(pady=12)
        
        # Line 3 of the latest results
        
        self.homeresu_pageFour_L3 = Frame(self.homeresu_pageFour, width=305, height=45, bg="Red")
        self.homeresu_pageFour_L3.pack_propagate(False)
        self.homeresu_pageFour_L3.pack()
        
        # Line subdivisions
        
        self.homeresu_pageFour_L3S1 = Frame(self.homeresu_pageFour_L3, width=100, height=45, bg="Yellow")
        self.homeresu_pageFour_L3S1.pack_propagate(False)
        self.homeresu_pageFour_L3S1.pack(side=LEFT)
        
        self.homeresu_pageFour_L3Team1 = Label(self.homeresu_pageFour_L3S1, text="Junior")
        self.homeresu_pageFour_L3Team1.pack(pady=12)
        
        
        self.homeresu_pageFour_L3S2 = Frame(self.homeresu_pageFour_L3, width=52.5, height=45, bg="Green")
        self.homeresu_pageFour_L3S2.pack_propagate(False)
        self.homeresu_pageFour_L3S2.pack(side=LEFT)
        
        self.homeresu_pageFour_L3Score1 = Label(self.homeresu_pageFour_L3S2, text="2")
        self.homeresu_pageFour_L3Score1.pack(pady=12)
        
        
        self.homeresu_pageFour_L3S4 = Frame(self.homeresu_pageFour_L3, width=100, height=45, bg="Blue")
        self.homeresu_pageFour_L3S4.pack_propagate(False)
        self.homeresu_pageFour_L3S4.pack(side=RIGHT)        
        
        self.homeresu_pageFour_L3Team2 = Label(self.homeresu_pageFour_L3S4, text="Junior")
        self.homeresu_pageFour_L3Team2.pack(pady=12)
        
        
        self.homeresu_pageFour_L3S3 = Frame(self.homeresu_pageFour_L3, width=52.5, height=45, bg="Red")
        self.homeresu_pageFour_L3S3.pack_propagate(False)
        self.homeresu_pageFour_L3S3.pack(side=RIGHT)
        
        self.homeresu_pageFour_L3Score2 = Label(self.homeresu_pageFour_L3S3, text="26")
        self.homeresu_pageFour_L3Score2.pack(pady=12)
        
        # Home resu page indicator
            # which page is shown, to be replaced by a different indicator like 4 circles total, and the greyed out circle is the current page
        
        self.homeresu_bottom = Frame(self.homeresu_box, width=305, height=26, bg="Orange")  
        self.homeresu_bottom.pack_propagate(False)
        self.homeresu_bottom.grid(row=2,columnspan=TRUE)
        
        self.page_indicator = Label(self.homeresu_bottom, text=self.page_number)
        self.page_indicator.pack(pady=5)

        # School-sport info page frame
        
        self.info_page = Frame(self.content_frame, background="Purple", width=w_width, height=600)
        self.info_page.grid_propagate(False)
        
        # Stat page frame or statistics is the sports analytics screen
        
        self.stat_page = Frame(self.content_frame, background="Red", width=w_width, height=600)        
        self.stat_page.grid_propagate(False)
        
        # Leaderboard page frame
        
        self.lead_page = Frame(self.content_frame, background="Green", width=w_width, height=600)        
        self.lead_page.grid_propagate(False)
        
        # Navigation bar frame

        self.navigation_bar = Frame(self.window, bg="#FC6736", width=w_width, height=150)
        self.navigation_bar.pack_propagate(False)
        self.navigation_bar.grid(row=2, column=0)

        # Placing buttons on nav bar
        
        self.home_button = Button(self.navigation_bar, text="Home", bg="White", width=7, height=10, command=self.go_to_home)
        self.home_button.pack(side=LEFT, padx=20, pady=60)

        self.info_button = Button(self.navigation_bar, text="Info", bg="White", width=7, height=10, command=self.go_to_info)
        self.info_button.pack(side=LEFT, padx=20, pady=60)

        self.lead_button = Button(self.navigation_bar, text="Lead", bg="White", width=7, height=10, command=self.go_to_lead)
        self.lead_button.pack(side=RIGHT, padx=20, pady=60)

        self.stat_button = Button(self.navigation_bar, text="Stat", bg="White", width=7, height=10, command=self.go_to_stat)
        self.stat_button.pack(side=RIGHT, padx=20, pady=60)



        
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
                
        self.page_indicator.config(text=self.page_number)
        
        self.change_resu_page()
        
    def go_to_home(self):
        self.info_page.grid_remove()
        self.stat_page.grid_remove()
        self.lead_page.grid_remove()
        self.home_page.grid(rowspan=TRUE, columnspan=TRUE)
        
    def go_to_info(self):
        self.stat_page.grid_remove()
        self.lead_page.grid_remove()
        self.home_page.grid_remove()
        self.info_page.grid(rowspan=TRUE, columnspan=TRUE)
 
    def go_to_stat(self):
        self.info_page.grid_remove()
        self.lead_page.grid_remove()
        self.home_page.grid_remove()
        self.stat_page.grid(rowspan=TRUE, columnspan=TRUE)       
        
    def go_to_lead(self):
        self.info_page.grid_remove()
        self.stat_page.grid_remove()
        self.home_page.grid_remove()
        self.lead_page.grid(rowspan=TRUE, columnspan=TRUE)
           
    def change_resu_page(self):
        # Update visibility of each page
        self.homeresu_pageOne.grid_remove()
        self.homeresu_pageTwo.grid_remove()
        self.homeresu_pageThree.grid_remove()
        self.homeresu_pageFour.grid_remove()

        if self.page_number == 1:
            self.homeresu_pageOne.grid(row=1, columnspan=TRUE)
            self.homeresu_sportname.config(text="Football")
        elif self.page_number == 2:
            self.homeresu_pageTwo.grid(row=1, columnspan=TRUE)
            self.homeresu_sportname.config(text="Basketball")
        elif self.page_number == 3:
            self.homeresu_pageThree.grid(row=1, columnspan=TRUE)
            self.homeresu_sportname.config(text="Hockey")
        elif self.page_number == 4:
            self.homeresu_pageFour.grid(row=1, columnspan=TRUE)
            self.homeresu_sportname.config(text="Cricket")