
import sys


class State:
    def __init__(self, x,y,d):
        self.x = x
        self.y = y
        self.d = d
    def __eq__(self, other) -> bool:
        return(self.x == other.x and self.y == other.y and self.d == other.d)
    def __hash__(self):
        return hash((self.x, self.y, self.d))

if(len(sys.argv) < 2):
    print("Include cmd arg for file name")
    exit()

lines = []
with open(sys.argv[1], "r") as file:
    lines= [list(line.strip()) for line in file.readlines()]

start_char= ['>', 'v', '<', '^']
movement =  ['0,1', '1,0', '0,-1', '-1,0']

char = ''
line_id = 0
letter_id = 0
has_start = lambda line: next((c for c in start_char if c in line), None)

for index, line in enumerate(lines):
    if((char := has_start(line)) != None):
        line_id = index
        letter_id = line.index(char)
        print(char)
        break


    # print(f"{movement[start_char.index(char or '>')]}")
    # put in a direction, current location, and the map pointer
    # return the map and if there was a change
def test_map(current_map):
    states = set()
    def tick(direction, pos, char, map, changes):
        if State(pos[0],pos[1], char) in states:
            states.clear()
            # print("Loop detected")
            return [changes, True]
        else:
            states.add(State(pos[0],pos[1], char))
        # print(pos)
        new_pos = [pos[0] + direction[0], pos[1]+direction[1]]
        # print(new_pos)
        if(not (0 <= new_pos[0] < len(lines))):
            # print("OUT OF BOUNDS")
            return [changes]
        elif(not (0 <= new_pos[1] < len(lines[0]))):
            # print("OUT OF BOUNDS")
            return [changes]
        elif(map[new_pos[0]][new_pos[1]]) == '.' or (map[new_pos[0]][new_pos[1]]) == 'X':
            n_c = map[new_pos[0]][new_pos[1]] 
            if n_c == '.':
                changes = changes + 1
            map[pos[0]][pos[1]] = 'X'
            map[new_pos[0]][new_pos[1]] = char
                
            # print("moved")
            return [direction, new_pos, char, map, changes]
        elif(map[new_pos[0]][new_pos[1]]) == '#':
            n_char = start_char[(start_char.index(char) + 1) % len(start_char)]
            # print("boundary")
            return [[int(object) for object in movement[start_char.index(n_char or '>')].split(',')], pos, n_char, map, changes]
        return []


    d =[int(object) for object in movement[start_char.index(char or '>')].split(',')] 
    # while(result:=tick(d, [line_id, letter_id], char, lines) != -1):
    #     continue

    changes = 0
    result = [d, [line_id, letter_id], char, current_map, changes]
    while(len(result:=tick(*result)) == 5):
        # for line in lines:
        #     print(line)
        continue

    if(len(result) == 1):
        # print("No loop detected")
        return 0
    else:
        # print("Loop!!!")
        return 1
foo = 0

def deep_copy(original_list):
    n_list = []
    for i in range(len(original_list)):
        n_list.append(original_list[i].copy())
    return n_list

for i_index, line in enumerate(lines):
    for j_index, word in enumerate(line):
        curr_lines = deep_copy(lines)
        if curr_lines[i_index][j_index] == '.':
            curr_lines[i_index][j_index] = '#'
            foo += test_map(curr_lines)
        print(f"Completed {i_index}:{j_index}")
        


print(foo)
# print(test_map(lines))


    

    
    



