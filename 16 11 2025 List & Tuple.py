#1.
my_tuple=(1,2,4,4,2,1,35,54,6,7,8,8)
x=len(my_tuple)
y=min(my_tuple)
z=max(my_tuple)
list1=list(my_tuple)
tuple1=tuple(list1)
print(f'The length of the tuple is {x}')
print(f'The minimum value of the tuple is {y}')
print(f'The maximum value of the tuple is {z}')
print(list1)
print(tuple1)

#2.
t2=tuple("ABCD")
t3=tuple("EFGHIABCDJKL")
print(t2*2+t3*1)

#3.
t1=tuple(['1','2','4','2','1','3','5','5','5','2','3','2'])
print(t1)

#4.
t=(10,20,30,40,50)
temp=list(t)
temp.append(60)
temp[1]=25
temp.remove(30)
temp.pop(2)
t=tuple(temp)
print(t)

#5.Given a list of integers, use built-in functions to find the second largest element.
#Example list: [12, 45, 3, 67, 22, 67]
L1=[12, 45, 3, 67, 22, 67,239,1234,664]
x=list(set(L1))
x.sort()
n=x[-2]
print("The Second Largest number is: ",n)

#6.Write a program to count how many times each element appears in a given tuple ex; (2, 3, 2, 5, 6, 5, 5)
tuple1=(2, 3, 2, 5, 6, 5, 5)
tuple2=tuple1.count(2)
tup3=tuple1.count(5)
print("The number of times 2 is repeating is:" ,tuple2)
print("The number of times 5 is repeating is:" ,tup3)

#7.Using built-in functions, convert a tuple of numbers into a list and then find the sum, max, and min values.
tup1=(1,2,4,6,2,8,9)
temp=list(tup1)
x=max(temp)
y=min(temp)
z=sum(temp)
tuple(temp)
print("The maximum value of the list is :",x)
print("The minimum value of the list is :",y)
print("The resultant sum of the list is :",z)














































