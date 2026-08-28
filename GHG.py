#Tim August
#12 /4 / 25

#Greenhouse Gas concentrations

import numpy as np
import pandas as pd

#Make sure the years chosen match the selected start and end year from the SimpleClimateModelParameterFile.txt
start = 2026
end = 2090
years = list(range(start, end + 1))

co2_val_2025 = 38.1 #Pg CO2

#Base 2025 values -> SOx is not included here but can be
co2_val = co2_val_2025 / (44.01 / 12.011)     #PgC
ch4_val = 0.00424  #PgCH4
n2o_val = 0.0108   #PgN2O

#Annual growth rates -> can be changed and modified
co2_pct = 0.0025   #0.25%
ch4_pct = 0.0005   #0.05%
n2o_pct = 0.0002   #0.02%

co2, ch4, n2o, sox = [], [], [], []

for y in years:
    #Growth rate compounding from base
    co2_val *= (1 + co2_pct)
    ch4_val *= (1 + ch4_pct)
    n2o_val *= (1 + n2o_pct)
    
    co2.append(co2_val)
    ch4.append(ch4_val)
    n2o.append(n2o_val)
    sox.append(0.0)
    

data = {"CO2": co2, "CH4": ch4, "N2O": n2o, "SOx": sox}
table = pd.DataFrame(data, index = years)

#Export directly to EmissionsForSCM input file
table.to_csv("EmissionsForSCM.txt", sep = "\t", float_format = "%.6f")
print(table)
