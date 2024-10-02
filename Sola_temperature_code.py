#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 12:38:14 2024

@author: abayomibuys
"""

import datetime
import csv
data = []
with open("test_data.txt","r") as sola_temp:
    for line in sola_temp:
        #Split data into different components
        values_sola = line.split(";")
         
        #Convert date and time
        date_part = values_sola[2]
        date_comp = datetime.datetime.strptime(date_part, "%d.%m.%Y %H:%M")
            
        #convert pressure to readable in python
        temperature_sola = float(values_sola[3].replace(",","."))
        data.append((date_comp, temperature_sola))   
        
        with open("sola_pressure.txt", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date Time', 'Temperature'])
            writer.writerows(data)