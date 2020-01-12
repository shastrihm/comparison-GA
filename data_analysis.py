"""
Computes statistics from a text file
"""
import numpy
import os

def analyze(fnames):
    """
    returns average, standard deviation of data points in fnames
    """
    lines = []
    for fname in fnames:
        with open (fname, 'r') as f:
            lines += [float(line.rstrip()) for line in f]

    return [numpy.mean(lines), numpy.std(lines)]


NUM_RUNS = 10
rep = "BRG" # change to "BIN" for binary stats
for f in range(1,6):
    fnames = [os.path.join("caruana_data", "f" + str(f) + "_" + rep + "_T" + str(i) + ".txt") for i in range(1,NUM_RUNS+1)]
    print(analyze(fnames))
