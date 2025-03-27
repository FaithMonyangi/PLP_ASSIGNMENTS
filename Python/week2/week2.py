my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
my_list.insert(2, 15)
print(my_list)
list2 = [50, 60, 70]
my_list.extend(list2)
print(my_list)
del my_list[-1]
print(my_list)
my_list.sort()
print(my_list)
index_30 = my_list.index(30)  # Find the index of 30
print(index_30)  # Output: 3

