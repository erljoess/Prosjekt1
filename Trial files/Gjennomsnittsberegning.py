import convert_met_data as cmd

Time_data = []
Time_data = cmd.convert_Time_data(Time_data)
Time_temp_total = []
Time_temp_snitt = []

for i, linje in enumerate(Time_data):           #Går gjennom kvar linje i Time_data, og bereknar snitt av dei siste 5 minutta.
    Time_temp_total.append(float(linje[8]))
    if i % 6 == 0:
        while len(Time_temp_total) > 30:         #For å få rett lengde på gjennomsnitts-berekninga:
            Time_temp_total.pop(0)               #Fjernar det eldste elementet i Time_act_total[].
        if i >= 29:
            Time_temp_snitt.append([linje[0], linje[1], linje[2], linje[3], linje[4], linje[5], float(f"{sum(Time_temp_total)/30:.2f}")])

print(Time_temp_snitt[:10])
#print(Time_temp_total)