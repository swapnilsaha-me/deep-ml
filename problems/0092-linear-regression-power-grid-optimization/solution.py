import math
import numpy as np

PI = 3.14159

def power_grid_forecast(consumption_data):
    # 1) Subtract the daily fluctuation (10 * sin(2π * i / 10)) from each data point.
    X = np.zeros_like(consumption_data)
    y = np.zeros_like(consumption_data)
    for i in range(len(consumption_data)):
        fluctuation = 10.0 * math.sin((2 * math.pi * (i + 1)) / 10.0)
        X[i] = consumption_data[i] - fluctuation
        y[i] = i + 1
    # 2) Perform linear regression on the detrended data.
    # y = mx + c
    m, c = np.polyfit(y, X, 1)
    # 3) Predict day 15's base consumption.
    consumption_on_day_15 = m * 15 + c;
    # 4) Add the day 15 fluctuation back.
    fluctuation_on_day_15 = 10.0 * math.sin((2 * math.pi * 15) / 10.0)
    consumption_on_day_15 = consumption_on_day_15 + fluctuation_on_day_15
    # 5) Round, then add a 5% safety margin (rounded up).
    consumption_on_day_15 = round(consumption_on_day_15)
    consumption_on_day_15 = math.ceil(consumption_on_day_15 + (consumption_on_day_15 * 0.05))
    # 6) Return the final integer.
    return consumption_on_day_15