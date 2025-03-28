import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

# List of CSV files to plot
csv_files = [
    "LongerFlexionKai_NormalSetUp.csv",
    "NormalFlexion_DifferentReferenceInbetweenOtherSensors.csv",
    "NormalFlexion_DifferentReferencePalm.csv",
    "NormalFlexion_DifferentReferenceParallelForearm.csv",
    "NormalFlexion_ParallelShortDistance.csv",
    "NormalFlexion_PerpElectrodes1.csv",
    "NormalFlexion_PerpElectrodes2.csv",
    "NormalFlexion_PerpElectrodes3.csv",
    "restKai_normalSetUp.csv",
    "ThumbtoPinky1_NormalSetUp.csv",
    "TwoLightTwoStrong_NormalSetUp.csv",
    "wristKai_normalSetUp.csv"
]

# Create time axis (each step is 2ms)
time = np.arange(0, 5000 * 2, 2)

# 4 flexions - electrodes perpendicular
data_perp = pd.read_csv('data/'+ "NormalFlexion_PerpElectrodes1.csv")

# 4 flecxions - lectordes parallel - normal distance
data_parallel = pd.read_csv('data/'+ "NormalFlexion_DifferentReferenceParallelForearm.csv")

# 4 flecxions - electordes parallel - short distance
data_parallel_short = pd.read_csv('data/'+ "NormalFlexion_ParallelShortDistance.csv")

# 4 flexions resting at normal set up 
data_rest = pd.read_csv('data/'+ "restKai_normalSetUp.csv")


plt.figure(figsize=(10, 6))

#different plots
plt.plot(time[:len(data_perp)]/1000, data_perp, label = "Perpendicular Electrodes")
#plt.plot(time[:len(data_parallel)]/1000, data_parallel, label = "Parallel Electrodes")
#plt.plot(time[:len(data_parallel_short)]/1000, data_parallel_short, label = "Shorter Distance - Parallel Electrodes")

# rest plot
plt.plot(time[:len(data_rest)]/1000, data_rest, label = "Rest")

#plt.plot(time[:len(data_rest)]/1000, data_rest, label="Rest")
plt.title("Comparison of Different Orientations")
plt.xlabel("Time (s)")
plt.ylabel("Signal Amplitude")
plt.legend()
plt.grid(True)
plt.show()

# -----------
'''
This code was used to plot different experimenst against the resting
electromagnetic potential detected by surface EMG technology.
'''
# -----------