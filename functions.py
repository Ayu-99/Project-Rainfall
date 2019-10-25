from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from  sklearn import tree
import numpy as np
from tkinter import messagebox
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


#119.9	45.6	30.9	55.8	533.9	458.2	317.3	369.6	868.9	209.7	300.5	187.3
#57.8	35.8
# 134.2	403.4	187.4	645.8	638.9	316	724.9	248.1	22	26.2


states = {"ANDAMAN & NICOBAR ISLANDS":0, "ARUNACHAL PRADESH":1, "ASSAM & MEGHALAYA":2, "NAGA MANI MIZO TRIPURA":3,
          "SUB HIMALAYAN WEST BENGAL & SIKKIM":4, "GANGETIC WEST BENGAL":5, "ORISSA":6, "JHARKHAND":7,
          "BIHAR":8, "EAST UTTAR PRADESH":9, "WEST UTTAR PRADESH":10, "UTTARAKHAND":11, "HARYANA, DELHI AND CHANDIGARH":12,
          "PUNJAB":13, "HIMACHAL PRADESH":14, "JAMMU & KASHMIR":15, "WEST RAJASTHAN":16, "EAST RAJASTHAN":17,
          "WEST MADHYA PRADESH":18, "EAST MADHYA PRADESH":19, "GUJARAT":20, "SAURASHTRA & KUTCH":21,
          "KONKAN & GOA":22, "MADHYA MAHARASHTRA":23, "MATATHWADA":24, "VIDARBHA":25, "CHATTISGARH":26,
          "COASTAL ANDHRA PRADESH":27, "TELENGANA":28, "RAYALSEEMA":29, "TAMIL NADU":30,
          "COASTAL KARNATKA":28, "NORTH INTERIOR KARNATKA":29, "SOUTH INTERIOR KARNATKA":30,
          "KERALA":31, "LAKSHADWEEP":32}





year = {'2000':0, '2001':1, '2002':2, '2003':3, '2004':4, '2005':5, '2006':6, '2007':7, '2008':8, '2009'
:9, '2010':10, '2011':11, '2012':
            12, '2013':13, '2014':14, '2015':15, '2016':16, '2017':17}

