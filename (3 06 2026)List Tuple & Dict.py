#1.Create a list of 10 numbers and print the sum of all elements
list_1=[1,2,3,4,5,6,7,8,9,10]
print(sum(list_1))

#2.Write a program to find the largest and smallest element in a list.
print(max(list_1))
print(min(list_1))

#3.Take a list from user input and remove all duplicate elements
x=[1,2,3,3,3,4,5,6]
y=list(set(x))  # set can only contain unique values, passing the list to set() automatically removes duplicates
print(y)

#4.Create a list of numbers and print only the even numbers.
y=[1,2,3,4,5,6,7,8,9]
even=[]
for i in y:
    if i%2==0:
        even.append(i)
print(even)

#5.Reverse a list without using built-in reverse() method
z=[1,2,3,4,5,6,9,7,8]
x=z[::-1]
print(x)

#6.Create a tuple and count how many times a given element appears in it.
tup=(1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,4,5,6,7,8)
print(tup.count(2))


#7.Convert a tuple into a list, add an element, and convert it back to a tuple
tup=(1,3,2,4)
list_new=list(tup)
list_new.append(5)
print(tuple(list_new))

#8.Write a program to find the maximum and minimum values in a tuple.
tup=(1,2,3,4,5,2,2,4,2,4,5)
print(max(tup))
print(min(tup))

#9.Create a tuple of numbers and print the sum of all elements
tup=(1,2,3,1,4,7,4,2,5,7)
print(sum(tup))

#10.Unpack a tuple into different variables and print each variable.
tup=('ram',2,3,5,'Value','Shyam',[1,2,3])
a,b,c,d,e,f,g=tup
print(a,b,c,d,e,f,g)

#11.Create a dictionary with student names as keys and marks as values Print all students who scored more than 70
dict1={'Shubham':60,'Yurva':86,'Tuyva':76,'Suma':81}
for name,marks in dict1.items():
    if marks>70:
        print(name)
        print(marks)

#12.Count the frequency of each character in a string using a dictionary.
dict2 = {1: 'string1', 2: 'hello', 3: 'Kind'}
for number, string in dict2.items():
    freq = {}   # empty dictionary
    for ch in string:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    print("String:", string)
    print("Frequency:", freq)


#13.Merge two dictionaries into one.
dict1={'Shubham':60,'Yurva':86,'Tuyva':76,'Suma':81}
dict2 = {1: 'string1', 2: 'hello', 3: 'Kind'}
print(dict1|dict2)

#14.Create a dictionary and sort it by values (ascending order).
dict2 = {1: 'string1', 8: 'hello', 2: 'Kind'}
sorted_dict = dict(sorted(dict2.items(), key=lambda x: x[1]))
print(sorted_dict)

#15.Take a dictionary and print the key with the maximum value.
dict2 = {1: 'string1', 2: 'hello', 3: 'Kind'}
max_key=max(dict2, key=dict2.get)
print(max_key)







