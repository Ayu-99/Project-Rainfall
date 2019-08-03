from tkinter import *
from functions import DataRainfall


df = DataRainfall()

def analysisGUI():
    window = Tk()
    window.configure(background="lightskyblue1")
    window.geometry("400x400")
    window.title("Data Analysis")

    emptyLabel100 = Label(window, text="", bg="lightskyblue1")
    emptyLabel100.pack()

    emptyLabel0 = Label(window, text="Choose any option...", font=("Courier", 24), bg="lightskyblue1", fg="purple3")
    emptyLabel0.pack()

    emptyLabel200= Label(window, text="", bg="lightskyblue1")
    emptyLabel200.pack()

    option1 = Button(window, text="Rainfall of one state in specific year", activebackground="light yellow", bg="light green", fg="black",command=df.oneState)
    option1.pack()
    emptyLabel1 = Label(window, text="", bg="lightskyblue1")
    emptyLabel1.pack()

    option2 = Button(window, text="Compare rainfall of two states in specific year ", activebackground="light yellow", bg="light green", fg="black")
    option2.pack()
    emptyLabel2 = Label(window, text="", bg="lightskyblue1")
    emptyLabel2.pack()

    option3 = Button(window, text="Show Rainfall all over India in one specific year", activebackground="light yellow", bg="light green", fg="black")
    option3.pack()
    emptyLabel3 = Label(window, text="", bg="lightskyblue1")
    emptyLabel3.pack()

    option4 = Button(window, text="Compare rainfall for one year with another", activebackground="light yellow", bg="light green", fg="black")
    option4.pack()
    emptyLabel4 = Label(window, text="", bg="lightskyblue1")
    emptyLabel4.pack()


    window.mainloop()


window = Tk()

window.configure(background="lightskyblue1")
window.geometry("500x405")
window.title("Rainfall")

emptyLabel = Label(window, text="WELCOME", font=("Courier", 44), bg="lightskyblue1")
emptyLabel.pack()

emptyLabel100= Label(window, text="", bg="lightskyblue1")
emptyLabel100.pack()


emptyLabel0 = Label(window, text="Choose any option...", font=("Courier", 24), bg="lightskyblue1", fg="purple3")
emptyLabel0.pack()

emptyLabel200 = Label(window, text="", bg="lightskyblue1")
emptyLabel200.pack()

option1 = Button(window, text="Data Analysis", activebackground="light yellow", bg="light green", fg="black", command=analysisGUI)
option1.pack()
emptyLabel1 = Label(window, text="", bg="lightskyblue1")
emptyLabel1.pack()

option2 = Button(window, text="Prediction", activebackground="light yellow", bg="light green", fg="black")
option2.pack()
emptyLabel2 = Label(window, text="", bg="lightskyblue1")
emptyLabel2.pack()

option3 = Button(window, text="Classification", activebackground="light yellow", bg="light green", fg="black")
option3.pack()
emptyLabel3 = Label(window, text="", bg="lightskyblue1")
emptyLabel3.pack()

option4 = Button(window, text="Image Classification", activebackground="light yellow", bg="light green", fg="black")
option4.pack()
emptyLabel4 = Label(window, text="", bg="lightskyblue1")
emptyLabel4.pack()


window.mainloop()
