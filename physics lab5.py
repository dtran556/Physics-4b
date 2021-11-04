#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 10:55:13 2021

@author: dtran556
"""

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0,1,1000,endpoint=True)

plt.plot(t, 2*np.sin(t*np.pi*10))
#plt.plot(t, np.sin(t*np.pi*2))

plt.title('Sine wave sampled at 1000 Hz')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True, which='both')
plt.axhline(y=0, color = 'k')
plt.ylim(-2, 2)
plt.show()

plt.plot(t, 2*signal.square(t*np.pi*10))

plt.title('Square_wave_sampled_at_1000_Hz')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True, which='both')
plt.axhline(y=0, color = 'k')
plt.ylim(-3, 3)
plt.show()

plt.plot(t, 2*signal.sawtooth(t*np.pi*10))

plt.title('Sawtooth wave sampled at 1000 Hz')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True, which='both')
plt.axhline(y=0, color = 'k')
plt.ylim(-2, 2)
plt.show()

plt.plot(t, signal.triang(len(t*np.pi*10)))

plt.title('Triangle_wave_sampled_at_1000_Hz')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True, which='both')
plt.axhline(y=0, color = 'k')
plt.ylim(-2, 2)
plt.show()