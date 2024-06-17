from tkinter import *

app_width = 400
app_height = 850
margin_length = 50

class LayoutApp():
    
    def __init__(self):
        
        root = Tk()
        root.geometry(str(app_width) + "x" + str(app_height))
        
        top_frame = Frame(width=app_width - margin_length, height=70, bg='blue')
        top_frame.pack()
        main_frame = Frame(width=app_width - margin_length, height=300, bg='red')
        main_frame.pack_propagate(False)
        main_frame.pack(pady=10)
        
        results_frame = Frame()
        navigation_frame = Frame()
            
        
        # Main Frame layout
        
        event_frame = Frame(main_frame, bg='green', height=50, width=app_width - margin_length)
        event_frame.pack_propagate(False)
        event_frame.pack()
        
        sports_frame = Frame(event_frame, bg='black', height=40, width=200)
        sports_frame.pack(padx=5, side=LEFT)
        schedule_frame = Frame(event_frame, bg='grey', height=40, width=80)
        schedule_frame.pack(padx=5, side=RIGHT)
        
        
        root.mainloop()
    
    
if __name__ == "__main__":
    app = LayoutApp()