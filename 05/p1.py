import sys



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

    # print('one entry:')
    # print(local_dict)
    # print(len(local_rules))
    # print(local_rules)
    failure = 0
    for rule in local_rules:
        if(local_dict[rule[0]] > local_dict[rule[1]]):
            failure = 1

    if(failure == 0):
        sum += int(entry[int(len(entry)/2)])

    


    

    

print(sum)
