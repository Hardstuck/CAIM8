import argparse
from subprocess import check_output
import numpy as np
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', default=20, type=int)
    args = parser.parse_args()
    k = range(1, args.k + 1)
    times = []
    for i in range(0, args.k):
        timing = 0
        for j in range(0, 5):
            out = check_output(["python3", "lsh.py", "-k " + str(i+1) ])
            out = str(out)
            output = out.split(" ")
            timing += float(output[len(output)-2])
        times.append(timing/5)    
    
    result = zip(k, times)
    plt.plot(k, times)
    plt.xlabel('k')
    plt.ylabel('times')
    plt.title('time - k graph')
    
    plt.yticks(np.arange(0, max(times), 0.1))
    plt.show()

if __name__ == "__main__":
    main()
