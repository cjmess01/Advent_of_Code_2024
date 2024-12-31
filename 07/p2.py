from typing import List



def can_equal(total : int, numbers : List[int], position: int = 0, curr_val : int = 0) -> bool:
    combine = lambda x,y : int(str(x) + str(y))
    if(position == len(numbers)):
        # print(f"evaluating on {curr_val}")
        return curr_val == total

    else: 
        return can_equal(total, numbers, position+1, max(curr_val, 1) * numbers[position]) or can_equal(total, numbers, position+1, curr_val + numbers[position]) or can_equal(total, numbers, position+1, combine(curr_val, numbers[position]))


import sys


if(len(sys.argv) < 2):
    print("Include cmd arg for file name")
    exit()
lines = []
with open(sys.argv[1], "r") as file:
    lines= file.readlines()

# Pretty good one liner, expecially with the list comprehension with the [1:], which gets rid of the extra " " in the list of factors
equations = [[int(line.split(':')[0]), line.split(':')[1].split(" ")[1:]] for line in lines]
sum = 0

for index, eq in enumerate(equations):
    for i in range(0, len(eq[1])):
        eq[1][i] = int(eq[1][i].strip())
    if (result:=can_equal(int(eq[0]), eq[1])):
        sum += eq[0]
    print(result)
print(sum)

