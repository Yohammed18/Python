my_list = ['a', 'b', 'c']
my_list2 = ['d', 'e', 'f']
my_list3 = my_list + my_list2
print(type(my_list))
print(len(my_list))
print(my_list[2])
print(my_list[0:2])
print(my_list[::-1])
print(my_list3)
my_list3.append('g')
print(my_list3)
my_list3.pop(3)
print(my_list3)
unordered_list = ['z', 'r', 'a', 'c', 'q']
unordered_list.sort()
print(unordered_list)
unordered_list.reverse()
print(unordered_list)
