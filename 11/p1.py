import sys
from collections import defaultdict

if len(sys.argv) != 3:
    print("Usage: python3 p1.py <file> <num_generations")
    exit()

generations =int(sys.argv[2]) 

lines = []
with open(sys.argv[1], "r") as file:
    stones = [int(item.strip()) for item in file.readlines()[0].split(" ")]

freqs = defaultdict(int)
for item in stones:
    freqs[item] += 1

num_cache = {}
for i in range(0, generations):
    print(f"Gen {i}")
    print(freqs)
    next_gen = defaultdict(int) 
    next_gen[1] = freqs[0]
    for key in freqs.keys():
        if freqs[key] == 0 or key == 0:
            print(f"Skipping {key}")
            continue
        elif key in num_cache:
            for item in num_cache[key]:
                print(f"Adding {item} from cache")
                next_gen[item] += freqs[key]
        else:
            if len(str(key)) % 2 == 0:
                half = int(len(str(key)) / 2)
                first_half =int(str(key)[0:half]) 
                second_half = int(str(key)[half: len(str(key))]) 
                next_gen[first_half] += freqs[key]
                next_gen[second_half] += freqs[key]
                num_cache[key] = [first_half, second_half]
                print(f"Adding {first_half}, {second_half}, first time")

            else:
                next_gen[key*2024] += freqs[key]
                num_cache[key] = [2024 * key]
                print(f"Adding {key*2024}, first time")
    freqs.clear()
    freqs = next_gen

sum = 0
for key in freqs.keys():
    sum += freqs[key]

print(sum)



