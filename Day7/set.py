# Set is a collection of items. Let me take you back to your elementary or high school Mathematics lesson. The Mathematics definition of a set can be applied also in Python. Set is a collection of unordered and un-indexed distinct elements. In Python set is used to store unique items, and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# Find the length of the set it_companies
print(f"Set length: {len(it_companies)}")
# Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)
# Insert multiple IT companies at once to the set it_companies
it_companies.update(["NVDIA", "AMD", "Palantir"])
print(it_companies)
# Remove one of the companies from the set it_companies
it_companies.remove("Oracle")
print(it_companies)
# What is the difference between remove and discard: when using remove(), the application will raise an error if not handle, whereas discard() will do nothing.
# Exercises: Level 2
# Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
A.union(B)
print(A)
# Find A intersection B
print(f"A & B intersection= {A.intersection(B)}")
# Are A and B disjoint sets
print(A.isdisjoint(B)) # False because there are common numbers
# Join A with B and B with A
A_B = A.union(B)
B_A = B.union(A)
print(A_B)
print(B_A)
# What is the symmetric difference between A and B
print(A.symmetric_difference(B)) # {27, 28}
# Delete the sets completely
del A
del B




















