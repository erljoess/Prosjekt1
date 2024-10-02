# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 22:18:20 2024

@author: erljo
"""
Time = []

def convert data(filename):
    with open(filename, "r") as file:
       next(file)
        data = file.read()

        for line in data.split("\n"):
            part = line.split(";")
            date_time = part[0].split(" ")
            date = date_time[0].split(".")
            time = date_time[1].split(":")
            seconds = int(part[1]) % 60
            Time.append(f"{date[2]};{date[1]};{date[0]};{time[0]};{time[1]};{seconds};{part[2]};{part[3]};{part[4]}")
    return Time

data = "06.12.2021 18:11;100090;;101,055;14,85"

Time = []

part = data.split(";")

date_time = part[0].split(" ")
date = date_time[0].split(".")
time = date_time[1].split(":")
seconds = int(part[1]) % 60

Time.append(f"{date[2]};{date[1]};{date[0]};{time[0]};{time[1]};{seconds};{part[2]};{part[3]};{part[4]}")

print(Time)