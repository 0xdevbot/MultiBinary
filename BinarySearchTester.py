import random, BinarySearch
list = []
for i in range(random.randint(20,100)):
    list.append(random.randint(300,399))

print(BinarySearch.binary_search(list, 369))
