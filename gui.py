from tkinter import *
# from tkinter.ttk import *
# from login import *
from functions import DataRainfall
from functions import states
import matplotlib.pyplot as plt
from PIL import ImageTk
import PIL.Image

# from tkinter import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from tkinter import messagebox
from report import *

df = DataRainfall()
# window=Tk()

r = RegisterReport()

class User:

    def __init__(self, uname, pswd):
        self.uname = uname
        self.pswd = pswd

    def showUserDetails(self):
        print(">> uname: {} pswd: {}".format(self.uname, self.pswd))


def guiElementsdestroy(guiElements):
    for elements in guiElements:
        elements.destroy()


class Project:

    def __init__(self, window):
        self.x=window
        self.main(window)




    def popUp(self):
            # window=Tk()
            messagebox.showinfo("Signed Successfully", "You have been signed successfully!!!")
            self.loginGUI()
            # l.loginGUI()



    def login(self):

        firebase_admin.get_app()
        username=self.username.get()
        password=self.password.get()

        # print(username, " ", password)
        # print(db.collection("User").document().get())
        usernameDB=db.collection("User").where("uname", '==', username).stream()
        passwordDB=db.collection("User").where("pswd", '==', password).stream()
        # print(usernameDB)
        # print(passwordDB)
        try:
            first=next(usernameDB)
            second=next(passwordDB)

            if first.id==second.id:
                messagebox.showinfo("Logged in Successfully", "You have been logged in successfully!!")
                self.mainScreen()
            elif second!=password:
                messagebox.showerror("Password Incorrect", "You have entered the wrong password!!")
            else:
                messagebox.showwarning("Unable to log in..", "Encountering some issue..")


        except StopIteration:
            messagebox.showerror("Error", "User not found")





    def loginGUI(self):
        guiElementsdestroy(window2.widgets)
        menubar = Menu(window2.window)
        file = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Options', menu=file)
        # file.add_command(label='Main', command=)
        file.add_command(label='SignUp', command=self.signUpGUI)
        file.add_command(label='Logout', command=self.ExitApplication)
        file.add_separator()
        file.add_command(label='Exit', command=window2.window.destroy)
        window2.window.config(menu=menubar)


        emptyLabel = Label(self.window, text="LOGIN", font=("Courier", 44), bg="lightskyblue1")
        emptyLabel.pack()

        emptyLabel100 = Label(self.window, text="", bg="lightskyblue1")
        emptyLabel100.pack()
        emptyLabel800 = Label(self.window, text="", bg="lightskyblue1")
        emptyLabel800.pack()

        emptyLabel05 = Label(self.window, text="Enter the username:", font=("Courier", 14), bg="lightskyblue1",
                            fg="purple3")
        emptyLabel05.pack()
        emptyLabel900 = Label(self.window, text="", bg="lightskyblue1")
        emptyLabel900.pack()
        self.username = Entry(self.window)
        self.username.pack()
        emptyLabel500 = Label(self.window, text="", bg="lightskyblue1")
        emptyLabel500.pack()

        emptyLabel0 = Label(self.window, text="Enter the password:",
                            font=("Courier", 14), bg="lightskyblue1",
                            fg="purple3")
        emptyLabel0.pack()
        emptyLabel700 = Label(self.window, text="", bg="lightskyblue1")
        emptyLabel700.pack()
        self.password = Entry(self.window, show="*")
        self.password.pack()

        emptyLabel400 = Label(self.window, text="", bg="lightskyblue1")
        emptyLabel400.pack()

        emptyLabel1100 = Label(self.window, text="", bg="lightskyblue1")
        emptyLabel1100.pack()

        option1 = Button(self.window, text="LOGIN", activebackground="light yellow", bg="light green", fg="black",
                         command=self.login)
        option1.pack()


        # emptyLabel9 = Label(window2.window, text="", bg="lightskyblue1")
        # emptyLabel9.pack()
        #
        #
        # prev = Button(window2.window, text="PREV",
        #                  activebackground="light yellow",
        #                  bg="lightgreen", fg="black", command=self.main(self.x))
        # prev.pack()

        self.widgets = [emptyLabel, emptyLabel0, emptyLabel100, emptyLabel800, emptyLabel900,emptyLabel500, option1, emptyLabel400,
                        emptyLabel700, emptyLabel1100, emptyLabel05, self.password, self.username, menubar]

        # window.mainloop()


    def signUp(self):

        firebase_admin.get_app()
        user = User(None, None)

        # print(self.username.get())
        # print(self.password.get())
        user.uname = self.username.get()
        user.pswd = self.password.get()

        if len(self.password.get())>5:
            data = user.__dict__

            db.collection("User").document().set(data)
            self.popUp()
        elif '@' or '#' or '*' or '_' or '$' in self.password.get():
            data = user.__dict__

            db.collection("User").document().set(data)
            self.popUp()
        else:
            messagebox.showwarning("Weak Password", "You have entered a Weak Password.. Please enter a strong password")

        # user.showUserDetails()

        # data = user.__dict__
        #
        # db.collection("User").document().set(data)

        # print(">> ", user.uname, "Saved in Firebase")

        # self.popUp()


    def signUpGUI(self):



        # guiElementsdestroy(window2.widgets)

        # window = Tk()
        # window.configure(background="lightskyblue1")
        # window.geometry("500x505")
        guiElementsdestroy(window2.widgets)

        window2.window.title("SIGN UP")
        menubar = Menu(window2.window)
        file = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Options', menu=file)
        # file.add_command(label='Main', command=)
        file.add_command(label='Login', command=self.loginGUI)
        file.add_separator()
        file.add_command(label='Exit', command=window2.window.destroy)
        window2.window.config(menu=menubar)


        emptyLabel1 = Label(window2.window, text="SIGN UP", font=("Courier", 44), bg="lightskyblue1")
        emptyLabel1.pack()

        emptyLabel2 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel2.pack()
        emptyLabel3 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel3.pack()

        emptyLabel05 = Label(window2.window, text="Enter the username:", font=("Courier", 14), bg="lightskyblue1",
                            fg="purple3")
        emptyLabel05.pack()
        emptyLabel4 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel4.pack()
        self.username = Entry(window2.window)
        self.username.pack()
        emptyLabel5 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel5.pack()

        emptyLabel0 = Label(window2.window, text="Enter the password:",
                            font=("Courier", 14), bg="lightskyblue1",
                            fg="purple3")
        emptyLabel0.pack()
        emptyLabel6 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel6.pack()
        self.password = Entry(window2.window, show="*")
        self.password.pack()

        emptyLabel7 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel7.pack()

        emptyLabel8 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel8.pack()

        option1 = Button(window2.window, text="SIGN UP", activebackground="light yellow", bg="light green", fg="black",
                         command=self.signUp)
        option1.pack()
        #
        # emptyLabel9 = Label(window2.window, text="", bg="lightskyblue1")
        # emptyLabel9.pack()
        #
        #
        # prev = Button(window2.window, text="PREV",
        #                  activebackground="light yellow",
        #                  bg="lightgreen", fg="black", command=self.main(self.x))
        # prev.pack()

        self.widgets=[emptyLabel1, emptyLabel0,emptyLabel05, option1, emptyLabel3, emptyLabel4, emptyLabel5,
                        emptyLabel6,emptyLabel7,emptyLabel8, emptyLabel2, self.username, self.password]

    def main(self, window):
        # window = Tk()
        # guiElementsdestroy(self.widgets)
        self.window=window
        self.window.configure(background="lightskyblue1")
        self.window.geometry("900x700")
        self.window.title("WELCOME")
        # background_image = PhotoImage("london.jpg")
        # background_label = Label(self.window, image=background_image)
        # background_label.place(x=0, y=0, relwidth=1, relheight=1)

        emptyLabel = Label(self.window, text="WELCOME", font=("Courier", 44), bg="lightskyblue1")
        emptyLabel.pack()

        emptyLabel100= Label(self.window, text="", bg="lightskyblue1")
        emptyLabel100.pack()
        emptyLabel800= Label(self.window, text="", bg="lightskyblue1")
        emptyLabel800.pack()


        emptyLabel05 = Label(self.window, text="RAINFALL ANALYSIS, PREDICTION", font=("Courier", 24), bg="lightskyblue1", fg="purple3")
        emptyLabel05.pack()
        emptyLabel07 = Label(self.window, text=" AND IMAGE CLASSIFICATION", font=("Courier", 24), bg="lightskyblue1", fg="purple3")
        emptyLabel07.pack()

        emptyLabel0 = Label(self.window, text="This project is based on data collected from year:2000-2017", font=("Courier", 14), bg="lightskyblue1",
                            fg="black")
        emptyLabel0.pack()

        emptyLabel200 = Label(self.window, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        emptyLabel200 = Label(self.window, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        emptyLabel200 = Label(self.window, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        emptyLabel200 = Label(self.window, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        option1 = Button(self.window, text="SIGN UP", activebackground="light yellow", bg="light green", fg="black", command=self.signUpGUI)
        option1.pack()
        emptyLabel1 = Label(self.window, text="", bg="lightskyblue1")
        emptyLabel1.pack()

        emptyLabel200 = Label(self.window, text="", bg="lightskyblue1")
        emptyLabel200.pack()



        option2 = Button(self.window, text="LOGIN", activebackground="light yellow", bg="light green",
                         fg="black", command=self.loginGUI)
        option2.pack()
        emptyLabel2 = Label(self.window, text="", bg="lightskyblue1")
        emptyLabel2.pack()

        img = PIL.Image.open('rainfall.jpg', 'r')
        img = ImageTk.PhotoImage(img)
        panel = Label(self.window, image = img)
        panel.image=img

        panel.pack(side="left", padx=20, pady=10)

        # side = "bottom", fill = "both", expand = "yes"
        self.widgets=[emptyLabel, emptyLabel100, emptyLabel800, emptyLabel0, emptyLabel200, option1, emptyLabel1
                      ,option2, emptyLabel2, emptyLabel05, emptyLabel07, panel]
        # self.window.mainloop()
        # window.destroy()


    def regression1(self):
        # window = Tk()

        # window.configure(background="lightskyblue1")
        # window.geometry("500x405")
        # window.title("Prediction")

        guiElementsdestroy(window2.widgets)
        menubar = Menu(window2.window)
        file = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Options', menu=file)
        file.add_command(label='Main Screen', command=self.mainScreen)

        file.add_command(label='Data Analysis', command=self.analysisGUI)
        file.add_command(label='Prediction', command=self.priorRegression)
        file.add_command(label='Classification', command=self.Classify)
        file.add_command(label='Image Classification', command=self.take_image)
        file.add_command(label='Logout', command=self.ExitApplication)
        file.add_separator()
        file.add_command(label='Exit', command=window2.window.destroy)
        window2.window.config(menu=menubar)
        emptyLabel100 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel100.pack()

        stateLabel = Label(window2.window, text="Enter the State", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        stateLabel.pack()
        self.state = Entry(window2.window)
        self.state.pack()

        emptyLabel200 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        monthLabel = Label(window2.window, text="Prediction Month", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        monthLabel.pack()
        self.month = Entry(window2.window)
        self.month.pack()

        emptyLabel300 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel300.pack()

        yearLabel = Label(window2.window, text="Prediction Year", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        yearLabel.pack()
        self.year = Entry(window2.window)
        self.year.pack()

        emptyLabel400 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel400.pack()

        btnShow = Button(window2.window, text="Predict", activebackground="light yellow", bg="light green", fg="black",
                         command=lambda:df.predict1(self.state.get(), self.month.get(), self.year.get()))
        btnShow.pack()


        emptyLabel9 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel9.pack()


        prev = Button(window2.window, text="PREV",
                         activebackground="light yellow",
                         bg="lightgreen", fg="black", command=self.priorRegression)
        prev.pack()

        self.widgets=[emptyLabel200, emptyLabel300, emptyLabel400, emptyLabel100, monthLabel, self.month,
                      stateLabel, btnShow, self.state, yearLabel, self.year, emptyLabel9, prev,
                      menubar]
        # window.mainloop()

    def regression(self):
        # window = Tk()

        # window.configure(background="lightskyblue1")
        # window.geometry("500x405")

        guiElementsdestroy(window2.widgets)
        window2.window.title("Prediction")
        menubar = Menu(window2.window)
        file = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Options', menu=file)
        file.add_command(label='Main Screen', command=self.mainScreen)

        file.add_command(label='Data Analysis', command=self.analysisGUI)
        file.add_command(label='Prediction', command=self.priorRegression)
        file.add_command(label='Classification', command=self.Classify)
        file.add_command(label='Image Classification', command=self.take_image)
        file.add_command(label='Logout', command=self.ExitApplication)
        file.add_separator()
        file.add_command(label='Exit', command=window2.window.destroy)
        window2.window.config(menu=menubar)

        emptyLabel100 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel100.pack()

        stateLabel = Label(window2.window, text="Enter the State", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        stateLabel.pack()
        self.state = Entry(window2.window)
        self.state.pack()

        emptyLabel200 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel200.pack()



        yearLabel = Label(window2.window, text="Prediction Year", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        yearLabel.pack()
        self.year = Entry(window2.window)
        self.year.pack()

        emptyLabel300 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel300.pack()

        btnShow = Button(window2.window, text="Predict", activebackground="light yellow", bg="light green", fg="black",
                         command=lambda:df.predict(self.state.get(), self.year.get()))
        btnShow.pack()
        emptyLabel9 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel9.pack()

        prev = Button(window2.window, text="PREV",
                      activebackground="light yellow",
                      bg="lightgreen", fg="black", command=self.priorRegression)
        prev.pack()

        self.widgets=[emptyLabel9,self.state, self.year, prev, emptyLabel100, emptyLabel300, emptyLabel200, stateLabel, yearLabel, btnShow
                      ,menubar]
        # window.mainloop()

    def priorRegression(self):
        guiElementsdestroy(window2.widgets)
        # window = Tk()

        # window.configure(background="lightskyblue1")
        # window.geometry("700x405")
        # window.title("Prediction")
        menubar = Menu(window2.window)
        file = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Options', menu=file)
        file.add_command(label='Main Screen', command=self.mainScreen)
        file.add_command(label='Data Analysis', command=self.analysisGUI)

        file.add_command(label='Prediction', command=self.priorRegression)
        file.add_command(label='Classification', command=self.Classify)
        file.add_command(label='Image Classification', command=self.take_image)
        file.add_command(label='Logout', command=self.ExitApplication)
        file.add_separator()
        file.add_command(label='Exit', command=window2.window.destroy)
        window2.window.config(menu=menubar)
        emptyLabel200 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        emptyLabelA = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabelA.pack()
        emptyLabelB = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabelB.pack()

        emptyLabel0 = Label(window2.window, text="Choose any option...", font=("Courier", 24), bg="lightskyblue1", fg="purple3")
        emptyLabel0.pack()
        emptyLabelC = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabelC.pack()
        emptyLabelD = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabelD.pack()


        option1 = Button(window2.window, text="Do you want to predict rainfall for a specific month in a specific year for a specific state",
                         activebackground="light yellow", bg="light green", fg="black",
                         command=self.regression1)
        option1.pack()
        emptyLabel1 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel1.pack()

        option2 = Button(window2.window, text="Do you want to predict average rainfall for a specific year overall for a specific state",
                         activebackground="light yellow", bg="light green", fg="black",
                         command=self.regression)
        option2.pack()
        emptyLabel2 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel2.pack()

        #
        # emptyLabel9 = Label(window2.window, text="", bg="lightskyblue1")
        # emptyLabel9.pack()


        prev = Button(window2.window, text="PREV",
                         activebackground="light yellow",
                         bg="lightgreen", fg="black", command=self.mainScreen)
        prev.pack()


        self.widgets=[prev, emptyLabel200, emptyLabelA, emptyLabelB, emptyLabel0, emptyLabelC, emptyLabelD,
                      option1, option2, emptyLabel2, menubar]
        # window.mainloop()

    def oneState(self):

        # window = Tk()

        # window.configure(background="lightskyblue1")
        # window.geometry("500x405")
        guiElementsdestroy(window2.widgets)
        window2.window.title("One State")

        stateLabel = Label(window2.window, text="Enter the state", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        stateLabel.pack()
        self.state= Entry(window2.window)
        self.state.pack()

        emptyLabel100 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel100.pack()

        yearLabel = Label(window2.window, text="Enter the Year", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        yearLabel.pack()
        self.year = Entry(window2.window)
        self.year.pack()

        # df1=DataRainfall(self.state, self.year)

        btnShow = Button(window2.window, text="Show", activebackground="light yellow", bg="light green", fg="black",
                         command=lambda:df.state1(self.state.get(), self.year.get()))
        btnShow.pack()


        emptyLabel9 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel9.pack()

        prev = Button(window2.window, text="PREV",
                         activebackground="light yellow",
                         bg="lightgreen", fg="black", command=self.analysisGUI)
        prev.pack()

        self.widgets=[emptyLabel100, stateLabel, yearLabel,self.state, self.year,btnShow,emptyLabel9,prev]
        # window.mainloop()

    def twoStates(self):
        # window = Tk()

        # window.configure(background="lightskyblue1")
        # window.geometry("500x405")
        guiElementsdestroy(window2.widgets)
        window2.window.title("Two State")

        stateLabel1 = Label(window2.window, text="Enter the state 1", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        stateLabel1.pack()
        self.stateFirst = Entry(window2.window)
        self.stateFirst.pack()

        emptyLabel100 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel100.pack()

        stateLabel2 = Label(window2.window, text="Enter the state 2", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        stateLabel2.pack()
        self.stateSecond = Entry(window2.window)
        self.stateSecond.pack()

        emptyLabel200 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        yearLabel = Label(window2.window, text="Enter the Year", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        yearLabel.pack()
        self.year = Entry(window2.window)
        self.year.pack()

        btnShow = Button(window2.window, text="Show", activebackground="light yellow", bg="light green", fg="black",
                         command=lambda:df.state2(self.stateFirst.get(), self.stateSecond.get()
                                                  , self.year.get()))
        btnShow.pack()
        emptyLabel9 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel9.pack()

        prev = Button(window2.window, text="PREV",
                      activebackground="light yellow",
                      bg="lightgreen", fg="black", command=self.analysisGUI)
        prev.pack()

        self.widgets=[emptyLabel9, prev, emptyLabel100, emptyLabel200, stateLabel1, stateLabel2, self.stateFirst,
                      self.stateSecond, self.year , yearLabel, btnShow]
        # window.mainloop()

    def indiaSpecificYear(self):

        # window = Tk()

        # window.configure(background="lightskyblue1")
        # window.geometry("500x405")
        guiElementsdestroy(window2.widgets)
        window2.window.title("Analysis for India")

        yearLabel = Label(window2.window, text="Enter the Year", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        yearLabel.pack()
        self.year = Entry(window2.window)
        self.year.pack()

        emptyLabel100 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel100.pack()

        btnShow = Button(window2.window, text="Show", activebackground="light yellow", bg="light green", fg="black",
                         command=lambda:df.india1(self.year.get()))
        btnShow.pack()


        emptyLabel9 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel9.pack()

        prev = Button(window2.window, text="PREV",
                         activebackground="light yellow",
                         bg="lightgreen", fg="black", command=self.analysisGUI)
        prev.pack()

        self.widgets=[emptyLabel100,emptyLabel9, prev, yearLabel, btnShow, self.year]
        # window.mainloop()

    def indiaSpecific2Years(self):
        # window = Tk()

        # window2.window.configure(background="lightskyblue1")
        # window2.window.geometry("500x405")
        guiElementsdestroy(window2.widgets)
        window2.window.title("Compare Rainfall for specific 2 years for India")

        yearLabel1 = Label(window2.window, text="Enter the Year 1", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        yearLabel1.pack()
        self.year1 = Entry(window2.window)
        self.year1.pack()

        emptyLabel100 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel100.pack()

        yearLabel2 = Label(window2.window, text="Enter the Year 2", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        yearLabel2.pack()
        self.year2 = Entry(window2.window)
        self.year2.pack()

        emptyLabel200 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        btnShow = Button(window2.window, text="Show", activebackground="light yellow", bg="light green", fg="black",
                         command=lambda:df.india2(self.year1.get(), self.year2.get()))
        btnShow.pack()
        emptyLabel9 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel9.pack()

        prev = Button(window2.window, text="PREV",
                      activebackground="light yellow",
                      bg="lightgreen", fg="black", command=self.analysisGUI)
        prev.pack()

        self.widgets=[emptyLabel100, emptyLabel200, self.year1, self.year2, prev, emptyLabel9, btnShow, yearLabel1, yearLabel2]
        # window.mainloop()

    def compareMonthsOfSameState(self):
        # window = Tk()

        # window.configure(background="lightskyblue1")
        # window.geometry("500x405")
        guiElementsdestroy(window2.widgets)
        window2.window.title("One State")

        monthLabel1 = Label(window2.window, text="Enter the Month 1", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        monthLabel1.pack()
        self.month1 = Entry(window2.window)
        self.month1.pack()

        emptyLabel100 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel100.pack()

        monthLabel2 = Label(window2.window, text="Enter the Month 2", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        monthLabel2.pack()
        self.month2 = Entry(window2.window)
        self.month2.pack()

        emptyLabel200 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        stateLabel2 = Label(window2.window, text="Enter the State", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        stateLabel2.pack()
        self.state = Entry(window2.window)
        self.state.pack()

        btnShow = Button(window2.window, text="Show", activebackground="light yellow", bg="light green", fg="black",
                         command=lambda:df.sameStateDiffMonths(self.month1.get(), self.month2.get(),
                                                               self.state.get()))
        btnShow.pack()

        emptyLabel9 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel9.pack()

        prev = Button(window2.window, text="PREV",
                         activebackground="light yellow",
                         bg="lightgreen", fg="black", command=self.analysisGUI)
        prev.pack()
        self.widgets=[emptyLabel100,emptyLabel200, monthLabel1, monthLabel2, self.month1, self.month2,
                      self.state,stateLabel2,btnShow, prev, emptyLabel9]

        # window.mainloop()

    def compareMonthsOfDifferentStates(self):
        # window = Tk()

        # window.configure(background="lightskyblue1")
        # window.geometry("500x405")
        guiElementsdestroy(window2.widgets)
        window2.window.title("Compare Months of different States")

        monthLabel1 = Label(window2.window, text="Enter the Month 1", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        monthLabel1.pack()
        self.month1 = Entry(window2.window)
        self.month1.pack()

        emptyLabel100 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel100.pack()

        monthLabel2 = Label(window2.window, text="Enter the Month 2", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        monthLabel2.pack()
        self.month2 = Entry(window2.window)
        self.month2.pack()

        emptyLabel200 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        stateLabel2 = Label(window2.window, text="Enter the State 1", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        stateLabel2.pack()
        self.state1 = Entry(window2.window)
        self.state1.pack()

        emptyLabel300 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel300.pack()

        stateLabel3 = Label(window2.window, text="Enter the State 2", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        stateLabel3.pack()
        self.state2 = Entry(window2.window)
        self.state2.pack()

        btnShow = Button(window2.window, text="Show", activebackground="light yellow", bg="light green", fg="black",
                         command=lambda :df.DiffStateDiffMonths(self.state1.get(), self.state2.get(),
                                                                self.month1.get(), self.month2.get()))
        btnShow.pack()

        emptyLabel9 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel9.pack()

        prev = Button(window2.window, text="PREV",
                         activebackground="light yellow",
                         bg="lightgreen", fg="black", command=self.analysisGUI)
        prev.pack()

        self.widgets=[emptyLabel9, prev, btnShow, emptyLabel200, emptyLabel300, emptyLabel100, stateLabel3, self.state2,
                      stateLabel2, self.state1, monthLabel2, monthLabel1, self.month1, self.month2]
        # window.mainloop()

    def analysisGUI(self):
        # window = Tk()
        # window.configure(background="lightskyblue1")
        # window.geometry("600x600")
        # window.title("Data Analysis")

        guiElementsdestroy(window2.widgets)
        menubar = Menu(window2.window)
        file = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Options', menu=file)
        file.add_command(label='Main Screen', command=self.mainScreen)

        file.add_command(label='Data Analysis', command=self.analysisGUI)
        file.add_command(label='Prediction', command=self.priorRegression)
        file.add_command(label='Classification', command=self.Classify)
        file.add_command(label='Image Classification', command=self.take_image)
        file.add_command(label='Logout', command=self.ExitApplication)
        file.add_separator()
        file.add_command(label='Exit', command=window2.window.destroy)
        window2.window.config(menu=menubar)
        emptyLabel100 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel100.pack()

        emptyLabel0 = Label(window2.window, text="Choose any option...", font=("Courier", 24), bg="lightskyblue1", fg="purple3")
        emptyLabel0.pack()

        emptyLabel200= Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        option1 = Button(window2.window, text="Rainfall of one state in specific year", activebackground="light yellow", bg="light green", fg="black",command=self.oneState)
        option1.pack()
        emptyLabel300 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel300.pack()

        option2 = Button(window2.window, text="Compare rainfall of two states in specific year ", activebackground="light yellow", bg="light green", fg="black", command=self.twoStates)
        option2.pack()
        emptyLabel400 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel400.pack()

        option3 = Button(window2.window, text="Show Rainfall all over India in one specific year", activebackground="light yellow", bg="light green", fg="black", command=self.indiaSpecificYear)
        option3.pack()
        emptyLabel500 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel500.pack()

        option4 = Button(window2.window, text="Compare rainfall for one year with another", activebackground="light yellow", bg="light green", fg="black", command=self.indiaSpecific2Years)
        option4.pack()
        emptyLabel600 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel600.pack()

        # emptyLabel5 = Label(window, text="", bg="lightskyblue1")
        # emptyLabel5.pack()
        option5 = Button(window2.window, text="Compare rainfall of one month with another month of the same state", activebackground="light yellow",
                         bg="light green", fg="black", command=self.compareMonthsOfSameState)
        option5.pack()
        # emptyLabel5 = Label(window, text="", bg="lightskyblue1")
        # emptyLabel5.pack()

        emptyLabel700 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel700.pack()

        option6 = Button(window2.window, text="Compare rainfall of one month with another month for two different states", activebackground="light yellow",
                         bg="light green", fg="black", command=self.compareMonthsOfDifferentStates)
        option6.pack()
        emptyLabel9 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel9.pack()

        prev = Button(window2.window, text="PREV",
                         activebackground="light yellow",
                         bg="lightgreen", fg="black", command=self.mainScreen)
        prev.pack()

        self.widgets=[emptyLabel100, emptyLabel200, emptyLabel300, emptyLabel400, emptyLabel500,
                      emptyLabel600, emptyLabel700, emptyLabel9, option4, option3, option1, option2,
                      option5, option6, prev, emptyLabel0, menubar]

        # window.mainloop()
    #
    # def close_window(self, window):
    #     window.destroy()



    def Classify(self):
        # window = Tk()

        # window.configure(background="lightskyblue1")
        # window.geometry("500x405")
        guiElementsdestroy(window2.widgets)
        window2.window.title("State Classification")
        menubar = Menu(window2.window)
        file = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Options', menu=file)
        file.add_command(label='Main Screen', command=self.mainScreen)

        file.add_command(label='Data Analysis', command=self.analysisGUI)
        file.add_command(label='Prediction', command=self.priorRegression)
        file.add_command(label='Classification', command=self.Classify)
        file.add_command(label='Image Classification', command=self.take_image)
        file.add_command(label='Logout', command=self.ExitApplication)
        file.add_separator()
        file.add_command(label='Exit', command=window2.window.destroy)
        window2.window.config(menu=menubar)



        emptyLabel100 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel100.pack()

        stateLabel = Label(window2.window, text="Enter the State", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        stateLabel.pack()
        self.state = Entry(window2.window)
        self.state.pack()
        # print(self.state.get())

        emptyLabel200 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel200.pack()
        # df=DataRainfall(state)
        btnShow = Button(window2.window, text="Classify", activebackground="light yellow", bg="light green", fg="black",
                         command=lambda :df.classifyState(self.state.get()))
        btnShow.pack()

        emptyLabel9 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel9.pack()

        prev = Button(window2.window, text="PREV",
                      activebackground="light yellow",
                      bg="lightgreen", fg="black", command=self.mainScreen)
        prev.pack()

        self.widgets=[emptyLabel9, prev, emptyLabel100, emptyLabel200, self.state, btnShow, stateLabel,
                      menubar]
        # window.mainloop()

    def check_for_pithole(self):
        model = tf.keras.models.load_model('64X3-CNN.model1')
        prediction = model.predict([r.prepare("{}".format(self.path.get()))])
        # print(prediction)
        if prediction[0][0]>=0.35:
            messagebox.showinfo("No pothole", "Road is clear.. No signs of pothole!!!!")
        else:
            messagebox.showerror("Pothole present", "Presence of pothole is found!!!")
            self.register_report()

    def register_report(self):
        # window2.window = Tk()
        # window2.window.configure(background="lightskyblue1")
        # window2.window.geometry("700x505")

        guiElementsdestroy(window2.widgets)
        window2.window.title("REGISTER REPORT")

        emptyLabel = Label(window2.window, text="REGISTER REPORT", font=("Courier", 44), bg="lightskyblue1")
        emptyLabel.pack()

        emptyLabel100 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel100.pack()
        emptyLabel200 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        emptyLabel0 = Label(window2.window, text="Name of the Complainant:", font=("Courier", 14), bg="lightskyblue1",
                            fg="purple3")
        emptyLabel0.pack()
        emptyLabel300 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel300.pack()
        self.name = Entry(window2.window)
        self.name.pack()
        emptyLabel400 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel400.pack()

        emptyLabel1 = Label(window2.window, text="Phone number of the Complainant:",
                            font=("Courier", 14), bg="lightskyblue1",
                            fg="purple3")
        emptyLabel1.pack()
        emptyLabel500 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel500.pack()
        self.phone = Entry(window2.window)
        self.phone.pack()
        self.phone.insert(0, "+91 ")

        # name=self.name.get()
        # phone=self.phone.get()

        emptyLabel600 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel600.pack()

        emptyLabel700 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel700.pack()

        # r.values_for_dataBase(name, phone)

        option1 = Button(window2.window, text="NEXT", activebackground="light yellow", bg="light green", fg="black",
                         command=lambda:self.pithole_details(self.name.get(), self.phone.get()))
        option1.pack()


        emptyLabel9 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel9.pack()

        prev = Button(window2.window, text="PREV",
                         activebackground="light yellow",
                         bg="lightgreen", fg="black", command=self.take_image)
        prev.pack()


        self.widgets=[emptyLabel1, emptyLabel100, emptyLabel200, emptyLabel300, emptyLabel400, emptyLabel500,
                      emptyLabel600, emptyLabel700, option1, self.phone, self.name, emptyLabel,prev,
                      emptyLabel0]
        # window2.window.mainloop()



    def pithole_details(self, name, phone):
        # window1 = Tk()
        # window1.configure(background="lightskyblue1")
        # window1.geometry("700x505")
        guiElementsdestroy(window2.widgets)
        window2.window.title("Pothole details")
        emptyLabel100 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel100.pack()

        emptyLabelArea = Label(window2.window, text="Enter the Area:",
                            font=("Courier", 14), bg="lightskyblue1",
                            fg="purple3")
        emptyLabelArea.pack()
        self.area = Entry(window2.window)
        self.area.pack()

        emptyLabel200 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel200.pack()


        emptyLabelCity = Label(window2.window, text="Enter the City:",
                            font=("Courier", 14), bg="lightskyblue1",
                            fg="purple3")
        emptyLabelCity.pack()
        self.city = Entry(window2.window)
        self.city.pack()



        emptyLabel300 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel300.pack()
        emptyLabelState = Label(window2.window, text="Enter the State:",
                            font=("Courier", 14), bg="lightskyblue1",
                            fg="purple3")
        emptyLabelState.pack()
        self.state = Entry(window2.window)
        self.state.pack()

        emptyLabel400 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel400.pack()

        emptyLabelPitholes = Label(window2.window, text="Enter the number of potholes:",
                            font=("Courier", 14), bg="lightskyblue1",
                            fg="purple3")
        emptyLabelPitholes.pack()
        self.number = Entry(window2.window)
        self.number.pack()
        emptyLabel500 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel500.pack()

        emptyLabelDia = Label(window2.window, text="Enter the average diameter of pothole(s)",
                            font=("Courier", 14), bg="lightskyblue1",
                            fg="purple3")
        emptyLabelDia.pack()
        self.dia = Entry(window2.window)
        self.dia.pack()

        emptyLabel600 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel600.pack()

        emptyLabel700 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel700.pack()

        emptyLabel800 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel800.pack()

        # r.values_for_dataBase1(self.area.get(), self.city.get(), self.state.get(), self.dia.get(),
        #                        self.number.get())
        # name=self.name.get()
        # phone=self.phone.get()
        # area=self.area.get()
        # city=self.city.get()
        # state=self.state.get()
        # dia=self.dia.get()
        # number=self.number.get()
        option1 = Button(window2.window, text="FILE COMPLAINT", activebackground="light yellow", bg="light green", fg="black",
                         command=lambda:r.entry_in_database(name, phone, self.area.get(),
                                                            self.city.get(), self.state.get(),
                                                            self.dia.get(), self.number.get()))
        option1.pack()

        emptyLabel9 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel9.pack()

        prev = Button(window2.window, text="PREV",
                         activebackground="light yellow",
                         bg="lightgreen", fg="black", command=self.register_report)
        prev.pack()
        self.widgets=[emptyLabel600, emptyLabel700, emptyLabel800, emptyLabel9, prev,
                      emptyLabel500, emptyLabel400, emptyLabel300, emptyLabel200, emptyLabel100,
                      emptyLabelPitholes,emptyLabelArea, emptyLabelCity, emptyLabelDia, emptyLabelState,
                      self.area, self.dia, self.city, self.state, self.number, option1]

        # window2.window1.mainloop()



    def take_image(self):

        # window1 = Tk()
        # window1.configure(background="lightskyblue1")
        # window1.geometry("500x505")
        guiElementsdestroy(window2.widgets)
        window2.window.title("IMAGE CLASSIFICATION")
        menubar = Menu(window2.window)
        file = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Options', menu=file)
        file.add_command(label='Main Screen', command=self.mainScreen)

        file.add_command(label='Data Analysis', command=self.analysisGUI)
        file.add_command(label='Prediction', command=self.priorRegression)
        file.add_command(label='Classification', command=self.Classify)
        file.add_command(label='Image Classification', command=self.take_image)
        file.add_command(label='Logout', command=self.ExitApplication)
        file.add_separator()
        file.add_command(label='Exit', command=window2.window.destroy)
        window2.window.config(menu=menubar)

        emptyLabel0 = Label(window2.window, text="Enter the path for the image to be tested:",
                            font=("Courier", 14), bg="lightskyblue1",
                            fg="purple3")
        emptyLabel0.pack()
        self.path = Entry(window2.window)
        self.path.pack()

        r.take_path(self.path)

        emptyLabel200 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel200.pack()
        option1 = Button(window2.window, text="CHECK", activebackground="light yellow", bg="light green", fg="black",
                         command=self.check_for_pithole)
        option1.pack()

        emptyLabel9 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel9.pack()

        prev = Button(window2.window, text="PREV",
                      activebackground="light yellow",
                      bg="lightgreen", fg="black", command=self.mainScreen)
        prev.pack()

        self.widgets=[option1, self.path, emptyLabel200, emptyLabel0, emptyLabel9, prev,menubar]
        # window1.mainloop()

    def ExitApplication(self):
        MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                           icon='warning')
        if MsgBox == 'yes':
            # guiElementsdestroy(window2.window)
            self.signUpGUI()
        else:
            messagebox.showinfo('Return', 'You will now return to the application screen')


    def mainScreen(self):
        # window = Tk()

        # window.configure(background="lightskyblue1")

        # window.geometry("500x405")
        # window.title("Rainfall")

        guiElementsdestroy(window2.widgets)
        menubar=Menu(window2.window)
        file = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Options', menu=file)
        file.add_command(label='Data Analysis', command=self.analysisGUI)
        file.add_command(label='Prediction', command=self.priorRegression)
        file.add_command(label='Classification', command=self.Classify)
        file.add_command(label='Image Classification', command=self.take_image)
        file.add_command(label='Logout', command=self.ExitApplication)
        file.add_separator()
        file.add_command(label='Exit', command=window2.window.destroy)
        window2.window.config(menu=menubar)

        emptyLabel05 = Label(window2.window, text="WELCOME", font=("Courier", 44), bg="lightskyblue1")
        emptyLabel05.pack()

        emptyLabel100= Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel100.pack()


        emptyLabel0 = Label(window2.window, text="Choose any option...", font=("Courier", 24), bg="lightskyblue1", fg="purple3")
        emptyLabel0.pack()

        emptyLabel200 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel200.pack()
        option1 = Button(window2.window, text="Data Analysis", activebackground="light yellow", bg="light green", fg="black", command=self.analysisGUI)
        option1.pack()
        emptyLabel300 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel300.pack()

        option2 = Button(window2.window, text="Prediction", activebackground="light yellow", bg="light green", fg="black", command=self.priorRegression)
        option2.pack()
        emptyLabel400 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel400.pack()

        option3 = Button(window2.window, text="Classification", activebackground="light yellow", bg="light green", fg="black", command=self.Classify)
        option3.pack()
        emptyLabel500 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel500.pack()

        option4 = Button(window2.window, text="Image Classification", activebackground="light yellow", bg="light green", fg="black", command=self.take_image)
        option4.pack()
        emptyLabel600 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel600.pack()

        emptyLabel700 = Label(window2.window, text="", bg="lightskyblue1")
        emptyLabel700.pack()
        #
        # option4 = Button(window, text="CLOSE", activebackground="light yellow", bg="light green",
        #                  fg="black", command=self.close_window(window))
        # option4.pack()
        # emptyLabel4 = Label(window, text="", bg="lightskyblue1")
        # emptyLabel4.pack()

        self.widgets=[emptyLabel100,emptyLabel200, emptyLabel300, emptyLabel400, emptyLabel05,
                      emptyLabel500, emptyLabel600, emptyLabel700, emptyLabel0, option1, option2,
                      option3, option4, menubar]

        # window.mainloop()

        # window.destroy()

    def start(self):
        self.mainScreen()


# l=Login()
window1=Tk()
# canv = Canvas(window1, width=80, height=80, bg='white')
# canv.pack()
#
# img = ImageTk.PhotoImage(PIL.Image.open("rainfall.jpg"))  # PIL solution
# canv.create_image(20, 20, anchor=NW, image=img)# fp = open("rainfall.jpg","rb")
# img = PIL.Image.open(fp)
# # img = ImageTk.PhotoImage(Image.open("rainfall.jpg"))
# panel = Label(window1, image = img)
# panel.pack(side = "bottom", fill = "both", expand = "yes")
window2=Project(window1)
# p = Project()
# p.main()

window1.mainloop()
