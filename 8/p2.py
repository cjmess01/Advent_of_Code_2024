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
        add_points = lambda p1, p2: (p1[0] + p2[0], p1[1] + p2[1])
        sub_points = lambda p1, p2: (p1[0] - p2[0], p1[1] - p2[1])
        print(pair)
        
        curr = add_points(pair[0], [0,0])
        while is_valid(curr):
            unique_antis.add(curr)
            curr = add_points(curr, slope)
        curr = add_points(pair[0], [0,0])
        while is_valid(curr):
            unique_antis.add(curr)
            curr = sub_points(curr, slope)



print(len(unique_antis))
        


