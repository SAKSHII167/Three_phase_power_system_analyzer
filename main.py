#import numpy as np
import pandas as pd
from datetime import datetime
import os

# Import functions from other Python files
from calculations import (calculate_parameters, analyze_waveform)
from waveform import generate_waveforms
from plotter import plot_waveforms
from excel_rep import export_to_excel

# Create Output Folder

os.makedirs("output", exist_ok=True) #???

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")#??

graph_filename = f"output/waveform_{timestamp}.png"
excel_filename = f"output/waveform_{timestamp}.xlsx"

# Welcome Screen

print("==========THREE-PHASE WAVEFORM VISUALIZER==========")
print("\n----------System Assumptions----------")
print("---------------------------")
print("Balanced Three-Phase System")
print("Sinusoidal Supply")
print("Default Phase Sequence : ABC")

# User Inputs
print("\n----------User Inputs----------")
Vrms = float(input("\nEnter Phase RMS Voltage (Volts)For Example 230V: "))
if Vrms <= 0:
    print("Voltage must be greater than zero.")
    exit()

f = float(input("Enter Frequency (Hz)For Example 50Hz: "))
if f <= 0:
    print("Frequency must be greater than zero.")
    exit()

duration = float(input("Enter Duration (s)For Example 0.1s: "))
if duration <= 0:
    print("Duration must be greater than zero.")
    exit()

samples = int(input("Enter Number of Samples(For Example 1000): "))
if samples < 10:
    print("Please enter at least 10 samples.")
    exit()

connection = input("Enter Connection (Star/Delta): ").capitalize()
if connection not in ["Star", "Delta"]:
    print("Invalid Connection")
    exit()

# calculations.py

Vm, w, T, Vline = calculate_parameters(Vrms,f,connection)
'''results = calculate_parameters(Vrms,f,connection)
Vm, w, T, Vline = results["Peak Voltage (Vm)"], results["Angular Frequency (w)"], results["Time Period (T)"], results["Line Voltage (Vline)"]
print(results)'''

# waveform.py

t, Va, Vb, Vc = generate_waveforms( Vm, w,duration,samples)

# calculate rms of Va to verify
calculated_rms, Vmax, Vmin = analyze_waveform(Va)    

'''# calculate max and min of Va to verify
Vmax, Vmin = calculate_max_min(Va)'''

# plotter.py

plot_waveforms( t,  Va, Vb, Vc,graph_filename)

# Display Results

print("\n==========Three-Phase Power System Analysis Tool==========")

print("\n----------Input Parameters----------")

print("Phase Sequence                 : ABC")
print("Phase A                        : 0°")
print("Phase B                        : -120°")
print("Phase C                        : +120°")

print("\n----------Phase Specifications----------")

print(f"Frequency                     : {f:.2f} Hz")
print(f"Phase Voltage (RMS)           : {Vrms:.2f} V")
print(f"Connection                    : {connection}")

print("\n----------Calculated Parameters----------")

print(f"Peak Voltage                  : {Vm:.2f} V")
print(f"Line Voltage                  : {Vline:.2f} V")
print(f"Maximum Instantaneous Voltage : {Vmax:.2f} V")
print(f"Minimum Instantaneous Voltage : {Vmin:.2f} V")
print(f"Angular Frequency             : {w:.2f} rad/s")
print(f"Time Period                   : {T:.4f} s")

# creating dataframes for excel export

waveform_df = pd.DataFrame({

    "Time (s)": t,
    "Phase A (V)": Va,
    "Phase B (V)": Vb,
    "Phase C (V)": Vc

})

summary_df = pd.DataFrame({
    "Parameter":[
        "Analysis Date & Time",
        "Connection",
        "Phase Sequence",
        "Phase Voltage (RMS)",
        "Calculated RMS",
        "Peak Voltage",
        "Maximum Voltage",
        "Minimum Voltage",
        "Line Voltage",
        "Frequency",
        "Angular Frequency",
        "Time Period",
        "Samples"
    ],
    "Value":[
        current_time,
        connection,
        "ABC",
        Vrms,
        round(calculated_rms, 2),
        round(Vm, 2),
        round(Vmax, 2),
        round(Vmin, 2),
        round(Vline, 2),
        f,
        round(w, 2),
        round(T, 4),
        samples
    ]
})

''' Vrms,Vm,Vline,f,w,T,connection,samples,calculated_rms,Vmax,Vmin'''
    
    

'''"Phase Voltage (RMS)",
        "Peak Voltage",
        "Line Voltage",
        "Frequency",
        "Angular Frequency",
        "Time Period",
        "Connection",
        "Samples",
        "Calculated RMS",
        "Maximum Voltage",
        "Minimum Voltage",
        "Analysis Date & Time",'''

# excel_rep.py

export_to_excel(
    excel_filename,
    waveform_df,
    summary_df
)

# done

print("\n----------Output Files----------")

print(f"Graph Saved                   : {graph_filename}")
print(f"Excel Saved                   : {excel_filename}")


print("\n---------Simulation Completed Successfully!---------")