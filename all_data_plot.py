import pandas as pd
import matplotlib.pyplot as plt
import time 

start = time.time()

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

# Create a figure and subplots
fig, axes = plt.subplots(nrows=3, ncols=4, figsize=(24, 16))  # Increase the figure size
axes = axes.flatten()  # Flatten to easily iterate

# Adjust the spacing between subplots:
# wspace: width space, hspace: height space
fig.subplots_adjust(wspace=0.4, hspace=0.6)


for i, csv_file in enumerate(csv_files):
    
    data = pd.read_csv('data/'+ csv_file)

    new_time = time.time()

    print(f'{i}th plot takes {new_time-start}')
    
    signal = data.iloc[:, 0]
    
    axes[i].plot(signal)
    axes[i].set_title(csv_file)
    axes[i].set_xlabel("Sample Index")
    axes[i].set_ylabel("Signal Amplitude")

    start = time.time()

plt.show()


