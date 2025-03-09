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

# normal set up - 4 flexions
#data_4flexions = pd.read_csv('data/'+ "wristKai_normalSetUp.csv")

# normal set up - two long two short
#data_2strong2light = pd.read_csv('data/'+ "TwoLightTwoStrong_NormalSetUp.csv")

# normal set up - thumb to finger
data_thumb2pinky = pd.read_csv('data/'+ "ThumbtoPinky1_NormalSetUp.csv")

# normal set up  - rest
data_rest = pd.read_csv('data/'+ "restKai_normalSetUp.csv")

plt.figure(figsize=(10, 6))
#plt.plot(time[:len(data_4flexions)]/1000, data_4flexions, label="4 Flexions")
#plt.plot(time[:len(data_2strong2light)]/1000, data_2strong2light, label="2 Strong 2 Light")
plt.plot(time[:len(data_thumb2pinky)]/1000, data_thumb2pinky, label="Thumb to Pinky")
plt.plot(time[:len(data_rest)]/1000, data_rest, label="Rest")
plt.title("Comparison of Standard Set Up Signal")
plt.xlabel("Time (s)")
plt.ylabel("Signal Amplitude")
plt.legend()
plt.grid(True)
plt.show()