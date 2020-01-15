"""
Computes statistics from a text file
"""
import numpy
import os
import math

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

def best_sol_perf(fnames, key, out_fname):
    """
    writes average best sol perf averaged over fnames to .dat file out_fname

    Output .dat file will be in same level directory as this python file
    """
    sols = []
    if key == min:
        best = math.inf 
    else:
        best = -math.inf

    for fname in fnames:
        lines = []
        with open(fname, 'r') as f:
            for line in f:
                best = key(best, float(line.rstrip()))
                lines.append(best)
            sols.append(lines)

    listify_jth_coord = lambda l,j : [l[i][j] for i in range(len(l))]

    sols = [round(numpy.mean(listify_jth_coord(sols, j)), 4) for j in range(len(sols[0]))]

    # dump to .dat file e.g.
    # Eval #    mean best sol
    # 1         sols[1]
    # ...       ...
    # i         sols[i]

    f = open(out_fname, 'w')
    f.write("Eval no." + "\t" + "mean best sol" + "\n")
    for i in range(len(sols)):
        f.write(str(i) + "\t" + str(sols[i]) + "\n")

    print("Output best sol plot data to " + out_fname)





NUM_RUNS = 1000
reps = ["BIN", "BRG", "UBL", "NGG"]
for rep in reps:
    for f in range(1,6):
        fnames = [os.path.join("caruana_data", "f" + str(f) + "_" + rep + "_T" + str(i) + ".txt") for i in range(1,NUM_RUNS+1)]
        print(rep, ' f' + str(f))
        print(analyze(fnames))
        best_sol_perf(fnames, min, rep + "_f" + str(f) + ".dat")
