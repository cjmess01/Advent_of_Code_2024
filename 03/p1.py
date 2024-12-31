import sys
import re
if(len(sys.argv) < 2):
    print("Include cmd arg for file name")
    exit()


matches = []

pattern = r"mul[(][0-9]+,[0-9]+[)]"

with open(sys.argv[1], "r") as file:
    lines = file.readlines()
    for line in lines:
        for i in range(0, len(line)):
            start_char = line[i]
            if(start_char== 'm'):
                last_char = line.find(')', i)
                if last_char != -1:
                    if re.match(pattern, line[i:last_char+1]):
                        matches.append(line[i:last_char+1])




sum = 0
for match in matches:

    first_paren = match.find('(')
    comma = match.find(',')
    last_paren = match.find(')')
    num1 = match[first_paren+1:comma]
    num2 = match[comma+1:last_paren]
    sum += int(num1)*int(num2)

print(sum)



