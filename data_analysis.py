"""
Computes statistics from a text file
"""
import numpy
import os

def analyze(fnames):
    """
    returns average, standard deviation of data points in fnames

    # Table 3
    """
    lines = []
    for fname in fnames:
        with open(fname, 'r') as f:
            lines += [float(line.rstrip()) for line in f]

    return [round(numpy.mean(lines), 4), round(numpy.std(lines), 4)]

def best_sol_perf(fnames, key):
    """
    returns best sol performance 
    """
    sols = []

    for fname in fnames:
        lines = []
        with open(fname, 'r') as f:
            lines += [float(line.rstrip()) for line in f]
            sols.append(key(lines))

    return [round(numpy.mean(sols), 4), round(numpy.std(sols), 4)]



NUM_RUNS = 5
reps = ["BIN", "BRG", "UBL", "NGG"]
for rep in reps:
    for f in range(1,6):
        fnames = [os.path.join("caruana_data", "f" + str(f) + "_" + rep + "_T" + str(i) + ".txt") for i in range(1,NUM_RUNS+1)]
        print(rep, ' f' + str(f))
        print(analyze(fnames), best_sol_perf(fnames, min))
