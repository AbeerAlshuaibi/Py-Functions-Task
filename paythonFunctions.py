

List=[1,2,3,4]

# Question 1: Write a function that takes two numbers and return their sum
def sumOfTwo(x,y):
    return x+y

# Question 2: Prints all the elements in the list using a for loop
for l in List:
    print(l)

# Question 3: Write a Python program to sum all the items in the list
print("the sum of all the items= ", sum(List))

# Question 4: Write a Python program to get the largest number from the list
print("the largest number= ", max(List))

# Question 5: write a function that take a list and a number then return a new partial list starting from index 0 to index "number"
def partial(list, num):
    newList= []
    counter= 0
    for l in list:
        newList.append(l)
        counter+= 1
        if counter == num:
            break  
    return newList

print(partial(List, 2))

# Question 6: Loop through the letters in the string: "Tuwaiq_Academy"

string= "Tuwaiq_Academy"
for i in string:
    print(i)

# Question 7: Consider this list = ["Python", "C++", "Java"] Exit the loop when x is equal to "C++"

list = ["Python", "C++", "Java"]

for x in list:
    print(x)
    if x == "C++":
        break

# Question 8: Write a function that receives a list containing different numbers, rearranges the list so that the zeros are the end of the list, and finally returns the arranged list

def rearrange(list):
    for l in list:
        if l == 0:
            list.remove(l)
            list.append(0)
    return list

print(rearrange([1, 0, 2, 0, 0, 3]))


