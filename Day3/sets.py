# Sets
# can be declared by using the set() keyword in parenthesis or the bracket
# no duplicates, not sorted in indexes or re-arrange the elements. Immutable

my_set = {1, 2, 3, 4, 5, 1, 3, 2}
print(type(my_set))
print(my_set)

other_set = set((1, 2, 3))
print(type(other_set))
print(other_set)

print(my_set.pop())
print(my_set)

# you can include tuples in sets
tuple_set = set((1, 4, 12, 5, (1, 2, 3), -1, 3))
print(tuple_set)

print(2 in tuple_set)
print(4 in tuple_set)

# Sets Practice= Join the following sets into one, called
my_set_1 = {1, 2, "three", "four"}
my_set_2 = {"three", 4, 5}
my_set_3 = set((1, 2, "three", "four", "three", 4, 5))

raffle = {"Rachel", "Monica", "Phoebe", "Joey", "Chandler", "Ross"}
raffle = set(("Rachel", "Monica", "Phoebe", "Joey", "Chandler"))
print(raffle)


