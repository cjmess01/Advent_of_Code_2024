


# Helper function to print the grid
def print_grid(rows, cols, bots_pos):
    dists_from_left =[bot[0] for bot in bots_pos] 
    dists_from_top  = [bot[1] for bot in bots_pos]
    positions = list(zip(dists_from_top,dists_from_left)) 
    print(positions)
    for i in range(rows):
        for j in range(cols):
            # One-liner I am proud of
            # I wanted to do a one liner, but I didn't want to run positions.count((i,j)) twice
            # I originally had it with a := BEFORE the 'if'. 
            # However, it was impossible to use the walrus-created item in the if statement, because ...
            # THE IF STATEMENT GOES FIRST
            # So I did the assignment in the conditional statement instead (making sure to surround the walrus operator in () before)
            # And it works. Pretty cool, right?
            print(val if (val:=positions.count((i,j)))>0 else '.', end="")
        print("")

def partition_and_sum(rows, cols, bots_pos):
    q1,q2,q3,q4 = 0,0,0,0
    get_bounds = lambda length :[int(length/2), int(length/2)] if length%2!=0 else [length/2, length/2+1] 
    height_bounds = get_bounds(rows)
    width_bounds = get_bounds(cols)
    # print(height_bounds)
    # print(width_bounds)

    dists_from_left =[bot[0] for bot in bots_pos] 
    dists_from_top  = [bot[1] for bot in bots_pos]
    positions = list(zip(dists_from_top,dists_from_left)) 
    for position in positions:
        h = position[0]
        w = position[1]
        print(f"{h}, {w}")
        if h < height_bounds[0]:
            if w < width_bounds[0]:
                q1+=1
            elif w > width_bounds[1]:
                q2+=1
        elif h > height_bounds[1]:
            if w < width_bounds[0]:
                q3+=1
            elif w > width_bounds[1]:
                q4+=1


    sum = 0
    
    sum = q1 * q2 * q3* q4
    return sum


        




import sys
import re

if len(sys.argv) != 5:
    print("Usage: python3 p1.py <file_name> <rows> <cols> <num_seconds>")
    exit()

rows =int (sys.argv[2]) 
cols =int(sys.argv[3]) 
seconds = int(sys.argv[4])

lines = []
with open(sys.argv[1], "r") as file:
    lines =[line.strip() for line in file.readlines()] 

bots = []
for entry in lines:
    stats = re.findall(r"-?\d+", entry)
    # Must have the [] thing to convert from generator to list
    # Kind of weird
    bots.append([int(stat) for stat in list(stats)])

# Have bots travel
if(seconds > 0):
    for bot in bots:
        bot[0] += bot[2]*seconds
        bot[1] += bot[3]*seconds
        bot[0] %= cols
        bot[1] %= rows


    


print_grid(rows, cols, bots)
print(partition_and_sum(rows, cols, bots))
