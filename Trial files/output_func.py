import convert_met_data as cmd

Time_data = [cmd.convert_Time_data()]
Sola_data = [cmd.convert_Sola_data()]

print(Time_data)    

act_data_time = []
bar_data_time = []
temp_data_time = []
bar_data_met = []
temp_data_met = []

def Sola_Lister():

    for data in Sola_data:
        print(data)
#        yyyy, mo, dd, hh, mm, bar, temperature = data
#
#        dtg = f"{yyyy:04d}-{mo:02d}-{dd:02d} {hh:02d}:{mm:02d}"
#
#        bar_data_met.append(dtg, bar)
#        temp_data_met.append(dtg, temperature)

def Time_Lister():
    for data in Time_data:
        yyyy, mo, dd, hh, mm, ss, bar, act, temperature = data
#
#        dtg = f"{yyyy:04d}-{mo:02d}-{dd:02d} {hh:02d}:{mm:02d}:{ss:02d}"
#
#        bar_data_time.append(dtg, bar)
#        act_data_time.append(dtg, act)
#        temp_data_time.append(dtg, temperature)

#Sola_Lister()
Time_Lister()

#print(bar_data_met)
#print(temp_data_met)
#print(bar_data_time)
#print(act_data_time)
#print(temp_data_time)