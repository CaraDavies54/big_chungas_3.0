#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

def plot_csv(csv_file:str, N, title:str=None) -> None:
    """ Plots the timings from a given CSV file, using matplotlib.
    :pre: file contains N=3 or N=5 values per line
    :raises ValueError: if precondition not satisfied
    """
    with open(csv_file) as csv:
        # This assumes the CSV contains 3 columns: {instance size, construction time, process time}
        try:
            data = np.loadtxt(csv_file, delimiter=',', unpack=True)
        except Exception:
            pass
        # Set up the figure and axes
        fig = plt.figure()
        ax = plt.axes()
        ax.set(xlabel='list size', ylabel='time (s)', title=title)
        if N == 3: 
            (size, construct, sort) = data
        elif N == 5: 
            (size, construct, sort, sorted, reversed) = data
        else:
            raise ValueError("N must be 3 or 5")
        # Plot the data, and place the legend
        ax.plot(size, construct, label='construction')
        ax.plot(size, sort, label='process')
        if N == 5:
            ax.plot(size, sorted, label='Sorted')
            ax.plot(size, reversed, label='Reversed')
        ax.legend()
        # Save the figure as a pdf.
        # Alternatively, call fig.show() to display the figure.
        fig.savefig(csv_file + '.pdf', format='pdf')
        #fig.show()

if __name__ == '__main__':
  import sys
  csv_file = sys.argv[1]
  plot_csv(csv_file)