class DataRainfall:

    def oneState(self):

        window = Tk()

        window.configure(background="lightskyblue1")
        window.geometry("500x405")
        window.title("One State")

        stateLabel = Label(window, text="Enter the state", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        stateLabel.pack()
        self.state= Entry(window)
        self.state.pack()

        emptyLabel200 = Label(window, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        yearLabel = Label(window, text="Enter the Year", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        yearLabel.pack()
        self.year = Entry(window)
        self.year.pack()

        btnShow = Button(window, text="Show", activebackground="light yellow", bg="light green", fg="black",
                         command= self.state1)
        btnShow.pack()


        window.mainloop()

    def state1(self):
        # print("hello")

        y = self.year.get()
        s = self.state.get().upper()
        # print(s)
        # print(y)

        #print(s)
        stateNo = states[s]

        monthValues = []
        #print(y)
        yearNo = year[y]

        rainfall = pd.read_csv("r.csv")
        # print(rainfall)

        jan = rainfall.JAN
        jans=[]

        for i in range(stateNo*18, stateNo*18+18):

            jans.append(jan[i])

        # print(jans)
        monthValues.append(jans[yearNo])

        feb = rainfall.FEB
        febs = []
        for i in range(stateNo*18, stateNo*18+18):

            febs.append(feb[i])

        monthValues.append(febs[yearNo])

        mar = rainfall.MAR
        mars=[]
        for i in range(stateNo*18, stateNo*18+18):

            mars.append(mar[i])

        monthValues.append(mars[yearNo])

        apr = rainfall.APR
        aprs=[]
        for i in range(stateNo*18, stateNo*18+18):

            aprs.append(apr[i])
        monthValues.append(aprs[yearNo])

        may = rainfall.MAY
        mays=[]
        for i in range(stateNo*18, stateNo*18+18):

            mays.append(may[i])
        monthValues.append(mays[yearNo])

        jun = rainfall.JUN
        juns=[]
        for i in range(stateNo*18, stateNo*18+18):

            juns.append(jun[i])
        monthValues.append(juns[yearNo])

        jul = rainfall.JUL
        juls=[]
        for i in range(stateNo*18, stateNo*18+18):

            juls.append(jul[i])
        monthValues.append(juls[yearNo])

        aug = rainfall.AUG
        augs=[]
        for i in range(stateNo*18, stateNo*18+18):

            augs.append(aug[i])
        monthValues.append(augs[yearNo])

        sep = rainfall.SEP
        seps=[]
        for i in range(stateNo*18, stateNo*18+18):

            seps.append(sep[i])
        monthValues.append(seps[yearNo])

        oct = rainfall.OCT
        octs=[]
        for i in range(stateNo*18, stateNo*18+18):

            octs.append(oct[i])
        monthValues.append(octs[yearNo])

        nov = rainfall.NOV
        novs=[]
        for i in range(stateNo*18, stateNo*18+18):

            novs.append(nov[i])
        monthValues.append(novs[yearNo])

        dec = rainfall.DEC
        decs=[]
        for i in range(stateNo*18, stateNo*18+18):

            decs.append(dec[i])
        monthValues.append(decs[yearNo])
        #
        # print((jans[yearNo], feb[yearNo], mar[yearNo], apr[yearNo], may[yearNo], jun[yearNo], jul[yearNo]
        #       , aug[yearNo], sep[yearNo], oct[yearNo], nov[yearNo], dec[yearNo]))
        #
        # print(jans[yearNo], febs[yearNo], mars[yearNo], aprs[yearNo], mays[yearNo], jun[yearNo], jul[yearNo]
        #       , aug[yearNo], sep[yearNo], oct[yearNo], nov[yearNo], dec[yearNo])


        # print(monthValues)

        months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

        # plt.plot(months, monthValues)
        # plt.xlabel("Months")
        # plt.ylabel("rainfall(in mm)")
        # plt.show()

        ax = sns.lineplot(months, monthValues)
        ax.set(xlabel='Months', ylabel='Rainfall(in mm)')
        plt.title("Rainfall Stats in {} in {}".format(s, y))
        plt.show()


    def twoStates(self):
        window = Tk()

        window.configure(background="lightskyblue1")
        window.geometry("500x405")
        window.title("One State")

        stateLabel1 = Label(window, text="Enter the state 1", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        stateLabel1.pack()
        self.stateFirst = Entry(window)
        self.stateFirst.pack()

        emptyLabel200 = Label(window, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        stateLabel2 = Label(window, text="Enter the state 2", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        stateLabel2.pack()
        self.stateSecond = Entry(window)
        self.stateSecond.pack()

        emptyLabel300 = Label(window, text="", bg="lightskyblue1")
        emptyLabel300.pack()

        yearLabel = Label(window, text="Enter the Year", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        yearLabel.pack()
        self.year = Entry(window)
        self.year.pack()

        btnShow = Button(window, text="Show", activebackground="light yellow", bg="light green", fg="black",
                         command=self.state2)
        btnShow.pack()

        window.mainloop()



    def state2(self):
        s1 = self.stateFirst.get().upper()
        s2 = self.stateSecond.get().upper()
        y = self.year.get()

        # print(s1)
        # print(s2)
        # print(y)

        stateNo1 = states[s1]
        stateNo2 = states[s2]
        yearNo = year[y]
        monthValues1 = []

        rainfall = pd.read_csv("r.csv")
        # print(rainfall)

        jan = rainfall.JAN
        jans1 = []

        for i in range(stateNo1 * 18, stateNo1 * 18 + 18):
            jans1.append(jan[i])

        # print(jans)
        monthValues1.append(jans1[yearNo])

        feb = rainfall.FEB
        febs1 = []
        for i in range(stateNo1 * 18, stateNo1 * 18 + 18):
            febs1.append(feb[i])

        monthValues1.append(febs1[yearNo])

        mar = rainfall.MAR
        mars1 = []
        for i in range(stateNo1 * 18, stateNo1 * 18 + 18):
            mars1.append(mar[i])

        monthValues1.append(mars1[yearNo])

        apr = rainfall.APR
        aprs1 = []
        for i in range(stateNo1 * 18, stateNo1 * 18 + 18):
            aprs1.append(apr[i])
        monthValues1.append(aprs1[yearNo])

        may = rainfall.MAY
        mays1 = []
        for i in range(stateNo1 * 18, stateNo1 * 18 + 18):
            mays1.append(may[i])
        monthValues1.append(mays1[yearNo])

        jun = rainfall.JUN
        juns1 = []
        for i in range(stateNo1 * 18, stateNo1 * 18 + 18):
            juns1.append(jun[i])
        monthValues1.append(juns1[yearNo])

        jul = rainfall.JUL
        juls1 = []
        for i in range(stateNo1 * 18, stateNo1 * 18 + 18):
            juls1.append(jul[i])
        monthValues1.append(juls1[yearNo])

        aug = rainfall.AUG
        augs1 = []
        for i in range(stateNo1 * 18, stateNo1 * 18 + 18):
            augs1.append(aug[i])
        monthValues1.append(augs1[yearNo])

        sep = rainfall.SEP
        seps1 = []
        for i in range(stateNo1 * 18, stateNo1 * 18 + 18):
            seps1.append(sep[i])
        monthValues1.append(seps1[yearNo])

        oct = rainfall.OCT
        octs1 = []
        for i in range(stateNo1 * 18, stateNo1 * 18 + 18):
            octs1.append(oct[i])
        monthValues1.append(octs1[yearNo])

        nov = rainfall.NOV
        novs1 = []
        for i in range(stateNo1 * 18, stateNo1 * 18 + 18):
            novs1.append(nov[i])
        monthValues1.append(novs1[yearNo])

        dec = rainfall.DEC
        decs1 = []
        for i in range(stateNo1 * 18, stateNo1 * 18 + 18):
            decs1.append(dec[i])
        monthValues1.append(decs1[yearNo])

        # print(rainfall)
        monthValues2 = []

        jan = rainfall.JAN
        jans2 = []

        for i in range(stateNo2 * 18, stateNo2 * 18 + 18):
            jans2.append(jan[i])

        # print(jans)
        monthValues2.append(jans2[yearNo])

        feb = rainfall.FEB
        febs2 = []
        for i in range(stateNo2 * 18, stateNo2 * 18 + 18):
            febs2.append(feb[i])

        monthValues2.append(febs2[yearNo])

        mar = rainfall.MAR
        mars2 = []
        for i in range(stateNo2 * 18, stateNo2 * 18 + 18):
            mars2.append(mar[i])

        monthValues2.append(mars2[yearNo])

        apr = rainfall.APR
        aprs2 = []
        for i in range(stateNo2 * 18, stateNo2 * 18 + 18):
            aprs2.append(apr[i])
        monthValues2.append(aprs2[yearNo])

        may = rainfall.MAY
        mays2 = []
        for i in range(stateNo2 * 18, stateNo2 * 18 + 18):
            mays2.append(may[i])
        monthValues2.append(mays2[yearNo])

        jun = rainfall.JUN
        juns2 = []
        for i in range(stateNo2 * 18, stateNo2 * 18 + 18):
            juns2.append(jun[i])
        monthValues2.append(juns2[yearNo])

        jul = rainfall.JUL
        juls2 = []
        for i in range(stateNo2 * 18, stateNo2 * 18 + 18):
            juls2.append(jul[i])
        monthValues2.append(juls2[yearNo])

        aug = rainfall.AUG
        augs2 = []
        for i in range(stateNo2 * 18, stateNo2 * 18 + 18):
            augs2.append(aug[i])
        monthValues2.append(augs2[yearNo])

        sep = rainfall.SEP
        seps2 = []
        for i in range(stateNo2 * 18, stateNo2 * 18 + 18):
            seps2.append(sep[i])
        monthValues2.append(seps2[yearNo])

        oct = rainfall.OCT
        octs2 = []
        for i in range(stateNo2 * 18, stateNo2 * 18 + 18):
            octs2.append(oct[i])
        monthValues2.append(octs2[yearNo])

        nov = rainfall.NOV
        novs2 = []
        for i in range(stateNo2 * 18, stateNo2 * 18 + 18):
            novs2.append(nov[i])
        monthValues2.append(novs2[yearNo])

        dec = rainfall.DEC
        decs2 = []
        for i in range(stateNo2 * 18, stateNo2 * 18 + 18):
            decs2.append(dec[i])
        monthValues2.append(decs2[yearNo])



        months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

        plt.title("Rainfall in {} and {} in {}".format(s1,s2,y))
        plt.plot(months, monthValues1, label='{}'.format(s1))
        plt.plot(months, monthValues2, label='{}'.format(s2))
        plt.legend(loc='best')
        plt.xlabel("Months")
        plt.ylabel("rainfall(in mm)")
        plt.show()






    def indiaSpecificYear(self):

        window = Tk()

        window.configure(background="lightskyblue1")
        window.geometry("500x405")
        window.title("One State")

        yearLabel = Label(window, text="Enter the Year", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        yearLabel.pack()
        self.year = Entry(window)
        self.year.pack()

        emptyLabel200 = Label(window, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        btnShow = Button(window, text="Show", activebackground="light yellow", bg="light green", fg="black",
                         command=self.india1)
        btnShow.pack()

        window.mainloop()


    def india1(self):
        # print("hello")
        rainfall = pd.read_csv("r.csv")
        # print(rainfall)
        annualRainfall = rainfall.ANNUAL
        # print(annualRainfall)
        y = self.year.get()
        yearNo = year[y]

        values = []
        i = yearNo
        while i<len(annualRainfall):
            values.append(annualRainfall[i])
            i=i+18

        # print(values)



        statesShort = ["A&N", "AR", "AS & ML", "NG", "SK", "WB", "OR", "JH", "BH", "E.UP", "W.UP", "UK"
                       , "HR, DL & CH", "PB", "HP", "J&K", "W.RJ", "E.RJ", "W.MP", "E.MP", "GJ", "KCH"
                       , "GOA", "M.MH", "MAT", "VD", "CG", "C.AP", "TG", "RLS", "TN", "C.KA", "N.KA"
                       , "S.KA", "KL", "LD"]

        plt.plot(statesShort, values)
        plt.title("Annual Rainfall in India in {}".format(y))
        plt.xlabel("States")
        plt.ylabel("Annual Rainfall(in mm)")
        plt.show()

    def indiaSpecific2Years(self):
        window = Tk()

        window.configure(background="lightskyblue1")
        window.geometry("500x405")
        window.title("One State")

        yearLabel1 = Label(window, text="Enter the Year 1", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        yearLabel1.pack()
        self.year1 = Entry(window)
        self.year1.pack()

        emptyLabel200 = Label(window, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        yearLabel2 = Label(window, text="Enter the Year 2", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        yearLabel2.pack()
        self.year2 = Entry(window)
        self.year2.pack()

        emptyLabel300 = Label(window, text="", bg="lightskyblue1")
        emptyLabel300.pack()

        btnShow = Button(window, text="Show", activebackground="light yellow", bg="light green", fg="black",
                         command=self.india2)
        btnShow.pack()

        window.mainloop()



    def india2(self):
        # print("hello")
        y1 = self.year1.get()
        y2 = self.year2.get()

        rainfall = pd.read_csv("r.csv")
        annualRainfall = rainfall.ANNUAL
        yearNo1 = year[y1]
        yearNo2 = year[y2]



        values1 = []
        values2 = []
        i1 = yearNo1
        while i1 < len(annualRainfall):
            values1.append(annualRainfall[i1])
            i1 = i1 + 18

        # print(values1)


        i2 = yearNo2
        while i2 < len(annualRainfall):
            values2.append(annualRainfall[i2])
            i2 = i2 + 18

        # print(values2)

        statesShort = ["A&N", "AR", "AS & ML", "NG", "SK", "WB", "OR", "JH", "BH", "E.UP", "W.UP", "UK"
            , "HR, DL & CH", "PB", "HP", "J&K", "W.RJ", "E.RJ", "W.MP", "E.MP", "GJ", "KCH"
            , "GOA", "M.MH", "MAT", "VD", "CG", "C.AP", "TG", "RLS", "TN", "C.KA", "N.KA"
            , "S.KA", "KL", "LD"]

        plt.plot(statesShort, values1, label='Rainfall in {}'.format(y1))
        plt.plot(statesShort, values2, label='Rainfall in {}'.format(y2))
        plt.title("Comparison of Annual Rainfall in India in {} and {}".format(y1, y2))
        plt.legend(loc='best')
        plt.title("Annual Rainfall in India in {} and {}".format(y1, y2))
        plt.xlabel("States")
        plt.ylabel("Annual Rainfall(in mm)")
        plt.show()


    def Classify(self):
        window = Tk()

        window.configure(background="lightskyblue1")
        window.geometry("500x405")
        window.title("Data Classification")



        emptyLabel200 = Label(window, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        stateLabel = Label(window, text="Enter the State", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        stateLabel.pack()
        self.state = Entry(window)
        self.state.pack()

        emptyLabel300 = Label(window, text="", bg="lightskyblue1")
        emptyLabel300.pack()

        btnShow = Button(window, text="Classify", activebackground="light yellow", bg="light green", fg="black",
                         command=self.classifyState)
        btnShow.pack()

        window.mainloop()



    def classifyState(self):
        # print("hello")

        y = self.state.get().upper()
        # print(y)
        content = pd.read_csv("averageRainfall.csv")

        data = content.ANNUAL.values

        stateNo = states[y]
        value = data[stateNo]
        # print(value)
        # print(data)

        # print("**********************************************************************")
        data = data.reshape(len(data), 1)
        # print(data)

        labels = content.LABELS.values
        # print(labels)

        # print("**********************************************************************")
        labels = labels.reshape(len(labels), 1)
        # print(labels)

        model = tree.DecisionTreeClassifier()
        model.fit(data, labels)


        # print(stateNo)
        inputData = [value]
        # print(inputData)
        predictedClass = model.predict([inputData])
        # print("**", predictedClass)
        if predictedClass[0] == 0:
            # window = Tk()
            # window.config(background="lightskyblue1")
            # window.title("Classification")
            # window.geometry("500x405")
            # #
            # heavyStateLabel = Label(window, text="Heavy Rainfall State !!", font=("Courier", 14), bg="lightskyblue1", fg="purple3" )
            # heavyStateLabel.pack()

            messagebox.showwarning("Heavy Alert", "Heavy Rainfall State !!")

        elif predictedClass[0] == 1:
            messagebox.showwarning("Alert", "Medium Rainfall State !!")

        else:
            messagebox.showinfo("Info", "Less Rainfall State !!")





    def regression(self):
        window = Tk()

        window.configure(background="lightskyblue1")
        window.geometry("500x405")
        window.title("Prediction")

        emptyLabel200 = Label(window, text="", bg="lightskyblue1")
        emptyLabel200.pack()

        stateLabel = Label(window, text="Enter the State", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        stateLabel.pack()
        self.state = Entry(window)
        self.state.pack()

        emptyLabel300 = Label(window, text="", bg="lightskyblue1")
        emptyLabel300.pack()


        yearLabel = Label(window, text="Prediction Year", font=("Courier", 14), bg="lightskyblue1", fg="purple3")
        yearLabel.pack()
        self.year = Entry(window)
        self.year.pack()

        emptyLabel400 = Label(window, text="", bg="lightskyblue1")
        emptyLabel400.pack()

        btnShow = Button(window, text="Predict", activebackground="light yellow", bg="light green", fg="black",
                         command=self.predict)
        btnShow.pack()

        window.mainloop()



    def predict(self):
        state = self.state.get().upper()
        # print(state)
        y1 = self.year.get()
        # print(year)

        stateNo = states[state]
        # print(stateNo)

        rainfall = pd.read_csv("r.csv")

        values = rainfall.ANNUAL
        annual = []
        for i in range(stateNo * 18, stateNo * 18 + 18):
            annual.append(values[i])

        # print(values1)

        # annual = np.array([values1])
        # print(annual)

        annual1 = np.array(annual)
        yearValues = rainfall.YEAR
        year = []
        for i in range(stateNo * 18, stateNo * 18 + 18):
            year.append(yearValues[i])



        # print(yearValues1)
        # year = np.array([yearValues1])
        print(year)
        year1 = np.array(year)

        annual_train = annual1[:11]

        annual_train = annual_train.reshape(len(annual_train), 1)


        # print(annual_train)
        # print(len(annual_train))

        annual_test = annual1[11:]
        annual_test = annual_test.reshape(len(annual_test), 1)

        # print(annual_test)
        # print(len(annual_test))

        year_train = year1[:11]
        year_test = year1[11:]

        year_train = year_train.reshape(len(year_train), 1)
        year_test = year_test.reshape(len(year_test), 1)

        # print(year_train)
        # print(len(year_train))
        # print(year_test)
        # print(len(year_test))

        model = linear_model.LinearRegression()

        model.fit(year_train, annual_train)

        prediction = model.predict(year_train)

        score = r2_score(annual_train, prediction)
        print(score)

        b1 = model.coef_
        # print(b1)

        plt.scatter(year_train, annual_train, color='black')
        plt.plot(year_train, prediction, color='blue', linewidth=3)
        # plt.show()
        #

        y2 = int(y1)
        # print(y2)
        # print(type(y2))
        y = model.predict([[y2]])
        print(y)

        if y[0][0] < 1000:
            messagebox.showinfo("Low Rainfall", "Predicted Rainfall is:{} for year:{} ".format(round(y[0][0],2), y2))

        elif 1000 <= y[0][0] <= 2000:
            messagebox.showwarning("Heavy Rainfall", "Predicted Rainfall is:{} for year:{}".format(round(y[0][0],2),y2))

        else:
            messagebox.showwarning("ThunderStorm", "Predicted Rainfall is:{} for year:{}".format(round(y[0][0],2), y2))



    def imageClassify(self):
        print("Hello")



