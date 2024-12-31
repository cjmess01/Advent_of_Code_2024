
import sys

def check_failure(l_dict, l_rules):
    for rule in l_rules:
        if(l_dict[rule[0]] > l_dict[rule[1]]):
            return [True, rule]

    return [False, None]


if(len(sys.argv) < 2):
    print("Include cmd arg for file name")
    exit()


lines = []
with open(sys.argv[1], "r") as file:
    lines = file.readlines() 

rules = []
updates = []


for index, line in enumerate(lines):
    lines[index] = line.strip()
    if(lines[index].find('|') != -1):
        rules.append(lines[index].split('|'))
    else:
        updates.append(lines[index].split(','))


sum = 0

for index, entry in enumerate(updates):
    if(entry[0] == ''):
       continue
    local_dict = {item:index for index, item in enumerate(entry)}
    residents = local_dict.keys()
    local_rules = []
    for rule in rules:
        if ((rule[0] in local_dict.keys()) and (rule[1] in local_dict.keys())):
            local_rules.append(rule)

    # Really cool walrus operator, allows assigning a variable within an expression
    failed_at_any_point = 0
    while (condition := check_failure(local_dict, local_rules))[0]:
        failed_at_any_point = 1
        data = condition[1]
        # print("Fixing...")
        # # if a rule has failed, that means the first number should be 
        # # before the second, but it isn't 
        # # therefore, (in 97|75, it must be changed so 97 is before 75)
        # # we could just insert 97 into where 75 is, and have the rest move up
        # print(f"{data[0]}|{data[1]}")
        values = list(local_dict.keys())
        values.remove((data[0]))
        values.insert(values.index(data[1]), data[0])
        local_dict = {item:index for index, item in enumerate(values)}
        
        # print(local_dict)

    if failed_at_any_point == 1:
        sum +=int(list(local_dict.keys())[int(len(list(local_dict.keys())) / 2)])


        
        



        

        


    


    

    

print(sum)
