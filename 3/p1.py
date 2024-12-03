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
        print(line)
        for i in range(0, len(line)):
            start_char = line[i]
            if(start_char== 'm'):
                print(f"m at {i}")
                last_char = line.find(')', i)
                print(f") at {last_char}")
                if last_char != -1:
                    if re.match(pattern, line[i:last_char+1]):
                        print(f"Match : {line[i:last_char+1]}")
                        matches.append(line[i:last_char+1])




sum = 0
for match in matches:
    print(match)


    first_paren = match.find('(')
    comma = match.find(',')
    last_paren = match.find(')')
    num1 = match[first_paren+1:comma]
    num2 = match[comma+1:last_paren]
    # print(match)
    # print(num1)
    # print(num2)
    sum += int(num1)*int(num2)

print(sum)



