#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 09:19:28 2024

@author: abayomibuys and erljoess
"""

import convert_met_data as cmd                                      # Hentar inn funksjonane frå convert_met_data.py og kallar på dei med cmd.

Sola_data = []
Sola_data = cmd.convert_Sola_data(Sola_data)                        # Hentar inn data til Sola_data[].

Time_data = []
Time_data = cmd.convert_Time_data(Time_data)                        # Hentar inn data til Time_data[].

Time_temp_min = [00,00,00,00,00,00,50]
Time_temp_max = [00,00,00,00,00,00,-50]
Time_coldest = []
Time_warmest = []

for linje in Time_data:
    if Time_temp_min[2] != linje[2]:
        Time_coldest.append(Time_temp_min)                         # Legg til Time_temp_min i Time_coldest[], altså det kaldaste i Time_temp[] siste døgn.
        Time_warmest.append(Time_temp_max)                         # Legg til Time_temp_max i Time_warmest[], altså det varmaste i Time_temp[] siste døgn.
        Time_temp_min = [linje[0], linje[1], linje[2], linje [3], linje[4], linje[5], linje[8]]   # Set Time_temp_min til første temp i nytt døgn.
        Time_temp_max = [linje[0], linje[1], linje[2], linje [3], linje[4], linje[5], linje[8]]   # Set Time_temp_max til første temp i nytt døgn.
    if Time_temp_min[6] > linje[8]:                                     #Viss registrert temperatur er lågare enn Time_temp_min, oppdater Time_temp_min.
        Time_temp_min = [linje[0], linje[1], linje[2], linje [3], linje[4], linje[5], linje[8]]
    if Time_temp_max[6] < linje[8]:                                     #Viss registrert temperatur er høgare enn Time_temp_max, oppdater Time_temp_max.
        Time_temp_max = [linje[0], linje[1], linje[2], linje [3], linje[4], linje[5], linje[8]]

    #Lagar ein loop for å etablere ei liste med tid og temperatur for den høgaste og lågaste temperaturen i Time_temp[]:
Time_temp_drop = []

for i in range((len(Time_warmest))*2-1):
    if i %2 == 0:
        Time_temp_drop.append(Time_warmest[(int(i/2))])
    elif i %2 == 1:
        Time_temp_drop.append(Time_coldest[(int((i+1)/2))])
Time_coldest = None
Time_warmest = None #Fjernar desse frå listene.

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

    # Startar arbeidet med plotting:
import matplotlib.pyplot as plt
import matplotlib.dates as mdates                # For formatering av dato-data.
import datetime

    # Hentar ut tid og temperatur frå listene:
 
Sola_tider = [datetime.datetime(d[0], d[1], d[2], d[3], d[4]) for d in Sola_data]
Sola_temps = [d[6] for d in Sola_data]
        # Konverterer tid til datetime-objekt
Time_tider = [datetime.datetime(d[0], d[1], d[2], d[3], d[4]) for d in Time_data]
Time_temps = [d[8] for d in Time_data]
Time_temp_avg = [d[6] for d in Time_temp_snitt]  
Time_temp_avg_tider = [datetime.datetime(d[0], d[1], d[2], d[3], d[4]) for d in Time_temp_snitt]
Time_temp_drop = Time_temp_drop[2:4] 
Time_temp_drop_tider = [datetime.datetime(d[0], d[1], d[2], d[3], d[4]) for d in Time_temp_drop]
Time_temp_drop = [d[6] for d in Time_temp_drop]

        #Lagar ein funksjon for å plotte temperaturdata:
def plot_temperature():
        # Opprettar bildet og aksen
    fig, ax = plt.subplots(figsize=(14, 4))
        # Plottar dataene
    ax.plot(Time_tider, Time_temps, color="blue", label="Temperature (Time)")
    ax.plot(Time_temp_avg_tider, Time_temp_avg, color="orange", linewidth=0.5, label="Average temperature (Time)")
    ax.plot(Sola_tider, Sola_temps, color="green", label="Temperature (MET)")
    ax.plot(Time_temp_drop_tider, Time_temp_drop, color="violet", label='Temperature drop from max til min')
        # Formaterer x-aksen. 
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m %H:%M'))
        #Set overskrift og aksetitlar, samt plasserer "skiltet" (legend) med plot labels der det er best plass:
    ax.set_title('Temperature/Date graph')
    ax.set_xlabel('Time (DD-MM HH:MM)')
    ax.set_ylabel('Temperature (°C)')
    ax.legend()
    # Vis plottet
    plt.tight_layout()
    plt.show()

plot_temperature() #Kallar på funksjonen for å plotte temperaturdata.