"""
Simulated RF Signal Processing Script

This script generates and processes a synthetic radio frequency (RF) signal
spanning a wide range of frequencies. It simulates the capture and analysis
of RF signals using Python, without the need for actual hardware like an
RTL-SDR dongle. The script generates a composite signal containing multiple
sinusoidal components and adds Gaussian noise to simulate a real-world scenario.
The signal is then visualized in both time and frequency domains, and peaks
in the frequency spectrum are detected and annotated.

Dependencies:
- numpy
- matplotlib
- scipy

Install the necessary libraries using:
pip install numpy matplotlib scipy

Author: [Your Name]
License: [Choose a license, e.g., MIT]

Parameters:
fs : float
    Sample rate in Hz (e.g., 2.048e6)
T : float
    Duration of the signal in seconds (e.g., 1.0)
frequencies : list of float
    List of frequencies in Hz to be included in the composite signal
    (e.g., [50e6, 75e6, 100e6, 125e6, 150e6])

Generated Data:
t : numpy.ndarray
    Array of time values
signal : numpy.ndarray
    Composite signal containing multiple frequency components with added noise

Visualization:
The script generates two plots:
1. Time Domain Signal: Shows the amplitude of the signal over time.
2. Frequency Domain Signal: Displays the power spectral density (PSD) of the signal
   and annotates the detected peak frequencies.

Peak Detection:
The script uses scipy's find_peaks function to detect peaks in the frequency
spectrum. Detected peaks are annotated on the frequency domain plot, and their
frequencies are printed to the console.

Usage:
Run the script in a Python environment to generate and analyze the simulated
RF signal.

Example:
python rf_signal_processing.py

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Parameters
fs = 2.048e6  # Sample rate (Hz)
T = 1.0       # Duration of the signal (seconds)
frequencies = [50e6, 75e6, 100e6, 125e6, 150e6]  # List of frequencies (Hz)

# Time array
t = np.linspace(0, T, int(T * fs), endpoint=False)

# Generate a composite signal with multiple frequencies
signal = np.zeros_like(t)
for freq in frequencies:
    signal += np.sin(2 * np.pi * freq * t)

# Add some noise to the signal
noise = np.random.normal(0, 0.5, signal.shape)
signal += noise

# Plot the time-domain signal
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Time Domain Signal')

# Frequency-domain plot
plt.subplot(2, 1, 2)
frequencies, power_spectrum = plt.psd(signal, NFFT=2048, Fs=fs)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power Spectral Density (dB/Hz)')
plt.title('Frequency Domain Signal')

# Detect peaks in the frequency spectrum
peaks, _ = find_peaks(power_spectrum, height=10)
peak_freqs = frequencies[peaks]

# Annotate peaks
for peak in peaks:
    plt.annotate(f'{frequencies[peak]:.2e} Hz', xy=(frequencies[peak], power_spectrum[peak]),
                 xytext=(frequencies[peak], power_spectrum[peak] + 10),
                 arrowprops=dict(facecolor='red', shrink=0.05),
                 horizontalalignment='center')

plt.tight_layout()
plt.show()

# Print detected peak frequencies
print("Detected peak frequencies:")
for freq in peak_freqs:
    print(f"{freq:.2e} Hz")
