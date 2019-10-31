from tkinter import *
# from tkinter.ttk import *
# from login import *
from functions import DataRainfall
# from tkinter import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from tkinter import messagebox
from report import *


#
# cred = credentials.Certificate("serviceAccountKey.json")
# firebase_admin.initialize_app(cred)
#
# db = firestore.client()
df = DataRainfall()
# window=Tk()

r = RegisterReport()


class User:

    def __init__(self, uname, pswd):
        self.uname = uname
        self.pswd = pswd

    def showUserDetails(self):
        print(">> uname: {} pswd: {}".format(self.uname, self.pswd))


class Project:

    def signUp(self):
        firebase_admin.get_app()
        user = User(None, None)

        # print(self.username.get())
        # print(self.password.get())
        user.uname = self.username.get()
        user.pswd = self.password.get()

        # user.showUserDetails()

        data = user.__dict__

        db.collection("User").document().set(data)

        # print(">> ", user.uname, "Saved in Firebase")

        self.popUp()


    def popUp(self):
            # window=Tk()
            messagebox.showinfo("Signed Successfully", "You have been signed successfully!!!")
            self.loginGUI()


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







    def signUpGUI(self):
        window = Tk()
        window.configure(background="lightskyblue1")
        window.geometry("500x505")
        window.title("SIGN UP")

        emptyLabel = Label(window, text="SIGN UP", font=("Courier", 44), bg="lightskyblue1")
        emptyLabel.pack()

        emptyLabel100 = Label(window, text="", bg="lightskyblue1")
        emptyLabel100.pack()
        emptyLabel800 = Label(window, text="", bg="lightskyblue1")
        emptyLabel800.pack()

        emptyLabel0 = Label(window, text="Enter the username:", font=("Courier", 14), bg="lightskyblue1",
                            fg="purple3")
        emptyLabel0.pack()
        emptyLabel800 = Label(window, text="", bg="lightskyblue1")
        emptyLabel800.pack()
        self.username = Entry(window)
        self.username.pack()
        emptyLabel800 = Label(window, text="", bg="lightskyblue1")
        emptyLabel800.pack()

        emptyLabel0 = Label(window, text="Enter the password:",
                            font=("Courier", 14), bg="lightskyblue1",
                            fg="purple3")
        emptyLabel0.pack()
        emptyLabel800 = Label(window, text="", bg="lightskyblue1")
        emptyLabel800.pack()
        self.password = Entry(window, show="*")
        self.password.pack()

        emptyLabel200 = Label(window, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        emptyLabel200 = Label(window, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        option1 = Button(window, text="SIGN UP", activebackground="light yellow", bg="light green", fg="black",
                         command=self.signUp)
        option1.pack()

        window.mainloop()

    def loginGUI(self):
        window = Tk()
        window.configure(background="lightskyblue1")
        window.geometry("500x505")
        window.title("LOGIN")

        emptyLabel = Label(window, text="LOGIN", font=("Courier", 44), bg="lightskyblue1")
        emptyLabel.pack()

        emptyLabel100 = Label(window, text="", bg="lightskyblue1")
        emptyLabel100.pack()
        emptyLabel800 = Label(window, text="", bg="lightskyblue1")
        emptyLabel800.pack()

        emptyLabel0 = Label(window, text="Enter the username:", font=("Courier", 14), bg="lightskyblue1",
                            fg="purple3")
        emptyLabel0.pack()
        emptyLabel800 = Label(window, text="", bg="lightskyblue1")
        emptyLabel800.pack()
        self.username = Entry(window)
        self.username.pack()
        emptyLabel800 = Label(window, text="", bg="lightskyblue1")
        emptyLabel800.pack()

        emptyLabel0 = Label(window, text="Enter the password:",
                            font=("Courier", 14), bg="lightskyblue1",
                            fg="purple3")
        emptyLabel0.pack()
        emptyLabel800 = Label(window, text="", bg="lightskyblue1")
        emptyLabel800.pack()
        self.password = Entry(window, show="*")
        self.password.pack()

        emptyLabel200 = Label(window, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        emptyLabel200 = Label(window, text="", bg="lightskyblue1")
        emptyLabel200.pack()


        option1 = Button(window, text="LOGIN", activebackground="light yellow", bg="light green", fg="black",
                         command=self.login)
        option1.pack()

        window.mainloop()

    def main(self):
        window = Tk()
        window.configure(background="lightskyblue1")
        window.geometry("1200x505")
        window.title("WELCOME")

        emptyLabel = Label(window, text="WELCOME", font=("Courier", 44), bg="lightskyblue1")
        emptyLabel.pack()

        emptyLabel100= Label(window, text="", bg="lightskyblue1")
        emptyLabel100.pack()
        emptyLabel800= Label(window, text="", bg="lightskyblue1")
        emptyLabel800.pack()


        emptyLabel0 = Label(window, text="RAINFALL ANALYSIS, PREDICTION AND IMAGE CLASSIFICATION", font=("Courier", 24), bg="lightskyblue1", fg="purple3")
        emptyLabel0.pack()

        emptyLabel0 = Label(window, text="This  project is based on data collected from year:2000-2017", font=("Courier", 14), bg="lightskyblue1",
                            fg="black")
        emptyLabel0.pack()

        emptyLabel200 = Label(window, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        emptyLabel200 = Label(window, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        emptyLabel200 = Label(window, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        emptyLabel200 = Label(window, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        option1 = Button(window, text="SIGN UP", activebackground="light yellow", bg="light green", fg="black", command=self.signUpGUI)
        option1.pack()
        emptyLabel1 = Label(window, text="", bg="lightskyblue1")
        emptyLabel1.pack()

        emptyLabel200 = Label(window, text="", bg="lightskyblue1")
        emptyLabel200.pack()



        option2 = Button(window, text="LOGIN", activebackground="light yellow", bg="light green", fg="black", command=self.loginGUI)
        option2.pack()
        emptyLabel2 = Label(window, text="", bg="lightskyblue1")
        emptyLabel2.pack()



        window.mainloop()
        window.destroy()


    def analysisGUI(self):
        window = Tk()
        window.configure(background="lightskyblue1")
        window.geometry("600x600")
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

        option2 = Button(window, text="Compare rainfall of two states in specific year ", activebackground="light yellow", bg="light green", fg="black", command=df.twoStates)
        option2.pack()
        emptyLabel2 = Label(window, text="", bg="lightskyblue1")
        emptyLabel2.pack()

        option3 = Button(window, text="Show Rainfall all over India in one specific year", activebackground="light yellow", bg="light green", fg="black", command=df.indiaSpecificYear)
        option3.pack()
        emptyLabel3 = Label(window, text="", bg="lightskyblue1")
        emptyLabel3.pack()

        option4 = Button(window, text="Compare rainfall for one year with another", activebackground="light yellow", bg="light green", fg="black", command=df.indiaSpecific2Years)
        option4.pack()
        emptyLabel4 = Label(window, text="", bg="lightskyblue1")
        emptyLabel4.pack()

        # emptyLabel5 = Label(window, text="", bg="lightskyblue1")
        # emptyLabel5.pack()
        option5 = Button(window, text="Compare rainfall of one month with another month of the same state", activebackground="light yellow",
                         bg="light green", fg="black", command=df.compareMonthsOfSameState)
        option5.pack()
        # emptyLabel5 = Label(window, text="", bg="lightskyblue1")
        # emptyLabel5.pack()

        emptyLabel6 = Label(window, text="", bg="lightskyblue1")
        emptyLabel6.pack()

        option6 = Button(window, text="Compare rainfall of one month with another month for two different states", activebackground="light yellow",
                         bg="light green", fg="black", command=df.compareMonthsOfDifferentStates)
        option6.pack()
        emptyLabel7 = Label(window, text="", bg="lightskyblue1")
        emptyLabel7.pack()

        prev = Button(window, text="PREV",
                         activebackground="light yellow",
                         bg="lightyellow", fg="black", command=self.mainScreen)
        prev.pack()
        emptyLabel7 = Label(window, text="", bg="lightskyblue1")
        emptyLabel7.pack()

        window.mainloop()
    #
    # def close_window(self, window):
    #     window.destroy()

    def mainScreen(self):
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

        option1 = Button(window, text="Data Analysis", activebackground="light yellow", bg="light green", fg="black", command=self.analysisGUI)
        option1.pack()
        emptyLabel1 = Label(window, text="", bg="lightskyblue1")
        emptyLabel1.pack()

        option2 = Button(window, text="Prediction", activebackground="light yellow", bg="light green", fg="black", command=df.priorRegression)
        option2.pack()
        emptyLabel2 = Label(window, text="", bg="lightskyblue1")
        emptyLabel2.pack()

        option3 = Button(window, text="Classification", activebackground="light yellow", bg="light green", fg="black", command=df.Classify)
        option3.pack()
        emptyLabel3 = Label(window, text="", bg="lightskyblue1")
        emptyLabel3.pack()

        option4 = Button(window, text="Image Classification", activebackground="light yellow", bg="light green", fg="black", command=r.take_image)
        option4.pack()
        emptyLabel4 = Label(window, text="", bg="lightskyblue1")
        emptyLabel4.pack()

        emptyLabel3 = Label(window, text="", bg="lightskyblue1")
        emptyLabel3.pack()
        #
        # option4 = Button(window, text="CLOSE", activebackground="light yellow", bg="light green",
        #                  fg="black", command=self.close_window(window))
        # option4.pack()
        # emptyLabel4 = Label(window, text="", bg="lightskyblue1")
        # emptyLabel4.pack()

        window.mainloop()

        # window.destroy()

    def start(self):
        self.mainScreen()


p = Project()
p.main()

