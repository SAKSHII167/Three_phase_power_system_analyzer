# Generates time vector and three phase waveforms 
import numpy as np

def generate_waveforms(Vm, w, duration, samples):

    t = np.linspace(0, duration, samples)

    phase_shift = np.deg2rad(120)

    Va = Vm * np.sin(w * t)

    Vb = Vm * np.sin(w * t - phase_shift)

    Vc = Vm * np.sin(w * t + phase_shift)

    return t, Va, Vb, Vc