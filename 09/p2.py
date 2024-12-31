import sys
if(len(sys.argv) < 2):
    print("Include cmd arg for file name")
    exit()

lines = []
with open(sys.argv[1], "r") as file:
    lines = file.readline()
    lines = lines.strip()
raw = []
id = 0
raw_str_len = 0
id_len_and_loc = {}
for i in range(0, len(lines)):
    if i % 2 == 0:
        id_len_and_loc[id] = (lines[i], len(raw)) 
        for j in range(0, int(lines[i])):
            raw.append(str(id))
        id+=1
    else:
        for j in range(0, int(lines[i])):
            raw.append('.')
raw = list(raw)

# print(raw)
for item in reversed(id_len_and_loc.keys()):
    print(f"{item} - {id_len_and_loc[item]}")
    index_of_id = raw.index(str(item))

    def find_gap(min_size, max_location):
        start = 0
        current_gap = 0
        st_curr_gap = 0
        while start < max_location:
            # print(raw[start])
            if raw[start] != '.':
                start+=1
                current_gap = 0
                continue
            if(current_gap == 0):
                st_curr_gap = start
            
            current_gap += 1
            if current_gap == min_size:
                return st_curr_gap
            else:
                start+=1
        return -1
    earliest_gap = find_gap(int(id_len_and_loc[item][0]), index_of_id)
    if(earliest_gap == -1):
        continue
    for i in range(earliest_gap, earliest_gap +int(id_len_and_loc[item][0]) ):
        raw[i] = item
    for i in range(int(id_len_and_loc[item][1]), int(id_len_and_loc[item][1]) +int(id_len_and_loc[item][0]) ):
        raw[i] = '.'

print(raw)

sum = 0
for index, character in enumerate(raw):
    if character == '.':
        continue 
    sum += int(character) * index

print(sum)















































# import sys
# if(len(sys.argv) < 2):
#     print("Include cmd arg for file name")
#     exit()
#
# lines = []
# with open(sys.argv[1], "r") as file:
#     lines = file.readline()
#     lines = lines.strip()
#
# raw = []
# id = 0
# raw_str_len = 0
#
# # The key is id, Will contain a tuple of a length and starting index
# id_len_and_loc = {}
# # The key is LENGTH, and will point to a list of indexes that have a gap of that length
# space_len_and_loc = {}
# for i in range(0, len(lines)):
#     if i % 2 == 0:
#         id_len_and_loc[id] = (lines[i], raw_str_len) 
#         for j in range(0, int(lines[i])):
#             raw_str_len += 1
#             raw.append(str(id))
#         id+=1
#     else:
#         if not lines[i] in space_len_and_loc.keys():
#             space_len_and_loc[lines[i]] = []
#         space_len_and_loc[lines[i]].append(raw_str_len) 
#         for j in range(0, int(lines[i])):
#             raw_str_len += 1
#             raw.append('.')
#
# print(id_len_and_loc)
# print(space_len_and_loc)
# for key in id_len_and_loc.keys():
#     print(f"{key} - {id_len_and_loc[key]}")
# for spot in space_len_and_loc.keys():
#     print(f"{spot} - {space_len_and_loc[spot]}")
# raw = list(raw)
# print(raw)
# # print(front)
# # print(back)
# for i in range(id-1, -1, -1):
#     # print(f"On id - {i}")
#     required_length = id_len_and_loc[i][0]
#     current_location = id_len_and_loc[i][1]
#     max_space = max(space_len_and_loc.keys())
#
#     earliest_match_index = raw_str_len + 5
#     len_of_earliest_match_index = raw_str_len + 5
#     for j in range(int(required_length), int(max_space)+1):
#         if(str(j) in space_len_and_loc.keys() and len(space_len_and_loc[str(j)]) > 0 and space_len_and_loc[str(j)][0] < current_location):
#             earliest_match_index = space_len_and_loc[str(j)][0]
#             len_of_earliest_match_index = j
#     if(not earliest_match_index < raw_str_len):
#         continue
#
#
#     # print(f"Found spot for {i} at a hole of {len_of_earliest_match_index} located at {earliest_match_index}")
#     id_len_and_loc[i] = (required_length, earliest_match_index)
#     space_len_and_loc[str(len_of_earliest_match_index)].pop(0)
#     if not str(len_of_earliest_match_index - int(required_length)) in space_len_and_loc.keys():
#         space_len_and_loc[str(len_of_earliest_match_index - int(required_length))] = []
#     space_len_and_loc[str(len_of_earliest_match_index - int(required_length))].append(earliest_match_index + int(required_length)) 
#     space_len_and_loc[str(len_of_earliest_match_index - int(required_length))].sort()
#
#
#     # print(f"New whole created of length {len_of_earliest_match_index - int(required_length)} at index {earliest_match_index + int(required_length)}")
#     # print(space_len_and_loc)
#
#
#
#
#
#     # Get the needed length
#     # search space dict for lengths of that side
#     # If found, do following
#     #   Change id_len_and_loc for the id, change the starting index only
#     #   Change space_len_and_loc, first remove first item of list
#     #   Add new item to prev_length - id_len with the index prev_index+ length_of_id
#     #   Then, add a new item (in order!) to the 
#
#
# # print(id_len_and_loc)
# reconstructed = list('.') * raw_str_len
# for entry in id_len_and_loc.keys():
#     # print(f"{entry} - {id_len_and_loc[entry]}")
#     starting_index =int(id_len_and_loc[entry][1]) 
#     ending_index   = int(id_len_and_loc[entry][0]) + starting_index
#     # print(starting_index)
#     # print(ending_index)
#     for i in range(starting_index, ending_index):
#         reconstructed[i] = entry
#     # print(reconstructed)
#
# print(reconstructed)
# sum = 0
# for index, character in enumerate(reconstructed):
#     if character == '.':
#         continue 
#     sum += int(character) * index
#
# print(sum)
