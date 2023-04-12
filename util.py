import numpy as np
from math import floor, sqrt, pow


def readSeq():
    with open('jugglerseq.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            data = line.split(" ")
            if (int(data[1]) > 100):
                print(line)

def findNumberSteps(n):
    current = n
    count = 0
    while True:
        if current == 1:
            return count
        if current % 2 == 0:
            current = floor(sqrt(current))
        else:
            current = floor(pow(current, 1.5))
        count += 1

def generateMoreNumbers():
    with open('jugglerseq.txt', 'a') as f:
        for i in range(100000, 10000000):
            f.write(str(i))
            f.write(" ")
            f.write(str(findNumberSteps(i)))
            f.write('\n')

def getData():
    numbers = []
    steps = []
    with open('jugglerseq.txt', 'r') as f:
        count = 0
        for line in f.readlines():
            if count == 10000000:
                break
            line = line.rstrip('\n')
            data = line.split(" ")
            numbers.append(data[0])
            steps.append(data[1])
    return numbers, steps

def generateSeq(rule, start, end):
    for i in range(start, end + 1):
        print(i, " ", rule(i), '\n')