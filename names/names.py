# This solution uses a binary search tree 
# Worst case time complexity would be 0(n)
# The original solution took 11 seconds to run on my computer.
# The updated solution took less than 1 second.
# A balanced binary search tree will improve the time complexity to O(log n)


import time
from name_checker import NameChecker

start_time = time.time()

f = open('names_1.txt', 'r')
lists_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
lists_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# This was the original solution provided with the code

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

duplicates = []

first_name_list = NameChecker(lists_1[0])
for i in range(1, len(lists_1)):
    first_name_list.insert(lists_1[i])

for list_2 in lists_2:
    if first_name_list.contains(list_2):
        duplicates.append(list_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

