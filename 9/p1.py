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
for i in range(0, len(lines)):
    if i % 2 == 0:
        for i in range(0, int(lines[i])):
            raw.append(str(id))
        id+=1
    else:
        for i in range(0, int(lines[i])):
            raw.append('.')
# print(raw)
raw = list(raw)
# print(raw)
front = 0
back = len(raw) - 1
# print(front)
# print(back)
while front < back:
    # print(f"pointers at front:{raw[front]}  back:{raw[back]}")
    # print(f"pointers at front:{front}  back:{back}")
    if(raw[front] == '.' and raw[back] != '.'):
        # print("Swapping ")
        raw[front], raw[back] = raw[back], raw[front]
        front += 1
        back -= 1
    else:
        # print("skipping...")
        front = front + 1 if raw[front] != '.' else front
        back  = back - 1 if raw[back] == '.' else back

sum = 0
for index, character in enumerate(raw):
    if character == '.':
        break
    sum += int(character) * index

print(sum)
