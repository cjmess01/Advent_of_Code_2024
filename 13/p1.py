


def solve_system(eq1, eq2):
    
    factor1 = eq1[0]
    factor2 = eq2[0]

    eq1_w_factor = [x*factor2 for x in eq1]
    eq2_w_factor = [x*factor1 for x in eq2]
    eq_solved = [eq1_w_factor[0] - eq2_w_factor[0],eq1_w_factor[1] - eq2_w_factor[1],eq1_w_factor[2] - eq2_w_factor[2]] 

    j = eq_solved[2] / eq_solved[1]
    i = (eq1[2] - eq1[1]*j) / eq1[0] 
    return i,j
    



import sys
import re
if len(sys.argv) != 2:
    print("Usage: python3 p1.py <file_name>")
    exit()

nums = []
with open(sys.argv[1], "r") as file:
    lines = file.readlines()
    nums = [re.findall(r'\d+', line) for line in lines if len(line)>1]

possible = []
for i in range(0, int(len(nums)/3)):
    nums1 =(nums[i*3]) 
    nums2 = nums[i*3+1]
    nums3 = nums[i*3+2]
    eq1 = [int(nums1[0]),int(nums2[0]),int(nums3[0])]
    eq2 = [int(nums1[1]),int(nums2[1]),int(nums3[1])]
    ans = solve_system(eq1, eq2)
    if ans[0] % 1 != 0 or ans[1] % 1 != 0:
        print("Failure")
    else:
        print(i)
        possible.append(ans)
sum = 0
for match in possible:
    sum += match[0]*3 + match[1]
print(sum)


    
