# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 22:18:20 2024

@author: erljo
"""
Time_data = []
delt_linje =[]

def convert_data():
    with open("time.csv.txt", "r") as fila:
        next(fila)
        data = fila.read()
        for linje in data.split("\n"):
            delt_linje = linje.split(";")
#            print(delt_linje)
            date_time = delt_linje[0].split(" ")
#            print(date_time)
            if len(date_time) == 3:
                date = date_time[0].split("/")
                time = date_time[1].split(":")
#                print(date)
#                print(time)
                if date_time[2] == "am":
                    hh = int(time[0])
                    if hh == 12:
                        hh = 0
                    else:
                        if hh != 12:
                            hh += 12
            else:
                time = date_time[1].split(":")
                date = date_time[0].split(".")
                hh = int(time[0])
            yyyy = int(date[2])
            mo = int(date[0])
            dd = int(date[1])
            mi = int(time[1])
            ss = int(delt_linje[1]) % 60
 #           print(f"{yyyy:04d}-{mo:02d}-{dd:02d} {hh:02d}:{mi:02d}:{ss:02d}")
            bar_p = (delt_linje[2].replace(",", "."))
            if bar_p != "":
                bar_p = 10 * float(bar_p)
            else:
                bar_p = -1
            act_p = (delt_linje[3].replace(",", "."))
            act_p = 10 * float(act_p)
            temp = (delt_linje[4].replace(",", "."))
            temp = float(temp)
#            print(f"{yyyy:04d}-{mo:02d}-{dd:02d} {hh:02d}:{mi:02d}:{ss:02d} {act_p} {temp}")
            Time_data.append([yyyy,mo,dd,hh,mi,ss,bar_p,act_p,temp])


#            date = date_time[0].split("/")
#            time = date_time[1].split(":")
#            print(date)
#            print(time)
#            yyyy = int(date[2])
#            mo = int(date[0])
#            dd = int(date[1])
#            hh = int(time[0])
#            if date_time[2] == "am":
#                if hh == 12:
#                    hh = 0
#            else:
#                if hh != 12:
#                    hh += 12
#            mi = int(time[1])
#            ss = int(delt_linje[1]) % 60
#            print(f"{yyyy:04d}-{mo:02d}-{dd:02d} {hh:02d}:{mi:02d}:{ss:02d}")
#            bar_p = (delt_linje[2].replace(",", "."))
#            if bar_p != "":
#                bar_p = float(bar_p)
#            else:
#                bar_p = -1
#            act_p = (delt_linje[3].replace(",", "."))
#            act_p = float(act_p)
#            temp = (delt_linje[4].replace(",", "."))
#            temp = float(temp)
#            Time_data.append([yyyy,mo,dd,hh,mi,ss,bar_p,act_p,temp])

#    return Time_data

convert_data()
print(Time_data)

#data = "06.12.2021 18:11;100090;;101,055;14,85"

#met_data = []

#delt_linje = data.split(";")

#date_time = delt_linje[0].split(" ")
#date = date_time[0].split(".")
#time = date_time[1].split(":")
#ss = int(delt_linje[1]) % 60

#Time.append(f"{date[2]};{date[1]};{date[0]};{time[0]};{time[1]};{ss};{delt_linje[2]};{delt_linje[3]};{delt_linje[4]}")

#print(Time)