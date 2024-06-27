import json
import sys
import os

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline

def usage():
    """
    This returns the basic help usage.
    """
    return "Usage:\n" \
        "python3 plotter.py <recording-path>"

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(usage())
        sys.exit()
    if not os.path.exists(sys.argv[1]):
        raise FileNotFoundError(f"File at {sys.argv[1]} inexistant.")
    with open(sys.argv[1], encoding='utf-8-sig') as f:
        text = f.read()
        data = json.loads(text)
        monster_times = data['monster_time']
        monster_time_score = {}
        
        # Compute density in mons/min
        last_minute = 0
        current = 0
        for i, timestamp in enumerate(monster_times):
            t = float(timestamp)
            if (t < 60):
                # Set score to i * 60 / timestamp (scaled to a minute)
                monster_time_score[timestamp] = i * 60 / t
            else:
                while float(monster_times[last_minute]) < float(monster_times[i]) - 60.0:
                    last_minute += 1
                monster_time_score[timestamp] = i - last_minute

        # Visualization
        #print(json.dumps(monster_time_score, indent=4))
        x = [float(timestamp) for timestamp in monster_times]
        y = list(monster_time_score.values())

        x_sm = np.array(x)
        y_sm = np.array(y)

        x_smooth = np.linspace(x[0], x[-1], 1000)
        spline = make_interp_spline(x, y, k=1)
        y_smooth = spline(x_smooth)

        plt.figure()
        plt.plot(x_smooth, y_smooth)  # Plot some data on the (implicit) Axes.
        plt.xlabel('Time')
        plt.ylabel('Score')
        plt.title("Test")
        plt.show()
