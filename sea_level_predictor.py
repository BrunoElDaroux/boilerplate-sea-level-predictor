import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats

# Import data
df = pd.read_csv("epa-sea-level.csv")

# Draw Scatter Plot
def draw_plot():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Data")
    
    # Line of best fit for all data
    slope, intercept, _, _, _ = stats.linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_pred = np.arange(1880, 2051)
    y_pred = slope * x_pred + intercept
    ax.plot(x_pred, y_pred, 'r', label="Best Fit (1880-2050)")
    
    # Line of best fit from 2000 onwards
    df_recent = df[df["Year"] >= 2000]
    slope_recent, intercept_recent, _, _, _ = stats.linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    x_pred_recent = np.arange(2000, 2051)
    y_pred_recent = slope_recent * x_pred_recent + intercept_recent
    ax.plot(x_pred_recent, y_pred_recent, 'g', label="Best Fit (2000-2050)")
    
    # Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()
    
    return fig

 # Save plot and return data for testing (DO NOT MODIFY)
    # plt.savefig('sea_level_plot.png')
    # return plt.gca()
