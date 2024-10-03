#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 11:48:38 2024

@author: abayomibuys
"""
import datetime
import csv
data = []
with open("met.csv.txt","r") as sola_press:
    next
    for line in sola_press:
        #Split data into different components
        values_sola = line.split(";")
         
        #Convert date and time
        date_part = values_sola[2]
        date_comp = datetime.datetime.strptime(date_part, "%d.%m.%Y %H:%M")
            
        #convert pressure to readable in python
        pressure_sola = float(values_sola[4].replace(",","."))
        data.append((date_comp, pressure_sola))   
        
        with open("sola_pressure.txt", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date Time', 'Pressure'])
            writer.writerows(data)