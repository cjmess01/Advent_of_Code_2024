import sys

if(len(sys.argv) < 2):
    print("Include cmd arg for file name")
    exit()


def analyze_letter(i : int, j: int,  lines: list) -> int:
        
    cross_1 = [lines[i-1][j-1], lines[i+1][j+1]]
    cross_2 = [lines[i+1][j-1], lines[i-1][j+1]]
    if ('m' in cross_1 and 's' in cross_1) and ('m' in cross_2 and 's' in cross_2): return 1
    else: return 0


    

    
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
            if char == 'a':
                total += analyze_letter(i,j,lines)
    print(total)
