import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
import numpy as np

# Search in the current directory
folder_path = './'

# Get all CSV files in the folder
csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

for file in csv_files:
    # Read CSV with semicolon delimiter, dot decimal, and header
    df = pd.read_csv(file, delimiter=';', decimal='.', header=0)

    # Extract columns
    x = df.iloc[:, 0]
    vout = df.iloc[:, 1]
    dvout = df.iloc[:, 2]

    # Find index where dVout/dX is closest to -1
    idx_closest = (np.abs(dvout + 1)).idxmin()
    x_cursor = x[idx_closest]
    dvout_cursor = dvout[idx_closest]
    vout_cursor = vout[idx_closest]

    # Find the second crossing (next point where dvout crosses the same horizontal value)
    second_cross_idx = None
    x_cross = None
    vout_cross = None
    for i in range(idx_closest + 1, len(dvout) - 1):
        if (dvout[i] - dvout_cursor) * (dvout[i + 1] - dvout_cursor) < 0:
            # Linear interpolation to estimate x at crossing point
            x1, x2 = x[i], x[i + 1]
            y1, y2 = dvout[i], dvout[i + 1]
            x_cross = x1 + (x2 - x1) * (dvout_cursor - y1) / (y2 - y1)
            # Interpolate corresponding Vout value
            v1, v2 = vout[i], vout[i + 1]
            vout_cross = v1 + (v2 - v1) * (x_cross - x1) / (x2 - x1)
            second_cross_idx = i
            break

    # Create subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    # --- Top plot: dVout/dX ---
    ax1.plot(x, dvout, label='dVout/dX', color='tab:orange', linewidth=2, linestyle='--')
    ax1.plot(x_cursor, dvout_cursor, 'ro')  # Cursor point
    ax1.axvline(x=x_cursor, color='red', linestyle=':', linewidth=1)  # Vertical line
    ax1.axhline(y=dvout_cursor, color='gray', linestyle=':', linewidth=1)  # Horizontal line
    ax1.annotate(f'({x_cursor:.3g}, {dvout_cursor:.3g})',
                 xy=(x_cursor, dvout_cursor),
                 xytext=(10, 10),
                 textcoords='offset points',
                 arrowprops=dict(arrowstyle='->', color='red'),
                 fontsize=9,
                 color='red')

    # Add second vertical line if found
    if second_cross_idx is not None:
        ax1.axvline(x=x_cross, color='green', linestyle=':', linewidth=1)
        ax1.plot(x_cross, dvout_cursor, 'go')
        ax1.annotate(f'({x_cross:.3g}, {dvout_cursor:.3g})',
                     xy=(x_cross, dvout_cursor),
                     xytext=(10, -15),
                     textcoords='offset points',
                     arrowprops=dict(arrowstyle='->', color='green'),
                     fontsize=9,
                     color='green')

    ax1.set_ylabel('dVout/dX')
    ax1.set_xlim(0, 1.8)
    ax1.set_xticks(np.arange(0, 2.0, 0.2))
    ax1.grid(True)
    ax1.legend()

    # --- Bottom plot: Vout ---
    ax2.plot(x, vout, label='Vout', color='tab:blue', linewidth=2)
    ax2.plot(x_cursor, vout_cursor, 'ro')  # Red circle at first vertical line crossing
    ax2.axvline(x=x_cursor, color='red', linestyle=':', linewidth=1)  # Vertical line
    ax2.axhline(y=vout_cursor, color='gray', linestyle=':', linewidth=1)  # Horizontal line
    ax2.annotate(f'({x_cursor:.3g}, {vout_cursor:.3g})',
                 xy=(x_cursor, vout_cursor),
                 xytext=(10, 10),
                 textcoords='offset points',
                 arrowprops=dict(arrowstyle='->', color='blue'),
                 fontsize=9,
                 color='blue')

    # Add second vertical + horizontal cross point on Vout plot if found
    if second_cross_idx is not None:
        ax2.axvline(x=x_cross, color='green', linestyle=':', linewidth=1)
        ax2.axhline(y=vout_cross, color='gray', linestyle=':', linewidth=1)
        ax2.plot(x_cross, vout_cross, 'go')
        ax2.annotate(f'({x_cross:.3g}, {vout_cross:.3g})',
                     xy=(x_cross, vout_cross),
                     xytext=(10, 10),
                     textcoords='offset points',
                     arrowprops=dict(arrowstyle='->', color='green'),
                     fontsize=9,
                     color='green')

    ax2.set_xlabel(df.columns[0])
    ax2.set_ylabel('Vout')
    ax2.set_xlim(0, 1.8)
    ax2.set_xticks(np.arange(0, 2.0, 0.2))
    ax2.grid(True)
    ax2.legend()

    # Title
    fig.suptitle(os.path.basename(file), fontsize=14)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()
