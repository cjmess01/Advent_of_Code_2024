# Read in data

# For every special character in the map, find all other matching ones
# Form a line for each pair, and calculate slope, which will always be two whole numbers (rise and run)
# Use slope on either side, positive y on top line, negative on other, to find two antinodes
# If both antinodes are within bounds, add to set (include symbol with set)
# Add the single current antinode location to the visited set. If it is visited, do not make more connections with it
# get length of set

import sys
from collections import deque
if(len(sys.argv) < 2):
    print("Include cmd arg for file name")
    exit()

lines = []
with open(sys.argv[1], "r") as file:
    lines= [list(line.strip()) for line in file.readlines()]


antenna_d ={}
for i in range(0, len(lines)):
    for j in range(0, len(lines[0])):
        if(lines[i][j] != '.'):
            if not str(lines[i][j]) in antenna_d.keys():
                antenna_d[lines[i][j]] = []
            antenna_d[str(lines[i][j])].append([i,j])

unique_antis = set()

for ant in antenna_d.keys():
    all_pairs = [[antenna_d[ant][i], antenna_d[ant][j]] for i in range(0, len(antenna_d[ant])) for j in range(i+1, len(antenna_d[ant]))]
    get_slope = lambda p1,p2 : [(p1[0]- p2[0]), (p1[1] - p2[1])]
    is_valid = lambda p : 0 <= p[0] < len(lines) and 0 <= p[1] < len(lines[0])
    for pair in all_pairs:
        slope = get_slope(pair[0], pair[1])
        anti1 =(pair[0][0] + slope[0], pair[0][1] + slope[1]) 
        anti2 =(pair[1][0] - slope[0], pair[1][1] - slope[1])
        if(is_valid(anti1)): 
            print(f"{anti1} is valid")
            unique_antis.add(anti1)
        if(is_valid(anti2)): 
            print(f"{anti2} is valid")
            unique_antis.add(anti2)

print(len(unique_antis))
        




