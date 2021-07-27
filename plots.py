# Boarda count plots
import matplotlib.pyplot as plt
from bipolar_bias import bipolar

def borda_count_frequency(preference_profile, show_plot):
    rows, cols = preference_profile.shape[0], preference_profile.shape[1]
    print(cols)
    counts = dict.fromkeys(range(0, cols), 0)
    for x in range(0, rows):
        for y in range(0, cols):
            # Calculates the individual borda counts and sums them up
            counts[y] += rows - preference_profile[x,y]
    if show_plot:
        candidate = list(counts.keys())
        values = list(counts.values())
        plt.bar(range(len(counts)), values, tick_label=candidate)
        plt.show()
    return counts

if __name__ == "__main__":
    data = bipolar(6, 10, 0.5)
    counts = borda_count_frequency(data, True)
    print(data)
    print(counts)