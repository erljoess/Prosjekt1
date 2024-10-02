# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 22:18:20 2024

@author: erljo
"""

data = "06/13/2021 10:31:08 pm;202080;101,91;101,315;13,93"

Time = []

part = data.split(";")

date_time = part[0].split(" ")
date = date_time[0].split(".")
time = date_time[1].split(":")
seconds = int(part[1]) % 60

Time.append(f"{date[2]};{date[1]};{date[0]};{time[0]};{time[1]};{seconds};{part[2]};{part[3]};{part[4]}")

print(Time)