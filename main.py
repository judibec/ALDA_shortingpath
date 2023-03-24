from functions import shortingPath
from complexity import executionTime
import matplotlib.pyplot as mlt

if __name__ == "__main__":
    table = executionTime.take_execution_time(500, 2000, 100, 5)
    xpoints = []
    ypoints = []
    for row in table:
        print(row)
        xpoints += [row[2]]
        ypoints += [row[0]]

    mlt.plot(xpoints, ypoints)
    mlt.show()

