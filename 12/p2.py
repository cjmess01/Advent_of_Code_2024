import sys

if len(sys.argv) != 2:
    print("Usage: python3 p1.py <file_name>")
    exit()

lines = []
with open(sys.argv[1], "r") as file:
    lines = [list(line.strip()) for line in file.readlines()]

visited =[[0 for _ in range(len(lines[0]))] for _ in range(0, len(lines))] 

from collections import deque
q = deque()
directions = [(-1,0), (0,1), (1,0), (0,-1)]

plant_areas = {}
plant_perimeters = {}
plant_sides = {}

for i, row in enumerate(lines):
    for j, col in enumerate(row):

        if visited[i][j] == 0:
            # print(f"Beginning {i},{j}")
            plant_areas[f"{lines[i][j]}-{i}{j}"] = 0
            plant_perimeters[f"{lines[i][j]}-{i}{j}"] = 0
            plant_sides[f"{lines[i][j]}-{i}{j}"] = 0
            q.append([i,j])
        while(len(q) != 0):
            curr = q.pop()
            # print(f"Queue getting {curr[0]},{curr[1]}")
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
            get_char = lambda x,y : lines[x][y] if (0<=x<len(lines) and 0<=y<(len(lines[0]))) else '#'

            # directions = [(-1,0), (0,1), (1,0), (0,-1)]
            center = get_char(curr[0], curr[1])
            top = get_char(curr[0]-1, curr[1]+0)
            right = get_char(curr[0]-0, curr[1]+1)
            bottom = get_char(curr[0]+1, curr[1]+0)
            left = get_char(curr[0]+0, curr[1]-1)
            if center != top and center != right:
                plant_sides[f"{lines[i][j]}-{i}{j}"]+=1
                # print("1")
            if center != right and center != bottom:
                plant_sides[f"{lines[i][j]}-{i}{j}"]+=1
                # print("2")
            if center != bottom and center != left:
                plant_sides[f"{lines[i][j]}-{i}{j}"]+=1
                # print("3")
            if center != left and center != top:
                plant_sides[f"{lines[i][j]}-{i}{j}"]+=1
                # print("4")

            tr = get_char(curr[0] - 1, curr[1] + 1)
            br = get_char(curr[0] + 1, curr[1] + 1)
            bl = get_char(curr[0] + 1, curr[1] - 1)
            tl = get_char(curr[0] - 1, curr[1] - 1)

            if center == top == right and tr != center:
                plant_sides[f"{lines[i][j]}-{i}{j}"]+=1
                # print("5")
            if center == right == bottom and br != center: 
                plant_sides[f"{lines[i][j]}-{i}{j}"]+=1
                # print("6")
            if center == bottom == left and bl != center: 
                plant_sides[f"{lines[i][j]}-{i}{j}"]+=1
                # print("7")
            if center == left == top and tl != center: 
                plant_sides[f"{lines[i][j]}-{i}{j}"]+=1
                # print("8")


            



            



                
            
                    

sum = 0
for key in plant_areas:
    print(f"{key} has \n\tarea = {plant_areas[key]}\n\tsides= {plant_sides[key]}\n")
    sum += plant_areas[key] * plant_sides[key]

print(sum)

