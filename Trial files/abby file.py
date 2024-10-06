#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 09:19:28 2024

@author: abayomibuys
"""



def temp_drop():
    sunset_sunrise = []
    for line in temp_data_time:
        yyyy, mo, dd, hh, mm, bar, temperature = line
        if (yyyy== 2021 and mo== 6 and dd==11 and hh==17):
            sunset_sunrise.append(temperature)

        if (yyyy== 2021 and mo==6 and dd==11 and hh==17):
            sunset_sunrise.append(temperature)
            
    







import matplotlib.pyplot as plt
import numpy as np

def plot_temperature():
    
    plt.plot(temp_data_time, color='blue', label='Temperature')
#    plt.plot(......., color='red', label='Average Temperature')
    plt.plot(temp_data_met, color='green', label='Temperature Met')
    plt.plot(sunset_sunrise, color='black', label='Temperature drop from sunset til sunrise')
 #   plt.plot(..........., color='red', label='Temperature drop from max til min')
    
    
    plt.xlabel('Dates')
    plt.ylabel('Temperature')
    plt.title('Temperature/Date graph')
    plt.legend()

    plt.show()
    
def plot_pressure():
    
    plt.plot(act_data_time, color='blue', label='Absolute Pressure')
    plt.plot(bar_data_time, color='red', label='Barometer pressure')
    plt.plot(bar_data_met, color='green', label='Absolute pressure Met')
    
    
    plt.xlabel('Dates')
    plt.ylabel('Pressure')
    plt.title('Pressure/Date graph')
    plt.legend()

    plt.show()