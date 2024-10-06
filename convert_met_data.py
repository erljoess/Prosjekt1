# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 22:18:20 2024

@author: erljo
"""
Time_data = []
Sola_data = []

def convert_Sola_data(Sola_data):
    with open("met.csv.txt", "r") as fila:
        next(fila)
        data = fila.read()
        for linje in data.split("\n"):
            delt_linje = linje.split(";")
            if delt_linje[0] == "Sola":
                date_time = delt_linje[2].split(" ")
                date = date_time[0].split(".")
                time = date_time[1].split(":")
                yyyy = int(date[2])
                mo = int(date[1])
                dd = int(date[0])
                hh = int(time[0])
                mi = 0
                bar_p = (delt_linje[4].replace(",", "."))
                bar_p = float(bar_p)
                temp = (delt_linje[3].replace(",", "."))
                temp = float(temp)
                Sola_data.append([yyyy,mo,dd,hh,mi,bar_p,temp])
        else:
            next
    return Sola_data

def convert_Time_data(Time_data):
    with open("time.csv.txt", "r") as fila:
        next(fila)
        for linje in fila:
            delt_linje = linje.strip().split(";")
            date_time = delt_linje[0].split(" ")
            if len(date_time) == 2:
                date = date_time[0].split(".")
                time = date_time[1].split(":")
                hh = int(time[0])
            elif len(date_time) == 3:
                date = date_time[0].split("/")
                time = date_time[1].split(":")
                if date_time[2] == "am":
                    hh = int(time[0])
                    if hh == 12:
                        hh = 0
                elif date_time[2] == "pm":
                    hh = int(time[0])
                    if hh != 12:
                        hh += 12
            else:
                continue

            yyyy = int(date[2])
            mo = int(date[0])
            dd = int(date[1])
            mi = int(time[1])
            ss = int(delt_linje[1]) % 60
            bar_p = (delt_linje[2].replace(",", "."))
            if bar_p != "":
                bar_p = "{:.2f}".format(10 * float(bar_p))
                bar_p = float(bar_p)
            else:
                bar_p = -1
            act_p = (delt_linje[3].replace(",", "."))
            act_p = "{:.2f}".format(10 * float(act_p))
            act_p = float(act_p)
            temp = (delt_linje[4].replace(",", "."))
            temp = float(temp)
            Time_data.append([yyyy,mo,dd,hh,mi,ss,bar_p,act_p,temp])
    return Time_data

#convert_Time_data(Time_data)
#print(Time_data[:3])
#convert_Sola_data(Sola_data)
#print(Sola_data[:3])

