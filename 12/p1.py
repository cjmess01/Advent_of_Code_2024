import sys

if len(sys.argv) != 2:
    print("Usage: python3 p1.py <file_name>")
    exit()

lines = []
with open(sys.argv[1], "r") as file:
    lines = [list(line.strip()) for line in file.readlines()]


# Make a parallel 2d array, and as I observe spots within lines, mark them in the parallel array! 

# If I try and investigate a marked one, continue.

# Easy peasy 
visited =[[0 for _ in range(len(lines[0]))] for _ in range(0, len(lines))] 

from collections import deque
q = deque()

directions = [(0,-1), (0,1), (-1,0), (1,0)]

plant_areas = {}
plant_perimeters = {}

for i, row in enumerate(lines):
    for j, col in enumerate(row):

        if visited[i][j] == 0:
            print(f"Beginning {i},{j}")
            plant_areas[f"{lines[i][j]}-{i}{j}"] = 0
            plant_perimeters[f"{lines[i][j]}-{i}{j}"] = 0

            q.append([i,j])
        while(len(q) != 0):
            curr = q.pop()
            print(f"Queue getting {curr[0]},{curr[1]}")
            visited[curr[0]][curr[1]] = 1 
            plant_areas[f"{lines[i][j]}-{i}{j}"] += 1
            # print(f"Adding 1 to AREA {lines[curr[0]][curr[1]]} for {curr[0]},{curr[1]}")
            # for visit in visited:
            #     print(visit)

            for direction in directions:
                newI = curr[0] + direction[0]
                newJ = curr[1] + direction[1]



                if 0 <= newI < len(lines) and 0<=newJ<len(lines[0]):
                    if lines[newI][newJ] == lines[curr[0]][curr[1]] and visited[newI][newJ] == 0:
                        visited[newI][newJ] = 1
                        q.append([newI, newJ])
                    elif lines[newI][newJ] != lines[curr[0]][curr[1]]:
                        plant_perimeters[f"{lines[i][j]}-{i}{j}"] += 1
                else:
                    plant_perimeters[f"{lines[i][j]}-{i}{j}"] += 1
                    


        



sum = 0
for key in plant_areas:
    print(f"{key} has \n\tarea = {plant_areas[key]}\n\tperimeter= {plant_perimeters[key]}\n")

    sum += plant_areas[key] * plant_perimeters[key]


print(sum)
