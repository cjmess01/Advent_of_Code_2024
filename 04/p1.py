
import sys

if(len(sys.argv) < 2):
    print("Include cmd arg for file name")
    exit()


def analyze_letter(i : int, j: int, prev_letter: str, lines: list, dI : int = 0, dJ : int = 0) -> int:
    total = 0



    next = ' '
    if prev_letter == 'x': next = 'm'
    elif prev_letter == 'm': next = 'a'
    elif prev_letter == 'a': next = 's'
    elif prev_letter == 's': return 1 
    

    if(next == 'm'):
        # print("Parsing 8 directions")
        parse_m = lambda ii,jj  : lines[ii][jj] == 'm'
        for x in range(-1, 2):
            for y in range(-1, 2):
                if(parse_m(i+x, j+y)):
                    # print(f"M at {i+x,j+y}")
                    total += analyze_letter(i+x,j+y, 'm', lines, x,y)
                
    else:
        # print("Only going 1 direction")
        parse_letter = lambda ii,jj, letter  : lines[ii][jj] == letter
        if(next == 'a'):
            if parse_letter(i+dI, j+dJ, 'a'):
                total += analyze_letter(i+dI,j+dJ, 'a', lines, dI, dJ)
        if(next == 's'):
            if parse_letter(i+dI, j+dJ, 's'):
                total += analyze_letter(i+dI,j+dJ, 's', lines, dI,dJ)
        


    
    return total 
# total = all 8 neighbors with next letter
# AHHH But I have to have the direction as part of it
    
    



with open(sys.argv[1], "r") as file:
    lines = file.readlines()
    for index, line in enumerate(lines, start=0):
        lines[index] = 'f'+line.strip().lower()+'f'
    lines.insert(0, f"{'f' * (len(lines[1]))}" )
    lines.insert(len(lines), f"{'f' * (len(lines[1]))}" )

        
    total = 0
    
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            # print(char)
            if char == 'x':
                total += analyze_letter(i,j,'x',lines)
            # if(char == 'x'):
            #     print("1 x")
    print(total)
