# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 22:18:20 2024

@author: erljo
"""
Sola_data = []
delt_linje =[]

def convert_Sola_data():
    with open("test.csv.txt", "r") as fila:
        next(fila)
        data = fila.read()
        for linje in data.split("\n"):
            delt_linje = linje.split(";")
            print(delt_linje)
            date_time = delt_linje[2].split(" ")
#            print(date_time)
            date = date_time[0].split(".")
            time = date_time[1].split(":")
#            print(date)
#            print(time)
            yyyy = int(date[2])
            mo = int(date[1])
            dd = int(date[0])
            hh = int(time[0])
            mi = int(time[1])
#            print(f"{yyyy:04d}-{mo:02d}-{dd:02d} {hh:02d}:{mi:02d}")
            bar_p = (delt_linje[4].replace(",", "."))
            temp = (delt_linje[3].replace(",", "."))
            temp = float(temp)
            Sola_data.append([yyyy,mo,dd,hh,mi,bar_p,temp])
    return Sola_data

convert_Sola_data()
print(Sola_data)

#data = "06.12.2021 18:11;100090;;101,055;14,85"

#met_data = []

#delt_linje = data.split(";")

#date_time = delt_linje[0].split(" ")
#date = date_time[0].split(".")
#time = date_time[1].split(":")
#ss = int(delt_linje[1]) % 60

#Time.append(f"{date[2]};{date[1]};{date[0]};{time[0]};{time[1]};{ss};{delt_linje[2]};{delt_linje[3]};{delt_linje[4]}")

#print(Time)