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
# from gui import Project

CATEGORIES = ['with', 'without']

# p=Project()


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

    def values_for_dataBase(self, name, phone):
        self.name=name
        self.phone=phone

    def values_for_dataBase1(self, area, city, state, dia, number):

        self.area=area
        self.city=city
        self.state=state
        self.dia=dia
        self.number=number

    def take_path(self, path):
        self.path=path

    def prepare(self, filepath):
        # print(filepath)
        IMG_SIZE = 250
        img_array = cv2.imread("{}".format(filepath), cv2.IMREAD_GRAYSCALE)
        img_array=img_array/255
        # print(img_array)
        new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))

        return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

    

    def popUp(self):
        messagebox.showinfo("FILLED", "Your complaint has been successfully filled.. Action will be taken shortly...")

   

    def entry_in_database(self, name, phone, area, city, state, dia, number):
        report = Report(None, None, None, None, None, None, None)
        
        report.name = name
        report.phone = phone
        report.area = area
        report.city = city
        report.state = state
        report.number = number
        report.dia = dia

        # report.showUserDetails()

        data = report.__dict__

        db.collection("Complaints").document().set(data)

        # print(">> ", report.name, "Your complaint has been filled!!!!")

        self.popUp()
        
# r=RegisterReport()
# r.take_image()

