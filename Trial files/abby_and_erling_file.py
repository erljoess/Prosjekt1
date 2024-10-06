#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 09:19:28 2024

@author: abayomibuys and erljoess
"""
import matplotlib.pyplot as plt
import convert_met_data as cmd                                      # Hentar inn funksjonane frå convert_met_data.py og kallar på dei med cmd.

Sola_data = []
Time_data = []
Sola_data = cmd.convert_Sola_data(Sola_data)                        # Hentar inn data til xxxx_data[] med cmd.convert_xxxx_data(xxxx_data).
Time_data = cmd.convert_Time_data(Time_data)

Sola_bar = []
Sola_temp = []
Sola_temp_min = [00,00,00,00,50]
Sola_temp_max = [00,00,00,00,-50]
Sola_coldest = []
Sola_warmest = []

for linje in Sola_data:                                      
    Sola_bar.append([linje[0], linje[1], linje[2], linje[3], linje[4], linje[5]])   # Legg til yyyy mo dd tt og bar til Sola_bar[].
    Sola_temp.append([linje[0], linje[1], linje[2], linje[3], linje[4], linje[6]])   # Legg til yyyy mo dd tt og temp til Sola_temp[].
    if Sola_temp_min[2] != linje[2]:
        Sola_coldest.append(Sola_temp_min)                                  # Legg til Sola_temp_min i Sola_coldest[], altså det kaldaste i Sola_temp[] siste døgn.
        Sola_warmest.append(Sola_temp_max)                                  # Legg til Sola_temp_max i Sola_warmest[], altså det varmaste i Sola_temp[] siste døgn.
        Sola_temp_min = [linje[0], linje[1], linje[2], linje[3], linje[4], linje[6]]   # Set Sola_temp_min til første temp i nytt døgn.
        Sola_temp_max = [linje[0], linje[1], linje[2], linje[3], linje[4], linje[6]]   # Set Sola_temp_max til første temp i nytt døgn.
    if Sola_temp_min[4] > linje[6]:                                 #Viss registrert temperatur er lågare enn Sola_temp_min, oppdater Sola_temp_min.
        Sola_temp_min = [linje[0], linje[1], linje[2], linje[3], linje[4], linje[6]]
    if Sola_temp_max[4] < linje[6]:                                 #Viss registrert temperatur er høgare enn Sola_temp_max, oppdater Sola_temp_max.
        Sola_temp_max = [linje[0], linje[1], linje[2], linje[3], linje[4], linje[6]]
Sola_coldest.append(Sola_temp_min)
Sola_warmest.append(Sola_temp_max)
Sola_temp_min = None #Fjernar Sola_temp_min[] frå minnet.
Sola_temp_max = None #Fjernar Sola_temp_max[] frå minnet.

Time_bar = []
Time_act = []
Time_temp = []
Time_temp_min = [00,00,00,00,00,00,50]
Time_temp_max = [00,00,00,00,00,00,-50]
Time_coldest = []
Time_warmest = []

for linje in Time_data:                                      
    Time_act.append([linje[0], linje[1], linje[2], linje [3], linje[4], linje[5], linje[7]])   # Legg til yyyy mo dd tt og act til Time_bar[].
    Time_temp.append([linje[0], linje[1], linje[2], linje [3], linje[4], linje[5], linje[8]])   # Legg til yyyy mo dd tt og temp til Time_temp[].
    if linje[6] != -1:
        Time_bar.append([linje[0], linje[1], linje[2], linje [3], linje[4], linje[5], linje[6]])   # Legg til yyyy mo dd tt og bar til Time_bar[].
    if Time_temp_min[2] != linje[2]:
        Time_coldest.append(Time_temp_min)                         # Legg til Time_temp_min i Time_coldest[], altså det kaldaste i Time_temp[] siste døgn.
        Time_warmest.append(Time_temp_max)                         # Legg til Time_temp_max i Time_warmest[], altså det varmaste i Time_temp[] siste døgn.
        Time_temp_min = [linje[0], linje[1], linje[2], linje [3], linje[4], linje[5], linje[8]]   # Set Time_temp_min til første temp i nytt døgn.
        Time_temp_max = [linje[0], linje[1], linje[2], linje [3], linje[4], linje[5], linje[8]]   # Set Time_temp_max til første temp i nytt døgn.
    if Time_temp_min[6] > linje[8]:                                     #Viss registrert temperatur er lågare enn Time_temp_min, oppdater Time_temp_min.
        Time_temp_min = [linje[0], linje[1], linje[2], linje [3], linje[4], linje[5], linje[8]]
    if Time_temp_max[6] < linje[8]:                                     #Viss registrert temperatur er høgare enn Time_temp_max, oppdater Time_temp_max.
        Time_temp_max = [linje[0], linje[1], linje[2], linje [3], linje[4], linje[5], linje[8]]
Time_coldest.append(Time_temp_min)
Time_warmest.append(Time_temp_max)

    #Lagar ein loop for å etablere ei liste med tid og temperatur for den høgaste og lågaste temperaturen i Time_temp[] og Sola_temp[]:
Time_temp_drop = []

for i in range((len(Time_warmest))*2-1):
    if i %2 == 0:
        Time_temp_drop.append(Time_warmest[(int(i/2))])
    elif i %2 == 1:
        Time_temp_drop.append(Time_coldest[(int((i+1)/2))])
Time_coldest = None
Time_warmest = None

    #Lagar ei løkke for å berekne gjennomsnittstemperaturen for dei siste 5 minutta (30 linjer) i Time_act[]:
Time_act_total = []
Time_act_snitt = []

for i, linje in enumerate(Time_data):           #Går gjennom kvar linje i Time_data, og bereknar snitt av dei siste 5 minutta (30 linjer).
    Time_act_total.append(float(linje[7]))
    if linje[6] != -1:
        while len(Time_act_total) > 30:         #For å få rett lengde på gjennomsnitts-berekninga:
            Time_act_total.pop(0)               #Fjernar det eldste elementet i Time_act_total[].
        if i >= 29:                             #Startar berekninga av gjennomsnittet etter 30 linjer.
            Time_act_snitt.append([linje[0], linje[1], linje[2], linje[3], linje[4], linje[5], float(f"{sum(Time_act_total)/30:.2f}")])
Time_act_total = None #Fjernar Time_act_total[] frå minnet.

    #Lagar ei løkke for å berekne gjennomsnittstemperaturen for dei siste 5 minutta i Time_temp[]:
Time_temp_total = []
Time_temp_snitt = []

for i, linje in enumerate(Time_data):           #Går gjennom kvar linje i Time_data, og bereknar snitt av dei siste 5 minutta.
    Time_temp_total.append(float(linje[8]))
    if i % 6 == 0:
        while len(Time_temp_total) > 30:         #For å få rett lengde på gjennomsnitts-berekninga:
            Time_temp_total.pop(0)               #Fjernar det eldste elementet i Time_temp_total[].
        if i >= 29:                              #Igjen; startar berekninga av gjennomsnittet etter 30 linjer.
            Time_temp_snitt.append([linje[0], linje[1], linje[2], linje[3], linje[4], linje[5], float(f"{sum(Time_temp_total)/30:.2f}")]) #Her måtte eg bruke "float" for å ikkje få string?!.
Time_temp_total = None #Fjernar Time_temp_total[] frå minnet.
                                                # Startar arbeidet med plotting
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

                                                # Hentar ut tid og temperatur frå listene
Time_temp_tider = [f"{d[1]:02d}-{d[2]:02d} {d[3]:02d}:{d[4]:02d}" for d in Time_temp]
Time_temps = [d[6] for d in Time_temp]
Time_temp_avg_tider = [f"{d[1]:02d}-{d[2]:02d} {d[3]:02d}:{d[4]:02d}" for d in Time_temp_snitt]
Time_temp_avg = [d[6] for d in Time_temp_snitt]
Time_temp_drop_tider = [f"{d[1]:02d}-{d[2]:02d} {d[3]:02d}:{d[4]:02d}" for d in Time_temp_drop]
Time_temp_drop = Time_temp_drop[2:4]

Sola_tider = [f"{d[1]:2d}-{d[2]:2d} {d[3]:2d} {d[4]:2d}" for d in Sola_temp]
Sola_temps = [d[5] for d in Sola_temp]

                                                # Konverter tid til datetime-objekt
Time_temp_tider = [datetime.datetime(d[0], d[1], d[2], d[3], d[4]) for d in Time_temp]
Time_temp_avg_tider = [datetime.datetime(d[0], d[1], d[2], d[3], d[4]) for d in Time_temp_snitt]
Time_temp_drop_tider = [datetime.datetime(d[0], d[1], d[2], d[3], d[4]) for d in Time_temp_drop]
Time_temp_drop = [d[6] for d in Time_temp_drop]
Sola_tider = [datetime.datetime(d[0], d[1], d[2], d[3], d[4]) for d in Sola_temp]

    #Lagar ein funksjon for å plotte temperaturdata:
def plot_temperature():
        # Opprett bildet og aksen
    fig, ax = plt.subplots(figsize=(10, 6))
        # Plottar dataene
    ax.plot(Time_temp_tider, Time_temps, color="blue", label="Temperature (Time)")
    ax.plot(Time_temp_avg_tider, Time_temp_avg, color="orange", linewidth=0.5, label="Average temperature (Time)")
    ax.plot(Sola_tider, Sola_temps, color="green", label="Temperature (MET)")
    ax.plot(Time_temp_drop_tider, Time_temp_drop, color="red", label='Temperature drop from max til min')
        # Formaterer x-aksen
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m %H:%M'))
    plt.xticks(rotation=45)
        #Set overskrift og aksetitlar, samt plasserer "skiltet" (legend) med desse i der det er best plass
    ax.set_title('Temperature/Date graph')
    ax.set_xlabel('Tid (DD-MM HH:MM)')
    ax.set_ylabel('Temperatur (°C)')
    ax.legend()
    # Vis plottet
    plt.show()

plot_temperature() #Kallar på funksjonen for å plotte temperaturdata.


#    plt.plot(sunset_sunrise, color='black', label='Temperature drop from sunset til sunrise') #Har ikkje henta data til dette.
   
#def plot_pressure():
    
#    plt.plot(act_data_time, color='blue', label='Absolute Pressure')
#    plt.plot(bar_data_time, color='red', label='Barometer pressure')
#    plt.plot(bar_data_met, color='green', label='Absolute pressure Met')
    
    
#    plt.xlabel('Dates')
#    plt.ylabel('Pressure')
#    plt.title('Pressure/Date graph')
#    plt.legend()

#    plt.show()