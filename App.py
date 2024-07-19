from tkinter import *
from tkinter import messagebox, ttk
from app_settings import *
from os import *
import uuid
import json

w_width = 400
w_height = 850 
margin_length = 30



#leftarrow = PhotoImage(file = "C:\Users\21194\Downloads\683398_arrows_512x512.png")

class App():
    
    
    
    def __init__(self):
        self.window = Tk()
        self.window.geometry((str(w_width)) + "x" + (str(w_height)))
        self.window.title("MRGSports")
        
        #self.title_font and other fonts to replace unnecessary code
        
        self.page_number = 1
        self.max_page_numbers = 4
        
        self.teacher_code = 'KMR'
        self.teacher_input = StringVar()
        
        self.upcoming_weekday = StringVar()
        self.upcoming_time = StringVar()
        self.sports = ['Football', 'Basketball', 'Hockey', 'Cricket']
        self.teams = ['First XI', 'Second XI', 'Junior']
        

        
        
        
        # Login page

        self.login_page = Frame(self.window, background="#FC6736", width=w_width, height=w_height)
        self.login_page.pack_propagate(False)
        self.login_page.pack()
        
        self.login_logo = Label(self.login_page, text="MRGSports", bg="#FC6736", fg="White", font=("Courier", 45, "bold"))
        self.login_logo.pack(pady=190)
        
        self.login_question = Frame(self.login_page, width=w_width, height=300, bg="#FC6736")
        self.login_question.pack_propagate(False)
        self.login_question.pack(pady=5)
        
        self.login_text = Label(self.login_question, text="Are you a...", width=w_width, height=2, fg="Black", font=("Helvetica", 20))
        self.login_text.pack(pady=40)
        
        self.login_buttons = Frame(self.login_question, width=w_width, height=200, bg="White")
        self.login_buttons.pack_propagate(False)
        self.login_buttons.pack()
        
        self.login_student_button = Button(self.login_buttons, text="Student", font=("Helvetica", 15), width=12, height=5, command=self.student_login)
        self.login_student_button.pack(side=LEFT, padx=15)

        self.login_teacher_button = Button(self.login_buttons, text="Teacher", font=("Helvetica", 15), width=12, height=5, command=self.teacher_login)
        self.login_teacher_button.pack(side=RIGHT, padx=15)
        
        # Teacher page
        
        self.teacher_login_page = Frame(self.window, background="#EFECEC", width=w_width, height=w_height)
        self.teacher_login_page.pack_propagate(False)
        
        # Top section of the login page, the entry for the teacher code is here
        
        self.tlogin_top = Frame(self.teacher_login_page, background="#EFECEC", width=w_width, height=300)
        self.tlogin_top.pack_propagate(False)
        self.tlogin_top.pack()
        
        self.tcode_input_box = Frame(self.tlogin_top, background="White", width=320, height=140, bd=3, relief=GROOVE)
        self.tcode_input_box.pack_propagate(False)
        self.tcode_input_box.pack(pady=80)
        
        self.tcode_input_label = Label(self.tcode_input_box, text="Please enter your teacher code, e.g. 'MCS'", font=("Helvetica", 12))
        self.tcode_input_label.pack(pady=5)
        
        self.tcode_input_entry = Entry(self.tcode_input_box, textvariable = self.teacher_input, font=("Helvetica", 14))
        self.tcode_input_entry.pack(pady=5)
        
        self.tcode_input_confirm = Button(self.tcode_input_box, text="Confirm", font=("Helvetica", 14), command = self.tcode_confirm)
        self.tcode_input_confirm.pack(pady=5)
               
        # The buttons and logo appear only after the teacher code has been entered and will also be removed if the incorrect code is entered afterwards
        
        self.tlogin_bottom = Frame(self.teacher_login_page, background="#FC6736", width=w_width, height=550)
        self.tlogin_bottom.pack_propagate(False)
        self.tlogin_bottom.pack()
        
        self.create_upcoming_button = Button(self.tlogin_bottom, text="Schedule an upcoming match", font=("Helvetica", 14), background="White", width=30, height=3, command=self.show_upcoming_creator)

        self.create_result_button = Button(self.tlogin_bottom, text="Enter a match result", font=("Helvetica", 14), background="White", width=30, height=3, command=self.show_result_creator)

        self.tlogin_logo = Label(self.tlogin_bottom, text="MRGSports", bg="#FC6736", fg="White", font=("Courier", 45, "bold"))
        
        
        # Upcoming match scheduling page
        
        self.upcoming_sched_page = Frame(self.window, background="#EFECEC", width=w_width, height=w_height)
        self.upcoming_sched_page.pack_propagate(False)
        
        self.upcoming_sched_top = Frame(self.upcoming_sched_page, background="#EFECEC", width=w_width, height=650)
        self.upcoming_sched_top.pack_propagate(False)
        self.upcoming_sched_top.pack()
  
        self.upcoming_sched_test = Label(self.upcoming_sched_top, text="Schedule a match for next week", font=("Helvetica", 18))
        self.upcoming_sched_test.pack()
        
        self.upcoming_sport_label = Label(self.upcoming_sched_top, text="Sport")
        self.upcoming_sport_label.pack()
        
        self.upcoming_sport_entry = ttk.Combobox(self.upcoming_sched_top, values=self.sports)
        self.upcoming_sport_entry.pack()
        
        self.upcoming_team_label = Label(self.upcoming_sched_top, text="Team")
        self.upcoming_team_label.pack()
        
        self.upcoming_team_entry = ttk.Combobox(self.upcoming_sched_top, values=self.teams)
        self.upcoming_team_entry.pack()    
        
        self.upcoming_weekday_label = Label(self.upcoming_sched_top, text="What day next week will the game be? (e.g. Monday)")
        self.upcoming_weekday_label.pack()
        
        self.upcoming_weekday_entry = Entry(self.upcoming_sched_top, textvariable=self.upcoming_weekday)
        self.upcoming_weekday_entry.pack()
        
        self.upcoming_time_label = Label(self.upcoming_sched_top, text="What time on this day will the game be? (e.g. 15:30)")
        self.upcoming_time_label.pack()
        
        self.upcoming_time_entry = Entry(self.upcoming_sched_top, textvariable=self.upcoming_time)
        self.upcoming_time_entry.pack()
        
        
        self.trv = ttk.Treeview(self.upcoming_sched_top, columns=(1,2,3,4), show="headings", height="16")
        self.trv.pack()
        

        self.trv.heading(1, text="Sport")
        self.trv.heading(2, text="Team")
        self.trv.heading(3, text="Day")
        self.trv.heading(4, text="Time")
        
        self.trv.column("1",width=60,stretch=FALSE)
        self.trv.column("2",width=60,stretch=FALSE)
        self.trv.column("3",width=60,stretch=FALSE)
        self.trv.column("4",width=60,stretch=FALSE)
                        
        self.sport_label = Label(self.upcoming_sched_top, text="", font=("Helvetica", 14), bg="#FC6736")
        self.sport_label.pack(side=LEFT, padx=5)
        
        self.day_label = Label(self.upcoming_sched_top, text="", font=("Helvetica", 14), bg="#FC6736")
        self.day_label.pack(side=LEFT, padx=5)
        
        self.time_label = Label(self.upcoming_sched_top, text="", font=("Helvetica", 14), bg="#FC6736")
        self.time_label.pack(side=LEFT, padx=5)
        

        
        # Display the entries
        
        self.upcoming_sched_bottom = Frame(self.upcoming_sched_page, background="#FC6736", width=w_width, height=200)
        self.upcoming_sched_bottom.pack_propagate(False)
        self.upcoming_sched_bottom.pack()
        
        self.upcoming_data_confirm = Button(self.upcoming_sched_bottom, text="Done", bg="White", font=("Helvetica", 14), command=self.enter_upcoming_game)
        self.upcoming_data_confirm.pack(side=RIGHT, padx=5)
        

        
        # Result entering page
        
        self.result_enter_page = Frame(self.window, background="#EFECEC", width=w_width, height=w_height)
        self.result_enter_page.pack_propagate(False)
        
        self.result_enter_top = Frame(self.result_enter_page, background="#EFECEC", width=w_width, height=550)
        self.result_enter_top.pack_propagate(False)
        self.result_enter_top.pack()
        
        self.result_enter_test = Label(self.result_enter_top, text="Hello this is results cuzzie")
        self.result_enter_test.pack()
    
    
        
        self.result_enter_bottom = Frame(self.result_enter_page, background="#FC6736", width=w_width, height=300)
        self.result_enter_bottom.pack_propagate(False)
        self.result_enter_bottom.pack()
        
        
        
        
        # ---------------------- STUDENT PAGES BELOW ----------------------
        
        # Logo frame

        self.logo_frame = Frame(self.window, background="#FC6736", width=w_width, height=100)
        self.logo_frame.pack_propagate(False)
        

        # Logo text test (to be replaced by image)
        
        self.logo_text = Label(self.logo_frame, text="MRGSports", bg="#FC6736", fg="White", font=("Courier", 30, "bold"))
        self.logo_text.pack(pady=20)

        # Content frame containing the main student pages that are shown

        self.content_frame = Frame(self.window, background="Black", width=w_width, height=600)
        self.content_frame.grid_propagate(False)
        
        
        # Home page frame
        
        self.home_page = Frame(self.content_frame, background="#EFECEC", width=w_width, height=600)
        self.home_page.pack_propagate(False)
        self.home_page.grid_propagate(False)
        self.home_page.grid(rowspan=TRUE, columnspan=TRUE)

        # Upcoming section of the home page
        
        self.upcoming_main = Frame(self.home_page, width=w_width - margin_length, height=330, bg='#EFECEC')
        self.upcoming_main.pack_propagate(False)
        self.upcoming_main.pack()
        
        self.home_header_one = Label(self.upcoming_main, text="UPCOMING", bg="#EFECEC", font=("Cairo", 16, "bold"))
        self.home_header_one.pack(padx=20, pady=5)
        
        # First upcoming display, it is split up into 5 rows called one, two, three, four, and five which show the most relevant and most imminent sport matches for the school (the dictionary created for upcoming matches will be here and separate to results used below this)
        
        self.upcoming_row_one = Frame(self.upcoming_main, bg="#EFECEC", width=w_width - margin_length, height=70)
        self.upcoming_row_one.pack()
        
        self.upcoming_box_game = Frame(self.upcoming_row_one, bg="White", width=200, height=50, bd=3, relief=RIDGE)
        self.upcoming_box_game.pack_propagate(False)
        self.upcoming_box_game.pack(side=LEFT, padx=4.5, pady=3)
        
        self.upcoming_game_one = Label(self.upcoming_box_game, text="", bg="White")
        self.upcoming_game_one.pack(padx=5,pady=5)

        self.upcoming_box_time = Frame(self.upcoming_row_one, bg="White", width=100, height=50, bd=3, relief=RIDGE)
        self.upcoming_box_time.pack_propagate(False)
        self.upcoming_box_time.pack(side=RIGHT, padx=4.5, pady=3)        
        
        self.upcoming_day_one = Label(self.upcoming_box_time, text="", bg="White")
        self.upcoming_day_one.pack()
        
        self.upcoming_time_one = Label(self.upcoming_box_time, text="", bg="White")
        self.upcoming_time_one.pack()
        
        # Second upcoming display
        
        self.upcoming_row_two = Frame(self.upcoming_main, bg="#EFECEC", width=w_width - margin_length, height=70)
        self.upcoming_row_two.pack()
        
        self.upcoming_box_game2 = Frame(self.upcoming_row_two, bg="White", width=200, height=50, bd=3, relief=RIDGE)
        self.upcoming_box_game2.pack_propagate(False)
        self.upcoming_box_game2.pack(side=LEFT, padx=4.5, pady=3)
        
        self.upcoming_game_two = Label(self.upcoming_box_game2, text="Basketball Game", bg="White")
        self.upcoming_game_two.pack(padx=5,pady=5)

        self.upcoming_box_time2 = Frame(self.upcoming_row_two, bg="White", width=100, height=50, bd=3, relief=RIDGE)
        self.upcoming_box_time2.pack_propagate(False)
        self.upcoming_box_time2.pack(side=RIGHT, padx=4.5, pady=3)      

        self.upcoming_day_two = Label(self.upcoming_box_time2, text="Tuesday", bg="White")
        self.upcoming_day_two.pack()
        
        self.upcoming_time_two = Label(self.upcoming_box_time2, text="11:56", bg="White")
        self.upcoming_time_two.pack()
                
        # Third upcoming display
        
        self.upcoming_row_three = Frame(self.upcoming_main, bg="#EFECEC", width=w_width - margin_length, height=70)
        self.upcoming_row_three.pack()
        
        self.upcoming_box_game3 = Frame(self.upcoming_row_three, bg="White", width=200, height=50, bd=3, relief=RIDGE)
        self.upcoming_box_game3.pack_propagate(False)
        self.upcoming_box_game3.pack(side=LEFT, padx=4.5, pady=3)
        
        self.upcoming_game_three = Label(self.upcoming_box_game3, text="Volleyball Game", bg="White")
        self.upcoming_game_three.pack(padx=5,pady=5)

        self.upcoming_box_time3 = Frame(self.upcoming_row_three, bg="White", width=100, height=50, bd=3, relief=RIDGE)
        self.upcoming_box_time3.pack_propagate(False)
        self.upcoming_box_time3.pack(side=RIGHT, padx=4.5, pady=3)

        self.upcoming_day_three = Label(self.upcoming_box_time3, text="Monday", bg="White")
        self.upcoming_day_three.pack()
        
        self.upcoming_time_three = Label(self.upcoming_box_time3, text="8:17", bg="White")
        self.upcoming_time_three.pack()
                
        # Fourth upcoming display
        
        self.upcoming_row_four = Frame(self.upcoming_main, bg="#EFECEC", width=w_width - margin_length, height=70)
        self.upcoming_row_four.pack()
        
        self.upcoming_box_game4 = Frame(self.upcoming_row_four, bg="White", width=200, height=50, bd=3, relief=RIDGE)
        self.upcoming_box_game4.pack_propagate(False)
        self.upcoming_box_game4.pack(side=LEFT, padx=4.5, pady=3)
        
        self.upcoming_game_four = Label(self.upcoming_box_game4, text="Hockey Game", bg="White")
        self.upcoming_game_four.pack(padx=5,pady=5)

        self.upcoming_box_time4 = Frame(self.upcoming_row_four, bg="White", width=100, height=50, bd=3, relief=RIDGE)
        self.upcoming_box_time4.pack_propagate(False)
        self.upcoming_box_time4.pack(side=RIGHT, padx=4.5, pady=3)

        self.upcoming_day_four = Label(self.upcoming_box_time4, text="Friday", bg="White")
        self.upcoming_day_four.pack()
        
        self.upcoming_time_four = Label(self.upcoming_box_time4, text="19:20", bg="White")
        self.upcoming_time_four.pack()
                
        # Fifth upcoming display
        
        self.upcoming_row_five = Frame(self.upcoming_main, bg="#EFECEC", width=w_width - margin_length, height=70)
        self.upcoming_row_five.pack()
        
        self.upcoming_box_game5 = Frame(self.upcoming_row_five, bg="White", width=200, height=50, bd=3, relief=RIDGE)
        self.upcoming_box_game5.pack_propagate(False)
        self.upcoming_box_game5.pack(side=LEFT, padx=4.5, pady=3)
        
        self.upcoming_game_five = Label(self.upcoming_box_game5, text="Waterpolo Game", bg="White")
        self.upcoming_game_five.pack(padx=5,pady=5)

        self.upcoming_box_time5 = Frame(self.upcoming_row_five, bg="White", width=100, height=50, bd=3, relief=RIDGE)
        self.upcoming_box_time5.pack_propagate(False)
        self.upcoming_box_time5.pack(side=RIGHT, padx=4.5, pady=3)

        self.upcoming_day_five = Label(self.upcoming_box_time5, text="Thursday", bg="White")
        self.upcoming_day_five.pack()
        
        self.upcoming_time_five = Label(self.upcoming_box_time5, text="14:15", bg="White")
        self.upcoming_time_five.pack()
                                            
        # End of upcoming/Start of res-this-week
        
        self.homeresu_main = Frame(self.home_page, width=w_width - margin_length, height=270, bg='#EFECEC')
        self.homeresu_main.pack_propagate(False)
        self.homeresu_main.pack()
        
        self.home_header_two = Label(self.homeresu_main, text="LATEST RESULTS", bg="#EFECEC", font=("Cairo", 16, "bold"))
        self.home_header_two.pack(padx=20, pady=5)
        
        self.homeresu_box = Frame(self.homeresu_main, bg="White", width=305, height=190, bd=3, relief=RIDGE)
        self.homeresu_box.pack_propagate(False)
        self.homeresu_box.pack(padx=5, pady=3)        
        
        # First resu page (no L/R button press)
        # Top is split into two parts "Left top" and "Right top"
        
        self.homeresu_top = Frame(self.homeresu_box, width=305, height=29, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_top.pack_propagate(False)
        self.homeresu_top.grid_propagate(False)
        self.homeresu_top.grid(row=0,column=0)
        
        self.homeresu_topLeft = Frame(self.homeresu_top, width=152.5, height=29, bg="White")
        self.homeresu_topLeft.pack_propagate(False)        
        self.homeresu_topLeft.pack(side=LEFT)
        
        self.homeresu_sportname = Label(self.homeresu_topLeft, text="Football", relief=RIDGE, bg="White", width=10, height=1)
        self.homeresu_sportname.pack(side=LEFT, padx=10, pady=2)
        
        self.homeresu_topRight = Frame(self.homeresu_top, width=152.5, height=29, bg="White")
        self.homeresu_topRight.pack_propagate(False)        
        self.homeresu_topRight.pack(side=RIGHT)
         
        self.home_right_button = Button(self.homeresu_topRight, width=5, text="Right", bg="White", command=lambda: self.go_to_next_page("right"))
        self.home_right_button.pack(side=RIGHT, padx=1, pady=1)
       
        self.home_left_button = Button(self.homeresu_topRight, width=5, text="Left", bg="White", command=lambda: self.go_to_next_page("left"))
        self.home_left_button.pack(side=RIGHT, padx=5, pady=1)
        
        # Middle of homeresu, this is what changes on the button press containing the actual results
        # Home results page one
        
        self.homeresu_pageOne = Frame(self.homeresu_box, bg="White", width=305, height=135)
        self.homeresu_pageOne.pack_propagate(False)
        self.homeresu_pageOne.grid_propagate(False)        
        self.homeresu_pageOne.grid(row=1, columnspan=TRUE)

        # Divide the pages into 3 lines with each match
                                
        self.homeresu_pageOne_L1 = Frame(self.homeresu_pageOne, width=305, height=45, bg="White")
        self.homeresu_pageOne_L1.pack_propagate(False)
        self.homeresu_pageOne_L1.pack()
        
        # Sub the First XI for first_team and second which is a string variable decided by the user input on teacher page
        
        # Divide the lines into 4 sections, 1 = MRGS TEAM, 2 = MRGS SCORE, 3 = OTHER SCORE, 4 = OTHER TEAM
        
        self.homeresu_pageOne_L1S1 = Frame(self.homeresu_pageOne_L1, width=100, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageOne_L1S1.pack_propagate(False)
        self.homeresu_pageOne_L1S1.pack(side=LEFT)
        
        self.homeresu_pageOne_L1Team1 = Label(self.homeresu_pageOne_L1S1, text="First XI", bg="White")
        self.homeresu_pageOne_L1Team1.pack(pady=12)
        
        
        self.homeresu_pageOne_L1S2 = Frame(self.homeresu_pageOne_L1, width=52.5, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageOne_L1S2.pack_propagate(False)
        self.homeresu_pageOne_L1S2.pack(side=LEFT)
        
        self.homeresu_pageOne_L1Score1 = Label(self.homeresu_pageOne_L1S2, text="160", bg="White")
        self.homeresu_pageOne_L1Score1.pack(pady=12)
        
        
        self.homeresu_pageOne_L1S4 = Frame(self.homeresu_pageOne_L1, width=100, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageOne_L1S4.pack_propagate(False)
        self.homeresu_pageOne_L1S4.pack(side=RIGHT)        
        
        self.homeresu_pageOne_L1Team2 = Label(self.homeresu_pageOne_L1S4, text="First XI", bg="White")
        self.homeresu_pageOne_L1Team2.pack(pady=12)
        
        
        self.homeresu_pageOne_L1S3 = Frame(self.homeresu_pageOne_L1, width=52.5, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageOne_L1S3.pack_propagate(False)
        self.homeresu_pageOne_L1S3.pack(side=RIGHT)
        
        self.homeresu_pageOne_L1Score2 = Label(self.homeresu_pageOne_L1S3, text="70", bg="White")
        self.homeresu_pageOne_L1Score2.pack(pady=12)
    
        # Line 2 of the latest results
    
        self.homeresu_pageOne_L2 = Frame(self.homeresu_pageOne, width=305, height=45, bg="White")
        self.homeresu_pageOne_L2.pack_propagate(False)
        self.homeresu_pageOne_L2.pack()

        # Line subdivisions
        
        self.homeresu_pageOne_L2S1 = Frame(self.homeresu_pageOne_L2, width=100, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageOne_L2S1.pack_propagate(False)
        self.homeresu_pageOne_L2S1.pack(side=LEFT)
        
        self.homeresu_pageOne_L2Team1 = Label(self.homeresu_pageOne_L2S1, text="Second XI", bg="White")
        self.homeresu_pageOne_L2Team1.pack(pady=12)
        
        
        self.homeresu_pageOne_L2S2 = Frame(self.homeresu_pageOne_L2, width=52.5, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageOne_L2S2.pack_propagate(False)
        self.homeresu_pageOne_L2S2.pack(side=LEFT)
        
        self.homeresu_pageOne_L2Score1 = Label(self.homeresu_pageOne_L2S2, text="40", bg="White")
        self.homeresu_pageOne_L2Score1.pack(pady=12)
        
        
        self.homeresu_pageOne_L2S4 = Frame(self.homeresu_pageOne_L2, width=100, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageOne_L2S4.pack_propagate(False)
        self.homeresu_pageOne_L2S4.pack(side=RIGHT)        
        
        self.homeresu_pageOne_L2Team2 = Label(self.homeresu_pageOne_L2S4, text="Second XI", bg="White")
        self.homeresu_pageOne_L2Team2.pack(pady=12)
        
        
        self.homeresu_pageOne_L2S3 = Frame(self.homeresu_pageOne_L2, width=52.5, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageOne_L2S3.pack_propagate(False)
        self.homeresu_pageOne_L2S3.pack(side=RIGHT)
        
        self.homeresu_pageOne_L2Score2 = Label(self.homeresu_pageOne_L2S3, text="2", bg="White")
        self.homeresu_pageOne_L2Score2.pack(pady=12)
        
        # Line 3 of the latest results
        
        self.homeresu_pageOne_L3 = Frame(self.homeresu_pageOne, width=305, height=45, bg="White")
        self.homeresu_pageOne_L3.pack_propagate(False)
        self.homeresu_pageOne_L3.pack()
        
        # Line subdivisions
        
        self.homeresu_pageOne_L3S1 = Frame(self.homeresu_pageOne_L3, width=100, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageOne_L3S1.pack_propagate(False)
        self.homeresu_pageOne_L3S1.pack(side=LEFT)
        
        self.homeresu_pageOne_L3Team1 = Label(self.homeresu_pageOne_L3S1, text="Junior", bg="White")
        self.homeresu_pageOne_L3Team1.pack(pady=12)
        
        
        self.homeresu_pageOne_L3S2 = Frame(self.homeresu_pageOne_L3, width=52.5, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageOne_L3S2.pack_propagate(False)
        self.homeresu_pageOne_L3S2.pack(side=LEFT)
        
        self.homeresu_pageOne_L3Score1 = Label(self.homeresu_pageOne_L3S2, text="23", bg="White")
        self.homeresu_pageOne_L3Score1.pack(pady=12)
        
        
        self.homeresu_pageOne_L3S4 = Frame(self.homeresu_pageOne_L3, width=100, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageOne_L3S4.pack_propagate(False)
        self.homeresu_pageOne_L3S4.pack(side=RIGHT)        
        
        self.homeresu_pageOne_L3Team2 = Label(self.homeresu_pageOne_L3S4, text="Junior", bg="White")
        self.homeresu_pageOne_L3Team2.pack(pady=12)
        
        
        self.homeresu_pageOne_L3S3 = Frame(self.homeresu_pageOne_L3, width=52.5, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageOne_L3S3.pack_propagate(False)
        self.homeresu_pageOne_L3S3.pack(side=RIGHT)
        
        self.homeresu_pageOne_L3Score2 = Label(self.homeresu_pageOne_L3S3, text="203", bg="White")
        self.homeresu_pageOne_L3Score2.pack(pady=12)
        
        # Second resu page (page_number = 2), exactly the same as the first page but the numbers must change
        
        self.homeresu_pageTwo = Frame(self.homeresu_box, bg="White", width=305, height=135)
        self.homeresu_pageTwo.pack_propagate(False)
        self.homeresu_pageTwo.grid_propagate(False)
        
        # Divide the pages into 3 lines with each match
                                
        self.homeresu_pageTwo_L1 = Frame(self.homeresu_pageTwo, width=305, height=45, bg="White")
        self.homeresu_pageTwo_L1.pack_propagate(False)
        self.homeresu_pageTwo_L1.pack()

        # Divide the lines into 4 sections, 1 = MRGS TEAM, 2 = MRGS SCORE, 3 = OTHER SCORE, 4 = OTHER TEAM
        
        self.homeresu_pageTwo_L1S1 = Frame(self.homeresu_pageTwo_L1, width=100, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageTwo_L1S1.pack_propagate(False)
        self.homeresu_pageTwo_L1S1.pack(side=LEFT)
        
        self.homeresu_pageTwo_L1Team1 = Label(self.homeresu_pageTwo_L1S1, text="First XI", bg="White")
        self.homeresu_pageTwo_L1Team1.pack(pady=12)
        
        
        self.homeresu_pageTwo_L1S2 = Frame(self.homeresu_pageTwo_L1, width=52.5, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageTwo_L1S2.pack_propagate(False)
        self.homeresu_pageTwo_L1S2.pack(side=LEFT)
        
        self.homeresu_pageTwo_L1Score1 = Label(self.homeresu_pageTwo_L1S2, text="472", bg="White")
        self.homeresu_pageTwo_L1Score1.pack(pady=12)
        
        
        self.homeresu_pageTwo_L1S4 = Frame(self.homeresu_pageTwo_L1, width=100, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageTwo_L1S4.pack_propagate(False)
        self.homeresu_pageTwo_L1S4.pack(side=RIGHT)        
        
        self.homeresu_pageTwo_L1Team2 = Label(self.homeresu_pageTwo_L1S4, text="First XI", bg="White")
        self.homeresu_pageTwo_L1Team2.pack(pady=12)
        
        
        self.homeresu_pageTwo_L1S3 = Frame(self.homeresu_pageTwo_L1, width=52.5, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageTwo_L1S3.pack_propagate(False)
        self.homeresu_pageTwo_L1S3.pack(side=RIGHT)
        
        self.homeresu_pageTwo_L1Score2 = Label(self.homeresu_pageTwo_L1S3, text="143", bg="White")
        self.homeresu_pageTwo_L1Score2.pack(pady=12)
    
        # Line 2 of the latest results
    
        self.homeresu_pageTwo_L2 = Frame(self.homeresu_pageTwo, width=305, height=45, bg="White")
        self.homeresu_pageTwo_L2.pack_propagate(False)
        self.homeresu_pageTwo_L2.pack()

        # Line subdivisions
        
        self.homeresu_pageTwo_L2S1 = Frame(self.homeresu_pageTwo_L2, width=100, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageTwo_L2S1.pack_propagate(False)
        self.homeresu_pageTwo_L2S1.pack(side=LEFT)
        
        self.homeresu_pageTwo_L2Team1 = Label(self.homeresu_pageTwo_L2S1, text="Second XI", bg="White")
        self.homeresu_pageTwo_L2Team1.pack(pady=12)
        
        
        self.homeresu_pageTwo_L2S2 = Frame(self.homeresu_pageTwo_L2, width=52.5, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageTwo_L2S2.pack_propagate(False)
        self.homeresu_pageTwo_L2S2.pack(side=LEFT)
        
        self.homeresu_pageTwo_L2Score1 = Label(self.homeresu_pageTwo_L2S2, text="52", bg="White")
        self.homeresu_pageTwo_L2Score1.pack(pady=12)
        
        
        self.homeresu_pageTwo_L2S4 = Frame(self.homeresu_pageTwo_L2, width=100, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageTwo_L2S4.pack_propagate(False)
        self.homeresu_pageTwo_L2S4.pack(side=RIGHT)        
        
        self.homeresu_pageTwo_L2Team2 = Label(self.homeresu_pageTwo_L2S4, text="Second XI", bg="White")
        self.homeresu_pageTwo_L2Team2.pack(pady=12)
        
        
        self.homeresu_pageTwo_L2S3 = Frame(self.homeresu_pageTwo_L2, width=52.5, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageTwo_L2S3.pack_propagate(False)
        self.homeresu_pageTwo_L2S3.pack(side=RIGHT)
        
        self.homeresu_pageTwo_L2Score2 = Label(self.homeresu_pageTwo_L2S3, text="214", bg="White")
        self.homeresu_pageTwo_L2Score2.pack(pady=12)
        
        # Line 3 of the latest results
        
        self.homeresu_pageTwo_L3 = Frame(self.homeresu_pageTwo, width=305, height=45, bg="White")
        self.homeresu_pageTwo_L3.pack_propagate(False)
        self.homeresu_pageTwo_L3.pack()
        
        # Line subdivisions
        
        self.homeresu_pageTwo_L3S1 = Frame(self.homeresu_pageTwo_L3, width=100, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageTwo_L3S1.pack_propagate(False)
        self.homeresu_pageTwo_L3S1.pack(side=LEFT)
        
        self.homeresu_pageTwo_L3Team1 = Label(self.homeresu_pageTwo_L3S1, text="Junior", bg="White")
        self.homeresu_pageTwo_L3Team1.pack(pady=12)
        
        
        self.homeresu_pageTwo_L3S2 = Frame(self.homeresu_pageTwo_L3, width=52.5, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageTwo_L3S2.pack_propagate(False)
        self.homeresu_pageTwo_L3S2.pack(side=LEFT)
        
        self.homeresu_pageTwo_L3Score1 = Label(self.homeresu_pageTwo_L3S2, text="35", bg="White")
        self.homeresu_pageTwo_L3Score1.pack(pady=12)
        
        
        self.homeresu_pageTwo_L3S4 = Frame(self.homeresu_pageTwo_L3, width=100, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageTwo_L3S4.pack_propagate(False)
        self.homeresu_pageTwo_L3S4.pack(side=RIGHT)        
        
        self.homeresu_pageTwo_L3Team2 = Label(self.homeresu_pageTwo_L3S4, text="Junior", bg="White")
        self.homeresu_pageTwo_L3Team2.pack(pady=12)
        
        
        self.homeresu_pageTwo_L3S3 = Frame(self.homeresu_pageTwo_L3, width=52.5, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageTwo_L3S3.pack_propagate(False)
        self.homeresu_pageTwo_L3S3.pack(side=RIGHT)
        
        self.homeresu_pageTwo_L3Score2 = Label(self.homeresu_pageTwo_L3S3, text="17", bg="White")
        self.homeresu_pageTwo_L3Score2.pack(pady=12)
        
        # Third resu page (page_number = 3)
        
        self.homeresu_pageThree = Frame(self.homeresu_box, bg="White", width=305, height=135)
        self.homeresu_pageThree.pack_propagate(False)
        self.homeresu_pageThree.grid_propagate(False)
        
        # Divide the pages into 3 lines with each match
                                
        self.homeresu_pageThree_L1 = Frame(self.homeresu_pageThree, width=305, height=45, bg="White")
        self.homeresu_pageThree_L1.pack_propagate(False)
        self.homeresu_pageThree_L1.pack()

        # Divide the lines into 4 sections, 1 = MRGS TEAM, 2 = MRGS SCORE, 3 = OTHER SCORE, 4 = OTHER TEAM
        
        self.homeresu_pageThree_L1S1 = Frame(self.homeresu_pageThree_L1, width=100, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageThree_L1S1.pack_propagate(False)
        self.homeresu_pageThree_L1S1.pack(side=LEFT)
        
        self.homeresu_pageThree_L1Team1 = Label(self.homeresu_pageThree_L1S1, text="First XI", bg="White")
        self.homeresu_pageThree_L1Team1.pack(pady=12)
        
        
        self.homeresu_pageThree_L1S2 = Frame(self.homeresu_pageThree_L1, width=52.5, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageThree_L1S2.pack_propagate(False)
        self.homeresu_pageThree_L1S2.pack(side=LEFT)
        
        self.homeresu_pageThree_L1Score1 = Label(self.homeresu_pageThree_L1S2, text="12", bg="White")
        self.homeresu_pageThree_L1Score1.pack(pady=12)
        
        
        self.homeresu_pageThree_L1S4 = Frame(self.homeresu_pageThree_L1, width=100, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageThree_L1S4.pack_propagate(False)
        self.homeresu_pageThree_L1S4.pack(side=RIGHT)        
        
        self.homeresu_pageThree_L1Team2 = Label(self.homeresu_pageThree_L1S4, text="First XI", bg="White")
        self.homeresu_pageThree_L1Team2.pack(pady=12)
        
        
        self.homeresu_pageThree_L1S3 = Frame(self.homeresu_pageThree_L1, width=52.5, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageThree_L1S3.pack_propagate(False)
        self.homeresu_pageThree_L1S3.pack(side=RIGHT)
        
        self.homeresu_pageThree_L1Score2 = Label(self.homeresu_pageThree_L1S3, text="63", bg="White")
        self.homeresu_pageThree_L1Score2.pack(pady=12)
    
        # Line 2 of the latest results
    
        self.homeresu_pageThree_L2 = Frame(self.homeresu_pageThree, width=305, height=45, bg="White")
        self.homeresu_pageThree_L2.pack_propagate(False)
        self.homeresu_pageThree_L2.pack()

        # Line subdivisions
        
        self.homeresu_pageThree_L2S1 = Frame(self.homeresu_pageThree_L2, width=100, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageThree_L2S1.pack_propagate(False)
        self.homeresu_pageThree_L2S1.pack(side=LEFT)
        
        self.homeresu_pageThree_L2Team1 = Label(self.homeresu_pageThree_L2S1, text="Second XI", bg="White")
        self.homeresu_pageThree_L2Team1.pack(pady=12)
        
        
        self.homeresu_pageThree_L2S2 = Frame(self.homeresu_pageThree_L2, width=52.5, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageThree_L2S2.pack_propagate(False)
        self.homeresu_pageThree_L2S2.pack(side=LEFT)
        
        self.homeresu_pageThree_L2Score1 = Label(self.homeresu_pageThree_L2S2, text="2645", bg="White")
        self.homeresu_pageThree_L2Score1.pack(pady=12)
        
        
        self.homeresu_pageThree_L2S4 = Frame(self.homeresu_pageThree_L2, width=100, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageThree_L2S4.pack_propagate(False)
        self.homeresu_pageThree_L2S4.pack(side=RIGHT)        
        
        self.homeresu_pageThree_L2Team2 = Label(self.homeresu_pageThree_L2S4, text="Second XI", bg="White")
        self.homeresu_pageThree_L2Team2.pack(pady=12)
        
        
        self.homeresu_pageThree_L2S3 = Frame(self.homeresu_pageThree_L2, width=52.5, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageThree_L2S3.pack_propagate(False)
        self.homeresu_pageThree_L2S3.pack(side=RIGHT)
        
        self.homeresu_pageThree_L2Score2 = Label(self.homeresu_pageThree_L2S3, text="1", bg="White")
        self.homeresu_pageThree_L2Score2.pack(pady=12)
        
        # Line 3 of the latest results
        
        self.homeresu_pageThree_L3 = Frame(self.homeresu_pageThree, width=305, height=45, bg="White")
        self.homeresu_pageThree_L3.pack_propagate(False)
        self.homeresu_pageThree_L3.pack()
        
        # Line subdivisions
        
        self.homeresu_pageThree_L3S1 = Frame(self.homeresu_pageThree_L3, width=100, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageThree_L3S1.pack_propagate(False)
        self.homeresu_pageThree_L3S1.pack(side=LEFT)
        
        self.homeresu_pageThree_L3Team1 = Label(self.homeresu_pageThree_L3S1, text="Junior", bg="White")
        self.homeresu_pageThree_L3Team1.pack(pady=12)
        
        
        self.homeresu_pageThree_L3S2 = Frame(self.homeresu_pageThree_L3, width=52.5, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageThree_L3S2.pack_propagate(False)
        self.homeresu_pageThree_L3S2.pack(side=LEFT)
        
        self.homeresu_pageThree_L3Score1 = Label(self.homeresu_pageThree_L3S2, text="753", bg="White")
        self.homeresu_pageThree_L3Score1.pack(pady=12)
        
        
        self.homeresu_pageThree_L3S4 = Frame(self.homeresu_pageThree_L3, width=100, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageThree_L3S4.pack_propagate(False)
        self.homeresu_pageThree_L3S4.pack(side=RIGHT)        
        
        self.homeresu_pageThree_L3Team2 = Label(self.homeresu_pageThree_L3S4, text="Junior", bg="White")
        self.homeresu_pageThree_L3Team2.pack(pady=12)
        
        
        self.homeresu_pageThree_L3S3 = Frame(self.homeresu_pageThree_L3, width=52.5, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageThree_L3S3.pack_propagate(False)
        self.homeresu_pageThree_L3S3.pack(side=RIGHT)
        
        self.homeresu_pageThree_L3Score2 = Label(self.homeresu_pageThree_L3S3, text="4", bg="White")
        self.homeresu_pageThree_L3Score2.pack(pady=12)
        
        # Fourth resu page (page_number = 4)

        self.homeresu_pageFour = Frame(self.homeresu_box, bg="White", width=305, height=135)
        self.homeresu_pageFour.pack_propagate(False)
        self.homeresu_pageFour.grid_propagate(False)
        
        # Divide the pages into 3 lines with each match
                                
        self.homeresu_pageFour_L1 = Frame(self.homeresu_pageFour, width=305, height=45, bg="White")
        self.homeresu_pageFour_L1.pack_propagate(False)
        self.homeresu_pageFour_L1.pack()

        # Divide the lines into 4 sections, 1 = MRGS TEAM, 2 = MRGS SCORE, 3 = OTHER SCORE, 4 = OTHER TEAM
        
        self.homeresu_pageFour_L1S1 = Frame(self.homeresu_pageFour_L1, width=100, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageFour_L1S1.pack_propagate(False)
        self.homeresu_pageFour_L1S1.pack(side=LEFT)
        
        self.homeresu_pageFour_L1Team1 = Label(self.homeresu_pageFour_L1S1, text="First XI", bg="White")
        self.homeresu_pageFour_L1Team1.pack(pady=12)
        
        
        self.homeresu_pageFour_L1S2 = Frame(self.homeresu_pageFour_L1, width=52.5, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageFour_L1S2.pack_propagate(False)
        self.homeresu_pageFour_L1S2.pack(side=LEFT)
        
        self.homeresu_pageFour_L1Score1 = Label(self.homeresu_pageFour_L1S2, text="3", bg="White")
        self.homeresu_pageFour_L1Score1.pack(pady=12)
        
        
        self.homeresu_pageFour_L1S4 = Frame(self.homeresu_pageFour_L1, width=100, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageFour_L1S4.pack_propagate(False)
        self.homeresu_pageFour_L1S4.pack(side=RIGHT)        
        
        self.homeresu_pageFour_L1Team2 = Label(self.homeresu_pageFour_L1S4, text="First XI", bg="White")
        self.homeresu_pageFour_L1Team2.pack(pady=12)
        
        
        self.homeresu_pageFour_L1S3 = Frame(self.homeresu_pageFour_L1, width=52.5, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageFour_L1S3.pack_propagate(False)
        self.homeresu_pageFour_L1S3.pack(side=RIGHT)
        
        self.homeresu_pageFour_L1Score2 = Label(self.homeresu_pageFour_L1S3, text="5", bg="White")
        self.homeresu_pageFour_L1Score2.pack(pady=12)
    
        # Line 2 of the latest results
    
        self.homeresu_pageFour_L2 = Frame(self.homeresu_pageFour, width=305, height=45, bg="White")
        self.homeresu_pageFour_L2.pack_propagate(False)
        self.homeresu_pageFour_L2.pack()

        # Line subdivisions
        
        self.homeresu_pageFour_L2S1 = Frame(self.homeresu_pageFour_L2, width=100, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageFour_L2S1.pack_propagate(False)
        self.homeresu_pageFour_L2S1.pack(side=LEFT)
        
        self.homeresu_pageFour_L2Team1 = Label(self.homeresu_pageFour_L2S1, text="Second XI", bg="White")
        self.homeresu_pageFour_L2Team1.pack(pady=12)
        
        
        self.homeresu_pageFour_L2S2 = Frame(self.homeresu_pageFour_L2, width=52.5, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageFour_L2S2.pack_propagate(False)
        self.homeresu_pageFour_L2S2.pack(side=LEFT)
        
        self.homeresu_pageFour_L2Score1 = Label(self.homeresu_pageFour_L2S2, text="193", bg="White")
        self.homeresu_pageFour_L2Score1.pack(pady=12)
        
        
        self.homeresu_pageFour_L2S4 = Frame(self.homeresu_pageFour_L2, width=100, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageFour_L2S4.pack_propagate(False)
        self.homeresu_pageFour_L2S4.pack(side=RIGHT)        
        
        self.homeresu_pageFour_L2Team2 = Label(self.homeresu_pageFour_L2S4, text="Second XI", bg="White")
        self.homeresu_pageFour_L2Team2.pack(pady=12)
        
        
        self.homeresu_pageFour_L2S3 = Frame(self.homeresu_pageFour_L2, width=52.5, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageFour_L2S3.pack_propagate(False)
        self.homeresu_pageFour_L2S3.pack(side=RIGHT)
        
        self.homeresu_pageFour_L2Score2 = Label(self.homeresu_pageFour_L2S3, text="645", bg="White")
        self.homeresu_pageFour_L2Score2.pack(pady=12)
        
        # Line 3 of the latest results
        
        self.homeresu_pageFour_L3 = Frame(self.homeresu_pageFour, width=305, height=45, bg="White")
        self.homeresu_pageFour_L3.pack_propagate(False)
        self.homeresu_pageFour_L3.pack()
        
        # Line subdivisions
        
        self.homeresu_pageFour_L3S1 = Frame(self.homeresu_pageFour_L3, width=100, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageFour_L3S1.pack_propagate(False)
        self.homeresu_pageFour_L3S1.pack(side=LEFT)
        
        self.homeresu_pageFour_L3Team1 = Label(self.homeresu_pageFour_L3S1, text="Junior", bg="White")
        self.homeresu_pageFour_L3Team1.pack(pady=12)
        
        
        self.homeresu_pageFour_L3S2 = Frame(self.homeresu_pageFour_L3, width=52.5, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageFour_L3S2.pack_propagate(False)
        self.homeresu_pageFour_L3S2.pack(side=LEFT)
        
        self.homeresu_pageFour_L3Score1 = Label(self.homeresu_pageFour_L3S2, text="2", bg="White")
        self.homeresu_pageFour_L3Score1.pack(pady=12)
        
        
        self.homeresu_pageFour_L3S4 = Frame(self.homeresu_pageFour_L3, width=100, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageFour_L3S4.pack_propagate(False)
        self.homeresu_pageFour_L3S4.pack(side=RIGHT)        
        
        self.homeresu_pageFour_L3Team2 = Label(self.homeresu_pageFour_L3S4, text="Junior", bg="White")
        self.homeresu_pageFour_L3Team2.pack(pady=12)
        
        
        self.homeresu_pageFour_L3S3 = Frame(self.homeresu_pageFour_L3, width=52.5, height=45, bg="White", relief=SUNKEN, bd=0.5)
        self.homeresu_pageFour_L3S3.pack_propagate(False)
        self.homeresu_pageFour_L3S3.pack(side=RIGHT)
        
        self.homeresu_pageFour_L3Score2 = Label(self.homeresu_pageFour_L3S3, text="26", bg="White")
        self.homeresu_pageFour_L3Score2.pack(pady=12)
        
        # Home resu page indicator
            # which page is shown, to be replaced by a different indicator like 4 circles total, and the greyed out circle is the current page
        
        self.homeresu_bottom = Frame(self.homeresu_box, width=305, height=26, bg="White", relief=SUNKEN, bd=0.5)  
        self.homeresu_bottom.pack_propagate(False)
        self.homeresu_bottom.grid(row=2,columnspan=TRUE)
        
        self.page_indicator = Label(self.homeresu_bottom, text=self.page_number, relief=RIDGE, bg="White", width=5, height=1)
        self.page_indicator.pack(pady=2)

        #If MRGS Score is greater than other score then config it to green font colour and the other to red font colour

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
        
    def student_login(self):
        self.login_page.pack_forget()
        self.logo_frame.grid(row=0, column=0)
        self.content_frame.grid(row=1, column=0)
        self.navigation_bar.grid(row=2, column=0)
     
    def teacher_login(self):
        self.login_page.pack_forget()
        self.teacher_login_page.pack()
        
    def tcode_confirm(self):
        entered_code = self.teacher_input.get() # Retrieve the entered code from the entry box
        if entered_code == self.teacher_code: # Compare the two
            self.create_upcoming_button.pack(pady=50)
            self.create_result_button.pack()
            self.tlogin_logo.pack(pady=70)
        elif entered_code == "":
            messagebox.showerror("Box left empty ", "No code entered, please enter your teacher code.") # If the box is left empty, the user is shown an error, and told to enter a code, the buttons will also be removed if this is done after the correct teacher code is entered as a precaution
            self.create_upcoming_button.pack_forget()
            self.create_result_button.pack_forget()
            self.tlogin_logo.pack_forget()
        else:
            messagebox.showerror("Invalid Code", "Invalid teacher code. Please try again.") # If they enter the wrong code or something random, the user is shown an error, and told to enter a code, the buttons will also be removed if this is done after the correct teacher code is entered as a precaution
            self.create_upcoming_button.pack_forget()
            self.create_result_button.pack_forget()
            self.tlogin_logo.pack_forget()        
                 
    def show_upcoming_creator(self):
        self.teacher_login_page.pack_forget()
        self.upcoming_sched_page.pack()
        
    def show_result_creator(self):
        self.teacher_login_page.pack_forget()
        self.result_enter_page.pack()
        
    def enter_upcoming_game(self):
        sport = self.upcoming_sport_entry.get()
        team = self.upcoming_team_entry.get()
        day = self.upcoming_weekday.get()
        time = self.upcoming_time.get()
        
        if sport and team and day and time:
            new_game = {
                "sport": sport,
                "team": team,
                "day": day,
                "time": time
            }
            
            # Load existing data
            try:
                with open("schedule.json", "r") as file:
                    schedule_data = json.load(file)
            except FileNotFoundError:
                schedule_data = []
            
            # Add new data
            schedule_data.append(new_game)
            
            # Save updated data
            with open("schedule.json", "w") as file:
                json.dump(schedule_data, file, indent=4)
            
            self.update_treeview(schedule_data)
            self.update_labels(new_game)

    def load_schedule_data(self):
        try:
            with open("schedule.json", "r") as file:
                schedule_data = json.load(file)
                self.update_treeview(schedule_data)
        except FileNotFoundError:
            pass
        
    def update_treeview(self, schedule_data):
        for row in self.trv.get_children():
            self.trv.delete(row)
        
        for game in schedule_data:
            self.trv.insert("", "end", values=(game["sport"], game["team"], game["day"], game["time"]))
            
    def update_labels(self, latest_game):
        # Assuming you have labels to display the latest entry data
        self.latest_sport_label = Label(self.upcoming_sched_bottom, text=f"Sport: {latest_game['sport']}")
        self.latest_sport_label.pack()
        
        self.latest_team_label = Label(self.upcoming_sched_bottom, text=f"Team: {latest_game['team']}")
        self.latest_team_label.pack()
        
        self.latest_day_label = Label(self.upcoming_sched_bottom, text=f"Day: {latest_game['day']}")
        self.latest_day_label.pack()
        
        self.latest_time_label = Label(self.upcoming_sched_bottom, text=f"Time: {latest_game['time']}")
        self.latest_time_label.pack()  
     
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