import matplotlib.pyplot as plt
import csv

def potato(file_dest):
    original_csv = open(file_dest,"r")
    original_csv_read = csv.reader(original_csv, delimiter=',')
    _2d_original = [[],[],[],[],[]]

    for line in original_csv_read:
        _2d_original[0].append(float(line[1]))
        _2d_original[1].append(float(line[3]))
        _2d_original[2].append(float(line[0]))
        _2d_original[3].append(float(line[2]))
        _2d_original[4].append(float(line[4]))

    return _2d_original

##################################################

filter_egr = "C:/Users/HP Gold/Downloads/LOGS/Filter + EGR.CSV"
_2d_fil_egr = potato(filter_egr)

plt.plot(_2d_fil_egr[2], _2d_fil_egr[0], label = "Filter + EGR (V/T)")
plt.plot(_2d_fil_egr[2], _2d_fil_egr[1], label = "Filter + EGR (MAF ACT/T)")
plt.plot(_2d_fil_egr[2], _2d_fil_egr[3], label = "Filter + EGR (MAF SPEC/T)")
plt.plot(_2d_fil_egr[2], _2d_fil_egr[4], label = "Filter + EGR (EGR/T)")

##################################################

filters = "C:/Users/HP Gold/Downloads/LOGS/Filter.CSV"
_2d_fil = potato(filters)

plt.plot(_2d_fil[2], _2d_fil[0], label = "Filter Only (V/T)")
plt.plot(_2d_fil[2], _2d_fil[1], label = "Filter Only (MAF ACT/T)")
plt.plot(_2d_fil[2], _2d_fil[3], label = "Filter Only (MAF SPEC/T)")
plt.plot(_2d_fil[2], _2d_fil[4], label = "Filter Only (EGR/T)")

##################################################

original = "C:/Users/HP Gold/Downloads/LOGS/Original.CSV"
_2d_original = potato(original)

plt.plot(_2d_original[2], _2d_original[0], label = "Original (V/T)")
plt.plot(_2d_original[2], _2d_original[1], label = "Original (MAF ACT/T)")
plt.plot(_2d_original[2], _2d_original[3], label = "Original (MAF SPEC/T)")
plt.plot(_2d_original[2], _2d_original[4], label = "Original (EGR/T)")

plt.xlabel('time')  
plt.ylabel('MAF Act/Speed') 
 
plt.title("Dool's stooff") 
  
# show a legend on the plot 
plt.legend()


plt.show()

