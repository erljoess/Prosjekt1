#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 09:19:28 2024

@author: abayomibuys
"""
import convert_met_data as cmd                                     # Hentar inn funksjonane frå convert_met_data.py og kallar på dei med cmd.

Sola_data = []
Time_data = []
Sola_data = cmd.convert_Sola_data(Sola_data)                       # Hentar inn data til xxxx_data[] med cmd.convert_xxxx_data(xxxx_data).
Time_data = cmd.convert_Time_data(Time_data)
Sola_data = [dd for dd in Sola_data if dd[2] == 11 or dd[2] == 12] #[ein etter ein av elementa i xxxx_data blir kalla dd, og sjekkar om dd[2] er 11 eller 12.
Time_data = [dd for dd in Time_data if dd[2] == 11 or dd[2] == 12] #I så fall blir heile liste-elementet lagt til i xxxx_data[].
                                                                   #dd kan kallast kva som helst, eg kalte det dd fordi dd[2] er dd i xxxx_data.
Sola_bar = []
Sola_temp = []
Sola_temp_min = []
Sola_temp_max = []
Time_bar_raw = []
Time_bar = []
Time_act = []
Time_temp = []
Sola_temp_min = [00,00,00,00,50]
Sola_temp_max = [00,00,00,00,-50]
Sola_coldest = []
Sola_warmest = []

for linje in Sola_data:                                      # Her er linje litt misvisande, dette er kvart element i Sola_data.
    Sola_bar.append([linje[0], linje[1], linje[2], linje [3], linje[5]])   # Legg til yyyy mo dd tt og bar til Sola_bar[].
    Sola_temp.append([linje[0], linje[1], linje[2], linje[3], linje[6]])   # Legg til yyyy mo dd tt og temp til Sola_temp[].
    if Sola_temp_min[2] != linje[2]:
        Sola_coldest.append(Sola_temp_min)                         # Legg til Sola_temp_min i Sola_coldest[], altså det kaldaste i Sola_temp[] siste døgn.
        Sola_warmest.append(Sola_temp_max)                         # Legg til Sola_temp_max i Sola_warmest[], altså det varmaste i Sola_temp[] siste døgn.
        Sola_temp_min = [linje[0], linje[1], linje[2], linje[6]]   # Set Sola_temp_min til første temp i nytt døgn.
        Sola_temp_max = [linje[0], linje[1], linje[2], linje[6]]   # Set Sola_temp_max til første temp i nytt døgn.
    if Sola_temp_min[3] < linje[6]:
        Sola_temp_min[3] = linje[6]
    if Sola_temp_max[3] > linje[6]:
        Sola_temp_max[3] = linje[6]
Sola_coldest.append(Sola_temp_min)
Sola_warmest.append(Sola_temp_max)
    
print(Sola_coldest)
print(Sola_warmest)
#print(type(Sola_temp_min[3]))
#print(type(Sola_temp_max[3]))
print(Sola_temp_min)
print(Sola_temp_max)
#print(Sola_bar[:2])
#print(Sola_temp[:2])

for linje in Time_data:
    Time_bar_raw.append([linje[2], linje[3], linje[4], linje[6]])
    Time_act.append([linje[2], linje[3], linje[4], linje[7]])
    Time_temp.append([linje[2], linje[3], linje[4], linje[8]])
for linje in Time_bar_raw:
    if linje[3] != -1:
        Time_bar.append(linje)
Time_bar_raw = None                                               #Fjernar Time_bar_raw for å spare minne.
    
#Sjekk av innhald i listene:
#for i in Sola_data[:3]:
#    print(i)
#for linje in range(6):
#    print(Sola_data[linje])
#    print(Sola_bar[linje])
#    print(Sola_temp[linje])
#    print(Time_data[linje])
#    print(Time_bar_raw[linje])
#    print(Time_bar[linje])
#    print(Time_act[linje])
#    print(Time_temp[linje])

def temp_drop():
    sunset_sunrise = []
    for line in Time_temp:
        yyyy, mo, dd, hh, mm, bar, temperature = line
        if (yyyy== 2021 and mo== 6 and dd==11 and hh==17):
            sunset_sunrise.append(temperature)

        if (yyyy== 2021 and mo==6 and dd==11 and hh==17):
            sunset_sunrise.append(temperature)

import matplotlib.pyplot as plt
import numpy as np

def plot_temperature():
    
    plt.plot(Time_temp, color='blue', label='Temperature')
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