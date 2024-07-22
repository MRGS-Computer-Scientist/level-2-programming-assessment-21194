#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox, ttk, font
from app_settings import *
from os import *

w_width = 400
w_height = 850
margin_length = 30


class App:

    def __init__(self):
        self.window = Tk()
        self.window.geometry(str(w_width) + 'x' + str(w_height))
        self.window.title('MRGSports')

        # self.title_font and other fonts to replace unnecessary code

        self.header_font = font.Font(family='Cairo', size=16,
                weight='bold')
        self.subheader_font = font.Font(family='Helvetica', size=12,
                weight='bold')
        self.button_font = font.Font(family='Helvetica', size=14)

        self.page_number = 1
        self.max_page_numbers = 4

        self.teacher_code = 'KMR'
        self.teacher_input = StringVar()

        self.upcoming_weekday = StringVar()
        self.upcoming_time = StringVar()

        self.opposing_firstxi_team = StringVar()
        self.opposing_secondxi_team = StringVar()
        self.opposing_junior_team = StringVar()

        self.our_firstxi_score = StringVar()
        self.our_secondxi_score = StringVar()
        self.our_junior_score = StringVar()

        self.their_firstxi_score = StringVar()
        self.their_secondxi_score = StringVar()
        self.their_junior_score = StringVar()

        self.firstxi_wins = StringVar()
        self.secondxi_wins = StringVar()
        self.junior_wins = StringVar()

        self.firstxi_losses = StringVar()
        self.secondxi_losses = StringVar()
        self.junior_losses = StringVar()

        self.sports = ['Football', 'Basketball', 'Hockey', 'Rugby']
        self.teams = [
            'First XI Boys',
            'First XI Girls',
            'Second XI Boys',
            'Second XI Girls',
            'Junior Boys',
            'Junior Girls',
            ]
        self.weekdays = [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday',
            ]
        self.hours = [
            '00',
            '01',
            '02',
            '03',
            '04',
            '05',
            '06',
            '07',
            '08',
            '09',
            '10',
            '11',
            '12',
            '13',
            '14',
            '15',
            '16',
            '17',
            '18',
            '19',
            '20',
            '21',
            '22',
            '23',
            ]
        self.minutes = [
            '00',
            '05',
            '10',
            '15',
            '20',
            '25',
            '30',
            '35',
            '40',
            '45',
            '50',
            '55',
            ]

        # Login page

        self.login_page = Frame(self.window, background='#FC6736',
                                width=w_width, height=w_height)
        self.login_page.pack_propagate(False)
        self.login_page.pack()

        self.login_logo = Label(self.login_page, text='MRGSports',
                                bg='#FC6736', fg='White',
                                font=('Courier', 45, 'bold'))
        self.login_logo.pack(pady=190)

        self.login_question = Frame(self.login_page, width=w_width,
                                    height=300, bg='#FC6736')
        self.login_question.pack_propagate(False)
        self.login_question.pack(pady=5)

        self.login_text = Label(
            self.login_question,
            text='Are you a...',
            bg='#FC6736',
            width=w_width,
            height=2,
            fg='White',
            font=('Helvetica', 20),
            )
        self.login_text.pack(pady=40)

        self.login_buttons = Frame(self.login_question, width=w_width,
                                   height=200, bg='#FC6736')
        self.login_buttons.pack_propagate(False)
        self.login_buttons.pack()

        self.login_student_button = Button(
            self.login_buttons,
            text='Student',
            font=self.button_font,
            bg='White',
            fg='#FC6736',
            width=15,
            height=5,
            command=self.student_login,
            )
        self.login_student_button.pack(side=LEFT, padx=15)

        self.login_teacher_button = Button(
            self.login_buttons,
            text='Teacher',
            font=self.button_font,
            bg='White',
            fg='#FC6736',
            width=15,
            height=5,
            command=self.teacher_login,
            )
        self.login_teacher_button.pack(side=RIGHT, padx=15)

        # Teacher page

        self.teacher_login_page = Frame(self.window,
                background='#EFECEC', width=w_width, height=w_height)
        self.teacher_login_page.pack_propagate(False)

        # Top section of the login page, the entry for the teacher code is here

        self.tlogin_top = Frame(self.teacher_login_page,
                                background='#EFECEC', width=w_width,
                                height=300)
        self.tlogin_top.pack_propagate(False)
        self.tlogin_top.pack()

        self.tcode_space_box = Frame(self.tlogin_top,
                background='#EFECEC', width=w_width, height=80)
        self.tcode_space_box.pack_propagate(False)
        self.tcode_space_box.pack()

        self.tcode_input_cancel = Button(self.tcode_space_box,
                text='Close', bg='White', font=self.button_font,
                command=self.back_to_login)
        self.tcode_input_cancel.pack(pady=25)

        self.tcode_input_box = Frame(
            self.tlogin_top,
            background='White',
            width=320,
            height=140,
            bd=3,
            relief=GROOVE,
            )
        self.tcode_input_box.pack_propagate(False)
        self.tcode_input_box.pack()

        self.tcode_input_label = Label(self.tcode_input_box,
                text="Please enter your teacher code, e.g. 'MCS'",
                bg='White', font=('Helvetica', 12))
        self.tcode_input_label.pack(pady=5)

        self.tcode_input_entry = Entry(self.tcode_input_box,
                textvariable=self.teacher_input, font=('Helvetica', 14))
        self.tcode_input_entry.pack(pady=5)

        self.tcode_input_confirm = Button(self.tcode_input_box,
                text='Confirm', bg='White', font=self.button_font,
                command=self.tcode_confirm)
        self.tcode_input_confirm.pack(pady=5)

        # The buttons and logo appear only after the teacher code has been entered and will also be removed if the incorrect code is entered afterwards

        self.tlogin_bottom = Frame(self.teacher_login_page,
                                   background='#FC6736', width=w_width,
                                   height=550)
        self.tlogin_bottom.pack_propagate(False)
        self.tlogin_bottom.pack()

        self.create_upcoming_button = Button(
            self.tlogin_bottom,
            text='Schedule an upcoming match',
            font=self.button_font,
            background='White',
            width=30,
            height=3,
            command=self.show_upcoming_creator,
            )

        self.create_result_button = Button(
            self.tlogin_bottom,
            text='Enter a match result',
            font=self.button_font,
            background='White',
            width=30,
            height=3,
            command=self.show_result_creator,
            )

        self.tlogin_logo = Label(self.tlogin_bottom, text='MRGSports',
                                 bg='#FC6736', fg='White',
                                 font=('Courier', 45, 'bold'))

        # Upcoming match scheduling page

        self.upcoming_sched_page = Frame(self.window,
                background='#EFECEC', width=w_width, height=w_height)
        self.upcoming_sched_page.pack_propagate(False)

        self.upcoming_sched_top = Frame(self.upcoming_sched_page,
                background='#EFECEC', width=w_width, height=650)
        self.upcoming_sched_top.pack_propagate(False)
        self.upcoming_sched_top.pack()

        self.upcoming_sched_title = Label(self.upcoming_sched_top,
                bg='#EFECEC', text='Schedule a match for next week',
                font=('Helvetica', 18, 'bold'))
        self.upcoming_sched_title.pack()

        self.upcoming_sched_disclaimer = Label(self.upcoming_sched_top,
                bg='#EFECEC',
                text='You may only schedule one match per sport',
                font=('Helvetica', 14))
        self.upcoming_sched_disclaimer.pack()

        self.upcoming_sched_holder = Frame(
            self.upcoming_sched_top,
            bg='White',
            width=360,
            height=500,
            relief=RIDGE,
            bd=3,
            )
        self.upcoming_sched_holder.pack_propagate(False)
        self.upcoming_sched_holder.pack(pady=15)

        self.upcoming_sport_label = Label(self.upcoming_sched_holder,
                bg='White', text='Sport', font=('Helvetica', 11))
        self.upcoming_sport_label.pack(pady=5)

        self.upcoming_sport_entry = \
            ttk.Combobox(self.upcoming_sched_holder, values=self.sports)
        self.upcoming_sport_entry.pack()

        self.upcoming_team_label = Label(self.upcoming_sched_holder,
                bg='White', text='Team', font=('Helvetica', 11))
        self.upcoming_team_label.pack(pady=5)

        self.upcoming_team_entry = \
            ttk.Combobox(self.upcoming_sched_holder, values=self.teams)
        self.upcoming_team_entry.pack()

        self.upcoming_weekday_label = Label(self.upcoming_sched_holder,
                bg='White',
                text='What day next week will the game be? (e.g. Monday)'
                , font=('Helvetica', 11))
        self.upcoming_weekday_label.pack(pady=5)

        self.upcoming_weekday_entry = \
            ttk.Combobox(self.upcoming_sched_holder,
                         values=self.weekdays)
        self.upcoming_weekday_entry.pack()

        self.upcoming_time_label = Label(self.upcoming_sched_holder,
                bg='White',
                text='What time on this day will the game be?',
                font=('Helvetica', 11))
        self.upcoming_time_label.pack(pady=5)

        self.upcoming_time_label2 = Label(self.upcoming_sched_holder,
                bg='White', text='Hour of the day', font=('Helvetica',
                11))
        self.upcoming_time_label2.pack()

        self.upcoming_time_hours = \
            ttk.Combobox(self.upcoming_sched_holder, values=self.hours)
        self.upcoming_time_hours.pack()

        self.upcoming_time_label3 = Label(self.upcoming_sched_holder,
                bg='White', text='Minute of the hour', font=('Helvetica'
                , 11))
        self.upcoming_time_label3.pack()

        self.upcoming_time_minutes = \
            ttk.Combobox(self.upcoming_sched_holder,
                         values=self.minutes)
        self.upcoming_time_minutes.pack()

        self.upcoming_sched_disclaimer2 = \
            Label(self.upcoming_sched_holder, bg='White',
                  text='Re-enter data into boxes if a mistake is made',
                  font=('Helvetica', 12))
        self.upcoming_sched_disclaimer2.pack(pady=60)

        self.upcoming_sched_bottom = Frame(self.upcoming_sched_page,
                background='#FC6736', width=w_width, height=200)
        self.upcoming_sched_bottom.pack_propagate(False)
        self.upcoming_sched_bottom.pack()

        self.upcoming_data_confirm = Button(
            self.upcoming_sched_bottom,
            text='Done',
            width=6,
            bg='White',
            font=self.button_font,
            command=self.change_upcoming_labels,
            )
        self.upcoming_data_confirm.pack(side=RIGHT, padx=45)

        self.upcoming_data_cancel = Button(
            self.upcoming_sched_bottom,
            text='Cancel',
            width=6,
            bg='White',
            font=self.button_font,
            command=self.cancel_sched,
            )
        self.upcoming_data_cancel.pack(side=LEFT, padx=45)

        # Result entering page

        self.result_enter_page = Frame(self.window, background='#EFECEC'
                , width=w_width, height=w_height)
        self.result_enter_page.pack_propagate(False)

        self.result_enter_top = Frame(self.result_enter_page,
                background='#EFECEC', width=w_width, height=650)
        self.result_enter_top.pack_propagate(False)
        self.result_enter_top.pack()

        self.result_enter_title = Label(self.result_enter_top,
                bg='#EFECEC', text='Enter the latest results',
                font=('Helvetica', 18, 'bold'))
        self.result_enter_title.pack()

        self.result_enter_disclaimer = Label(self.result_enter_top,
                bg='#EFECEC',
                text='You may only enter one result per team',
                font=('Helvetica', 14))
        self.result_enter_disclaimer.pack()

        self.result_enter_holder = Frame(
            self.result_enter_top,
            bg='White',
            width=360,
            height=500,
            relief=RIDGE,
            bd=3,
            )
        self.result_enter_holder.pack_propagate(False)
        self.result_enter_holder.pack(pady=15)

        # Sport chooser

        self.result_sport_label = Label(self.result_enter_holder,
                bg='White', text='Sport', font=('Helvetica', 11))
        self.result_sport_label.pack(pady=5)

        self.result_sport_entry = \
            ttk.Combobox(self.result_enter_holder, values=self.sports)
        self.result_sport_entry.pack()

        # Opposing team layout

        self.result_opposing_label = Label(self.result_enter_holder,
                bg='White',
                text='What team did MRGS play against? (e.g. MAGS)',
                font=('Helvetica', 11))
        self.result_opposing_label.pack(pady=5)

        self.result_space_holder = Frame(self.result_enter_holder,
                bg='White', width=360, height=60)
        self.result_space_holder.pack_propagate(False)
        self.result_space_holder.pack()

        self.result_enter_firstxi_holder = \
            Frame(self.result_space_holder, bg='White', width=120,
                  height=60)
        self.result_enter_firstxi_holder.pack_propagate(False)
        self.result_enter_firstxi_holder.pack(side=LEFT)

        self.result_enter_secondxi_holder = \
            Frame(self.result_space_holder, bg='White', width=120,
                  height=60)
        self.result_enter_secondxi_holder.pack_propagate(False)
        self.result_enter_secondxi_holder.pack(side=LEFT)

        self.result_enter_junior_holder = \
            Frame(self.result_space_holder, bg='White', width=120,
                  height=60)
        self.result_enter_junior_holder.pack_propagate(False)
        self.result_enter_junior_holder.pack(side=LEFT)

        self.result_firstxi_label = \
            Label(self.result_enter_firstxi_holder, bg='White',
                  text='First XI', font=('Helvetica', 11))
        self.result_firstxi_label.pack()

        self.result_secondxi_label = \
            Label(self.result_enter_secondxi_holder, bg='White',
                  text='Second XI', font=('Helvetica', 11))
        self.result_secondxi_label.pack()

        self.result_junior_label = \
            Label(self.result_enter_junior_holder, bg='White',
                  text='Junior', font=('Helvetica', 11))
        self.result_junior_label.pack()

        # Opposing team entries

        self.result_opposing_entry = \
            Entry(self.result_enter_firstxi_holder,
                  textvariable=self.opposing_firstxi_team)
        self.result_opposing_entry.pack()

        self.result_opposing_entry2 = \
            Entry(self.result_enter_secondxi_holder,
                  textvariable=self.opposing_secondxi_team)
        self.result_opposing_entry2.pack()

        self.result_opposing_entry3 = \
            Entry(self.result_enter_junior_holder,
                  textvariable=self.opposing_junior_team)
        self.result_opposing_entry3.pack()

        # MRGS score

        self.result_score_label = Label(self.result_enter_holder,
                bg='White', text='What was the match score?',
                font=('Helvetica', 11))
        self.result_score_label.pack(pady=15)

        self.result_score_label2 = Label(self.result_enter_holder,
                bg='White', text='MRGS Score', font=('Helvetica', 11))
        self.result_score_label2.pack()

        self.result_space_holder2 = Frame(self.result_enter_holder,
                bg='White', width=360, height=30)
        self.result_space_holder2.pack_propagate(False)
        self.result_space_holder2.pack()

        self.result_enter_firstxi_holder2 = \
            Frame(self.result_space_holder2, bg='White', width=120,
                  height=30)
        self.result_enter_firstxi_holder2.pack_propagate(False)
        self.result_enter_firstxi_holder2.pack(side=LEFT)

        self.result_enter_secondxi_holder2 = \
            Frame(self.result_space_holder2, bg='White', width=120,
                  height=30)
        self.result_enter_secondxi_holder2.pack_propagate(False)
        self.result_enter_secondxi_holder2.pack(side=LEFT)

        self.result_enter_junior_holder2 = \
            Frame(self.result_space_holder2, bg='White', width=120,
                  height=30)
        self.result_enter_junior_holder2.pack_propagate(False)
        self.result_enter_junior_holder2.pack(side=LEFT)

        # MRGS score entries

        self.result_mrgs_score = \
            Entry(self.result_enter_firstxi_holder2,
                  textvariable=self.our_firstxi_score)
        self.result_mrgs_score.pack()

        self.result_mrgs_score2 = \
            Entry(self.result_enter_secondxi_holder2,
                  textvariable=self.our_secondxi_score)
        self.result_mrgs_score2.pack()

        self.result_mrgs_score3 = \
            Entry(self.result_enter_junior_holder2,
                  textvariable=self.our_junior_score)
        self.result_mrgs_score3.pack()

        # Opposing score

        self.result_score_label3 = Label(self.result_enter_holder,
                bg='White', text='Opposing score', font=('Helvetica',
                11))
        self.result_score_label3.pack()

        self.result_space_holder3 = Frame(self.result_enter_holder,
                bg='White', width=360, height=30)
        self.result_space_holder3.pack_propagate(False)
        self.result_space_holder3.pack()

        self.result_enter_firstxi_holder3 = \
            Frame(self.result_space_holder3, bg='White', width=120,
                  height=30)
        self.result_enter_firstxi_holder3.pack_propagate(False)
        self.result_enter_firstxi_holder3.pack(side=LEFT)

        self.result_enter_secondxi_holder3 = \
            Frame(self.result_space_holder3, bg='White', width=120,
                  height=30)
        self.result_enter_secondxi_holder3.pack_propagate(False)
        self.result_enter_secondxi_holder3.pack(side=LEFT)

        self.result_enter_junior_holder3 = \
            Frame(self.result_space_holder3, bg='White', width=120,
                  height=30)
        self.result_enter_junior_holder3.pack_propagate(False)
        self.result_enter_junior_holder3.pack(side=LEFT)

        # Opposing score entries

        self.result_opposing_score = \
            Entry(self.result_enter_firstxi_holder3,
                  textvariable=self.their_firstxi_score)
        self.result_opposing_score.pack()

        self.result_opposing_score2 = \
            Entry(self.result_enter_secondxi_holder3,
                  textvariable=self.their_secondxi_score)
        self.result_opposing_score2.pack()

        self.result_opposing_score3 = \
            Entry(self.result_enter_junior_holder3,
                  textvariable=self.their_junior_score)
        self.result_opposing_score3.pack()

        # Win loss record

        self.result_score_label4 = Label(self.result_enter_holder,
                bg='White', text='Total Wins this season',
                font=('Helvetica', 11))
        self.result_score_label4.pack()

        self.result_space_holder4 = Frame(self.result_enter_holder,
                bg='White', width=360, height=30)
        self.result_space_holder4.pack_propagate(False)
        self.result_space_holder4.pack()

        self.result_enter_firstxi_holder4 = \
            Frame(self.result_space_holder4, bg='White', width=120,
                  height=30)
        self.result_enter_firstxi_holder4.pack_propagate(False)
        self.result_enter_firstxi_holder4.pack(side=LEFT)

        self.result_enter_secondxi_holder4 = \
            Frame(self.result_space_holder4, bg='White', width=120,
                  height=30)
        self.result_enter_secondxi_holder4.pack_propagate(False)
        self.result_enter_secondxi_holder4.pack(side=LEFT)

        self.result_enter_junior_holder4 = \
            Frame(self.result_space_holder4, bg='White', width=120,
                  height=30)
        self.result_enter_junior_holder4.pack_propagate(False)
        self.result_enter_junior_holder4.pack(side=LEFT)

        # Wins entries

        self.result_wins = Entry(self.result_enter_firstxi_holder4,
                                 textvariable=self.firstxi_wins)
        self.result_wins.pack()

        self.result_wins2 = Entry(self.result_enter_secondxi_holder4,
                                  textvariable=self.secondxi_wins)
        self.result_wins2.pack()

        self.result_wins3 = Entry(self.result_enter_junior_holder4,
                                  textvariable=self.junior_wins)
        self.result_wins3.pack()

        # Losses entries

        self.result_score_label5 = Label(self.result_enter_holder,
                bg='White', text='Total Losses this season',
                font=('Helvetica', 11))
        self.result_score_label5.pack()

        self.result_space_holder5 = Frame(self.result_enter_holder,
                bg='White', width=360, height=30)
        self.result_space_holder5.pack_propagate(False)
        self.result_space_holder5.pack()

        self.result_enter_firstxi_holder5 = \
            Frame(self.result_space_holder5, bg='White', width=120,
                  height=30)
        self.result_enter_firstxi_holder5.pack_propagate(False)
        self.result_enter_firstxi_holder5.pack(side=LEFT)

        self.result_enter_secondxi_holder5 = \
            Frame(self.result_space_holder5, bg='White', width=120,
                  height=30)
        self.result_enter_secondxi_holder5.pack_propagate(False)
        self.result_enter_secondxi_holder5.pack(side=LEFT)

        self.result_enter_junior_holder5 = \
            Frame(self.result_space_holder5, bg='White', width=120,
                  height=30)
        self.result_enter_junior_holder5.pack_propagate(False)
        self.result_enter_junior_holder5.pack(side=LEFT)

        # Wins entries

        self.result_losses = Entry(self.result_enter_firstxi_holder5,
                                   textvariable=self.firstxi_losses)
        self.result_losses.pack()

        self.result_losses2 = Entry(self.result_enter_secondxi_holder5,
                                    textvariable=self.secondxi_losses)
        self.result_losses2.pack()

        self.result_losses3 = Entry(self.result_enter_junior_holder5,
                                    textvariable=self.junior_losses)
        self.result_losses3.pack()

        self.result_enter_disclaimer2 = Label(self.result_enter_holder,
                bg='White',
                text='Re-enter data for sport if a mistake is made',
                font=('Helvetica', 12))
        self.result_enter_disclaimer2.pack(pady=20)

        # Bottom of the page

        self.result_enter_bottom = Frame(self.result_enter_page,
                background='#FC6736', width=w_width, height=200)
        self.result_enter_bottom.pack_propagate(False)
        self.result_enter_bottom.pack()

        self.result_data_confirm = Button(
            self.result_enter_bottom,
            text='Done',
            width=6,
            bg='White',
            font=self.button_font,
            command=self.change_result_labels,
            )
        self.result_data_confirm.pack(side=RIGHT, padx=45)

        self.result_data_cancel = Button(
            self.result_enter_bottom,
            text='Cancel',
            width=6,
            bg='White',
            font=self.button_font,
            command=self.cancel_sched,
            )
        self.result_data_cancel.pack(side=LEFT, padx=45)

        # ---------------------- STUDENT PAGES BELOW ----------------------

        # Logo frame

        self.logo_frame = Frame(self.window, background='#FC6736',
                                width=w_width, height=100)
        self.logo_frame.pack_propagate(False)

        self.logo_text = Label(self.logo_frame, text='MRGSports',
                               bg='#FC6736', fg='White', font=('Courier'
                               , 28, 'bold'))
        self.logo_text.pack(pady=8)

        self.student_back = Button(self.logo_frame, text='Close',
                                   bg='White', font=('Helvetica', 10),
                                   command=self.back_to_login)
        self.student_back.pack(pady=5)

        # Content frame containing the main student pages that are shown

        self.content_frame = Frame(self.window, background='Black',
                                   width=w_width, height=600)
        self.content_frame.grid_propagate(False)
        self.content_frame.pack_propagate(False)

        # Home page frame

        self.home_page = Frame(self.content_frame, background='#EFECEC'
                               , width=w_width, height=600)
        self.home_page.pack_propagate(False)
        self.home_page.grid_propagate(False)
        self.home_page.grid(rowspan=TRUE, columnspan=TRUE)

        # Upcoming section of the home page

        self.upcoming_main = Frame(self.home_page, width=w_width
                                   - margin_length, height=330,
                                   bg='#EFECEC')
        self.upcoming_main.pack_propagate(False)
        self.upcoming_main.pack()

        self.home_header_one = Label(self.upcoming_main, text='UPCOMING'
                , bg='#EFECEC', font=self.header_font)
        self.home_header_one.pack(padx=20, pady=5)

        # First upcoming display, it is split up into 5 rows called one, two, three, four, and five which show the most relevant and most imminent sport matches for the school

        self.upcoming_row_one = Frame(self.upcoming_main, bg='#EFECEC',
                width=w_width - margin_length, height=70)
        self.upcoming_row_one.pack()

        self.upcoming_box_game = Frame(
            self.upcoming_row_one,
            bg='White',
            width=200,
            height=50,
            bd=3,
            relief=RIDGE,
            )
        self.upcoming_box_game.pack_propagate(False)
        self.upcoming_box_game.pack(side=LEFT, padx=4.5, pady=3)

        self.upcoming_game_one = Label(self.upcoming_box_game,
                text='Football Game', bg='White')
        self.upcoming_game_one.pack()

        self.upcoming_team_one = Label(self.upcoming_box_game,
                text='N/A', bg='White')
        self.upcoming_team_one.pack()

        self.upcoming_box_time = Frame(
            self.upcoming_row_one,
            bg='White',
            width=100,
            height=50,
            bd=3,
            relief=RIDGE,
            )
        self.upcoming_box_time.pack_propagate(False)
        self.upcoming_box_time.pack(side=RIGHT, padx=4.5, pady=3)

        self.upcoming_day_one = Label(self.upcoming_box_time, text='N/A'
                , bg='White')
        self.upcoming_day_one.pack()

        self.upcoming_time_one = Label(self.upcoming_box_time,
                text='N/A', bg='White')
        self.upcoming_time_one.pack()

        # Second upcoming display

        self.upcoming_row_two = Frame(self.upcoming_main, bg='#EFECEC',
                width=w_width - margin_length, height=70)
        self.upcoming_row_two.pack()

        self.upcoming_box_game2 = Frame(
            self.upcoming_row_two,
            bg='White',
            width=200,
            height=50,
            bd=3,
            relief=RIDGE,
            )
        self.upcoming_box_game2.pack_propagate(False)
        self.upcoming_box_game2.pack(side=LEFT, padx=4.5, pady=3)

        self.upcoming_game_two = Label(self.upcoming_box_game2,
                text='Basketball Game', bg='White')
        self.upcoming_game_two.pack()

        self.upcoming_team_two = Label(self.upcoming_box_game2,
                text='N/A', bg='White')
        self.upcoming_team_two.pack()

        self.upcoming_box_time2 = Frame(
            self.upcoming_row_two,
            bg='White',
            width=100,
            height=50,
            bd=3,
            relief=RIDGE,
            )
        self.upcoming_box_time2.pack_propagate(False)
        self.upcoming_box_time2.pack(side=RIGHT, padx=4.5, pady=3)

        self.upcoming_day_two = Label(self.upcoming_box_time2,
                text='N/A', bg='White')
        self.upcoming_day_two.pack()

        self.upcoming_time_two = Label(self.upcoming_box_time2,
                text='N/A', bg='White')
        self.upcoming_time_two.pack()

        # Third upcoming display

        self.upcoming_row_three = Frame(self.upcoming_main, bg='#EFECEC'
                , width=w_width - margin_length, height=70)
        self.upcoming_row_three.pack()

        self.upcoming_box_game3 = Frame(
            self.upcoming_row_three,
            bg='White',
            width=200,
            height=50,
            bd=3,
            relief=RIDGE,
            )
        self.upcoming_box_game3.pack_propagate(False)
        self.upcoming_box_game3.pack(side=LEFT, padx=4.5, pady=3)

        self.upcoming_game_three = Label(self.upcoming_box_game3,
                text='Hockey Game', bg='White')
        self.upcoming_game_three.pack()

        self.upcoming_team_three = Label(self.upcoming_box_game3,
                text='N/A', bg='White')
        self.upcoming_team_three.pack()

        self.upcoming_box_time3 = Frame(
            self.upcoming_row_three,
            bg='White',
            width=100,
            height=50,
            bd=3,
            relief=RIDGE,
            )
        self.upcoming_box_time3.pack_propagate(False)
        self.upcoming_box_time3.pack(side=RIGHT, padx=4.5, pady=3)

        self.upcoming_day_three = Label(self.upcoming_box_time3,
                text='N/A', bg='White')
        self.upcoming_day_three.pack()

        self.upcoming_time_three = Label(self.upcoming_box_time3,
                text='N/A', bg='White')
        self.upcoming_time_three.pack()

        # Fourth upcoming display

        self.upcoming_row_four = Frame(self.upcoming_main, bg='#EFECEC'
                , width=w_width - margin_length, height=70)
        self.upcoming_row_four.pack()

        self.upcoming_box_game4 = Frame(
            self.upcoming_row_four,
            bg='White',
            width=200,
            height=50,
            bd=3,
            relief=RIDGE,
            )
        self.upcoming_box_game4.pack_propagate(False)
        self.upcoming_box_game4.pack(side=LEFT, padx=4.5, pady=3)

        self.upcoming_game_four = Label(self.upcoming_box_game4,
                text='Rugby Game', bg='White')
        self.upcoming_game_four.pack()

        self.upcoming_team_four = Label(self.upcoming_box_game4,
                text='N/A', bg='White')
        self.upcoming_team_four.pack()

        self.upcoming_box_time4 = Frame(
            self.upcoming_row_four,
            bg='White',
            width=100,
            height=50,
            bd=3,
            relief=RIDGE,
            )
        self.upcoming_box_time4.pack_propagate(False)
        self.upcoming_box_time4.pack(side=RIGHT, padx=4.5, pady=3)

        self.upcoming_day_four = Label(self.upcoming_box_time4,
                text='N/A', bg='White')
        self.upcoming_day_four.pack()

        self.upcoming_time_four = Label(self.upcoming_box_time4,
                text='N/A', bg='White')
        self.upcoming_time_four.pack()

        # Fifth upcoming display

        self.upcoming_row_five = Frame(self.upcoming_main, bg='#EFECEC'
                , width=w_width - margin_length, height=70)
        self.upcoming_row_five.pack()

        self.upcoming_box_game5 = Frame(
            self.upcoming_row_five,
            bg='White',
            width=200,
            height=50,
            bd=3,
            relief=RIDGE,
            )
        self.upcoming_box_game5.pack_propagate(False)
        self.upcoming_box_game5.pack(side=LEFT, padx=4.5, pady=3)

        self.upcoming_game_five = Label(self.upcoming_box_game5,
                text='Cricket Game', bg='White')
        self.upcoming_game_five.pack()

        self.upcoming_team_five = Label(self.upcoming_box_game5,
                text='Unavailable', bg='White')
        self.upcoming_team_five.pack()

        self.upcoming_box_time5 = Frame(
            self.upcoming_row_five,
            bg='White',
            width=100,
            height=50,
            bd=3,
            relief=RIDGE,
            )
        self.upcoming_box_time5.pack_propagate(False)
        self.upcoming_box_time5.pack(side=RIGHT, padx=4.5, pady=3)

        self.upcoming_day_five = Label(self.upcoming_box_time5,
                text='September', bg='White')
        self.upcoming_day_five.pack()

        self.upcoming_time_five = Label(self.upcoming_box_time5,
                text='Summer sport', bg='White')
        self.upcoming_time_five.pack()

        # End of upcoming/Start of res-this-week

        self.homeresu_main = Frame(self.home_page, width=w_width
                                   - margin_length, height=270,
                                   bg='#EFECEC')
        self.homeresu_main.pack_propagate(False)
        self.homeresu_main.pack()

        self.home_header_two = Label(self.homeresu_main,
                text='LATEST RESULTS', bg='#EFECEC',
                font=self.header_font)
        self.home_header_two.pack(padx=20, pady=5)

        self.homeresu_box = Frame(
            self.homeresu_main,
            bg='White',
            width=305,
            height=190,
            bd=3,
            relief=RIDGE,
            )
        self.homeresu_box.pack_propagate(False)
        self.homeresu_box.pack(padx=5, pady=3)

        # First resu page (no L/R button press)
        # Top is split into two parts "Left top" and "Right top"

        self.homeresu_top = Frame(
            self.homeresu_box,
            width=305,
            height=29,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_top.pack_propagate(False)
        self.homeresu_top.grid_propagate(False)
        self.homeresu_top.grid(row=0, column=0)

        self.homeresu_topLeft = Frame(self.homeresu_top, width=152.5,
                height=29, bg='White')
        self.homeresu_topLeft.pack_propagate(False)
        self.homeresu_topLeft.pack(side=LEFT)

        self.homeresu_sportname = Label(
            self.homeresu_topLeft,
            text='Football',
            relief=RIDGE,
            bg='White',
            width=10,
            height=1,
            )
        self.homeresu_sportname.pack(side=LEFT, padx=10, pady=2)

        self.homeresu_topRight = Frame(self.homeresu_top, width=152.5,
                height=29, bg='White')
        self.homeresu_topRight.pack_propagate(False)
        self.homeresu_topRight.pack(side=RIGHT)

        self.home_right_button = Button(self.homeresu_topRight,
                width=5, text='Right', bg='White', command=lambda : \
                self.go_to_next_page('right'))
        self.home_right_button.pack(side=RIGHT, padx=1, pady=1)

        self.home_left_button = Button(self.homeresu_topRight, width=5,
                text='Left', bg='White', command=lambda : \
                self.go_to_next_page('left'))
        self.home_left_button.pack(side=RIGHT, padx=5, pady=1)

        # Middle of homeresu, this is what changes on the button press containing the actual results
        # Home results page one

        self.homeresu_pageOne = Frame(self.homeresu_box, bg='White',
                width=305, height=135)
        self.homeresu_pageOne.pack_propagate(False)
        self.homeresu_pageOne.grid_propagate(False)
        self.homeresu_pageOne.grid(row=1, columnspan=TRUE)

        # Divide the pages into 3 lines with each match

        self.homeresu_pageOne_L1 = Frame(self.homeresu_pageOne,
                width=305, height=45, bg='White')
        self.homeresu_pageOne_L1.pack_propagate(False)
        self.homeresu_pageOne_L1.pack()

        # Divide the lines into 4 sections, 1 = MRGS TEAM, 2 = MRGS SCORE, 3 = OTHER SCORE, 4 = OTHER TEAM, Labels are configured when data is updated
        # L1 = Line 1, S1 = Section 1

        self.homeresu_pageOne_L1S1 = Frame(
            self.homeresu_pageOne_L1,
            width=100,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageOne_L1S1.pack_propagate(False)
        self.homeresu_pageOne_L1S1.pack(side=LEFT)

        self.homeresu_pageOne_L1Team1 = \
            Label(self.homeresu_pageOne_L1S1, text='First XI',
                  bg='White')
        self.homeresu_pageOne_L1Team1.pack(pady=12)

        self.homeresu_pageOne_L1S2 = Frame(
            self.homeresu_pageOne_L1,
            width=52.5,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageOne_L1S2.pack_propagate(False)
        self.homeresu_pageOne_L1S2.pack(side=LEFT)

        self.homeresu_pageOne_L1Score1 = \
            Label(self.homeresu_pageOne_L1S2, text='0', bg='White')
        self.homeresu_pageOne_L1Score1.pack(pady=12)

        self.homeresu_pageOne_L1S4 = Frame(
            self.homeresu_pageOne_L1,
            width=100,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageOne_L1S4.pack_propagate(False)
        self.homeresu_pageOne_L1S4.pack(side=RIGHT)

        self.homeresu_pageOne_L1Team2 = \
            Label(self.homeresu_pageOne_L1S4, text='N/A', bg='White')
        self.homeresu_pageOne_L1Team2.pack(pady=12)

        self.homeresu_pageOne_L1S3 = Frame(
            self.homeresu_pageOne_L1,
            width=52.5,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageOne_L1S3.pack_propagate(False)
        self.homeresu_pageOne_L1S3.pack(side=RIGHT)

        self.homeresu_pageOne_L1Score2 = \
            Label(self.homeresu_pageOne_L1S3, text='0', bg='White')
        self.homeresu_pageOne_L1Score2.pack(pady=12)

        # Line 2 of the latest results

        self.homeresu_pageOne_L2 = Frame(self.homeresu_pageOne,
                width=305, height=45, bg='White')
        self.homeresu_pageOne_L2.pack_propagate(False)
        self.homeresu_pageOne_L2.pack()

        # Line subdivisions

        self.homeresu_pageOne_L2S1 = Frame(
            self.homeresu_pageOne_L2,
            width=100,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageOne_L2S1.pack_propagate(False)
        self.homeresu_pageOne_L2S1.pack(side=LEFT)

        self.homeresu_pageOne_L2Team1 = \
            Label(self.homeresu_pageOne_L2S1, text='Second XI',
                  bg='White')
        self.homeresu_pageOne_L2Team1.pack(pady=12)

        self.homeresu_pageOne_L2S2 = Frame(
            self.homeresu_pageOne_L2,
            width=52.5,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageOne_L2S2.pack_propagate(False)
        self.homeresu_pageOne_L2S2.pack(side=LEFT)

        self.homeresu_pageOne_L2Score1 = \
            Label(self.homeresu_pageOne_L2S2, text='0', bg='White')
        self.homeresu_pageOne_L2Score1.pack(pady=12)

        self.homeresu_pageOne_L2S4 = Frame(
            self.homeresu_pageOne_L2,
            width=100,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageOne_L2S4.pack_propagate(False)
        self.homeresu_pageOne_L2S4.pack(side=RIGHT)

        self.homeresu_pageOne_L2Team2 = \
            Label(self.homeresu_pageOne_L2S4, text='N/A', bg='White')
        self.homeresu_pageOne_L2Team2.pack(pady=12)

        self.homeresu_pageOne_L2S3 = Frame(
            self.homeresu_pageOne_L2,
            width=52.5,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageOne_L2S3.pack_propagate(False)
        self.homeresu_pageOne_L2S3.pack(side=RIGHT)

        self.homeresu_pageOne_L2Score2 = \
            Label(self.homeresu_pageOne_L2S3, text='0', bg='White')
        self.homeresu_pageOne_L2Score2.pack(pady=12)

        # Line 3 of the latest results

        self.homeresu_pageOne_L3 = Frame(self.homeresu_pageOne,
                width=305, height=45, bg='White')
        self.homeresu_pageOne_L3.pack_propagate(False)
        self.homeresu_pageOne_L3.pack()

        # Line subdivisions

        self.homeresu_pageOne_L3S1 = Frame(
            self.homeresu_pageOne_L3,
            width=100,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageOne_L3S1.pack_propagate(False)
        self.homeresu_pageOne_L3S1.pack(side=LEFT)

        self.homeresu_pageOne_L3Team1 = \
            Label(self.homeresu_pageOne_L3S1, text='Junior', bg='White')
        self.homeresu_pageOne_L3Team1.pack(pady=12)

        self.homeresu_pageOne_L3S2 = Frame(
            self.homeresu_pageOne_L3,
            width=52.5,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageOne_L3S2.pack_propagate(False)
        self.homeresu_pageOne_L3S2.pack(side=LEFT)

        self.homeresu_pageOne_L3Score1 = \
            Label(self.homeresu_pageOne_L3S2, text='0', bg='White')
        self.homeresu_pageOne_L3Score1.pack(pady=12)

        self.homeresu_pageOne_L3S4 = Frame(
            self.homeresu_pageOne_L3,
            width=100,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageOne_L3S4.pack_propagate(False)
        self.homeresu_pageOne_L3S4.pack(side=RIGHT)

        self.homeresu_pageOne_L3Team2 = \
            Label(self.homeresu_pageOne_L3S4, text='N/A', bg='White')
        self.homeresu_pageOne_L3Team2.pack(pady=12)

        self.homeresu_pageOne_L3S3 = Frame(
            self.homeresu_pageOne_L3,
            width=52.5,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageOne_L3S3.pack_propagate(False)
        self.homeresu_pageOne_L3S3.pack(side=RIGHT)

        self.homeresu_pageOne_L3Score2 = \
            Label(self.homeresu_pageOne_L3S3, text='0', bg='White')
        self.homeresu_pageOne_L3Score2.pack(pady=12)

        # Second resu page (page_number = 2), exactly the same as the first page but the numbers must change

        self.homeresu_pageTwo = Frame(self.homeresu_box, bg='White',
                width=305, height=135)
        self.homeresu_pageTwo.pack_propagate(False)
        self.homeresu_pageTwo.grid_propagate(False)

        # Divide the pages into 3 lines with each match

        self.homeresu_pageTwo_L1 = Frame(self.homeresu_pageTwo,
                width=305, height=45, bg='White')
        self.homeresu_pageTwo_L1.pack_propagate(False)
        self.homeresu_pageTwo_L1.pack()

        # Divide the lines into 4 sections, 1 = MRGS TEAM, 2 = MRGS SCORE, 3 = OTHER SCORE, 4 = OTHER TEAM

        self.homeresu_pageTwo_L1S1 = Frame(
            self.homeresu_pageTwo_L1,
            width=100,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageTwo_L1S1.pack_propagate(False)
        self.homeresu_pageTwo_L1S1.pack(side=LEFT)

        self.homeresu_pageTwo_L1Team1 = \
            Label(self.homeresu_pageTwo_L1S1, text='First XI',
                  bg='White')
        self.homeresu_pageTwo_L1Team1.pack(pady=12)

        self.homeresu_pageTwo_L1S2 = Frame(
            self.homeresu_pageTwo_L1,
            width=52.5,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageTwo_L1S2.pack_propagate(False)
        self.homeresu_pageTwo_L1S2.pack(side=LEFT)

        self.homeresu_pageTwo_L1Score1 = \
            Label(self.homeresu_pageTwo_L1S2, text='0', bg='White')
        self.homeresu_pageTwo_L1Score1.pack(pady=12)

        self.homeresu_pageTwo_L1S4 = Frame(
            self.homeresu_pageTwo_L1,
            width=100,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageTwo_L1S4.pack_propagate(False)
        self.homeresu_pageTwo_L1S4.pack(side=RIGHT)

        self.homeresu_pageTwo_L1Team2 = \
            Label(self.homeresu_pageTwo_L1S4, text='N/A', bg='White')
        self.homeresu_pageTwo_L1Team2.pack(pady=12)

        self.homeresu_pageTwo_L1S3 = Frame(
            self.homeresu_pageTwo_L1,
            width=52.5,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageTwo_L1S3.pack_propagate(False)
        self.homeresu_pageTwo_L1S3.pack(side=RIGHT)

        self.homeresu_pageTwo_L1Score2 = \
            Label(self.homeresu_pageTwo_L1S3, text='0', bg='White')
        self.homeresu_pageTwo_L1Score2.pack(pady=12)

        # Line 2 of the latest results

        self.homeresu_pageTwo_L2 = Frame(self.homeresu_pageTwo,
                width=305, height=45, bg='White')
        self.homeresu_pageTwo_L2.pack_propagate(False)
        self.homeresu_pageTwo_L2.pack()

        # Line subdivisions

        self.homeresu_pageTwo_L2S1 = Frame(
            self.homeresu_pageTwo_L2,
            width=100,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageTwo_L2S1.pack_propagate(False)
        self.homeresu_pageTwo_L2S1.pack(side=LEFT)

        self.homeresu_pageTwo_L2Team1 = \
            Label(self.homeresu_pageTwo_L2S1, text='U17', bg='White')
        self.homeresu_pageTwo_L2Team1.pack(pady=12)

        self.homeresu_pageTwo_L2S2 = Frame(
            self.homeresu_pageTwo_L2,
            width=52.5,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageTwo_L2S2.pack_propagate(False)
        self.homeresu_pageTwo_L2S2.pack(side=LEFT)

        self.homeresu_pageTwo_L2Score1 = \
            Label(self.homeresu_pageTwo_L2S2, text='0', bg='White')
        self.homeresu_pageTwo_L2Score1.pack(pady=12)

        self.homeresu_pageTwo_L2S4 = Frame(
            self.homeresu_pageTwo_L2,
            width=100,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageTwo_L2S4.pack_propagate(False)
        self.homeresu_pageTwo_L2S4.pack(side=RIGHT)

        self.homeresu_pageTwo_L2Team2 = \
            Label(self.homeresu_pageTwo_L2S4, text='N/A', bg='White')
        self.homeresu_pageTwo_L2Team2.pack(pady=12)

        self.homeresu_pageTwo_L2S3 = Frame(
            self.homeresu_pageTwo_L2,
            width=52.5,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageTwo_L2S3.pack_propagate(False)
        self.homeresu_pageTwo_L2S3.pack(side=RIGHT)

        self.homeresu_pageTwo_L2Score2 = \
            Label(self.homeresu_pageTwo_L2S3, text='0', bg='White')
        self.homeresu_pageTwo_L2Score2.pack(pady=12)

        # Line 3 of the latest results

        self.homeresu_pageTwo_L3 = Frame(self.homeresu_pageTwo,
                width=305, height=45, bg='White')
        self.homeresu_pageTwo_L3.pack_propagate(False)
        self.homeresu_pageTwo_L3.pack()

        # Line subdivisions

        self.homeresu_pageTwo_L3S1 = Frame(
            self.homeresu_pageTwo_L3,
            width=100,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageTwo_L3S1.pack_propagate(False)
        self.homeresu_pageTwo_L3S1.pack(side=LEFT)

        self.homeresu_pageTwo_L3Team1 = \
            Label(self.homeresu_pageTwo_L3S1, text='Junior', bg='White')
        self.homeresu_pageTwo_L3Team1.pack(pady=12)

        self.homeresu_pageTwo_L3S2 = Frame(
            self.homeresu_pageTwo_L3,
            width=52.5,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageTwo_L3S2.pack_propagate(False)
        self.homeresu_pageTwo_L3S2.pack(side=LEFT)

        self.homeresu_pageTwo_L3Score1 = \
            Label(self.homeresu_pageTwo_L3S2, text='0', bg='White')
        self.homeresu_pageTwo_L3Score1.pack(pady=12)

        self.homeresu_pageTwo_L3S4 = Frame(
            self.homeresu_pageTwo_L3,
            width=100,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageTwo_L3S4.pack_propagate(False)
        self.homeresu_pageTwo_L3S4.pack(side=RIGHT)

        self.homeresu_pageTwo_L3Team2 = \
            Label(self.homeresu_pageTwo_L3S4, text='N/A', bg='White')
        self.homeresu_pageTwo_L3Team2.pack(pady=12)

        self.homeresu_pageTwo_L3S3 = Frame(
            self.homeresu_pageTwo_L3,
            width=52.5,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageTwo_L3S3.pack_propagate(False)
        self.homeresu_pageTwo_L3S3.pack(side=RIGHT)

        self.homeresu_pageTwo_L3Score2 = \
            Label(self.homeresu_pageTwo_L3S3, text='0', bg='White')
        self.homeresu_pageTwo_L3Score2.pack(pady=12)

        # Third resu page (page_number = 3)

        self.homeresu_pageThree = Frame(self.homeresu_box, bg='White',
                width=305, height=135)
        self.homeresu_pageThree.pack_propagate(False)
        self.homeresu_pageThree.grid_propagate(False)

        # Divide the pages into 3 lines with each match

        self.homeresu_pageThree_L1 = Frame(self.homeresu_pageThree,
                width=305, height=45, bg='White')
        self.homeresu_pageThree_L1.pack_propagate(False)
        self.homeresu_pageThree_L1.pack()

        # Divide the lines into 4 sections, 1 = MRGS TEAM, 2 = MRGS SCORE, 3 = OTHER SCORE, 4 = OTHER TEAM

        self.homeresu_pageThree_L1S1 = Frame(
            self.homeresu_pageThree_L1,
            width=100,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageThree_L1S1.pack_propagate(False)
        self.homeresu_pageThree_L1S1.pack(side=LEFT)

        self.homeresu_pageThree_L1Team1 = \
            Label(self.homeresu_pageThree_L1S1, text='First XI',
                  bg='White')
        self.homeresu_pageThree_L1Team1.pack(pady=12)

        self.homeresu_pageThree_L1S2 = Frame(
            self.homeresu_pageThree_L1,
            width=52.5,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageThree_L1S2.pack_propagate(False)
        self.homeresu_pageThree_L1S2.pack(side=LEFT)

        self.homeresu_pageThree_L1Score1 = \
            Label(self.homeresu_pageThree_L1S2, text='0', bg='White')
        self.homeresu_pageThree_L1Score1.pack(pady=12)

        self.homeresu_pageThree_L1S4 = Frame(
            self.homeresu_pageThree_L1,
            width=100,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageThree_L1S4.pack_propagate(False)
        self.homeresu_pageThree_L1S4.pack(side=RIGHT)

        self.homeresu_pageThree_L1Team2 = \
            Label(self.homeresu_pageThree_L1S4, text='N/A', bg='White')
        self.homeresu_pageThree_L1Team2.pack(pady=12)

        self.homeresu_pageThree_L1S3 = Frame(
            self.homeresu_pageThree_L1,
            width=52.5,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageThree_L1S3.pack_propagate(False)
        self.homeresu_pageThree_L1S3.pack(side=RIGHT)

        self.homeresu_pageThree_L1Score2 = \
            Label(self.homeresu_pageThree_L1S3, text='0', bg='White')
        self.homeresu_pageThree_L1Score2.pack(pady=12)

        # Line 2 of the latest results

        self.homeresu_pageThree_L2 = Frame(self.homeresu_pageThree,
                width=305, height=45, bg='White')
        self.homeresu_pageThree_L2.pack_propagate(False)
        self.homeresu_pageThree_L2.pack()

        # Line subdivisions

        self.homeresu_pageThree_L2S1 = Frame(
            self.homeresu_pageThree_L2,
            width=100,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageThree_L2S1.pack_propagate(False)
        self.homeresu_pageThree_L2S1.pack(side=LEFT)

        self.homeresu_pageThree_L2Team1 = \
            Label(self.homeresu_pageThree_L2S1, text='Second XI',
                  bg='White')
        self.homeresu_pageThree_L2Team1.pack(pady=12)

        self.homeresu_pageThree_L2S2 = Frame(
            self.homeresu_pageThree_L2,
            width=52.5,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageThree_L2S2.pack_propagate(False)
        self.homeresu_pageThree_L2S2.pack(side=LEFT)

        self.homeresu_pageThree_L2Score1 = \
            Label(self.homeresu_pageThree_L2S2, text='0', bg='White')
        self.homeresu_pageThree_L2Score1.pack(pady=12)

        self.homeresu_pageThree_L2S4 = Frame(
            self.homeresu_pageThree_L2,
            width=100,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageThree_L2S4.pack_propagate(False)
        self.homeresu_pageThree_L2S4.pack(side=RIGHT)

        self.homeresu_pageThree_L2Team2 = \
            Label(self.homeresu_pageThree_L2S4, text='N/A', bg='White')
        self.homeresu_pageThree_L2Team2.pack(pady=12)

        self.homeresu_pageThree_L2S3 = Frame(
            self.homeresu_pageThree_L2,
            width=52.5,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageThree_L2S3.pack_propagate(False)
        self.homeresu_pageThree_L2S3.pack(side=RIGHT)

        self.homeresu_pageThree_L2Score2 = \
            Label(self.homeresu_pageThree_L2S3, text='0', bg='White')
        self.homeresu_pageThree_L2Score2.pack(pady=12)

        # Line 3 of the latest results

        self.homeresu_pageThree_L3 = Frame(self.homeresu_pageThree,
                width=305, height=45, bg='White')
        self.homeresu_pageThree_L3.pack_propagate(False)
        self.homeresu_pageThree_L3.pack()

        # Line subdivisions

        self.homeresu_pageThree_L3S1 = Frame(
            self.homeresu_pageThree_L3,
            width=100,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageThree_L3S1.pack_propagate(False)
        self.homeresu_pageThree_L3S1.pack(side=LEFT)

        self.homeresu_pageThree_L3Team1 = \
            Label(self.homeresu_pageThree_L3S1, text='Junior',
                  bg='White')
        self.homeresu_pageThree_L3Team1.pack(pady=12)

        self.homeresu_pageThree_L3S2 = Frame(
            self.homeresu_pageThree_L3,
            width=52.5,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageThree_L3S2.pack_propagate(False)
        self.homeresu_pageThree_L3S2.pack(side=LEFT)

        self.homeresu_pageThree_L3Score1 = \
            Label(self.homeresu_pageThree_L3S2, text='0', bg='White')
        self.homeresu_pageThree_L3Score1.pack(pady=12)

        self.homeresu_pageThree_L3S4 = Frame(
            self.homeresu_pageThree_L3,
            width=100,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageThree_L3S4.pack_propagate(False)
        self.homeresu_pageThree_L3S4.pack(side=RIGHT)

        self.homeresu_pageThree_L3Team2 = \
            Label(self.homeresu_pageThree_L3S4, text='N/A', bg='White')
        self.homeresu_pageThree_L3Team2.pack(pady=12)

        self.homeresu_pageThree_L3S3 = Frame(
            self.homeresu_pageThree_L3,
            width=52.5,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageThree_L3S3.pack_propagate(False)
        self.homeresu_pageThree_L3S3.pack(side=RIGHT)

        self.homeresu_pageThree_L3Score2 = \
            Label(self.homeresu_pageThree_L3S3, text='0', bg='White')
        self.homeresu_pageThree_L3Score2.pack(pady=12)

        # Fourth resu page (page_number = 4)

        self.homeresu_pageFour = Frame(self.homeresu_box, bg='White',
                width=305, height=135)
        self.homeresu_pageFour.pack_propagate(False)
        self.homeresu_pageFour.grid_propagate(False)

        # Divide the pages into 3 lines with each match

        self.homeresu_pageFour_L1 = Frame(self.homeresu_pageFour,
                width=305, height=45, bg='White')
        self.homeresu_pageFour_L1.pack_propagate(False)
        self.homeresu_pageFour_L1.pack()

        # Divide the lines into 4 sections, 1 = MRGS TEAM, 2 = MRGS SCORE, 3 = OTHER SCORE, 4 = OTHER TEAM

        self.homeresu_pageFour_L1S1 = Frame(
            self.homeresu_pageFour_L1,
            width=100,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageFour_L1S1.pack_propagate(False)
        self.homeresu_pageFour_L1S1.pack(side=LEFT)

        self.homeresu_pageFour_L1Team1 = \
            Label(self.homeresu_pageFour_L1S1, text='First XI',
                  bg='White')
        self.homeresu_pageFour_L1Team1.pack(pady=12)

        self.homeresu_pageFour_L1S2 = Frame(
            self.homeresu_pageFour_L1,
            width=52.5,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageFour_L1S2.pack_propagate(False)
        self.homeresu_pageFour_L1S2.pack(side=LEFT)

        self.homeresu_pageFour_L1Score1 = \
            Label(self.homeresu_pageFour_L1S2, text='0', bg='White')
        self.homeresu_pageFour_L1Score1.pack(pady=12)

        self.homeresu_pageFour_L1S4 = Frame(
            self.homeresu_pageFour_L1,
            width=100,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageFour_L1S4.pack_propagate(False)
        self.homeresu_pageFour_L1S4.pack(side=RIGHT)

        self.homeresu_pageFour_L1Team2 = \
            Label(self.homeresu_pageFour_L1S4, text='N/A', bg='White')
        self.homeresu_pageFour_L1Team2.pack(pady=12)

        self.homeresu_pageFour_L1S3 = Frame(
            self.homeresu_pageFour_L1,
            width=52.5,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageFour_L1S3.pack_propagate(False)
        self.homeresu_pageFour_L1S3.pack(side=RIGHT)

        self.homeresu_pageFour_L1Score2 = \
            Label(self.homeresu_pageFour_L1S3, text='0', bg='White')
        self.homeresu_pageFour_L1Score2.pack(pady=12)

        # Line 2 of the latest results

        self.homeresu_pageFour_L2 = Frame(self.homeresu_pageFour,
                width=305, height=45, bg='White')
        self.homeresu_pageFour_L2.pack_propagate(False)
        self.homeresu_pageFour_L2.pack()

        # Line subdivisions

        self.homeresu_pageFour_L2S1 = Frame(
            self.homeresu_pageFour_L2,
            width=100,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageFour_L2S1.pack_propagate(False)
        self.homeresu_pageFour_L2S1.pack(side=LEFT)

        self.homeresu_pageFour_L2Team1 = \
            Label(self.homeresu_pageFour_L2S1, text='Second XI',
                  bg='White')
        self.homeresu_pageFour_L2Team1.pack(pady=12)

        self.homeresu_pageFour_L2S2 = Frame(
            self.homeresu_pageFour_L2,
            width=52.5,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageFour_L2S2.pack_propagate(False)
        self.homeresu_pageFour_L2S2.pack(side=LEFT)

        self.homeresu_pageFour_L2Score1 = \
            Label(self.homeresu_pageFour_L2S2, text='0', bg='White')
        self.homeresu_pageFour_L2Score1.pack(pady=12)

        self.homeresu_pageFour_L2S4 = Frame(
            self.homeresu_pageFour_L2,
            width=100,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageFour_L2S4.pack_propagate(False)
        self.homeresu_pageFour_L2S4.pack(side=RIGHT)

        self.homeresu_pageFour_L2Team2 = \
            Label(self.homeresu_pageFour_L2S4, text='N/A', bg='White')
        self.homeresu_pageFour_L2Team2.pack(pady=12)

        self.homeresu_pageFour_L2S3 = Frame(
            self.homeresu_pageFour_L2,
            width=52.5,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageFour_L2S3.pack_propagate(False)
        self.homeresu_pageFour_L2S3.pack(side=RIGHT)

        self.homeresu_pageFour_L2Score2 = \
            Label(self.homeresu_pageFour_L2S3, text='0', bg='White')
        self.homeresu_pageFour_L2Score2.pack(pady=12)

        # Line 3 of the latest results

        self.homeresu_pageFour_L3 = Frame(self.homeresu_pageFour,
                width=305, height=45, bg='White')
        self.homeresu_pageFour_L3.pack_propagate(False)
        self.homeresu_pageFour_L3.pack()

        # Line subdivisions

        self.homeresu_pageFour_L3S1 = Frame(
            self.homeresu_pageFour_L3,
            width=100,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageFour_L3S1.pack_propagate(False)
        self.homeresu_pageFour_L3S1.pack(side=LEFT)

        self.homeresu_pageFour_L3Team1 = \
            Label(self.homeresu_pageFour_L3S1, text='Junior', bg='White'
                  )
        self.homeresu_pageFour_L3Team1.pack(pady=12)

        self.homeresu_pageFour_L3S2 = Frame(
            self.homeresu_pageFour_L3,
            width=52.5,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageFour_L3S2.pack_propagate(False)
        self.homeresu_pageFour_L3S2.pack(side=LEFT)

        self.homeresu_pageFour_L3Score1 = \
            Label(self.homeresu_pageFour_L3S2, text='0', bg='White')
        self.homeresu_pageFour_L3Score1.pack(pady=12)

        self.homeresu_pageFour_L3S4 = Frame(
            self.homeresu_pageFour_L3,
            width=100,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageFour_L3S4.pack_propagate(False)
        self.homeresu_pageFour_L3S4.pack(side=RIGHT)

        self.homeresu_pageFour_L3Team2 = \
            Label(self.homeresu_pageFour_L3S4, text='N/A', bg='White')
        self.homeresu_pageFour_L3Team2.pack(pady=12)

        self.homeresu_pageFour_L3S3 = Frame(
            self.homeresu_pageFour_L3,
            width=52.5,
            height=45,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_pageFour_L3S3.pack_propagate(False)
        self.homeresu_pageFour_L3S3.pack(side=RIGHT)

        self.homeresu_pageFour_L3Score2 = \
            Label(self.homeresu_pageFour_L3S3, text='0', bg='White')
        self.homeresu_pageFour_L3Score2.pack(pady=12)

        # Home resu page indicator
            # which page is shown

        self.homeresu_bottom = Frame(
            self.homeresu_box,
            width=305,
            height=26,
            bg='White',
            relief=SUNKEN,
            bd=0.5,
            )
        self.homeresu_bottom.pack_propagate(False)
        self.homeresu_bottom.grid(row=2, columnspan=TRUE)

        self.page_indicator = Label(
            self.homeresu_bottom,
            text=self.page_number,
            relief=RIDGE,
            bg='White',
            width=5,
            height=1,
            )
        self.page_indicator.pack(pady=2)

        # School-sport info page frame ---------------------------

        self.info_page = Frame(self.content_frame, background='#EFECEC'
                               , width=w_width, height=600)
        self.info_page.grid_propagate(False)
        self.info_page.pack_propagate(False)

        self.info_page_hub = Frame(self.info_page, background='#EFECEC'
                                   , width=w_width, height=600)
        self.info_page_hub.pack_propagate(False)
        self.info_page_hub.pack()

        self.sports_info_label = Label(self.info_page_hub, bg='#EFECEC'
                , text='School sports info', font=self.header_font)
        self.sports_info_label.pack(pady=5)

        self.sports_info_label_two = Label(self.info_page_hub,
                text='Click to expand trainings / organiser info',
                font=self.subheader_font)
        self.sports_info_label_two.pack(pady=50)

        # Sport buttons that expand respective windows for info on the sport

        self.football_info_button = Button(
            self.info_page_hub,
            bg='White',
            text='Football',
            font=self.button_font,
            width=27,
            height=2,
            relief=RIDGE,
            bd=3,
            command=self.expand_football_info,
            )
        self.football_info_button.pack(pady=10)

        self.basketball_info_button = Button(
            self.info_page_hub,
            bg='White',
            text='Basketball',
            font=self.button_font,
            width=27,
            height=2,
            relief=RIDGE,
            bd=3,
            command=self.expand_basketball_info,
            )
        self.basketball_info_button.pack(pady=8)

        self.hockey_info_button = Button(
            self.info_page_hub,
            bg='White',
            text='Hockey',
            font=self.button_font,
            width=27,
            height=2,
            relief=RIDGE,
            bd=3,
            command=self.expand_hockey_info,
            )
        self.hockey_info_button.pack(pady=8)

        self.cricket_info_button = Button(
            self.info_page_hub,
            bg='White',
            text='Cricket',
            font=self.button_font,
            width=27,
            height=2,
            relief=RIDGE,
            bd=3,
            command=self.expand_cricket_info,
            )
        self.cricket_info_button.pack(pady=8)

        self.rugby_info_button = Button(
            self.info_page_hub,
            bg='White',
            text='Rugby',
            font=self.button_font,
            width=27,
            height=2,
            relief=RIDGE,
            bd=3,
            command=self.expand_rugby_info,
            )
        self.rugby_info_button.pack(pady=8)

        # Information pages for each sport, the same layout on each one

        self.football_info_page = Frame(self.info_page, bg='White',
                width=w_width, height=600)
        self.football_info_page.pack_propagate(False)

        self.football_top_gap = Frame(self.football_info_page,
                bg='White', width=w_width, height=25)
        self.football_top_gap.pack()

        self.football_info_top = Frame(
            self.football_info_page,
            bg='White',
            width=w_width - margin_length,
            height=70,
            relief=RIDGE,
            bd=3,
            )
        self.football_info_top.pack_propagate(False)
        self.football_info_top.pack(pady=3)

        self.back_to_info_football = Button(self.football_info_top,
                bg='White', text='Back', font=self.button_font,
                command=self.return_to_info)
        self.back_to_info_football.pack(side=RIGHT, padx=5)

        self.football_info_label = Label(self.football_info_top,
                bg='White', text='Football', font=self.header_font)
        self.football_info_label.pack(side=LEFT, padx=5)

        self.football_info_label_two = Label(self.football_info_top,
                bg='White', text='Winter sport', font=('Helvetica', 12))
        self.football_info_label_two.pack(side=LEFT)

        # First XI box

        self.football_info_firstXI = Frame(
            self.football_info_page,
            bg='White',
            width=w_width - margin_length,
            height=150,
            relief=RIDGE,
            bd=3,
            )
        self.football_info_firstXI.pack_propagate(False)
        self.football_info_firstXI.pack(pady=3)

        self.football_firstXI_top = Frame(self.football_info_firstXI,
                bg='White', width=w_width - margin_length, height=30)
        self.football_firstXI_top.pack_propagate(False)
        self.football_firstXI_top.pack(pady=3)

        self.football_firstXI_label = Label(self.football_firstXI_top,
                text='First XI', bg='White', font=self.subheader_font)
        self.football_firstXI_label.pack(side=LEFT, padx=5)

        self.football_firstXI_organiser = \
            Label(self.football_firstXI_top,
                  text='Teacher in charge: Mr Chellew, Ms Thomas',
                  bg='White', font=('Helvetica', 10))
        self.football_firstXI_organiser.pack(side=LEFT)

        self.football_firstXI_textbox = \
            Frame(self.football_info_firstXI, bg='White', width=w_width
                  - margin_length, height=55)
        self.football_firstXI_textbox.pack_propagate(False)
        self.football_firstXI_textbox.pack()

        self.football_firstXI_trainingLabel = \
            Label(self.football_firstXI_textbox,
                  text='Boys trainings on Monday / Wednesday morning',
                  bg='White', font=('Helvetica', 11))
        self.football_firstXI_trainingLabel.pack(side=LEFT, padx=5)

        self.football_firstXI_textbox_two = \
            Frame(self.football_info_firstXI, bg='White', width=w_width
                  - margin_length, height=55)
        self.football_firstXI_textbox_two.pack_propagate(False)
        self.football_firstXI_textbox_two.pack()

        self.football_firstXI_trainingLabel_two = \
            Label(self.football_firstXI_textbox_two,
                  text='Girls trainings on Monday / Tuesday after school'
                  , bg='White', font=('Helvetica', 11))
        self.football_firstXI_trainingLabel_two.pack(side=LEFT, padx=5)

        # Second XI box

        self.football_info_secondXI = Frame(
            self.football_info_page,
            bg='White',
            width=w_width - margin_length,
            height=150,
            relief=RIDGE,
            bd=3,
            )
        self.football_info_secondXI.pack_propagate(False)
        self.football_info_secondXI.pack(pady=3)

        self.football_secondXI_top = Frame(self.football_info_secondXI,
                bg='White', width=w_width - margin_length, height=30)
        self.football_secondXI_top.pack_propagate(False)
        self.football_secondXI_top.pack(pady=3)

        self.football_secondXI_label = \
            Label(self.football_secondXI_top, text='Second XI',
                  bg='White', font=self.subheader_font)
        self.football_secondXI_label.pack(side=LEFT, padx=5)

        self.football_secondXI_organiser = \
            Label(self.football_secondXI_top,
                  text='Teacher in charge: Mr Carter', bg='White',
                  font=('Helvetica', 10))
        self.football_secondXI_organiser.pack(side=LEFT)

        self.football_secondXI_textbox = \
            Frame(self.football_info_secondXI, bg='White',
                  width=w_width - margin_length, height=55)
        self.football_secondXI_textbox.pack_propagate(False)
        self.football_secondXI_textbox.pack()

        self.football_secondXI_trainingLabel = \
            Label(self.football_secondXI_textbox,
                  text='Boys trainings on Monday / Wednesday after school'
                  , bg='White', font=('Helvetica', 11))
        self.football_secondXI_trainingLabel.pack(side=LEFT, padx=5)

        self.football_secondXI_textbox_two = \
            Frame(self.football_info_secondXI, bg='White',
                  width=w_width - margin_length, height=55)
        self.football_secondXI_textbox_two.pack_propagate(False)
        self.football_secondXI_textbox_two.pack()

        self.football_secondXI_trainingLabel_two = \
            Label(self.football_secondXI_textbox_two,
                  text='Girls trainings on Monday / Tuesday morning',
                  bg='White', font=('Helvetica', 11))
        self.football_secondXI_trainingLabel_two.pack(side=LEFT, padx=5)

        # Junior box

        self.football_info_Junior = Frame(
            self.football_info_page,
            bg='White',
            width=w_width - margin_length,
            height=150,
            relief=RIDGE,
            bd=3,
            )
        self.football_info_Junior.pack_propagate(False)
        self.football_info_Junior.pack(pady=3)

        self.football_Junior_top = Frame(self.football_info_Junior,
                bg='White', width=w_width - margin_length, height=30)
        self.football_Junior_top.pack_propagate(False)
        self.football_Junior_top.pack(pady=3)

        self.football_Junior_label = Label(self.football_Junior_top,
                text='Junior', bg='White', font=self.subheader_font)
        self.football_Junior_label.pack(side=LEFT, padx=5)

        self.football_Junior_organiser = \
            Label(self.football_Junior_top,
                  text='Teacher in charge: Ms Winterton', bg='White',
                  font=('Helvetica', 10))
        self.football_Junior_organiser.pack(side=LEFT)

        self.football_Junior_textbox = Frame(self.football_info_Junior,
                bg='White', width=w_width - margin_length, height=55)
        self.football_Junior_textbox.pack_propagate(False)
        self.football_Junior_textbox.pack()

        self.football_Junior_trainingLabel = \
            Label(self.football_Junior_textbox,
                  text='Boys trainings on Monday morning', bg='White',
                  font=('Helvetica', 11))
        self.football_Junior_trainingLabel.pack(side=LEFT, padx=5)

        self.football_Junior_textbox_two = \
            Frame(self.football_info_Junior, bg='White', width=w_width
                  - margin_length, height=55)
        self.football_Junior_textbox_two.pack_propagate(False)
        self.football_Junior_textbox_two.pack()

        self.football_Junior_trainingLabel_two = \
            Label(self.football_Junior_textbox_two,
                  text='Girls trainings on Friday after school',
                  bg='White', font=('Helvetica', 11))
        self.football_Junior_trainingLabel_two.pack(side=LEFT, padx=5)

        # Basketball info page

        self.basketball_info_page = Frame(self.info_page, bg='White',
                width=w_width, height=600)
        self.basketball_info_page.pack_propagate(False)

        self.basketball_top_gap = Frame(self.basketball_info_page,
                bg='White', width=w_width, height=25)
        self.basketball_top_gap.pack()

        self.basketball_info_top = Frame(
            self.basketball_info_page,
            bg='White',
            width=w_width - margin_length,
            height=70,
            relief=RIDGE,
            bd=3,
            )
        self.basketball_info_top.pack_propagate(False)
        self.basketball_info_top.pack(pady=3)

        self.back_to_info_basketball = Button(self.basketball_info_top,
                bg='White', text='Back', font=self.button_font,
                command=self.return_to_info)
        self.back_to_info_basketball.pack(side=RIGHT, padx=5)

        self.basketball_info_label = Label(self.basketball_info_top,
                bg='White', text='Basketball', font=self.header_font)
        self.basketball_info_label.pack(side=LEFT, padx=5)

        self.basketball_info_label_two = \
            Label(self.basketball_info_top, bg='White',
                  text='Winter sport', font=('Helvetica', 12))
        self.basketball_info_label_two.pack(side=LEFT)

        # First XI box

        self.basketball_info_firstXI = Frame(
            self.basketball_info_page,
            bg='White',
            width=w_width - margin_length,
            height=150,
            relief=RIDGE,
            bd=3,
            )
        self.basketball_info_firstXI.pack_propagate(False)
        self.basketball_info_firstXI.pack(pady=3)

        self.basketball_firstXI_top = \
            Frame(self.basketball_info_firstXI, bg='White',
                  width=w_width - margin_length, height=30)
        self.basketball_firstXI_top.pack_propagate(False)
        self.basketball_firstXI_top.pack(pady=3)

        self.basketball_firstXI_label = \
            Label(self.basketball_firstXI_top, text='Senior', bg='White'
                  , font=self.subheader_font)
        self.basketball_firstXI_label.pack(side=LEFT, padx=5)

        self.basketball_firstXI_organiser = \
            Label(self.basketball_firstXI_top,
                  text='Teacher in charge: Mr Windsor', bg='White',
                  font=('Helvetica', 10))
        self.basketball_firstXI_organiser.pack(side=LEFT)

        self.basketball_firstXI_textbox = \
            Frame(self.basketball_info_firstXI, bg='White',
                  width=w_width - margin_length, height=55)
        self.basketball_firstXI_textbox.pack_propagate(False)
        self.basketball_firstXI_textbox.pack()

        self.basketball_firstXI_trainingLabel = \
            Label(self.basketball_firstXI_textbox,
                  text='Boys trainings on Tuesday / Thursday after school'
                  , bg='White', font=('Helvetica', 11))
        self.basketball_firstXI_trainingLabel.pack(side=LEFT, padx=5)

        self.basketball_firstXI_textbox_two = \
            Frame(self.basketball_info_firstXI, bg='White',
                  width=w_width - margin_length, height=55)
        self.basketball_firstXI_textbox_two.pack_propagate(False)
        self.basketball_firstXI_textbox_two.pack()

        self.basketball_firstXI_trainingLabel_two = \
            Label(self.basketball_firstXI_textbox_two,
                  text='Girls trainings on Monday / Wednesday after school'
                  , bg='White', font=('Helvetica', 11))
        self.basketball_firstXI_trainingLabel_two.pack(side=LEFT,
                padx=5)

        # Second XI box

        self.basketball_info_secondXI = Frame(
            self.basketball_info_page,
            bg='White',
            width=w_width - margin_length,
            height=150,
            relief=RIDGE,
            bd=3,
            )
        self.basketball_info_secondXI.pack_propagate(False)
        self.basketball_info_secondXI.pack(pady=3)

        self.basketball_secondXI_top = \
            Frame(self.basketball_info_secondXI, bg='White',
                  width=w_width - margin_length, height=30)
        self.basketball_secondXI_top.pack_propagate(False)
        self.basketball_secondXI_top.pack(pady=3)

        self.basketball_secondXI_label = \
            Label(self.basketball_secondXI_top, text='U17', bg='White',
                  font=self.subheader_font)
        self.basketball_secondXI_label.pack(side=LEFT, padx=5)

        self.basketball_secondXI_organiser = \
            Label(self.basketball_secondXI_top,
                  text='Teacher in charge: Mr Windsor', bg='White',
                  font=('Helvetica', 10))
        self.basketball_secondXI_organiser.pack(side=LEFT)

        self.basketball_secondXI_textbox = \
            Frame(self.basketball_info_secondXI, bg='White',
                  width=w_width - margin_length, height=55)
        self.basketball_secondXI_textbox.pack_propagate(False)
        self.basketball_secondXI_textbox.pack()

        self.basketball_secondXI_trainingLabel = \
            Label(self.basketball_secondXI_textbox,
                  text='Boys trainings on Thursday after school',
                  bg='White', font=('Helvetica', 11))
        self.basketball_secondXI_trainingLabel.pack(side=LEFT, padx=5)

        self.basketball_secondXI_textbox_two = \
            Frame(self.basketball_info_secondXI, bg='White',
                  width=w_width - margin_length, height=55)
        self.basketball_secondXI_textbox_two.pack_propagate(False)
        self.basketball_secondXI_textbox_two.pack()

        self.basketball_secondXI_trainingLabel_two = \
            Label(self.basketball_secondXI_textbox_two,
                  text='Girls trainings on Tuesday after school',
                  bg='White', font=('Helvetica', 11))
        self.basketball_secondXI_trainingLabel_two.pack(side=LEFT,
                padx=5)

        # Junior box

        self.basketball_info_Junior = Frame(
            self.basketball_info_page,
            bg='White',
            width=w_width - margin_length,
            height=150,
            relief=RIDGE,
            bd=3,
            )
        self.basketball_info_Junior.pack_propagate(False)
        self.basketball_info_Junior.pack(pady=3)

        self.basketball_Junior_top = Frame(self.basketball_info_Junior,
                bg='White', width=w_width - margin_length, height=30)
        self.basketball_Junior_top.pack_propagate(False)
        self.basketball_Junior_top.pack(pady=3)

        self.basketball_Junior_label = \
            Label(self.basketball_Junior_top, text='Junior', bg='White'
                  , font=self.subheader_font)
        self.basketball_Junior_label.pack(side=LEFT, padx=5)

        self.basketball_Junior_organiser = \
            Label(self.basketball_Junior_top,
                  text='Teacher in charge: Mr Singh', bg='White',
                  font=('Helvetica', 10))
        self.basketball_Junior_organiser.pack(side=LEFT)

        self.basketball_Junior_textbox = \
            Frame(self.basketball_info_Junior, bg='White',
                  width=w_width - margin_length, height=55)
        self.basketball_Junior_textbox.pack_propagate(False)
        self.basketball_Junior_textbox.pack()

        self.basketball_Junior_trainingLabel = \
            Label(self.basketball_Junior_textbox,
                  text='Boys trainings on Wednesday after school',
                  bg='White', font=('Helvetica', 11))
        self.basketball_Junior_trainingLabel.pack(side=LEFT, padx=5)

        self.basketball_Junior_textbox_two = \
            Frame(self.basketball_info_Junior, bg='White',
                  width=w_width - margin_length, height=55)
        self.basketball_Junior_textbox_two.pack_propagate(False)
        self.basketball_Junior_textbox_two.pack()

        self.basketball_Junior_trainingLabel_two = \
            Label(self.basketball_Junior_textbox_two,
                  text='Girls trainings on Tuesday after school',
                  bg='White', font=('Helvetica', 11))
        self.basketball_Junior_trainingLabel_two.pack(side=LEFT, padx=5)

        # Hockey info page

        self.hockey_info_page = Frame(self.info_page, bg='White',
                width=w_width, height=600)
        self.hockey_info_page.pack_propagate(False)

        self.hockey_top_gap = Frame(self.hockey_info_page, bg='White',
                                    width=w_width, height=25)
        self.hockey_top_gap.pack()

        self.hockey_info_top = Frame(
            self.hockey_info_page,
            bg='White',
            width=w_width - margin_length,
            height=70,
            relief=RIDGE,
            bd=3,
            )
        self.hockey_info_top.pack_propagate(False)
        self.hockey_info_top.pack(pady=3)

        self.back_to_info_hockey = Button(self.hockey_info_top,
                bg='White', text='Back', font=self.button_font,
                command=self.return_to_info)
        self.back_to_info_hockey.pack(side=RIGHT, padx=5)

        self.hockey_info_label = Label(self.hockey_info_top, bg='White'
                , text='Hockey', font=self.header_font)
        self.hockey_info_label.pack(side=LEFT, padx=5)

        self.hockey_info_label_two = Label(self.hockey_info_top,
                bg='White', text='Winter sport', font=('Helvetica', 12))
        self.hockey_info_label_two.pack(side=LEFT)

        # First XI box

        self.hockey_info_firstXI = Frame(
            self.hockey_info_page,
            bg='White',
            width=w_width - margin_length,
            height=150,
            relief=RIDGE,
            bd=3,
            )
        self.hockey_info_firstXI.pack_propagate(False)
        self.hockey_info_firstXI.pack(pady=3)

        self.hockey_firstXI_top = Frame(self.hockey_info_firstXI,
                bg='White', width=w_width - margin_length, height=30)
        self.hockey_firstXI_top.pack_propagate(False)
        self.hockey_firstXI_top.pack(pady=3)

        self.hockey_firstXI_label = Label(self.hockey_firstXI_top,
                text='First XI', bg='White', font=self.subheader_font)
        self.hockey_firstXI_label.pack(side=LEFT, padx=5)

        self.hockey_firstXI_organiser = Label(self.hockey_firstXI_top,
                text='Teacher in charge: Mr Bitchener', bg='White',
                font=('Helvetica', 10))
        self.hockey_firstXI_organiser.pack(side=LEFT)

        self.hockey_firstXI_textbox = Frame(self.hockey_info_firstXI,
                bg='White', width=w_width - margin_length, height=55)
        self.hockey_firstXI_textbox.pack_propagate(False)
        self.hockey_firstXI_textbox.pack()

        self.hockey_firstXI_trainingLabel = \
            Label(self.hockey_firstXI_textbox,
                  text='Boys trainings on Monday / Friday morning',
                  bg='White', font=('Helvetica', 11))
        self.hockey_firstXI_trainingLabel.pack(side=LEFT, padx=5)

        self.hockey_firstXI_textbox_two = \
            Frame(self.hockey_info_firstXI, bg='White', width=w_width
                  - margin_length, height=55)
        self.hockey_firstXI_textbox_two.pack_propagate(False)
        self.hockey_firstXI_textbox_two.pack()

        self.hockey_firstXI_trainingLabel_two = \
            Label(self.hockey_firstXI_textbox_two,
                  text='Girls trainings on Tuesday / Friday after school'
                  , bg='White', font=('Helvetica', 11))
        self.hockey_firstXI_trainingLabel_two.pack(side=LEFT, padx=5)

        # Second XI box

        self.hockey_info_secondXI = Frame(
            self.hockey_info_page,
            bg='White',
            width=w_width - margin_length,
            height=150,
            relief=RIDGE,
            bd=3,
            )
        self.hockey_info_secondXI.pack_propagate(False)
        self.hockey_info_secondXI.pack(pady=3)

        self.hockey_secondXI_top = Frame(self.hockey_info_secondXI,
                bg='White', width=w_width - margin_length, height=30)
        self.hockey_secondXI_top.pack_propagate(False)
        self.hockey_secondXI_top.pack(pady=3)

        self.hockey_secondXI_label = Label(self.hockey_secondXI_top,
                text='Second XI', bg='White', font=self.subheader_font)
        self.hockey_secondXI_label.pack(side=LEFT, padx=5)

        self.hockey_secondXI_organiser = \
            Label(self.hockey_secondXI_top,
                  text='Teacher in charge: Mr Bogle', bg='White',
                  font=('Helvetica', 10))
        self.hockey_secondXI_organiser.pack(side=LEFT)

        self.hockey_secondXI_textbox = Frame(self.hockey_info_secondXI,
                bg='White', width=w_width - margin_length, height=55)
        self.hockey_secondXI_textbox.pack_propagate(False)
        self.hockey_secondXI_textbox.pack()

        self.hockey_secondXI_trainingLabel = \
            Label(self.hockey_secondXI_textbox,
                  text='Boys trainings on Tuesday / Thursday after school'
                  , bg='White', font=('Helvetica', 11))
        self.hockey_secondXI_trainingLabel.pack(side=LEFT, padx=5)

        self.hockey_secondXI_textbox_two = \
            Frame(self.hockey_info_secondXI, bg='White', width=w_width
                  - margin_length, height=55)
        self.hockey_secondXI_textbox_two.pack_propagate(False)
        self.hockey_secondXI_textbox_two.pack()

        self.hockey_secondXI_trainingLabel_two = \
            Label(self.hockey_secondXI_textbox_two,
                  text='Girls trainings on Monday / Wednesday after school'
                  , bg='White', font=('Helvetica', 11))
        self.hockey_secondXI_trainingLabel_two.pack(side=LEFT, padx=5)

        # Junior box

        self.hockey_info_Junior = Frame(
            self.hockey_info_page,
            bg='White',
            width=w_width - margin_length,
            height=150,
            relief=RIDGE,
            bd=3,
            )
        self.hockey_info_Junior.pack_propagate(False)
        self.hockey_info_Junior.pack(pady=3)

        self.hockey_Junior_top = Frame(self.hockey_info_Junior,
                bg='White', width=w_width - margin_length, height=30)
        self.hockey_Junior_top.pack_propagate(False)
        self.hockey_Junior_top.pack(pady=3)

        self.hockey_Junior_label = Label(self.hockey_Junior_top,
                text='Junior', bg='White', font=self.subheader_font)
        self.hockey_Junior_label.pack(side=LEFT, padx=5)

        self.hockey_Junior_organiser = Label(self.hockey_Junior_top,
                text='Teacher in charge: Ms Kelly', bg='White',
                font=('Helvetica', 10))
        self.hockey_Junior_organiser.pack(side=LEFT)

        self.hockey_Junior_textbox = Frame(self.hockey_info_Junior,
                bg='White', width=w_width - margin_length, height=55)
        self.hockey_Junior_textbox.pack_propagate(False)
        self.hockey_Junior_textbox.pack()

        self.hockey_Junior_trainingLabel = \
            Label(self.hockey_Junior_textbox,
                  text='Boys trainings on Thursday morning', bg='White'
                  , font=('Helvetica', 11))
        self.hockey_Junior_trainingLabel.pack(side=LEFT, padx=5)

        self.hockey_Junior_textbox_two = Frame(self.hockey_info_Junior,
                bg='White', width=w_width - margin_length, height=55)
        self.hockey_Junior_textbox_two.pack_propagate(False)
        self.hockey_Junior_textbox_two.pack()

        self.hockey_Junior_trainingLabel_two = \
            Label(self.hockey_Junior_textbox_two,
                  text='Girls trainings on Tuesday after school',
                  bg='White', font=('Helvetica', 11))
        self.hockey_Junior_trainingLabel_two.pack(side=LEFT, padx=5)

        # Cricket info page

        self.cricket_info_page = Frame(self.info_page, bg='White',
                width=w_width, height=600)
        self.cricket_info_page.pack_propagate(False)

        self.cricket_top_gap = Frame(self.cricket_info_page, bg='White'
                , width=w_width, height=25)
        self.cricket_top_gap.pack()

        self.cricket_info_top = Frame(
            self.cricket_info_page,
            bg='White',
            width=w_width - margin_length,
            height=70,
            relief=RIDGE,
            bd=3,
            )
        self.cricket_info_top.pack_propagate(False)
        self.cricket_info_top.pack(pady=3)

        self.back_to_info_cricket = Button(self.cricket_info_top,
                bg='White', text='Back', font=self.button_font,
                command=self.return_to_info)
        self.back_to_info_cricket.pack(side=RIGHT, padx=5)

        self.cricket_info_label = Label(self.cricket_info_top,
                bg='White', text='Cricket', font=self.header_font)
        self.cricket_info_label.pack(side=LEFT, padx=5)

        self.cricket_info_label_two = Label(self.cricket_info_top,
                bg='White', text='Summer sport', font=('Helvetica', 12))
        self.cricket_info_label_two.pack(side=LEFT)

        # First XI box

        self.cricket_info_firstXI = Frame(
            self.cricket_info_page,
            bg='White',
            width=w_width - margin_length,
            height=150,
            relief=RIDGE,
            bd=3,
            )
        self.cricket_info_firstXI.pack_propagate(False)
        self.cricket_info_firstXI.pack(pady=3)

        self.cricket_firstXI_top = Frame(self.cricket_info_firstXI,
                bg='White', width=w_width - margin_length, height=30)
        self.cricket_firstXI_top.pack_propagate(False)
        self.cricket_firstXI_top.pack(pady=3)

        self.cricket_firstXI_label = Label(self.cricket_firstXI_top,
                text='First XI', bg='White', font=self.subheader_font)
        self.cricket_firstXI_label.pack(side=LEFT, padx=5)

        self.cricket_firstXI_organiser = \
            Label(self.cricket_firstXI_top,
                  text='Teacher in charge: Mr Chopra', bg='White',
                  font=('Helvetica', 10))
        self.cricket_firstXI_organiser.pack(side=LEFT)

        self.cricket_firstXI_textbox = Frame(self.cricket_info_firstXI,
                bg='White', width=w_width - margin_length, height=55)
        self.cricket_firstXI_textbox.pack_propagate(False)
        self.cricket_firstXI_textbox.pack()

        self.cricket_firstXI_trainingLabel = \
            Label(self.cricket_firstXI_textbox,
                  text='Boys trainings on Wednesday / Friday after school'
                  , bg='White', font=('Helvetica', 11))
        self.cricket_firstXI_trainingLabel.pack(side=LEFT, padx=5)

        self.cricket_firstXI_textbox_two = \
            Frame(self.cricket_info_firstXI, bg='White', width=w_width
                  - margin_length, height=55)
        self.cricket_firstXI_textbox_two.pack_propagate(False)
        self.cricket_firstXI_textbox_two.pack()

        self.cricket_firstXI_trainingLabel_two = \
            Label(self.cricket_firstXI_textbox_two,
                  text='Girls trainings on Monday / Tuesday after school'
                  , bg='White', font=('Helvetica', 11))
        self.cricket_firstXI_trainingLabel_two.pack(side=LEFT, padx=5)

        # Second XI box

        self.cricket_info_secondXI = Frame(
            self.cricket_info_page,
            bg='White',
            width=w_width - margin_length,
            height=150,
            relief=RIDGE,
            bd=3,
            )
        self.cricket_info_secondXI.pack_propagate(False)
        self.cricket_info_secondXI.pack(pady=3)

        self.cricket_secondXI_top = Frame(self.cricket_info_secondXI,
                bg='White', width=w_width - margin_length, height=30)
        self.cricket_secondXI_top.pack_propagate(False)
        self.cricket_secondXI_top.pack(pady=3)

        self.cricket_secondXI_label = Label(self.cricket_secondXI_top,
                text='Second XI', bg='White', font=self.subheader_font)
        self.cricket_secondXI_label.pack(side=LEFT, padx=5)

        self.cricket_secondXI_organiser = \
            Label(self.cricket_secondXI_top,
                  text='Teacher in charge: Mr Kerins', bg='White',
                  font=('Helvetica', 10))
        self.cricket_secondXI_organiser.pack(side=LEFT)

        self.cricket_secondXI_textbox = \
            Frame(self.cricket_info_secondXI, bg='White', width=w_width
                  - margin_length, height=55)
        self.cricket_secondXI_textbox.pack_propagate(False)
        self.cricket_secondXI_textbox.pack()

        self.cricket_secondXI_trainingLabel = \
            Label(self.cricket_secondXI_textbox,
                  text='Boys trainings on Monday / Wednesday after school'
                  , bg='White', font=('Helvetica', 11))
        self.cricket_secondXI_trainingLabel.pack(side=LEFT, padx=5)

        self.cricket_secondXI_textbox_two = \
            Frame(self.cricket_info_secondXI, bg='White', width=w_width
                  - margin_length, height=55)
        self.cricket_secondXI_textbox_two.pack_propagate(False)
        self.cricket_secondXI_textbox_two.pack()

        self.cricket_secondXI_trainingLabel_two = \
            Label(self.cricket_secondXI_textbox_two,
                  text='Girls trainings on Tuesday / Thursday after school'
                  , bg='White', font=('Helvetica', 11))
        self.cricket_secondXI_trainingLabel_two.pack(side=LEFT, padx=5)

        # Junior box

        self.cricket_info_Junior = Frame(
            self.cricket_info_page,
            bg='White',
            width=w_width - margin_length,
            height=150,
            relief=RIDGE,
            bd=3,
            )
        self.cricket_info_Junior.pack_propagate(False)
        self.cricket_info_Junior.pack(pady=3)

        self.cricket_Junior_top = Frame(self.cricket_info_Junior,
                bg='White', width=w_width - margin_length, height=30)
        self.cricket_Junior_top.pack_propagate(False)
        self.cricket_Junior_top.pack(pady=3)

        self.cricket_Junior_label = Label(self.cricket_Junior_top,
                text='Junior', bg='White', font=self.subheader_font)
        self.cricket_Junior_label.pack(side=LEFT, padx=5)

        self.cricket_Junior_organiser = Label(self.cricket_Junior_top,
                text='Teacher in charge: Mr Singh', bg='White',
                font=('Helvetica', 10))
        self.cricket_Junior_organiser.pack(side=LEFT)

        self.cricket_Junior_textbox = Frame(self.cricket_info_Junior,
                bg='White', width=w_width - margin_length, height=55)
        self.cricket_Junior_textbox.pack_propagate(False)
        self.cricket_Junior_textbox.pack()

        self.cricket_Junior_trainingLabel = \
            Label(self.cricket_Junior_textbox,
                  text='Boys trainings on Tuesday after school',
                  bg='White', font=('Helvetica', 11))
        self.cricket_Junior_trainingLabel.pack(side=LEFT, padx=5)

        self.cricket_Junior_textbox_two = \
            Frame(self.cricket_info_Junior, bg='White', width=w_width
                  - margin_length, height=55)
        self.cricket_Junior_textbox_two.pack_propagate(False)
        self.cricket_Junior_textbox_two.pack()

        self.cricket_Junior_trainingLabel_two = \
            Label(self.cricket_Junior_textbox_two,
                  text='Girls trainings on Wednesday after school',
                  bg='White', font=('Helvetica', 11))
        self.cricket_Junior_trainingLabel_two.pack(side=LEFT, padx=5)

        # Rugby info page

        self.rugby_info_page = Frame(self.info_page, bg='White',
                width=w_width, height=600)
        self.rugby_info_page.pack_propagate(False)

        self.rugby_top_gap = Frame(self.rugby_info_page, bg='White',
                                   width=w_width, height=25)
        self.rugby_top_gap.pack()

        self.rugby_info_top = Frame(
            self.rugby_info_page,
            bg='White',
            width=w_width - margin_length,
            height=70,
            relief=RIDGE,
            bd=3,
            )
        self.rugby_info_top.pack_propagate(False)
        self.rugby_info_top.pack(pady=3)

        self.back_to_info_rugby = Button(self.rugby_info_top, bg='White'
                , text='Back', font=self.button_font,
                command=self.return_to_info)
        self.back_to_info_rugby.pack(side=RIGHT, padx=5)

        self.rugby_info_label = Label(self.rugby_info_top, bg='White',
                text='Rugby', font=self.header_font)
        self.rugby_info_label.pack(side=LEFT, padx=5)

        self.rugby_info_label_two = Label(self.rugby_info_top,
                bg='White', text='Winter sport', font=('Helvetica', 12))
        self.rugby_info_label_two.pack(side=LEFT)

        # First XI box

        self.rugby_info_firstXI = Frame(
            self.rugby_info_page,
            bg='White',
            width=w_width - margin_length,
            height=150,
            relief=RIDGE,
            bd=3,
            )
        self.rugby_info_firstXI.pack_propagate(False)
        self.rugby_info_firstXI.pack(pady=3)

        self.rugby_firstXI_top = Frame(self.rugby_info_firstXI,
                bg='White', width=w_width - margin_length, height=30)
        self.rugby_firstXI_top.pack_propagate(False)
        self.rugby_firstXI_top.pack(pady=3)

        self.rugby_firstXI_label = Label(self.rugby_firstXI_top,
                text='First XI', bg='White', font=self.subheader_font)
        self.rugby_firstXI_label.pack(side=LEFT, padx=5)

        self.rugby_firstXI_organiser = Label(self.rugby_firstXI_top,
                text='Teacher in charge: Mr Tuiali i', bg='White',
                font=('Helvetica', 10))
        self.rugby_firstXI_organiser.pack(side=LEFT)

        self.rugby_firstXI_textbox = Frame(self.rugby_info_firstXI,
                bg='White', width=w_width - margin_length, height=55)
        self.rugby_firstXI_textbox.pack_propagate(False)
        self.rugby_firstXI_textbox.pack()

        self.rugby_firstXI_trainingLabel = \
            Label(self.rugby_firstXI_textbox,
                  text='Boys trainings on Monday / Wednesday after school'
                  , bg='White', font=('Helvetica', 11))
        self.rugby_firstXI_trainingLabel.pack(side=LEFT, padx=5)

        self.rugby_firstXI_textbox_two = Frame(self.rugby_info_firstXI,
                bg='White', width=w_width - margin_length, height=55)
        self.rugby_firstXI_textbox_two.pack_propagate(False)
        self.rugby_firstXI_textbox_two.pack()

        self.rugby_firstXI_trainingLabel_two = \
            Label(self.rugby_firstXI_textbox_two,
                  text='Girls trainings on Wednesday / Thursday after school'
                  , bg='White', font=('Helvetica', 11))
        self.rugby_firstXI_trainingLabel_two.pack(side=LEFT, padx=5)

        # Second XI box

        self.rugby_info_secondXI = Frame(
            self.rugby_info_page,
            bg='White',
            width=w_width - margin_length,
            height=150,
            relief=RIDGE,
            bd=3,
            )
        self.rugby_info_secondXI.pack_propagate(False)
        self.rugby_info_secondXI.pack(pady=3)

        self.rugby_secondXI_top = Frame(self.rugby_info_secondXI,
                bg='White', width=w_width - margin_length, height=30)
        self.rugby_secondXI_top.pack_propagate(False)
        self.rugby_secondXI_top.pack(pady=3)

        self.rugby_secondXI_label = Label(self.rugby_secondXI_top,
                text='Second XI', bg='White', font=self.subheader_font)
        self.rugby_secondXI_label.pack(side=LEFT, padx=5)

        self.rugby_secondXI_organiser = Label(self.rugby_secondXI_top,
                text='Teacher in charge: Ms Burns', bg='White',
                font=('Helvetica', 10))
        self.rugby_secondXI_organiser.pack(side=LEFT)

        self.rugby_secondXI_textbox = Frame(self.rugby_info_secondXI,
                bg='White', width=w_width - margin_length, height=55)
        self.rugby_secondXI_textbox.pack_propagate(False)
        self.rugby_secondXI_textbox.pack()

        self.rugby_secondXI_trainingLabel = \
            Label(self.rugby_secondXI_textbox,
                  text='Boys trainings on Tuesday / Wednesday morning',
                  bg='White', font=('Helvetica', 11))
        self.rugby_secondXI_trainingLabel.pack(side=LEFT, padx=5)

        self.rugby_secondXI_textbox_two = \
            Frame(self.rugby_info_secondXI, bg='White', width=w_width
                  - margin_length, height=55)
        self.rugby_secondXI_textbox_two.pack_propagate(False)
        self.rugby_secondXI_textbox_two.pack()

        self.rugby_secondXI_trainingLabel_two = \
            Label(self.rugby_secondXI_textbox_two,
                  text='Girls trainings on Tuesday / Friday after school'
                  , bg='White', font=('Helvetica', 11))
        self.rugby_secondXI_trainingLabel_two.pack(side=LEFT, padx=5)

        # Junior box

        self.rugby_info_Junior = Frame(
            self.rugby_info_page,
            bg='White',
            width=w_width - margin_length,
            height=150,
            relief=RIDGE,
            bd=3,
            )
        self.rugby_info_Junior.pack_propagate(False)
        self.rugby_info_Junior.pack(pady=3)

        self.rugby_Junior_top = Frame(self.rugby_info_Junior, bg='White'
                , width=w_width - margin_length, height=30)
        self.rugby_Junior_top.pack_propagate(False)
        self.rugby_Junior_top.pack(pady=3)

        self.rugby_Junior_label = Label(self.rugby_Junior_top,
                text='Junior', bg='White', font=self.subheader_font)
        self.rugby_Junior_label.pack(side=LEFT, padx=5)

        self.rugby_Junior_organiser = Label(self.rugby_Junior_top,
                text='Teacher in charge: Ms Yang', bg='White',
                font=('Helvetica', 10))
        self.rugby_Junior_organiser.pack(side=LEFT)

        self.rugby_Junior_textbox = Frame(self.rugby_info_Junior,
                bg='White', width=w_width - margin_length, height=55)
        self.rugby_Junior_textbox.pack_propagate(False)
        self.rugby_Junior_textbox.pack()

        self.rugby_Junior_trainingLabel = \
            Label(self.rugby_Junior_textbox,
                  text='Boys trainings on Monday after school',
                  bg='White', font=('Helvetica', 11))
        self.rugby_Junior_trainingLabel.pack(side=LEFT, padx=5)

        self.rugby_Junior_textbox_two = Frame(self.rugby_info_Junior,
                bg='White', width=w_width - margin_length, height=55)
        self.rugby_Junior_textbox_two.pack_propagate(False)
        self.rugby_Junior_textbox_two.pack()

        self.rugby_Junior_trainingLabel_two = \
            Label(self.rugby_Junior_textbox_two,
                  text='Girls trainings on Tuesday after school',
                  bg='White', font=('Helvetica', 11))
        self.rugby_Junior_trainingLabel_two.pack(side=LEFT, padx=5)

        # Stat page frame / statistics is the sports analytics screen ---------------------------

        self.stat_page = Frame(self.content_frame, background='#EFECEC'
                               , width=w_width, height=600)
        self.stat_page.grid_propagate(False)
        self.stat_page.pack_propagate(False)

        self.sports_stat_label = Label(self.stat_page, bg='#EFECEC',
                text='Sport analytics', font=self.header_font)
        self.sports_stat_label.pack(pady=5)

        self.sports_stat_football_box = Frame(
            self.stat_page,
            bg='White',
            width=w_width - margin_length,
            height=100,
            relief=RIDGE,
            bd=3,
            )
        self.sports_stat_football_box.pack_propagate(False)
        self.sports_stat_football_box.grid_propagate(False)
        self.sports_stat_football_box.pack(pady=3)

        # First column of the box

        self.sports_stat_football_names = \
            Frame(self.sports_stat_football_box, bg='White', width=100,
                  height=100)
        self.sports_stat_football_names.pack_propagate(False)
        self.sports_stat_football_names.grid(row=0, column=0)

        self.sports_stat_football_name1 = \
            Frame(self.sports_stat_football_names, bg='White',
                  width=100, height=19)
        self.sports_stat_football_name1.pack_propagate(False)
        self.sports_stat_football_name1.pack()

        self.sports_stat_football_namelabel = Label(
            self.sports_stat_football_name1,
            text='Football',
            bg='White',
            font=('Helvetica', 12),
            width=10,
            height=2,
            )
        self.sports_stat_football_namelabel.pack()

        self.sports_stat_football_name2 = \
            Frame(self.sports_stat_football_names, bg='White',
                  width=100, height=27)
        self.sports_stat_football_name2.pack_propagate(False)
        self.sports_stat_football_name2.pack()

        self.sports_stat_football_namelabel2 = Label(
            self.sports_stat_football_name2,
            text='First XI',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_football_namelabel2.pack()

        self.sports_stat_football_name3 = \
            Frame(self.sports_stat_football_names, bg='White',
                  width=100, height=27)
        self.sports_stat_football_name3.pack_propagate(False)
        self.sports_stat_football_name3.pack()

        self.sports_stat_football_namelabel3 = Label(
            self.sports_stat_football_name3,
            text='Second XI',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_football_namelabel3.pack()

        self.sports_stat_football_name4 = \
            Frame(self.sports_stat_football_names, bg='White',
                  width=100, height=27)
        self.sports_stat_football_name4.pack_propagate(False)
        self.sports_stat_football_name4.pack()

        self.sports_stat_football_namelabel4 = Label(
            self.sports_stat_football_name4,
            text='Junior',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_football_namelabel4.pack()

        # Second column of the box

        self.sports_stat_football_wins = \
            Frame(self.sports_stat_football_box, bg='White', width=90,
                  height=100)
        self.sports_stat_football_wins.pack_propagate(False)
        self.sports_stat_football_wins.grid(row=0, column=1)

        self.sports_stat_football_win1 = \
            Frame(self.sports_stat_football_wins, bg='White',
                  width=100, height=19)
        self.sports_stat_football_win1.pack_propagate(False)
        self.sports_stat_football_win1.pack()

        self.sports_stat_football_winlabel = Label(
            self.sports_stat_football_win1,
            text='Wins',
            bg='White',
            font=('Helvetica', 12),
            width=10,
            height=2,
            )
        self.sports_stat_football_winlabel.pack()

        self.sports_stat_football_win2 = \
            Frame(self.sports_stat_football_wins, bg='White',
                  width=100, height=27)
        self.sports_stat_football_win2.pack_propagate(False)
        self.sports_stat_football_win2.pack()

        self.sports_stat_football_winlabel2 = Label(
            self.sports_stat_football_win2,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_football_winlabel2.pack()

        self.sports_stat_football_win3 = \
            Frame(self.sports_stat_football_wins, bg='White',
                  width=100, height=27)
        self.sports_stat_football_win3.pack_propagate(False)
        self.sports_stat_football_win3.pack()

        self.sports_stat_football_winlabel3 = Label(
            self.sports_stat_football_win3,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_football_winlabel3.pack()

        self.sports_stat_football_win4 = \
            Frame(self.sports_stat_football_wins, bg='White',
                  width=100, height=27)
        self.sports_stat_football_win4.pack_propagate(False)
        self.sports_stat_football_win4.pack()

        self.sports_stat_football_winlabel4 = Label(
            self.sports_stat_football_win4,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_football_winlabel4.pack()

        # Third column of the box

        self.sports_stat_football_losses = \
            Frame(self.sports_stat_football_box, bg='White', width=90,
                  height=100)
        self.sports_stat_football_losses.pack_propagate(False)
        self.sports_stat_football_losses.grid(row=0, column=2)

        self.sports_stat_football_loss1 = \
            Frame(self.sports_stat_football_losses, bg='White',
                  width=100, height=19)
        self.sports_stat_football_loss1.pack_propagate(False)
        self.sports_stat_football_loss1.pack()

        self.sports_stat_football_losslabel = Label(
            self.sports_stat_football_loss1,
            text='Losses',
            bg='White',
            font=('Helvetica', 12),
            width=10,
            height=2,
            )
        self.sports_stat_football_losslabel.pack()

        self.sports_stat_football_loss2 = \
            Frame(self.sports_stat_football_losses, bg='White',
                  width=100, height=27)
        self.sports_stat_football_loss2.pack_propagate(False)
        self.sports_stat_football_loss2.pack()

        self.sports_stat_football_losslabel2 = Label(
            self.sports_stat_football_loss2,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_football_losslabel2.pack()

        self.sports_stat_football_loss3 = \
            Frame(self.sports_stat_football_losses, bg='White',
                  width=100, height=27)
        self.sports_stat_football_loss3.pack_propagate(False)
        self.sports_stat_football_loss3.pack()

        self.sports_stat_football_losslabel3 = Label(
            self.sports_stat_football_loss3,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_football_losslabel3.pack()

        self.sports_stat_football_loss4 = \
            Frame(self.sports_stat_football_losses, bg='White',
                  width=100, height=27)
        self.sports_stat_football_loss4.pack_propagate(False)
        self.sports_stat_football_loss4.pack()

        self.sports_stat_football_losslabel4 = Label(
            self.sports_stat_football_loss4,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_football_losslabel4.pack()

        # Fourth column of the box

        self.sports_stat_football_winlosses = \
            Frame(self.sports_stat_football_box, bg='White', width=90,
                  height=100)
        self.sports_stat_football_winlosses.pack_propagate(False)
        self.sports_stat_football_winlosses.grid(row=0, column=3)

        self.sports_stat_football_winloss1 = \
            Frame(self.sports_stat_football_winlosses, bg='White',
                  width=100, height=19)
        self.sports_stat_football_winloss1.pack_propagate(False)
        self.sports_stat_football_winloss1.pack()

        self.sports_stat_football_winlosslabel = Label(
            self.sports_stat_football_winloss1,
            text='W/L',
            bg='White',
            font=('Helvetica', 12),
            width=10,
            height=2,
            )
        self.sports_stat_football_winlosslabel.pack()

        self.sports_stat_football_winloss2 = \
            Frame(self.sports_stat_football_winlosses, bg='White',
                  width=100, height=27)
        self.sports_stat_football_winloss2.pack_propagate(False)
        self.sports_stat_football_winloss2.pack()

        self.sports_stat_football_winlosslabel2 = Label(
            self.sports_stat_football_winloss2,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_football_winlosslabel2.pack()

        self.sports_stat_football_winloss3 = \
            Frame(self.sports_stat_football_winlosses, bg='White',
                  width=100, height=27)
        self.sports_stat_football_winloss3.pack_propagate(False)
        self.sports_stat_football_winloss3.pack()

        self.sports_stat_football_winlosslabel3 = Label(
            self.sports_stat_football_winloss3,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_football_winlosslabel3.pack()

        self.sports_stat_football_winloss4 = \
            Frame(self.sports_stat_football_winlosses, bg='White',
                  width=100, height=27)
        self.sports_stat_football_winloss4.pack_propagate(False)
        self.sports_stat_football_winloss4.pack()

        self.sports_stat_football_winlosslabel4 = Label(
            self.sports_stat_football_winloss4,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_football_winlosslabel4.pack()

        # Basketball analytics box

        self.sports_stat_basketball_box = Frame(
            self.stat_page,
            bg='White',
            width=w_width - margin_length,
            height=100,
            relief=RIDGE,
            bd=3,
            )
        self.sports_stat_basketball_box.pack_propagate(False)
        self.sports_stat_basketball_box.grid_propagate(False)
        self.sports_stat_basketball_box.pack(pady=3)

        # First column of the box

        self.sports_stat_basketball_names = \
            Frame(self.sports_stat_basketball_box, bg='White',
                  width=100, height=100)
        self.sports_stat_basketball_names.pack_propagate(False)
        self.sports_stat_basketball_names.grid(row=0, column=0)

        self.sports_stat_basketball_name1 = \
            Frame(self.sports_stat_basketball_names, bg='White',
                  width=100, height=19)
        self.sports_stat_basketball_name1.pack_propagate(False)
        self.sports_stat_basketball_name1.pack()

        self.sports_stat_basketball_namelabel = Label(
            self.sports_stat_basketball_name1,
            text='Basketball',
            bg='White',
            font=('Helvetica', 12),
            width=10,
            height=2,
            )
        self.sports_stat_basketball_namelabel.pack()

        self.sports_stat_basketball_name2 = \
            Frame(self.sports_stat_basketball_names, bg='White',
                  width=100, height=27)
        self.sports_stat_basketball_name2.pack_propagate(False)
        self.sports_stat_basketball_name2.pack()

        self.sports_stat_basketball_namelabel2 = Label(
            self.sports_stat_basketball_name2,
            text='Senior',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_basketball_namelabel2.pack()

        self.sports_stat_basketball_name3 = \
            Frame(self.sports_stat_basketball_names, bg='White',
                  width=100, height=27)
        self.sports_stat_basketball_name3.pack_propagate(False)
        self.sports_stat_basketball_name3.pack()

        self.sports_stat_basketball_namelabel3 = Label(
            self.sports_stat_basketball_name3,
            text='U17',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_basketball_namelabel3.pack()

        self.sports_stat_basketball_name4 = \
            Frame(self.sports_stat_basketball_names, bg='White',
                  width=100, height=27)
        self.sports_stat_basketball_name4.pack_propagate(False)
        self.sports_stat_basketball_name4.pack()

        self.sports_stat_basketball_namelabel4 = Label(
            self.sports_stat_basketball_name4,
            text='Junior',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_basketball_namelabel4.pack()

        # Second column of the box

        self.sports_stat_basketball_wins = \
            Frame(self.sports_stat_basketball_box, bg='White',
                  width=90, height=100)
        self.sports_stat_basketball_wins.pack_propagate(False)
        self.sports_stat_basketball_wins.grid(row=0, column=1)

        self.sports_stat_basketball_win1 = \
            Frame(self.sports_stat_basketball_wins, bg='White',
                  width=100, height=19)
        self.sports_stat_basketball_win1.pack_propagate(False)
        self.sports_stat_basketball_win1.pack()

        self.sports_stat_basketball_winlabel = Label(
            self.sports_stat_basketball_win1,
            text='Wins',
            bg='White',
            font=('Helvetica', 12),
            width=10,
            height=2,
            )
        self.sports_stat_basketball_winlabel.pack()

        self.sports_stat_basketball_win2 = \
            Frame(self.sports_stat_basketball_wins, bg='White',
                  width=100, height=27)
        self.sports_stat_basketball_win2.pack_propagate(False)
        self.sports_stat_basketball_win2.pack()

        self.sports_stat_basketball_winlabel2 = Label(
            self.sports_stat_basketball_win2,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_basketball_winlabel2.pack()

        self.sports_stat_basketball_win3 = \
            Frame(self.sports_stat_basketball_wins, bg='White',
                  width=100, height=27)
        self.sports_stat_basketball_win3.pack_propagate(False)
        self.sports_stat_basketball_win3.pack()

        self.sports_stat_basketball_winlabel3 = Label(
            self.sports_stat_basketball_win3,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_basketball_winlabel3.pack()

        self.sports_stat_basketball_win4 = \
            Frame(self.sports_stat_basketball_wins, bg='White',
                  width=100, height=27)
        self.sports_stat_basketball_win4.pack_propagate(False)
        self.sports_stat_basketball_win4.pack()

        self.sports_stat_basketball_winlabel4 = Label(
            self.sports_stat_basketball_win4,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_basketball_winlabel4.pack()

        # Third column of the box

        self.sports_stat_basketball_losses = \
            Frame(self.sports_stat_basketball_box, bg='White',
                  width=90, height=100)
        self.sports_stat_basketball_losses.pack_propagate(False)
        self.sports_stat_basketball_losses.grid(row=0, column=2)

        self.sports_stat_basketball_loss1 = \
            Frame(self.sports_stat_basketball_losses, bg='White',
                  width=100, height=19)
        self.sports_stat_basketball_loss1.pack_propagate(False)
        self.sports_stat_basketball_loss1.pack()

        self.sports_stat_basketball_losslabel = Label(
            self.sports_stat_basketball_loss1,
            text='Losses',
            bg='White',
            font=('Helvetica', 12),
            width=10,
            height=2,
            )
        self.sports_stat_basketball_losslabel.pack()

        self.sports_stat_basketball_loss2 = \
            Frame(self.sports_stat_basketball_losses, bg='White',
                  width=100, height=27)
        self.sports_stat_basketball_loss2.pack_propagate(False)
        self.sports_stat_basketball_loss2.pack()

        self.sports_stat_basketball_losslabel2 = Label(
            self.sports_stat_basketball_loss2,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_basketball_losslabel2.pack()

        self.sports_stat_basketball_loss3 = \
            Frame(self.sports_stat_basketball_losses, bg='White',
                  width=100, height=27)
        self.sports_stat_basketball_loss3.pack_propagate(False)
        self.sports_stat_basketball_loss3.pack()

        self.sports_stat_basketball_losslabel3 = Label(
            self.sports_stat_basketball_loss3,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_basketball_losslabel3.pack()

        self.sports_stat_basketball_loss4 = \
            Frame(self.sports_stat_basketball_losses, bg='White',
                  width=100, height=27)
        self.sports_stat_basketball_loss4.pack_propagate(False)
        self.sports_stat_basketball_loss4.pack()

        self.sports_stat_basketball_losslabel4 = Label(
            self.sports_stat_basketball_loss4,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_basketball_losslabel4.pack()

        # Fourth column of the box

        self.sports_stat_basketball_winlosses = \
            Frame(self.sports_stat_basketball_box, bg='White',
                  width=90, height=100)
        self.sports_stat_basketball_winlosses.pack_propagate(False)
        self.sports_stat_basketball_winlosses.grid(row=0, column=3)

        self.sports_stat_basketball_winloss1 = \
            Frame(self.sports_stat_basketball_winlosses, bg='White',
                  width=100, height=19)
        self.sports_stat_basketball_winloss1.pack_propagate(False)
        self.sports_stat_basketball_winloss1.pack()

        self.sports_stat_basketball_winlosslabel = Label(
            self.sports_stat_basketball_winloss1,
            text='W/L',
            bg='White',
            font=('Helvetica', 12),
            width=10,
            height=2,
            )
        self.sports_stat_basketball_winlosslabel.pack()

        self.sports_stat_basketball_winloss2 = \
            Frame(self.sports_stat_basketball_winlosses, bg='White',
                  width=100, height=27)
        self.sports_stat_basketball_winloss2.pack_propagate(False)
        self.sports_stat_basketball_winloss2.pack()

        self.sports_stat_basketball_winlosslabel2 = Label(
            self.sports_stat_basketball_winloss2,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_basketball_winlosslabel2.pack()

        self.sports_stat_basketball_winloss3 = \
            Frame(self.sports_stat_basketball_winlosses, bg='White',
                  width=100, height=27)
        self.sports_stat_basketball_winloss3.pack_propagate(False)
        self.sports_stat_basketball_winloss3.pack()

        self.sports_stat_basketball_winlosslabel3 = Label(
            self.sports_stat_basketball_winloss3,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_basketball_winlosslabel3.pack()

        self.sports_stat_basketball_winloss4 = \
            Frame(self.sports_stat_basketball_winlosses, bg='White',
                  width=100, height=27)
        self.sports_stat_basketball_winloss4.pack_propagate(False)
        self.sports_stat_basketball_winloss4.pack()

        self.sports_stat_basketball_winlosslabel4 = Label(
            self.sports_stat_basketball_winloss4,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_basketball_winlosslabel4.pack()

        # Hockey analytics box

        self.sports_stat_hockey_box = Frame(
            self.stat_page,
            bg='White',
            width=w_width - margin_length,
            height=100,
            relief=RIDGE,
            bd=3,
            )
        self.sports_stat_hockey_box.pack_propagate(False)
        self.sports_stat_hockey_box.grid_propagate(False)
        self.sports_stat_hockey_box.pack(pady=3)

        # First column of the box

        self.sports_stat_hockey_names = \
            Frame(self.sports_stat_hockey_box, bg='White', width=100,
                  height=100)
        self.sports_stat_hockey_names.pack_propagate(False)
        self.sports_stat_hockey_names.grid(row=0, column=0)

        self.sports_stat_hockey_name1 = \
            Frame(self.sports_stat_hockey_names, bg='White', width=100,
                  height=19)
        self.sports_stat_hockey_name1.pack_propagate(False)
        self.sports_stat_hockey_name1.pack()

        self.sports_stat_hockey_namelabel = Label(
            self.sports_stat_hockey_name1,
            text='Hockey',
            bg='White',
            font=('Helvetica', 12),
            width=10,
            height=2,
            )
        self.sports_stat_hockey_namelabel.pack()

        self.sports_stat_hockey_name2 = \
            Frame(self.sports_stat_hockey_names, bg='White', width=100,
                  height=27)
        self.sports_stat_hockey_name2.pack_propagate(False)
        self.sports_stat_hockey_name2.pack()

        self.sports_stat_hockey_namelabel2 = Label(
            self.sports_stat_hockey_name2,
            text='First XI',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_hockey_namelabel2.pack()

        self.sports_stat_hockey_name3 = \
            Frame(self.sports_stat_hockey_names, bg='White', width=100,
                  height=27)
        self.sports_stat_hockey_name3.pack_propagate(False)
        self.sports_stat_hockey_name3.pack()

        self.sports_stat_hockey_namelabel3 = Label(
            self.sports_stat_hockey_name3,
            text='Second XI',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_hockey_namelabel3.pack()

        self.sports_stat_hockey_name4 = \
            Frame(self.sports_stat_hockey_names, bg='White', width=100,
                  height=27)
        self.sports_stat_hockey_name4.pack_propagate(False)
        self.sports_stat_hockey_name4.pack()

        self.sports_stat_hockey_namelabel4 = Label(
            self.sports_stat_hockey_name4,
            text='Junior',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_hockey_namelabel4.pack()

        # Second column of the box

        self.sports_stat_hockey_wins = \
            Frame(self.sports_stat_hockey_box, bg='White', width=90,
                  height=100)
        self.sports_stat_hockey_wins.pack_propagate(False)
        self.sports_stat_hockey_wins.grid(row=0, column=1)

        self.sports_stat_hockey_win1 = \
            Frame(self.sports_stat_hockey_wins, bg='White', width=100,
                  height=19)
        self.sports_stat_hockey_win1.pack_propagate(False)
        self.sports_stat_hockey_win1.pack()

        self.sports_stat_hockey_winlabel = Label(
            self.sports_stat_hockey_win1,
            text='Wins',
            bg='White',
            font=('Helvetica', 12),
            width=10,
            height=2,
            )
        self.sports_stat_hockey_winlabel.pack()

        self.sports_stat_hockey_win2 = \
            Frame(self.sports_stat_hockey_wins, bg='White', width=100,
                  height=27)
        self.sports_stat_hockey_win2.pack_propagate(False)
        self.sports_stat_hockey_win2.pack()

        self.sports_stat_hockey_winlabel2 = Label(
            self.sports_stat_hockey_win2,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_hockey_winlabel2.pack()

        self.sports_stat_hockey_win3 = \
            Frame(self.sports_stat_hockey_wins, bg='White', width=100,
                  height=27)
        self.sports_stat_hockey_win3.pack_propagate(False)
        self.sports_stat_hockey_win3.pack()

        self.sports_stat_hockey_winlabel3 = Label(
            self.sports_stat_hockey_win3,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_hockey_winlabel3.pack()

        self.sports_stat_hockey_win4 = \
            Frame(self.sports_stat_hockey_wins, bg='White', width=100,
                  height=27)
        self.sports_stat_hockey_win4.pack_propagate(False)
        self.sports_stat_hockey_win4.pack()

        self.sports_stat_hockey_winlabel4 = Label(
            self.sports_stat_hockey_win4,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_hockey_winlabel4.pack()

        # Third column of the box

        self.sports_stat_hockey_losses = \
            Frame(self.sports_stat_hockey_box, bg='White', width=90,
                  height=100)
        self.sports_stat_hockey_losses.pack_propagate(False)
        self.sports_stat_hockey_losses.grid(row=0, column=2)

        self.sports_stat_hockey_loss1 = \
            Frame(self.sports_stat_hockey_losses, bg='White',
                  width=100, height=19)
        self.sports_stat_hockey_loss1.pack_propagate(False)
        self.sports_stat_hockey_loss1.pack()

        self.sports_stat_hockey_losslabel = Label(
            self.sports_stat_hockey_loss1,
            text='Losses',
            bg='White',
            font=('Helvetica', 12),
            width=10,
            height=2,
            )
        self.sports_stat_hockey_losslabel.pack()

        self.sports_stat_hockey_loss2 = \
            Frame(self.sports_stat_hockey_losses, bg='White',
                  width=100, height=27)
        self.sports_stat_hockey_loss2.pack_propagate(False)
        self.sports_stat_hockey_loss2.pack()

        self.sports_stat_hockey_losslabel2 = Label(
            self.sports_stat_hockey_loss2,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_hockey_losslabel2.pack()

        self.sports_stat_hockey_loss3 = \
            Frame(self.sports_stat_hockey_losses, bg='White',
                  width=100, height=27)
        self.sports_stat_hockey_loss3.pack_propagate(False)
        self.sports_stat_hockey_loss3.pack()

        self.sports_stat_hockey_losslabel3 = Label(
            self.sports_stat_hockey_loss3,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_hockey_losslabel3.pack()

        self.sports_stat_hockey_loss4 = \
            Frame(self.sports_stat_hockey_losses, bg='White',
                  width=100, height=27)
        self.sports_stat_hockey_loss4.pack_propagate(False)
        self.sports_stat_hockey_loss4.pack()

        self.sports_stat_hockey_losslabel4 = Label(
            self.sports_stat_hockey_loss4,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_hockey_losslabel4.pack()

        # Fourth column of the box

        self.sports_stat_hockey_winlosses = \
            Frame(self.sports_stat_hockey_box, bg='White', width=90,
                  height=100)
        self.sports_stat_hockey_winlosses.pack_propagate(False)
        self.sports_stat_hockey_winlosses.grid(row=0, column=3)

        self.sports_stat_hockey_winloss1 = \
            Frame(self.sports_stat_hockey_winlosses, bg='White',
                  width=100, height=19)
        self.sports_stat_hockey_winloss1.pack_propagate(False)
        self.sports_stat_hockey_winloss1.pack()

        self.sports_stat_hockey_winlosslabel = Label(
            self.sports_stat_hockey_winloss1,
            text='W/L',
            bg='White',
            font=('Helvetica', 12),
            width=10,
            height=2,
            )
        self.sports_stat_hockey_winlosslabel.pack()

        self.sports_stat_hockey_winloss2 = \
            Frame(self.sports_stat_hockey_winlosses, bg='White',
                  width=100, height=27)
        self.sports_stat_hockey_winloss2.pack_propagate(False)
        self.sports_stat_hockey_winloss2.pack()

        self.sports_stat_hockey_winlosslabel2 = Label(
            self.sports_stat_hockey_winloss2,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_hockey_winlosslabel2.pack()

        self.sports_stat_hockey_winloss3 = \
            Frame(self.sports_stat_hockey_winlosses, bg='White',
                  width=100, height=27)
        self.sports_stat_hockey_winloss3.pack_propagate(False)
        self.sports_stat_hockey_winloss3.pack()

        self.sports_stat_hockey_winlosslabel3 = Label(
            self.sports_stat_hockey_winloss3,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_hockey_winlosslabel3.pack()

        self.sports_stat_hockey_winloss4 = \
            Frame(self.sports_stat_hockey_winlosses, bg='White',
                  width=100, height=27)
        self.sports_stat_hockey_winloss4.pack_propagate(False)
        self.sports_stat_hockey_winloss4.pack()

        self.sports_stat_hockey_winlosslabel4 = Label(
            self.sports_stat_hockey_winloss4,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_hockey_winlosslabel4.pack()

        # Cricket analytics box

        self.sports_stat_cricket_box = Frame(
            self.stat_page,
            bg='White',
            width=w_width - margin_length,
            height=100,
            relief=RIDGE,
            bd=3,
            )
        self.sports_stat_cricket_box.pack_propagate(False)
        self.sports_stat_cricket_box.grid_propagate(False)
        self.sports_stat_cricket_box.pack(pady=3)

        # First column of the box

        self.sports_stat_cricket_names = \
            Frame(self.sports_stat_cricket_box, bg='White', width=100,
                  height=100)
        self.sports_stat_cricket_names.pack_propagate(False)
        self.sports_stat_cricket_names.grid(row=0, column=0)

        self.sports_stat_cricket_name1 = \
            Frame(self.sports_stat_cricket_names, bg='White',
                  width=100, height=19)
        self.sports_stat_cricket_name1.pack_propagate(False)
        self.sports_stat_cricket_name1.pack()

        self.sports_stat_cricket_namelabel = Label(
            self.sports_stat_cricket_name1,
            text='Cricket',
            bg='White',
            font=('Helvetica', 12),
            width=10,
            height=2,
            )
        self.sports_stat_cricket_namelabel.pack()

        self.sports_stat_cricket_name2 = \
            Frame(self.sports_stat_cricket_names, bg='White',
                  width=100, height=27)
        self.sports_stat_cricket_name2.pack_propagate(False)
        self.sports_stat_cricket_name2.pack()

        self.sports_stat_cricket_namelabel2 = Label(
            self.sports_stat_cricket_name2,
            text='First XI',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_cricket_namelabel2.pack()

        self.sports_stat_cricket_name3 = \
            Frame(self.sports_stat_cricket_names, bg='White',
                  width=100, height=27)
        self.sports_stat_cricket_name3.pack_propagate(False)
        self.sports_stat_cricket_name3.pack()

        self.sports_stat_cricket_namelabel3 = Label(
            self.sports_stat_cricket_name3,
            text='Second XI',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_cricket_namelabel3.pack()

        self.sports_stat_cricket_name4 = \
            Frame(self.sports_stat_cricket_names, bg='White',
                  width=100, height=27)
        self.sports_stat_cricket_name4.pack_propagate(False)
        self.sports_stat_cricket_name4.pack()

        self.sports_stat_cricket_namelabel4 = Label(
            self.sports_stat_cricket_name4,
            text='Junior',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_cricket_namelabel4.pack()

        # Second column of the box

        self.sports_stat_cricket_wins = \
            Frame(self.sports_stat_cricket_box, bg='White', width=90,
                  height=100)
        self.sports_stat_cricket_wins.pack_propagate(False)
        self.sports_stat_cricket_wins.grid(row=0, column=1)

        self.sports_stat_cricket_win1 = \
            Frame(self.sports_stat_cricket_wins, bg='White', width=100,
                  height=19)
        self.sports_stat_cricket_win1.pack_propagate(False)
        self.sports_stat_cricket_win1.pack()

        self.sports_stat_cricket_winlabel = Label(
            self.sports_stat_cricket_win1,
            text='Wins',
            bg='White',
            font=('Helvetica', 12),
            width=10,
            height=2,
            )
        self.sports_stat_cricket_winlabel.pack()

        self.sports_stat_cricket_win2 = \
            Frame(self.sports_stat_cricket_wins, bg='White', width=100,
                  height=27)
        self.sports_stat_cricket_win2.pack_propagate(False)
        self.sports_stat_cricket_win2.pack()

        self.sports_stat_cricket_winlabel2 = Label(
            self.sports_stat_cricket_win2,
            text='12',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_cricket_winlabel2.pack()

        self.sports_stat_cricket_win3 = \
            Frame(self.sports_stat_cricket_wins, bg='White', width=100,
                  height=27)
        self.sports_stat_cricket_win3.pack_propagate(False)
        self.sports_stat_cricket_win3.pack()

        self.sports_stat_cricket_winlabel3 = Label(
            self.sports_stat_cricket_win3,
            text='6',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_cricket_winlabel3.pack()

        self.sports_stat_cricket_win4 = \
            Frame(self.sports_stat_cricket_wins, bg='White', width=100,
                  height=27)
        self.sports_stat_cricket_win4.pack_propagate(False)
        self.sports_stat_cricket_win4.pack()

        self.sports_stat_cricket_winlabel4 = Label(
            self.sports_stat_cricket_win4,
            text='3',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_cricket_winlabel4.pack()

        # Third column of the box

        self.sports_stat_cricket_losses = \
            Frame(self.sports_stat_cricket_box, bg='White', width=90,
                  height=100)
        self.sports_stat_cricket_losses.pack_propagate(False)
        self.sports_stat_cricket_losses.grid(row=0, column=2)

        self.sports_stat_cricket_loss1 = \
            Frame(self.sports_stat_cricket_losses, bg='White',
                  width=100, height=19)
        self.sports_stat_cricket_loss1.pack_propagate(False)
        self.sports_stat_cricket_loss1.pack()

        self.sports_stat_cricket_losslabel = Label(
            self.sports_stat_cricket_loss1,
            text='Losses',
            bg='White',
            font=('Helvetica', 12),
            width=10,
            height=2,
            )
        self.sports_stat_cricket_losslabel.pack()

        self.sports_stat_cricket_loss2 = \
            Frame(self.sports_stat_cricket_losses, bg='White',
                  width=100, height=27)
        self.sports_stat_cricket_loss2.pack_propagate(False)
        self.sports_stat_cricket_loss2.pack()

        self.sports_stat_cricket_losslabel2 = Label(
            self.sports_stat_cricket_loss2,
            text='2',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_cricket_losslabel2.pack()

        self.sports_stat_cricket_loss3 = \
            Frame(self.sports_stat_cricket_losses, bg='White',
                  width=100, height=27)
        self.sports_stat_cricket_loss3.pack_propagate(False)
        self.sports_stat_cricket_loss3.pack()

        self.sports_stat_cricket_losslabel3 = Label(
            self.sports_stat_cricket_loss3,
            text='7',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_cricket_losslabel3.pack()

        self.sports_stat_cricket_loss4 = \
            Frame(self.sports_stat_cricket_losses, bg='White',
                  width=100, height=27)
        self.sports_stat_cricket_loss4.pack_propagate(False)
        self.sports_stat_cricket_loss4.pack()

        self.sports_stat_cricket_losslabel4 = Label(
            self.sports_stat_cricket_loss4,
            text='13',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_cricket_losslabel4.pack()

        # Fourth column of the box

        self.sports_stat_cricket_winlosses = \
            Frame(self.sports_stat_cricket_box, bg='White', width=90,
                  height=100)
        self.sports_stat_cricket_winlosses.pack_propagate(False)
        self.sports_stat_cricket_winlosses.grid(row=0, column=3)

        self.sports_stat_cricket_winloss1 = \
            Frame(self.sports_stat_cricket_winlosses, bg='White',
                  width=100, height=19)
        self.sports_stat_cricket_winloss1.pack_propagate(False)
        self.sports_stat_cricket_winloss1.pack()

        self.sports_stat_cricket_winlosslabel = Label(
            self.sports_stat_cricket_winloss1,
            text='W/L',
            bg='White',
            font=('Helvetica', 12),
            width=10,
            height=2,
            )
        self.sports_stat_cricket_winlosslabel.pack()

        self.sports_stat_cricket_winloss2 = \
            Frame(self.sports_stat_cricket_winlosses, bg='White',
                  width=100, height=27)
        self.sports_stat_cricket_winloss2.pack_propagate(False)
        self.sports_stat_cricket_winloss2.pack()

        self.sports_stat_cricket_winlosslabel2 = Label(
            self.sports_stat_cricket_winloss2,
            text='0.4',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_cricket_winlosslabel2.pack()

        self.sports_stat_cricket_winloss3 = \
            Frame(self.sports_stat_cricket_winlosses, bg='White',
                  width=100, height=27)
        self.sports_stat_cricket_winloss3.pack_propagate(False)
        self.sports_stat_cricket_winloss3.pack()

        self.sports_stat_cricket_winlosslabel3 = Label(
            self.sports_stat_cricket_winloss3,
            text='1.2',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_cricket_winlosslabel3.pack()

        self.sports_stat_cricket_winloss4 = \
            Frame(self.sports_stat_cricket_winlosses, bg='White',
                  width=100, height=27)
        self.sports_stat_cricket_winloss4.pack_propagate(False)
        self.sports_stat_cricket_winloss4.pack()

        self.sports_stat_cricket_winlosslabel4 = Label(
            self.sports_stat_cricket_winloss4,
            text='1.3',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_cricket_winlosslabel4.pack()

        # Rugby analytics box

        self.sports_stat_rugby_box = Frame(
            self.stat_page,
            bg='White',
            width=w_width - margin_length,
            height=100,
            relief=RIDGE,
            bd=3,
            )
        self.sports_stat_rugby_box.pack_propagate(False)
        self.sports_stat_rugby_box.grid_propagate(False)
        self.sports_stat_rugby_box.pack(pady=3)

        # First column of the box

        self.sports_stat_rugby_names = \
            Frame(self.sports_stat_rugby_box, bg='White', width=100,
                  height=100)
        self.sports_stat_rugby_names.pack_propagate(False)
        self.sports_stat_rugby_names.grid(row=0, column=0)

        self.sports_stat_rugby_name1 = \
            Frame(self.sports_stat_rugby_names, bg='White', width=100,
                  height=19)
        self.sports_stat_rugby_name1.pack_propagate(False)
        self.sports_stat_rugby_name1.pack()

        self.sports_stat_rugby_namelabel = Label(
            self.sports_stat_rugby_name1,
            text='Rugby',
            bg='White',
            font=('Helvetica', 12),
            width=10,
            height=2,
            )
        self.sports_stat_rugby_namelabel.pack()

        self.sports_stat_rugby_name2 = \
            Frame(self.sports_stat_rugby_names, bg='White', width=100,
                  height=27)
        self.sports_stat_rugby_name2.pack_propagate(False)
        self.sports_stat_rugby_name2.pack()

        self.sports_stat_rugby_namelabel2 = Label(
            self.sports_stat_rugby_name2,
            text='First XI',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_rugby_namelabel2.pack()

        self.sports_stat_rugby_name3 = \
            Frame(self.sports_stat_rugby_names, bg='White', width=100,
                  height=27)
        self.sports_stat_rugby_name3.pack_propagate(False)
        self.sports_stat_rugby_name3.pack()

        self.sports_stat_rugby_namelabel3 = Label(
            self.sports_stat_rugby_name3,
            text='Second XI',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_rugby_namelabel3.pack()

        self.sports_stat_rugby_name4 = \
            Frame(self.sports_stat_rugby_names, bg='White', width=100,
                  height=27)
        self.sports_stat_rugby_name4.pack_propagate(False)
        self.sports_stat_rugby_name4.pack()

        self.sports_stat_rugby_namelabel4 = Label(
            self.sports_stat_rugby_name4,
            text='Junior',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_rugby_namelabel4.pack()

        # Second column of the box

        self.sports_stat_rugby_wins = Frame(self.sports_stat_rugby_box,
                bg='White', width=90, height=100)
        self.sports_stat_rugby_wins.pack_propagate(False)
        self.sports_stat_rugby_wins.grid(row=0, column=1)

        self.sports_stat_rugby_win1 = \
            Frame(self.sports_stat_rugby_wins, bg='White', width=100,
                  height=19)
        self.sports_stat_rugby_win1.pack_propagate(False)
        self.sports_stat_rugby_win1.pack()

        self.sports_stat_rugby_winlabel = Label(
            self.sports_stat_rugby_win1,
            text='Wins',
            bg='White',
            font=('Helvetica', 12),
            width=10,
            height=2,
            )
        self.sports_stat_rugby_winlabel.pack()

        self.sports_stat_rugby_win2 = \
            Frame(self.sports_stat_rugby_wins, bg='White', width=100,
                  height=27)
        self.sports_stat_rugby_win2.pack_propagate(False)
        self.sports_stat_rugby_win2.pack()

        self.sports_stat_rugby_winlabel2 = Label(
            self.sports_stat_rugby_win2,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_rugby_winlabel2.pack()

        self.sports_stat_rugby_win3 = \
            Frame(self.sports_stat_rugby_wins, bg='White', width=100,
                  height=27)
        self.sports_stat_rugby_win3.pack_propagate(False)
        self.sports_stat_rugby_win3.pack()

        self.sports_stat_rugby_winlabel3 = Label(
            self.sports_stat_rugby_win3,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_rugby_winlabel3.pack()

        self.sports_stat_rugby_win4 = \
            Frame(self.sports_stat_rugby_wins, bg='White', width=100,
                  height=27)
        self.sports_stat_rugby_win4.pack_propagate(False)
        self.sports_stat_rugby_win4.pack()

        self.sports_stat_rugby_winlabel4 = Label(
            self.sports_stat_rugby_win4,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_rugby_winlabel4.pack()

        # Third column of the box

        self.sports_stat_rugby_losses = \
            Frame(self.sports_stat_rugby_box, bg='White', width=90,
                  height=100)
        self.sports_stat_rugby_losses.pack_propagate(False)
        self.sports_stat_rugby_losses.grid(row=0, column=2)

        self.sports_stat_rugby_loss1 = \
            Frame(self.sports_stat_rugby_losses, bg='White', width=100,
                  height=19)
        self.sports_stat_rugby_loss1.pack_propagate(False)
        self.sports_stat_rugby_loss1.pack()

        self.sports_stat_rugby_losslabel = Label(
            self.sports_stat_rugby_loss1,
            text='Losses',
            bg='White',
            font=('Helvetica', 12),
            width=10,
            height=2,
            )
        self.sports_stat_rugby_losslabel.pack()

        self.sports_stat_rugby_loss2 = \
            Frame(self.sports_stat_rugby_losses, bg='White', width=100,
                  height=27)
        self.sports_stat_rugby_loss2.pack_propagate(False)
        self.sports_stat_rugby_loss2.pack()

        self.sports_stat_rugby_losslabel2 = Label(
            self.sports_stat_rugby_loss2,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_rugby_losslabel2.pack()

        self.sports_stat_rugby_loss3 = \
            Frame(self.sports_stat_rugby_losses, bg='White', width=100,
                  height=27)
        self.sports_stat_rugby_loss3.pack_propagate(False)
        self.sports_stat_rugby_loss3.pack()

        self.sports_stat_rugby_losslabel3 = Label(
            self.sports_stat_rugby_loss3,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_rugby_losslabel3.pack()

        self.sports_stat_rugby_loss4 = \
            Frame(self.sports_stat_rugby_losses, bg='White', width=100,
                  height=27)
        self.sports_stat_rugby_loss4.pack_propagate(False)
        self.sports_stat_rugby_loss4.pack()

        self.sports_stat_rugby_losslabel4 = Label(
            self.sports_stat_rugby_loss4,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_rugby_losslabel4.pack()

        # Fourth column of the box

        self.sports_stat_rugby_winlosses = \
            Frame(self.sports_stat_rugby_box, bg='White', width=90,
                  height=100)
        self.sports_stat_rugby_winlosses.pack_propagate(False)
        self.sports_stat_rugby_winlosses.grid(row=0, column=3)

        self.sports_stat_rugby_winloss1 = \
            Frame(self.sports_stat_rugby_winlosses, bg='White',
                  width=100, height=19)
        self.sports_stat_rugby_winloss1.pack_propagate(False)
        self.sports_stat_rugby_winloss1.pack()

        self.sports_stat_rugby_winlosslabel = Label(
            self.sports_stat_rugby_winloss1,
            text='W/L',
            bg='White',
            font=('Helvetica', 12),
            width=10,
            height=2,
            )
        self.sports_stat_rugby_winlosslabel.pack()

        self.sports_stat_rugby_winloss2 = \
            Frame(self.sports_stat_rugby_winlosses, bg='White',
                  width=100, height=27)
        self.sports_stat_rugby_winloss2.pack_propagate(False)
        self.sports_stat_rugby_winloss2.pack()

        self.sports_stat_rugby_winlosslabel2 = Label(
            self.sports_stat_rugby_winloss2,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_rugby_winlosslabel2.pack()

        self.sports_stat_rugby_winloss3 = \
            Frame(self.sports_stat_rugby_winlosses, bg='White',
                  width=100, height=27)
        self.sports_stat_rugby_winloss3.pack_propagate(False)
        self.sports_stat_rugby_winloss3.pack()

        self.sports_stat_rugby_winlosslabel3 = Label(
            self.sports_stat_rugby_winloss3,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_rugby_winlosslabel3.pack()

        self.sports_stat_rugby_winloss4 = \
            Frame(self.sports_stat_rugby_winlosses, bg='White',
                  width=100, height=27)
        self.sports_stat_rugby_winloss4.pack_propagate(False)
        self.sports_stat_rugby_winloss4.pack()

        self.sports_stat_rugby_winlosslabel4 = Label(
            self.sports_stat_rugby_winloss4,
            text='0',
            bg='White',
            font=('Helvetica', 11),
            width=10,
            height=2,
            )
        self.sports_stat_rugby_winlosslabel4.pack()

        # Navigation bar frame ---------------------------

        self.navigation_bar = Frame(self.window, bg='#FC6736',
                                    width=w_width, height=150)
        self.navigation_bar.pack_propagate(False)

        # Placing buttons on nav bar

        self.nav_space_one = Frame(self.navigation_bar, bg='#FC6736',
                                   width=133, height=150)
        self.nav_space_one.pack_propagate(False)
        self.nav_space_one.pack(side=LEFT)

        self.nav_space_two = Frame(self.navigation_bar, bg='#FC6736',
                                   width=134, height=150)
        self.nav_space_two.pack_propagate(False)
        self.nav_space_two.pack(side=LEFT)

        self.nav_space_three = Frame(self.navigation_bar, bg='#FC6736',
                width=133, height=150)
        self.nav_space_three.pack_propagate(False)
        self.nav_space_three.pack(side=LEFT)

        self.home_button = Button(
            self.nav_space_one,
            text='Home',
            bg='White',
            width=6,
            height=3,
            command=self.go_to_home,
            )
        self.home_button.pack(pady=40)

        self.info_button = Button(
            self.nav_space_two,
            text='Info',
            bg='White',
            width=6,
            height=3,
            command=self.go_to_info,
            )
        self.info_button.pack(pady=40)

        self.stat_button = Button(
            self.nav_space_three,
            text='Stat',
            bg='White',
            width=6,
            height=3,
            command=self.go_to_stat,
            )
        self.stat_button.pack(pady=40)

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
        entered_code = self.teacher_input.get()  # Retrieve the entered code from the entry box
        if entered_code == self.teacher_code:  # Compare the user inputted code to the required / set code 'KMR'
            self.create_upcoming_button.pack(pady=50)
            self.create_result_button.pack()
            self.tlogin_logo.pack(pady=70)
        elif entered_code == '':

                                 # If the box is left empty, the user is shown an error, and told to enter a code, the buttons will also be removed if this is done after the correct teacher code is entered as a precaution

            messagebox.showerror('Box left empty ',
                                 'No code entered, please enter your teacher code.'
                                 )
            self.create_upcoming_button.pack_forget()
            self.create_result_button.pack_forget()
            self.tlogin_logo.pack_forget()
        else:

              # If they enter the wrong code or something random, the user is shown an error, and told to enter a code, the buttons will also be removed if this is done after the correct teacher code is entered as a precaution

            messagebox.showerror('Invalid Code',
                                 'Invalid teacher code. Please try again.'
                                 )
            self.create_upcoming_button.pack_forget()
            self.create_result_button.pack_forget()
            self.tlogin_logo.pack_forget()

    def back_to_login(self):

        self.teacher_login_page.pack_forget()
        self.logo_frame.grid_remove()
        self.content_frame.grid_remove()
        self.navigation_bar.grid_remove()
        self.login_page.pack()

        self.tcode_input_entry.delete(0, 'end')
        self.create_upcoming_button.pack_forget()
        self.create_result_button.pack_forget()
        self.tlogin_logo.pack_forget()

    def show_upcoming_creator(self):
        self.teacher_login_page.pack_forget()
        self.upcoming_sched_page.pack()

    def show_result_creator(self):
        self.teacher_login_page.pack_forget()
        self.result_enter_page.pack()

    def cancel_sched(self):
        self.upcoming_sched_page.pack_forget()
        self.result_enter_page.pack_forget()
        self.teacher_login_page.pack()

        self.upcoming_sport_entry.delete(0, 'end')
        self.upcoming_team_entry.delete(0, 'end')
        self.upcoming_weekday_entry.delete(0, 'end')
        self.upcoming_time_hours.delete(0, 'end')
        self.upcoming_time_minutes.delete(0, 'end')

    def change_upcoming_labels(self):
        upcoming_sport_name = self.upcoming_sport_entry.get()
        team_name = self.upcoming_team_entry.get()
        week_day = self.upcoming_weekday_entry.get()
        time_hours = self.upcoming_time_hours.get()
        time_minutes = self.upcoming_time_minutes.get()

        # Takes the teacher user input from the entry boxes in the upcoming match scheduler and assigns them to a variable which is then compared to the list of values used for the dropdown box
        # Simply if one of the options are not entered into the box, then an error pops up on screen alerting the user of the issue

        if upcoming_sport_name in self.sports:
            if team_name in self.teams:
                if week_day in self.weekdays:
                    if time_hours in self.hours:
                        if time_minutes in self.minutes:
                            if upcoming_sport_name == 'Football':
                                self.change_football_upcoming_labels(team_name,
                                        week_day, time_hours,
                                        time_minutes)
                            elif upcoming_sport_name == 'Basketball':
                                self.change_basketball_upcoming_labels(team_name,
                                        week_day, time_hours,
                                        time_minutes)
                            elif upcoming_sport_name == 'Hockey':
                                self.change_hockey_upcoming_labels(team_name,
                                        week_day, time_hours,
                                        time_minutes)
                            elif upcoming_sport_name == 'Rugby':
                                self.change_rugby_upcoming_labels(team_name,
                                        week_day, time_hours,
                                        time_minutes)
                        else:
                            messagebox.showerror('Invalid time entered'
                                    ,
                                    'Please enter a valid time from the dropdown box (minutes error)'
                                    )
                    else:
                        messagebox.showerror('Invalid time entered',
                                'Please enter a valid time from the dropdown box (hours error)'
                                )
                else:
                    messagebox.showerror('Invalid week day',
                            'Please choose a day from the dropdown box')
            else:
                messagebox.showerror('Invalid team name',
                        'Please choose a team from the dropdown box')
        else:
            messagebox.showerror('Invalid sport name',
                                 'Please choose a sport from the dropdown box'
                                 )

    # If all required conditions are met for the user input, the label-changing functions are called which edit specific label widgets that were made to display the data put into a certain entrybox
    # e.g. upcoming_team_one was a label made to display the name of the team for the upcoming box on the home page so the function configures this label to display the string text of the assigned variable (of the corresponding entrybox)

    def change_football_upcoming_labels(
        self,
        team_name,
        week_day,
        time_hours,
        time_minutes,
        ):
        self.upcoming_team_one.config(text=team_name)
        self.upcoming_day_one.config(text=week_day)
        self.upcoming_time_one.config(text=time_hours + ':'
                + time_minutes)

        messagebox.showinfo('Match schedule updated',
                            'Football match scheduled!')

    def change_basketball_upcoming_labels(
        self,
        team_name,
        week_day,
        time_hours,
        time_minutes,
        ):
        self.upcoming_team_two.config(text=team_name)
        self.upcoming_day_two.config(text=week_day)
        self.upcoming_time_two.config(text=time_hours + ':'
                + time_minutes)

        messagebox.showinfo('Match schedule updated',
                            'Basketball match scheduled!')

    def change_hockey_upcoming_labels(
        self,
        team_name,
        week_day,
        time_hours,
        time_minutes,
        ):
        self.upcoming_team_three.config(text=team_name)
        self.upcoming_day_three.config(text=week_day)
        self.upcoming_time_three.config(text=time_hours + ':'
                + time_minutes)

        messagebox.showinfo('Match schedule updated',
                            'Hockey match scheduled!')

    def change_rugby_upcoming_labels(
        self,
        team_name,
        week_day,
        time_hours,
        time_minutes,
        ):
        self.upcoming_team_four.config(text=team_name)
        self.upcoming_day_four.config(text=week_day)
        self.upcoming_time_four.config(text=time_hours + ':'
                + time_minutes)

        messagebox.showinfo('Match schedule updated',
                            'Rugby match scheduled!')

    def change_result_labels(self):
        result_sport_name = self.result_sport_entry.get()

        other_first_team = self.opposing_firstxi_team.get()
        other_second_team = self.opposing_secondxi_team.get()
        other_third_team = self.opposing_junior_team.get()

        our_first_score = self.our_firstxi_score.get()
        our_second_score = self.our_secondxi_score.get()
        our_third_score = self.our_junior_score.get()

        their_first_score = self.their_firstxi_score.get()
        their_second_score = self.their_secondxi_score.get()
        their_third_score = self.their_junior_score.get()

        first_wins = self.firstxi_wins.get()
        second_wins = self.secondxi_wins.get()
        third_wins = self.junior_wins.get()

        first_losses = self.firstxi_losses.get()
        second_losses = self.secondxi_losses.get()
        third_losses = self.junior_losses.get()

        if not result_sport_name:
            messagebox.showerror('Invalid sport name', 'Please choose a sport from the dropdown box')
            return

        if not (other_first_team or other_second_team or other_third_team):
            messagebox.showerror('Invalid team entry', 'Please enter the opposing team(s)')
            return

        try:
            our_first_score = int(our_first_score)
            our_second_score = int(our_second_score)
            our_third_score = int(our_third_score)
            their_first_score = int(their_first_score)
            their_second_score = int(their_second_score)
            their_third_score = int(their_third_score)
            first_wins = int(first_wins)
            second_wins = int(second_wins)
            third_wins = int(third_wins)
            first_losses = int(first_losses)
            second_losses = int(second_losses)
            third_losses = int(third_losses)
        except ValueError:
            messagebox.showerror('Invalid score/record entry', 'Please ensure the scores/records entered are correct numbers')
            return

        if first_losses == 0:
            first_winlosses = '+'
        else:
            first_winlosses = first_wins // first_losses

        if second_losses == 0:
            second_winlosses = '+'
        else:
            second_winlosses = second_wins // second_losses

        if third_losses == 0:
            third_winlosses = '+'
        else:
            third_winlosses = third_wins // third_losses

        if result_sport_name == 'Football':
            self.change_football_result_labels(
                other_first_team,
                other_second_team,
                other_third_team,
                our_first_score,
                our_second_score,
                our_third_score,
                their_first_score,
                their_second_score,
                their_third_score,
                first_wins,
                second_wins,
                third_wins,
                first_losses,
                second_losses,
                third_losses,
                first_winlosses,
                second_winlosses,
                third_winlosses
            )
        elif result_sport_name == 'Basketball':
            self.change_basketball_result_labels(
                other_first_team,
                other_second_team,
                other_third_team,
                our_first_score,
                our_second_score,
                our_third_score,
                their_first_score,
                their_second_score,
                their_third_score,
                first_wins,
                second_wins,
                third_wins,
                first_losses,
                second_losses,
                third_losses,
                first_winlosses,
                second_winlosses,
                third_winlosses
            )
        elif result_sport_name == 'Hockey':
            self.change_hockey_result_labels(
                other_first_team,
                other_second_team,
                other_third_team,
                our_first_score,
                our_second_score,
                our_third_score,
                their_first_score,
                their_second_score,
                their_third_score,
                first_wins,
                second_wins,
                third_wins,
                first_losses,
                second_losses,
                third_losses,
                first_winlosses,
                second_winlosses,
                third_winlosses
            )
        elif result_sport_name == 'Rugby':
            self.change_rugby_result_labels(
                other_first_team,
                other_second_team,
                other_third_team,
                our_first_score,
                our_second_score,
                our_third_score,
                their_first_score,
                their_second_score,
                their_third_score,
                first_wins,
                second_wins,
                third_wins,
                first_losses,
                second_losses,
                third_losses,
                first_winlosses,
                second_winlosses,
                third_winlosses
            )

    def change_football_result_labels(
        self,
        other_first_team,
        other_second_team,
        other_third_team,
        our_first_score,
        our_second_score,
        our_third_score,
        their_first_score,
        their_second_score,
        their_third_score,
        first_wins,
        second_wins,
        third_wins,
        first_losses,
        second_losses,
        third_losses,
        first_winlosses,
        second_winlosses,
        third_winlosses
        ):
        self.homeresu_pageOne_L1Score1.config(text=our_first_score)
        self.homeresu_pageOne_L1Score2.config(text=their_first_score)
        self.homeresu_pageOne_L1Team2.config(text=other_first_team)

        self.homeresu_pageOne_L2Score1.config(text=our_second_score)
        self.homeresu_pageOne_L2Score2.config(text=their_second_score)
        self.homeresu_pageOne_L2Team2.config(text=other_second_team)

        self.homeresu_pageOne_L3Score1.config(text=our_third_score)
        self.homeresu_pageOne_L3Score2.config(text=their_third_score)
        self.homeresu_pageOne_L3Team2.config(text=other_third_team)

        self.sports_stat_football_winlabel2.config(text=str(first_wins))
        self.sports_stat_football_losslabel2.config(text=str(first_losses))
        self.sports_stat_football_winlosslabel2.config(text=str(first_winlosses))

        self.sports_stat_football_winlabel3.config(text=str(second_wins))
        self.sports_stat_football_losslabel3.config(text=str(second_losses))
        self.sports_stat_football_winlosslabel3.config(text=str(second_winlosses))

        self.sports_stat_football_winlabel4.config(text=str(third_wins))
        self.sports_stat_football_losslabel4.config(text=str(third_losses))
        self.sports_stat_football_winlosslabel4.config(text=str(third_winlosses))

        messagebox.showinfo('Match results updated',
                            'Football results updated!')

    def change_basketball_result_labels(
        self,
        other_first_team,
        other_second_team,
        other_third_team,
        our_first_score,
        our_second_score,
        our_third_score,
        their_first_score,
        their_second_score,
        their_third_score,
        first_wins,
        second_wins,
        third_wins,
        first_losses,
        second_losses,
        third_losses,
        first_winlosses,
        second_winlosses,
        third_winlosses
        ):
        self.homeresu_pageTwo_L1Score1.config(text=our_first_score)
        self.homeresu_pageTwo_L1Score2.config(text=their_first_score)
        self.homeresu_pageTwo_L1Team2.config(text=other_first_team)

        self.homeresu_pageTwo_L2Score1.config(text=our_second_score)
        self.homeresu_pageTwo_L2Score2.config(text=their_second_score)
        self.homeresu_pageTwo_L2Team2.config(text=other_second_team)

        self.homeresu_pageTwo_L3Score1.config(text=our_third_score)
        self.homeresu_pageTwo_L3Score2.config(text=their_third_score)
        self.homeresu_pageTwo_L3Team2.config(text=other_third_team)

        self.sports_stat_basketball_winlabel2.config(text=str(first_wins))
        self.sports_stat_basketball_losslabel2.config(text=str(first_losses))
        self.sports_stat_basketball_winlosslabel2.config(text=str(first_winlosses))

        self.sports_stat_basketball_winlabel3.config(text=str(second_wins))
        self.sports_stat_basketball_losslabel3.config(text=str(second_losses))
        self.sports_stat_basketball_winlosslabel3.config(text=str(second_winlosses))

        self.sports_stat_basketball_winlabel4.config(text=str(third_wins))
        self.sports_stat_basketball_losslabel4.config(text=str(third_losses))
        self.sports_stat_basketball_winlosslabel4.config(text=str(third_winlosses))

        messagebox.showinfo('Match results updated',
                            'Basketball results updated!')

    def change_hockey_result_labels(
        self,
        other_first_team,
        other_second_team,
        other_third_team,
        our_first_score,
        our_second_score,
        our_third_score,
        their_first_score,
        their_second_score,
        their_third_score,
        first_wins,
        second_wins,
        third_wins,
        first_losses,
        second_losses,
        third_losses,
        first_winlosses,
        second_winlosses,
        third_winlosses
        ):
        self.homeresu_pageThree_L1Score1.config(text=our_first_score)
        self.homeresu_pageThree_L1Score2.config(text=their_first_score)
        self.homeresu_pageThree_L1Team2.config(text=other_first_team)

        self.homeresu_pageThree_L2Score1.config(text=our_second_score)
        self.homeresu_pageThree_L2Score2.config(text=their_second_score)
        self.homeresu_pageThree_L2Team2.config(text=other_second_team)

        self.homeresu_pageThree_L3Score1.config(text=our_third_score)
        self.homeresu_pageThree_L3Score2.config(text=their_third_score)
        self.homeresu_pageThree_L3Team2.config(text=other_third_team)

        self.sports_stat_hockey_winlabel2.config(text=str(first_wins))
        self.sports_stat_hockey_losslabel2.config(text=str(first_losses))
        self.sports_stat_hockey_winlosslabel2.config(text=str(first_winlosses))

        self.sports_stat_hockey_winlabel3.config(text=str(second_wins))
        self.sports_stat_hockey_losslabel3.config(text=str(second_losses))
        self.sports_stat_hockey_winlosslabel3.config(text=str(second_winlosses))

        self.sports_stat_hockey_winlabel4.config(text=str(third_wins))
        self.sports_stat_hockey_losslabel4.config(text=str(third_losses))
        self.sports_stat_hockey_winlosslabel4.config(text=str(third_winlosses))

        messagebox.showinfo('Match results updated',
                            'Hockey results updated!')

    def change_rugby_result_labels(
        self,
        other_first_team,
        other_second_team,
        other_third_team,
        our_first_score,
        our_second_score,
        our_third_score,
        their_first_score,
        their_second_score,
        their_third_score,
        first_wins,
        second_wins,
        third_wins,
        first_losses,
        second_losses,
        third_losses,
        first_winlosses,
        second_winlosses,
        third_winlosses
        ):
        self.homeresu_pageFour_L1Score1.config(text=our_first_score)
        self.homeresu_pageFour_L1Score2.config(text=their_first_score)
        self.homeresu_pageFour_L1Team2.config(text=other_first_team)

        self.homeresu_pageFour_L2Score1.config(text=our_second_score)
        self.homeresu_pageFour_L2Score2.config(text=their_second_score)
        self.homeresu_pageFour_L2Team2.config(text=other_second_team)

        self.homeresu_pageFour_L3Score1.config(text=our_third_score)
        self.homeresu_pageFour_L3Score2.config(text=their_third_score)
        self.homeresu_pageFour_L3Team2.config(text=other_third_team)

        self.sports_stat_rugby_winlabel2.config(text=str(first_wins))
        self.sports_stat_rugby_losslabel2.config(text=str(first_losses))
        self.sports_stat_rugby_winlosslabel2.config(text=str(first_winlosses))

        self.sports_stat_rugby_winlabel3.config(text=str(second_wins))
        self.sports_stat_rugby_losslabel3.config(text=str(second_losses))
        self.sports_stat_rugby_winlosslabel3.config(text=str(second_winlosses))

        self.sports_stat_rugby_winlabel4.config(text=str(third_wins))
        self.sports_stat_rugby_losslabel4.config(text=str(third_losses))
        self.sports_stat_rugby_winlosslabel4.config(text=str(third_winlosses))

        messagebox.showinfo('Match results updated',
                            'Rugby results updated!')

    def go_to_next_page(self, direction):
        if direction == 'left':
            if self.page_number > 1:
                self.page_number -= 1
            elif self.page_number <= 1:
                self.page_number = self.max_page_numbers
        elif direction == 'right':
            if self.page_number < self.max_page_numbers:
                self.page_number += 1
            elif self.page_number >= self.max_page_numbers:
                self.page_number = 1

        self.page_indicator.config(text=self.page_number)

        self.change_resu_page()

    def expand_football_info(self):
        self.info_page_hub.pack_forget()
        self.football_info_page.pack()

    def expand_basketball_info(self):
        self.info_page_hub.pack_forget()
        self.basketball_info_page.pack()

    def expand_hockey_info(self):
        self.info_page_hub.pack_forget()
        self.hockey_info_page.pack()

    def expand_cricket_info(self):
        self.info_page_hub.pack_forget()
        self.cricket_info_page.pack()

    def expand_rugby_info(self):
        self.info_page_hub.pack_forget()
        self.rugby_info_page.pack()

    def return_to_info(self):
        self.football_info_page.pack_forget()
        self.basketball_info_page.pack_forget()
        self.hockey_info_page.pack_forget()
        self.cricket_info_page.pack_forget()
        self.rugby_info_page.pack_forget()
        self.info_page_hub.pack()

    def go_to_home(self):
        self.info_page.grid_remove()
        self.stat_page.grid_remove()
        self.home_page.grid(rowspan=TRUE, columnspan=TRUE)

    def go_to_info(self):
        self.stat_page.grid_remove()
        self.home_page.grid_remove()
        self.info_page.grid(rowspan=TRUE, columnspan=TRUE)

    def go_to_stat(self):
        self.info_page.grid_remove()
        self.home_page.grid_remove()
        self.stat_page.grid(rowspan=TRUE, columnspan=TRUE)

    def change_resu_page(self):

        # Update visibility of each page

        self.homeresu_pageOne.grid_remove()
        self.homeresu_pageTwo.grid_remove()
        self.homeresu_pageThree.grid_remove()
        self.homeresu_pageFour.grid_remove()

        if self.page_number == 1:
            self.homeresu_pageOne.grid(row=1, columnspan=TRUE)
            self.homeresu_sportname.config(text='Football')
        elif self.page_number == 2:
            self.homeresu_pageTwo.grid(row=1, columnspan=TRUE)
            self.homeresu_sportname.config(text='Basketball')
        elif self.page_number == 3:
            self.homeresu_pageThree.grid(row=1, columnspan=TRUE)
            self.homeresu_sportname.config(text='Hockey')
        elif self.page_number == 4:
            self.homeresu_pageFour.grid(row=1, columnspan=TRUE)
            self.homeresu_sportname.config(text='Rugby')
