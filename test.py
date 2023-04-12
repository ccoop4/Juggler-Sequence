import numpy as np

x = np.arange(1,40,2)
y = np.floor(x ** (3/2))
working = np.array([1])
previousWorking = np.array([1])

def generateWorkingNumbers():
    temp = np.array([])
    for _ in range(1):
        for item in working:
            to_append = np.arange(item ** 2, (item+1)**2, 2)
            np.concatenate(temp, to_append)
    previousWorking = temp
    np.concatenate(working, temp)

print(working)

for i in range(len(x)):
    print(x[i], " ", (x[i])**3, " ", y[i], '\n')