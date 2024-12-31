import sys
import queue

if len(sys.argv) != 2:
    print(len(sys.argv))
    print("Please include a file name")
    exit()

lines = []
with open(sys.argv[1], "r") as file:
    lines = [list(map(int, line.strip())) for line in file.readlines()]

starts = []
for lineno, line in enumerate(lines):
    for charno, char in enumerate(line):
        if char == 0:
            starts.append((lineno, charno))

directions = [(0,1), (0,-1), (1,0), (-1,0)] 

q = queue.Queue() 
sum = 0
for this_start in starts: 
    peaks = set()
    q.put(this_start)

    while not q.empty():
        item = q.get()
        current_val = lines[item[0]][item[1]]
        print(f"At {item}, with a value of {current_val}")

        get_new_spot = lambda x, y : lines[x][y] if 0 <= x < len(lines) and 0 <= y < len(lines[0]) else -1

        if current_val == 9:
            peaks.add(item)
        else: 
            for i in range(0,4):
                i, j = directions[i]
                if get_new_spot(item[0]+i,item[1] + j) == current_val + 1:
                    print(f"Enquing {(item[0]+i,item[1] + j)} because == {current_val+1}")
                    q.put((item[0]+i,item[1]+j))
                else:
                    print(f"{(item[0]+i,item[1] + j)} - {current_val} does not equal {current_val+1}")
    sum += len(peaks)
    print(this_start)
    print(peaks)

print(sum)
        

        


