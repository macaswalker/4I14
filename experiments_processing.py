import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import time

# Load EMG data (assuming CSV contains a single column of values)
file_path = 'data/ThumbtoPinky1_NormalSetUp.csv'
data_fingers = pd.read_csv(file_path, header=None)

# Extract signal from the first (and only) column and create time axis
signal_raw = data_fingers.iloc[:, 0].values
time_axis = np.arange(0, len(signal_raw) * 2, 2)  # Each step is 2ms

print("Signal length:", len(signal_raw))

# Define filter parameters
fs = 1000          # Sampling frequency in Hz
lowcut = 20        # Lower cutoff for band-pass filter (Hz)
highcut = 450      # Upper cutoff for band-pass filter (Hz)
rectification_type = 'half'  # 'half' for half-wave or 'full' for full-wave rectification
lowpass_cutoff = 5 # Low-pass filter cutoff for envelope detection (Hz)
ma_window = 50     # Moving average window size (samples)

# Dictionary to store processing times
processing_times = {}

# Band-pass filter (Step 1)
start_time = time.time()
b, a = signal.butter(2, [lowcut, highcut], btype='band', fs=fs)
filtered_signal = signal.filtfilt(b, a, signal_raw)
processing_times['Band-pass Filtering'] = time.time() - start_time

# Rectification (Step 2)
start_time = time.time()
if rectification_type == 'half':
    rectified_signal = np.maximum(filtered_signal, 0)  # Half-wave rectification
else:
    rectified_signal = np.abs(filtered_signal)           # Full-wave rectification
processing_times['Rectification'] = time.time() - start_time

# Low-pass filter for envelope detection (Step 3)
start_time = time.time()
b, a = signal.butter(4, lowpass_cutoff, btype='low', fs=fs)
envelope_signal = signal.filtfilt(b, a, rectified_signal)
processing_times['Envelope Detection'] = time.time() - start_time

# Moving average filter for smoothing (Step 4)
start_time = time.time()
smoothed_signal = np.convolve(envelope_signal, np.ones(ma_window)/ma_window, mode='same')
processing_times['Smoothing'] = time.time() - start_time

# Plot results in a 2x2 grid
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("EMG Signal Processing Steps")

# Raw vs. Band-pass filtered
axes[0, 0].plot(time_axis, signal_raw, label="Raw Signal", alpha=0.5)
axes[0, 0].plot(time_axis, filtered_signal, label="Band-pass Filtered", color='r')
axes[0, 0].set_title("1. Band-pass Filtering")
axes[0, 0].set_xlabel("Time (ms)")
axes[0, 0].set_ylabel("Amplitude")
axes[0, 0].legend()

# Rectified signal
axes[0, 1].plot(time_axis, rectified_signal, color='g')
axes[0, 1].set_title("2. Rectification")
axes[0, 1].set_xlabel("Time (ms)")
axes[0, 1].set_ylabel("Amplitude")

# Envelope detection
axes[1, 0].plot(time_axis, envelope_signal, color='orange')
axes[1, 0].set_title("3. Envelope Detection")
axes[1, 0].set_xlabel("Time (ms)")
axes[1, 0].set_ylabel("Amplitude")

# Smoothed signal
axes[1, 1].plot(time_axis, smoothed_signal, color='purple')
axes[1, 1].set_title("4. Smoothing")
axes[1, 1].set_xlabel("Time (ms)")
axes[1, 1].set_ylabel("Amplitude")

plt.tight_layout()
plt.show()

# Display processing times
df_times = pd.DataFrame(list(processing_times.items()), columns=["Processing Step", "Time (s)"])
print(df_times)
