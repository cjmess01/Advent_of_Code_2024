# Using a python dict, which uses a hashtable on the backend, get all the values and add them up
# This should be effectively O(n)


# Answer was 28786472
list2_map = {}

list1 = []

with open("data.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        nums =[int(obj) for obj in line.split('   ')]

        list1.append(nums[0])

        if nums[1] in list2_map.keys():
            list2_map[nums[1]] += 1
        else:
            list2_map[nums[1]] = 1


sum = 0
for val in list1:
    if val in list2_map:
        sum += val * list2_map[val]

print(sum)



