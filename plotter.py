# For plotting the generated waveforms w.r.t. time 
import matplotlib.pyplot as plt

def plot_waveforms(t, Va, Vb, Vc, graph_filename):

    plt.figure(figsize=(12,5))

    plt.plot(t, Va, color="red", linewidth=2,label="Phase A")

    plt.plot(t, Vb, color="gold", linewidth=2,label="Phase B")

    plt.plot(t, Vc, color="blue",linewidth=2, label="Phase C")

    plt.xlabel("Time (seconds)")

    plt.ylabel("Voltage (Volts)")

    plt.title("Three-Phase AC Waveforms")

    plt.grid(True , linestyle="--", alpha=0.7)

    plt.legend()

    plt.tight_layout() #Sometimes labels or titles get cut off. It automatically adjusts the spacing so everything fits nicely.

    plt.savefig(graph_filename, dpi=300) # dpi=300 standard/suitable for printing or presentations.

    plt.show()

    