import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from tkinter import *
from tkinter import messagebox
# from testing_model import *
import os
import tensorflow as tf
import cv2
from tensorflow import keras

CATEGORIES = ['with', 'without']




cred = credentials.Certificate("serviceAccountKey1.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


class Report:

    def __init__(self, name, phone, city, state, area, dia, number):
        self.name = name
        self.phone = phone
        self.area=area
        self.city=city
        self.state=state
        self.dia=dia
        self.number=number


    def showUserDetails(self):
        print(">> name: {} phone: {}".format(self.name, self.phone))
        print(">>area: {}  city: {} state:{} dia: {}".format(self.area,  self.state, self.city, self. dia))



class RegisterReport:

    def prepare(self, filepath):
        print(filepath)
        IMG_SIZE = 280
        img_array = cv2.imread("{}".format(filepath), cv2.IMREAD_GRAYSCALE)
        print(img_array)
        new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))

        return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

    def check_for_pithole(self):
        model = tf.keras.models.load_model('64X3-CNN.model')
        prediction = model.predict([self.prepare("{}".format(self.path.get()))])
        print(prediction)
        if prediction[0][0]==1:
            messagebox.showinfo("No pithole", "Road is clear.. No signs of pithole!!!!")
        else:
            messagebox.showerror("Pithole present", "Presence of pithole is found!!!")
            self.register_report()


    def take_image(self):
        window1 = Tk()
        window1.configure(background="lightskyblue1")
        window1.geometry("500x505")
        window1.title("IMAGE CLASSIFICATION")
        emptyLabel200 = Label(window1, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        emptyLabel0 = Label(window1, text="Enter the path for the image to be tested:",
                            font=("Courier", 14), bg="lightskyblue1",
                            fg="purple3")
        emptyLabel0.pack()
        self.path = Entry(window1)
        self.path.pack()

        emptyLabel200 = Label(window1, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        option1 = Button(window1, text="CHECK", activebackground="light yellow", bg="light green", fg="black",
                         command=self.check_for_pithole)
        option1.pack()

        window1.mainloop()


    def popUp(self):
        messagebox.showinfo("FILLED", "Your complaint has been successfully filled.. Action will be taken shortly...")


    def pithole_details(self):
        window1 = Tk()
        window1.configure(background="lightskyblue1")
        window1.geometry("700x505")
        window1.title("Pithole details")
        emptyLabel200 = Label(window1, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        emptyLabel0 = Label(window1, text="Enter the Area:",
                            font=("Courier", 14), bg="lightskyblue1",
                            fg="purple3")
        emptyLabel0.pack()
        self.area = Entry(window1)
        self.area.pack()

        emptyLabel200 = Label(window1, text="", bg="lightskyblue1")
        emptyLabel200.pack()


        emptyLabel0 = Label(window1, text="Enter the City:",
                            font=("Courier", 14), bg="lightskyblue1",
                            fg="purple3")
        emptyLabel0.pack()
        self.city = Entry(window1)
        self.city.pack()



        emptyLabel200 = Label(window1, text="", bg="lightskyblue1")
        emptyLabel200.pack()
        emptyLabel0 = Label(window1, text="Enter the State:",
                            font=("Courier", 14), bg="lightskyblue1",
                            fg="purple3")
        emptyLabel0.pack()
        self.state = Entry(window1)
        self.state.pack()

        emptyLabel200 = Label(window1, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        emptyLabel0 = Label(window1, text="Enter the number of pitholes:",
                            font=("Courier", 14), bg="lightskyblue1",
                            fg="purple3")
        emptyLabel0.pack()
        self.number = Entry(window1)
        self.number.pack()
        emptyLabel200 = Label(window1, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        emptyLabel0 = Label(window1, text="Enter the average diameter of pithole(s)",
                            font=("Courier", 14), bg="lightskyblue1",
                            fg="purple3")
        emptyLabel0.pack()
        self.dia = Entry(window1)
        self.dia.pack()

        emptyLabel200 = Label(window1, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        emptyLabel200 = Label(window1, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        emptyLabel200 = Label(window1, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        option1 = Button(window1, text="FILE COMPLAINT", activebackground="light yellow", bg="light green", fg="black",
                         command=self.entry_in_database)
        option1.pack()

        window1.mainloop()

    def register_report(self):
        window = Tk()
        window.configure(background="lightskyblue1")
        window.geometry("700x505")
        window.title("REGISTER REPORT")

        emptyLabel = Label(window, text="REGISTER REPORT", font=("Courier", 44), bg="lightskyblue1")
        emptyLabel.pack()

        emptyLabel100 = Label(window, text="", bg="lightskyblue1")
        emptyLabel100.pack()
        emptyLabel800 = Label(window, text="", bg="lightskyblue1")
        emptyLabel800.pack()

        emptyLabel0 = Label(window, text="Name of the Complainant:", font=("Courier", 14), bg="lightskyblue1",
                            fg="purple3")
        emptyLabel0.pack()
        emptyLabel800 = Label(window, text="", bg="lightskyblue1")
        emptyLabel800.pack()
        self.name = Entry(window)
        self.name.pack()
        emptyLabel800 = Label(window, text="", bg="lightskyblue1")
        emptyLabel800.pack()

        emptyLabel0 = Label(window, text="Phone number of the Complainant:",
                            font=("Courier", 14), bg="lightskyblue1",
                            fg="purple3")
        emptyLabel0.pack()
        emptyLabel800 = Label(window, text="", bg="lightskyblue1")
        emptyLabel800.pack()
        self.phone = Entry(window)
        self.phone.pack()
        self.phone.insert(0, "+91 ")

        emptyLabel200 = Label(window, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        emptyLabel200 = Label(window, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        option1 = Button(window, text="NEXT", activebackground="light yellow", bg="light green", fg="black",
                         command=self.pithole_details)
        option1.pack()

        window.mainloop()

    def entry_in_database(self):
        report = Report(None, None, None, None, None, None, None)

        # print(self.username.get())
        # print(self.password.get())
        report.name = self.name.get()
        report.phone = self.phone.get()
        report.area = self.area.get()
        report.city = self.city.get()
        report.state = self.state.get()
        report.number = self.number.get()
        report.dia = self.dia.get()

        report.showUserDetails()

        data = report.__dict__

        db.collection("Complaints").document().set(data)

        print(">> ", report.name, "Your complaint has been filled!!!!")

        self.popUp()




r=RegisterReport()
r.take_image()
#
#
