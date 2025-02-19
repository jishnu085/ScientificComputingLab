import numpy as np
import matplotlib.pyplot as plt

# Function to generate a square wave
def square_wave(x, frequency, amplitude=1):
    return amplitude * np.sign(np.sin(2 * np.pi * frequency * x))

# Function to compute Fourier transform
def fourier_transform(signal, dt):
    N = len(signal)
    freqs = np.fft.fftfreq(N, d=dt)
    fft_values = np.fft.fft(signal)
    return freqs, fft_values

# Parameters
sampling_rate = 1000  # Hz
duration = 1  # seconds
num_samples = int(sampling_rate * duration)
frequency = 10  # Hz

# Generate time array
t = np.linspace(0, duration, num_samples, endpoint=False)

# Generate square wave
square_wave_signal = square_wave(t, frequency)

# Compute Fourier transform
dt = t[1] - t[0]
freqs, fft_values = fourier_transform(square_wave_signal, dt)

# Plotting
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, square_wave_signal)
plt.title('Square Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(freqs, np.abs(fft_values))
plt.title('Fourier Transform')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.xlim(0, 2 * frequency)  # Limiting x-axis to 2 * frequency for better visualization

plt.tight_layout()
plt.show()
