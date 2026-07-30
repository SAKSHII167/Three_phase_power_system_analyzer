# For all necessary calculation
import numpy as np

def calculate_parameters(Vrms, f, connection ):

    Vm = Vrms * np.sqrt(2)

    w = 2 * np.pi * f

    T = 1 / f

    if connection == "Star":
        Vline = np.sqrt(3) * Vrms
    else:
        Vline = Vrms

    '''results= {
        "Peak Voltage (Vm)": Vm,
        "Angular Frequency (w)": w,
        "Time Period (T)": T,
        "Line Voltage (Vline)": Vline
    }'''
    return Vm, w, T, Vline

def analyze_waveform(signal):
    Vmax = np.max(signal)
    Vmin = np.min(signal)
    return np.sqrt(np.mean(signal**2)), Vmax, Vmin


'''def calculate_max_min(signal):
    Vmax = np.max(signal)
    Vmin = np.min(signal)

    return Vmax, Vmin'''