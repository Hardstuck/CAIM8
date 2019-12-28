import argparse
from subprocess import check_output
import numpy as np
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', default=10, type=int)
    args = parser.parse_args()
    k = range(1, args.m + 1)
    times = []
    for i in range(0, args.m):
        timing = 0
        for j in range(0, 5):
            out = check_output(["python3", "lsh.py", "-m " + str(i+1) ])
            out = str(out)
            output = out.split(" ")
            timing += float(output[len(output)-2])
        times.append(timing/5)    
    
    result = zip(k, times)
    plt.plot(k, times)
    plt.xlabel('m')
    plt.ylabel('times')
    plt.title('time - m graph')
    
    plt.yticks(np.arange(0, max(times), 0.1))
    plt.show()

if __name__ == "__main__":
    main()
