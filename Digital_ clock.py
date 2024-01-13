from tkinter import *
import datetime
def date_time():
    time = datetime.datetime.now()
    hour = time.strftime('%I')
    minutes = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')
    date = time.strftime('%D')
    month = time.strftime('%m')
    Year = time.strftime('%y')
    Day = time.strftime('%a')

    label_date.config(text=date)
    label_month.config(text= month)
    label_year.config(text=Year)
    label_day.config(text=Day)
    label_hour.config(text=hour)
    label_min.config(text= minutes)
    label_sec.config(text=sec)
    label_am.config(text=am)


    label_hour.after(200,date_time)#after() changes the graphic time every second(200 is a parameter which mean to change time after evry 200 sec... )


clock = Tk() #this function gives a graphic
clock.title("Digital clock")
clock.geometry('1000x500') #by this we can set the gui size on screen
clock.config(bg='grey') #congifg help us to change bd                                      

#time*****************************************
label_hour = Label(clock,text="00",font=("Time new",60,"bold"),bg="red",fg="white")
label_hour.place(x=120,y=50,height=110,width=100)  #place function is used to set the boxes height color
label_hour_txt = Label(clock,text="hour",font=("Time new",20,"bold"),bg="red",fg="white")
label_hour_txt.place(x=120,y=190,height=40,width=100)  


label_min = Label(clock,text="00",font=("Time new",60,"bold"),bg="red",fg="white")
label_min.place(x=340,y=50,height=110,width=100) 
label_min_txt = Label(clock,text="min.",font=("Time new",20,"bold"),bg="red",fg="white")
label_min_txt.place(x=340,y=190,height=40,width=100)  


label_sec = Label(clock,text="00",font=("Time new",60,"bold"),bg="red",fg="white")
label_sec.place(x=560,y=50,height=110,width=100) 
label_sec_txt = Label(clock,text="sec",font=("Time new",20,"bold"),bg="red",fg="white")
label_sec_txt.place(x=560,y=190,height=40,width=100)  


label_am = Label(clock,text="00",font=("Time new",40,"bold"),bg="red",fg="white")
label_am.place(x=780,y=50,height=110,width=100) 
label_am_txt = Label(clock,text="AM/PM",font=("Time new",20,"bold"),bg="red",fg="white")
label_am_txt.place(x=780,y=190,height=40,width=100)  

#date***************************************
label_date = Label(clock,text="00",font=("Time new",60,"bold"),bg="red",fg="white")
label_date.place(x=120,y=270,height=110,width=100)  #place function is used to set the boxes height color
label_date_txt = Label(clock,text="Date",font=("Time new",20,"bold"),bg="red",fg="white")
label_date_txt.place(x=120,y=410,height=40,width=100)  

label_month = Label(clock,text="00",font=("Time new",60,"bold"),bg="red",fg="white")
label_month.place(x=340,y=270,height=110,width=100) 
label_month_txt = Label(clock,text="Month",font=("Time new",20,"bold"),bg="red",fg="white")
label_month_txt.place(x=340,y=410,height=40,width=100)  


label_year = Label(clock,text="00",font=("Time new",60,"bold"),bg="red",fg="white")
label_year.place(x=560,y=270,height=110,width=100) 
label_year_txt = Label(clock,text="year",font=("Time new",20,"bold"),bg="red",fg="white")
label_year_txt.place(x=560,y=140,height=40,width=100)  




label_day = Label(clock,text="00",font=("Time new",40,"bold"),bg="red",fg="white")
label_day.place(x=780,y=270,height=110,width=100) 
label_day_txt = Label(clock,text="Day",font=("Time new",20,"bold"),bg="red",fg="white")
label_day_txt.place(x=780,y=410,height=40,width=100)




date_time() #function call
clock.mainloop()  #this function of TK() class continously slow the graphic on the screen
