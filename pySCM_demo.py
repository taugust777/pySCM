#Tim August
#12 / 4 / 25

import sys
sys.path.append("Filepath for pySCM env") #Insert the filepath for the pySCM environment

from pySCM import SimpleClimateModel
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#This actually runs the model
model = SimpleClimateModel("SimpleClimateModelParameterFile.txt")
model.run_model()

#Check
print("Model ran successfully")

#Save temp and slr outputs
df_T = pd.read_csv("temp_output.txt")
print(df_T)

df_SC = pd.read_csv("slr_output.txt")
print(df_SC)

#Store temp and slr outputs
array_T = np.array(df_T)
print(array_T)

array_SC = np.array(df_SC)
print(array_SC)

#Plot temp and slr output
years = [int(item[0].split()[0]) for item in array_T]
slr = [float(item[0].split()[1]) for item in array_SC]
temps = [float(item[0].split()[1]) for item in array_T]

plt.plot(years, temps, color = "red")
plt.xlabel("Years")
plt.ylabel("Temp (C)")
plt.title("Temperature")
plt.ylim(0, 4)
plt.show()

plt.plot(years, slr, color = "blue")
plt.xlabel("Years")
plt.ylabel("Sea Level Rise (m)")
plt.title("Sea Level Rise")
plt.ylim(0, 0.25)
plt.show()

#Save the concentrations of the gases: CO2, CH4, N2O
model.save_output()
