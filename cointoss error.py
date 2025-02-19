import numpy as np
import matplotlib.pyplot as plt

# Parameters
fc = 100  # Carrier frequency in Hz
fm = 10   # Message frequency in Hz
Am = 1    # Message amplitude
Ac = 1    # Carrier amplitude
t = np.linspace(0, 1, 1000)  # Time vector

# Message signal (m(t))
message = Am * np.cos(2 * np.pi * fm * t)

# Carrier signal (cos(2*pi*fc*t))
carrier = Ac * np.cos(2 * np.pi * fc * t)

# DSB-SC modulated signal (s(t) = m(t) * cos(2*pi*fc*t))
dsb_sc = message * carrier

# Plotting the signals
plt.figure(figsize=(10, 8))

# Plot the message signal
plt.subplot(3, 1, 1)
plt.plot(t, message)
plt.title('Message Signal m(t)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Plot the carrier signal
plt.subplot(3, 1, 2)
plt.plot(t, carrier)
plt.title('Carrier Signal cos(2πf_ct)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Plot the DSB-SC signal
plt.subplot(3, 1, 3)
plt.plot(t, dsb_sc)
plt.title('DSB-SC Modulated Signal s(t) = m(t) * cos(2πf_ct)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
