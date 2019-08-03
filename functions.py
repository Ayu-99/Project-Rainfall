from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#119.9	45.6	30.9	55.8	533.9	458.2	317.3	369.6	868.9	209.7	300.5	187.3
#57.8	35.8	134.2	403.4	187.4	645.8	638.9	316	724.9	248.1	22	26.2


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
        s1 = self.stateFirst.get()
        s2 = self.stateSecond.get()
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

        print(values)



        statesShort = ["A&N", "AR", "AS & ML", "NG", "SK", "WB", "OR", "JH", "BH", "E.UP", "W.UP", "UK"
                       , "HR, DL & CH", "PB", "HP", "J&K", "W.RJ", "E.RJ", "W.MP", "E.MP", "GJ", "KCH"
                       , "GOA", "M.MH", "MAT", "VD", "CG", "C.AP", "TG", "RLS", "TN", "C.KA", "N.KA"
                       , "S.KA", "KL", "LD"]

        plt.plot(statesShort, values)
        plt.title("Annual Rainfall in India in {}".format(y))
        plt.xlabel("States")
        plt.ylabel("Annual Rainfall(in mm)")
        plt.show()












