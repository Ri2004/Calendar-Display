from tkinter import *
import calendar

root = Tk()

root.geometry("300x260+500+220")
root.config(background= "light blue")
root.resizable(width= False, height= False)

def show():
    if userInput.get() == "":
        noYear = Label(root, text= "No Year Given", font= "Calibri 16 bold italic", bg= "light blue", fg= "red")
        noYear.pack()
    
    else:
        if userInput.get().isdigit():
            window = Tk()
            window.title(f"Calendar of {userInput.get()}")
            window.geometry("600x690+480+5") 
            window.resizable(width= False, height= False)
            
            year = Label(window, text= "CALENDAR", font= "Calibri 25 bold", fg= "navy blue")
            year.pack()
            
            displayCalendar = calendar.calendar(int(userInput.get()))
            
            outputCalendar = Text(window, width= 470, height= 450, font= "Consolas 11 bold", relief= RIDGE, bd= 2)
            outputCalendar.pack()
            
            outputCalendar.insert(END, displayCalendar)
        
        else:
            notYear = Label(root, text= "Please Insert a valid year", font= "Calibri 15 bold italic underline", fg= "red")
            notYear.pack()

text = Label(root, text="DISPLAY CALENDAR", foreground="green", background= "light yellow", font= "Arial 18 bold", justify=CENTER, padx= 10, pady= 10)
text.pack(pady= 30)

userInput = Entry(root, width= 20, font= "Arial 18 bold", justify= CENTER)
userInput.pack()

showCalendar = Button(root, text= "Show Calendar", width= 15, fg= "white", bg= "blue", font= "Arial 12 bold", command= show)

showCalendar.pack(pady= 14)

root.mainloop()