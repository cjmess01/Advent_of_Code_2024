import sys
import re
if(len(sys.argv) < 2):
    print("Include cmd arg for file name")
    exit()


matches = []
on = 1

do_pattern = r"do[(][)]"
dont_pattern = r"don[']t[(][)]"
mul_pattern = r"mul[(][0-9]+,[0-9]+[)]"

with open(sys.argv[1], "r") as file:
    lines = file.readlines()
    for line in lines:
        for i in range(0, len(line)):
            start_char = line[i]
            if(start_char == 'd'):
                last_char = line.find(')', i)
                if last_char != -1:
                    if re.match(do_pattern, line[i:last_char+1]):
                        on = 1
                    if re.match(dont_pattern, line[i:last_char+1]):
                        on = 0



            if(start_char == 'm'  and on == 1):
                last_char = line.find(')', i)
                if last_char != -1:
                    if re.match(mul_pattern, line[i:last_char+1]):
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



