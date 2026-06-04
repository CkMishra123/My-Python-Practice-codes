#1.Create two sets A and B. Find their union, intersection, and difference (A - B).
a={1,2,3,4,5}
b={3,2,4,9,6}
print(a.union(b)) #union of sets
print(a.intersection(b)) #intersection of sets
print(a.difference(b)) #difference of sets

#2.Given a list of numbers, convert it into a set and print only unique elements.
list1=[1,2,3,4,5,2,4,1,4,2,6,7,8,9]
print(set(list1))


#3.Take two lists and print the common elements using sets.
list1=[1,2,3,5,5,7,8]
list2=[2,4,5,2,1,4,5]
a=set(list1)
b=set(list2)
print(a.intersection(b))

#4.Given two lists, print elements that are present in the first list but not in the second.
list1=[1,2,3,5,5,7,8]
list2=[2,4,5,2,1,4,5]
print(set(list1).difference(set(list2)))

#5.Create two sets and find their symmetric difference.
a={1,2,4,8,2,9}
b={2,4,9,2,4,7}
print(a.symmetric_difference(b))

#6.Create a set of numbers and check whether a given number exists in the set or not.
set1={1,2,4,56,292,462,1326,12372,127}
if 8 in set1:
    print("Yes")
else:
    print("No")
 #Another way to write
set1={1,2,4,56,292,462,1326,12372,127}
print( 4 in set1)

#7.Create a set, add two elements, then remove one element, and print the final set.
set1={1,2,4,56,292,462,1326,12372,127}
set1.add(5)
print(set1)
set1.remove(1326)
print(set1)
print(sorted(set1))

#8.Given two sets, check whether one is a subset of the other and also check superset.
a={1,23,55,25,5}
b={49,24,13,23,5}
print(a.issubset(b))
print(a.issuperset(b))

#9.Create a set of numbers and find its length, maximum, and minimum value.
a={1,2,4,56,72,4,2,5,6,2,9}
print(len(a),max(a),min(a), sep="\n")

#10.Given a string, convert it into a set and print all unique characters.
a="Hello My Name is Shubham"
print(set(a))
print(tuple(sorted(a)))
















