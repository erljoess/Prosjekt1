# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 22:18:20 2024

@author: erljo
"""
met_data = []

def convert_data():
    with open("test.csv.txt", "r") as fila:
        next(fila)
        data = fila.read()
        for linje in data.split("\n"):
            delt_linje = linje.split(";")
            date_time = delt_linje[0].split(" ")
            print(delt_linje)
            print(date_time)
            time = date_time[1].split(":")
            date = date_time[0].split(".")
            yyyy = int(date[2])
            mo = int(date[0])
            dd = int(date[1])
            hh = int(time[0])
            mi = int(time[1])
            ss = int(delt_linje[1]) % 60
            bar_p = (delt_linje[2].replace(",", "."))
            if bar_p != "":
                bar_p = float(bar_p)
            else:
                bar_p = -1
            act_p = (delt_linje[3].replace(",", "."))
            act_p = float(act_p)
            temp = (delt_linje[4].replace(",", "."))
            temp = float(temp)
            met_data.append([yyyy,mo,dd,hh,mi,ss,bar_p,act_p,temp])
    return met_data

convert_data()
print(met_data)

#data = "06.12.2021 18:11;100090;;101,055;14,85"

#met_data = []

#delt_linje = data.split(";")

#date_time = delt_linje[0].split(" ")
#date = date_time[0].split(".")
#time = date_time[1].split(":")
#ss = int(delt_linje[1]) % 60

#Time.append(f"{date[2]};{date[1]};{date[0]};{time[0]};{time[1]};{ss};{delt_linje[2]};{delt_linje[3]};{delt_linje[4]}")

#print(Time)