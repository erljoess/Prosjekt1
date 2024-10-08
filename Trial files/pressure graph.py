#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:23:25 2024

@author: abayomibuys
"""

import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


sola_date_pressure = []

with open("met.csv.txt","r") as sola_temp:
    for line in sola_temp:
        try:
        #Split data into different components
            values_sola = line.split(";")
         
        #Convert date and time
            date_part = values_sola[2]
            date_time = datetime.datetime.strptime(date_part, "%d.%m.%Y %H:%M")
           
            
        #convert pressure to readable in python
            pressure_sola = float(values_sola[4].replace(",","."))
           
        except(ValueError):
            continue
        
        sola_date_pressure.append((date_time, pressure_sola))
            #print(sola_date_pressure)

date_press = np.array(sola_date_pressure)
date_met = date_press[:,0]
pressure = date_press[:,1]


data_abs_press = []
with open("time.csv.txt","r") as met_pressure:
    for line in met_pressure:
       try: 
       #Split data into different components
            values_met = line.split(";")
         
        #Convert date and time
            date_part = values_met[0]
            second_part = values_met[1]
            date_comp = datetime.datetime.strptime(date_part, "%m.%d.%Y %H:%M")
       except(ValueError):
            continue
        
       pressure_met = float(values_met[3].replace(",","."))
       pressure_adj = pressure_met*10
       data_abs_press.append((date_comp, pressure_adj))   
       #print(date_comp, pressure_adj)
            
       
date_abs_press = np.array(data_abs_press)
date_met_2 = date_abs_press[:,0]
abs_pressure = date_abs_press[:,1]      

data = []

with open("time.csv.txt","r") as met_pressure:
    for line in met_pressure:
        try:
            values_met = line.split(";")            #Split data into different components
            barometer_val = float(values_met[2].replace(",","."))  
            if values_met[2] != "":
           #convert pressure to readable in python
                 barometer_adj = barometer_val*10
                                        
        #Convert date and time
            date_part = values_met[0]
            date_comp = datetime.datetime.strptime(date_part, "%m.%d.%Y %H:%M")
        except(ValueError):
                continue
        data.append((date_comp, barometer_adj)) 
        #print(date_comp, barometer_adj)
        
       

date_barometer = np.array(data)
date_time = date_barometer[:,0]
barometer = date_barometer[:,1]  

def plot_pressure_graph():
   
    fig, ax = plt.subplots(figsize=(20, 6)) 

    
    ax.plot(date_met, pressure, color="red", label ="Absolute Pressure MET")
    ax.plot(date_met_2, abs_pressure, color="blue", label ="Absolute Pressure")
    ax.plot(date_time, barometer, color="black", label ="Barometer")

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m %H:%M'))  
    ax.set_xlabel('Dates')
    ax.set_ylabel('Pressure')
    ax.set_ylim(1000,1025)
    #ax.set_yticks(range(1000,1025,2.5))
    ax.set_title('Pressure/Date graph')
    ax.legend()

    plt.show()



plot_pressure_graph()






