#%% Import libraries and define CSV file list
import pandas as pd
import matplotlib.pyplot as plt
import time

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

for i, csv_file in enumerate(csv_files):
    start_time = time.time()  # start timing for this plot
    
    # Read the CSV file and select the signal (first column)
    data = pd.read_csv('data/'+ csv_file)
    signal = data.iloc[:, 0]  # Adjust column index if necessary
    
    # Create a new figure for this plot
    plt.figure(figsize=(10, 6))
    plt.plot(signal)
    plt.title(csv_file)
    plt.xlabel("Sample Index")
    plt.ylabel("Signal Amplitude")
    plt.grid(True)
    plt.show()
    
    end_time = time.time()  # end timing for this plot
    print(f"{csv_file}: Plot took {end_time - start_time:.2f} seconds")
    
    # Wait for user input to proceed to the next plot
    input("Press Enter to continue to the next plot...")