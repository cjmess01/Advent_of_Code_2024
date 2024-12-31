# This solution uses min heaps with duplicates to store the smallest value at the beginning of the list
# Then, it is relatively simple to keep popping the two smallest items in the list to continually summing the larger values together
# Overall pretty easy
# My variable naming conventions could use some work



# ANSWER WAS 2430334


import heapq

list1_heap = []
list2_heap = []
with open("data.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        nums =(line.split('   '))
        heapq.heappush(list1_heap, int(nums[0]))
        heapq.heappush(list2_heap, int(nums[1]))

sum = 0
for i in range(0, len(list1_heap)):
    item1 = heapq.heappop(list1_heap)
    item2 = heapq.heappop(list2_heap)
    sum += item1 - item2 if item1 > item2 else item2-item1
print(sum)
