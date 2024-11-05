1#Creating a list
fruit=['grape','mango','pinapple','apple','banana']
print('the fruit are',fruit)


2#Accessing Elements
#Given the list colors = ['red','blue','green','yellow','purple'],print the first, third, and last color in the list.
colors = ['red', 'blue', 'green', 'yellow', 'purple']
colors[0:2:4]
print('the colours are',colors)


3#Modifying a List
#Create a list numbers with values [10,20,30,40,50]. Change the second item to 25 and add 60 to the end of the list. Print the modified list.
numbers=[10, 20, 30, 40, 50]
numbers[1]=25
numbers.append(60)
#print updated list
print('the updated list ',numbers)


4#List Slicing
#Using the list names = ['Alice','Bob','Charlie','David','Emma'], create a new list subset containing only the first three names. Print subset.
names = ['Alice','Bob','Charlie','David','Emma']
subset=names[0:3]
print('the first three names are',subset)


5#Looping through a List
#Create a list of numbers from 1 to 10 and use a loop to print each number squared.
nums=[1,2,3,4,5,6,7,8,9,10]
for i in nums:
 print(i)
squared=[]
for i in  nums:
 squared.append(i * i)
print('the square of ',i ,'is',squared)

   
6#List Methods:Append and Extend
#Create an empty list called shopping_cart. Add the items 'milk','bread', and 'eggs' to it using the .append() method. Then use .extend() to add ['butter', 'cheese'] to the list. 
# Print the final list
shoping_cart=[]
shoping_cart.append('milk')
shoping_cart.append('bread')
shoping_cart.append('egg')    
shopings_cart=['butter','cheese']
shopings_cart.extend('shoping_cart')
print('the new shoping_cart is :,shopings_cart')


7#Finding Maximum and Minimum in a List
#Write a program to find the maximum and minimum values in the list numbers = [45,22,88,56,92,33].
list_number=[45,22,88,56,92,33,23,53,19,]
print('the maximum value',max(list_number))
print('the minimum value',min(list_number))


8# Counting Occurrences
#Given the list letters = ['a','b','a','c','b','a','d'], count how many times the letter 'a' appears in the list.
letter=['a','b','a','c','b','a','d']
print(letter.count('a'))


9#List Comprehension
#Use list comprehension to create a new list containing the squares of all even numbers from 0 to 10. Print the resulting list.
lets_num= [0,1,2,3,4,5,6,7,9,10]
squared_evens = [x*2 for x in numbers if x % 2 == 0]   


10#Removing Duplicates
#Given the list nums = [1,2,2,3,4,4,5,6,6,7], write a program to remove duplicates and print the unique elements only.
list_nums= [1,2,2,3,4,4,5,6,6,7]
unique_nums = (list)
print(unique_nums)