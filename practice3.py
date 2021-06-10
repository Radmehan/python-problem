"""
    Author: Harry
    Date: 4-9-2021
    Purpose: Practice Problem
"""

"""
Problem Statement:-
You visited a restaurant called CodeWithHarry, and the food items in that restaurant are sorted, based on their amount of calories. You have to reserve this list of food items containing calories.

You have to use the following three methods to reserve a list:

Inbuild method of python
List name [::-1] slicing trick
Swap the first element with the last one and second element with second last one and so on like,
[6 7 8 34 5] -> [5 34 8 7 6]

Input:
Take a list as an input from the user

[5, 4, 1]

Output:
[1, 4, 5]

[1, 4, 5]

[1, 4, 5]

All three methods give the same results!
"""

#take the siz efrom the user
print("Enter the numbers of list one by one ")
size=int(input("Enter the size of the list\n"))
#initialize a blank list
myList=[]

#take input from user one by one
for i in range(size):
    myList.append(int(input("Enter the list element\n")))

# myList=[7,3,2,1,0]
print(f"Your list is {myList}\n")

reverse1=myList[:]
reverse2=myList[::-1]

reverse1.reverse()

print(f"my first reverse list {myList} is {reverse1}")
print(f"my second reverse list {myList} is {reverse2}")

reverse3=myList[:]
# for i in range(len(myList)):
for i in range(len(myList)//2):
    reverse3[i],reverse3[len(reverse3) -i -1]=reverse3[len(reverse3) -i -1],reverse3[i]
    # print(f"third reverse list at i={2} is {reverse3}")
print(f"my third reverse list {myList} is {reverse3}\n")

if reverse1==reverse2 and reverse2==reverse3:
    print("All three methods gives same result")