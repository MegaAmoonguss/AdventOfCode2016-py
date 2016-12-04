'''
Created on Dec 4, 2016

@author: Graham
'''
import math

with open("Day01_Input.txt") as file:
    directions = file.read().split(", ")

# The direction being faced, 0 = North, 1 = East, 2 = South, 3 = West
facing = 0
coordinates = [0, 0]
for d in directions:
    if d[0] == "R":
        if facing == 3:
            facing = 0
        else:
            facing += 1
    else:
        if facing == 0:
            facing = 3
        else:
            facing -= 1
            
    if facing == 0:
        coordinates[1] += int(d[1:])
    elif facing == 1:
        coordinates[0] += int(d[1:])
    elif facing == 2:
        coordinates[1] -= int(d[1:])
    else:
        coordinates[0] -= int(d[1:])
        
print(coordinates)
print(int(math.fabs(coordinates[0] + coordinates[1])), "blocks away.")