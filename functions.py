from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#119.9	45.6	30.9	55.8	533.9	458.2	317.3	369.6	868.9	209.7	300.5	187.3
#57.8	35.8	134.2	403.4	187.4	645.8	638.9	316	724.9	248.1	22	26.2


states = {"Andaman & Nicobar Islands":0, "Arunachal Pradesh":1, "Assam & Meghalaya":2, "Naga Mani Mizo Tripura":3,
          "Sub Himalayan West Bengal & Sikkim":4}
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
        s = self.state.get()
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

        # statesFinal = rainfall.SUBDIVISION
        # print(statesFinal)
        # statesF = []
        # for i in range(len(statesFinal)):
        #     statesF.append(statesFinal[i][1])
        #
        #
        # print(statesF)
        # idx=statesFinal.index('Arunachal Pradesh')
        # print(idx)



