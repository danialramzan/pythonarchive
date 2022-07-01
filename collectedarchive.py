# syllabus => 

# 1D/2D Arrays: Sorting, Bubble Sort, Binary Search
# Recursive Fuctions
# Stack, Queue


########################1:
#1d data entry
arr = []
num = int(input("Enter number of elements to input into array: "))
for i in range(num):
    print("Enter number to enter at index ", i, ": ", end = "" )
    arr.append(int(input("")))
print(arr)


#1d min and max
arr = [5, 6, 2, 45, 2, 6, 8, 1, 10, 1 , -45, 3728] #index of array(starting address) = 0
min = 99999999999999
max = -99999999999999
for i in range(len(arr)):
    if arr[i] < min:
        min = arr[i]
    if arr[i] > max:
        max = arr[i]
print("min: ", min, "max: ", max)

#1d bubble sort #2 loops, inner loop is number of comparisons and outer loop is number of exeutions
arr = [3,44,32,523,31,65,-23,32,2313124,5435,12324,-434]
for j in range(len(arr)): #len(x) = 0 is possible
    for i in range(len(arr) - 1): #we use len(arr) - 1 rather than len(arr) because when we use i + 1 and i > index of arr we get error
        if arr[i] > arr[i + 1]: ##we use i and i+1 rather than i -1 and i because if we use i-1 and i it takes first parameter as index -1
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
print(arr)


#1d optimized bubble sort
arr = [3,44,32,523,31,65,-23,32,2313124,5435,12324,-434]
for i in range(len(arr)):
    sorted = False
    for j in range(len(arr) - 1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            sorted = True
    if sorted == False:
        break    
print(arr)


#1d linear search
arr = [3,44,32,523,32,31,65,-23]
found = False
sitem = int(input("Enter search term: "))
for i in range(len(arr)):
    if found == False:  ###deleting this line will cause program do display all indexes that number is found at rather than just first.
        if arr[i] == sitem:
            print(sitem, "found at index", i)
            found = True
if found == False:
    print("not found")


#1d binary search
import math
arr = [-354, -24, -3, 23, 45, 324, 5643, 2312]
highindex = lowindex = mid = num = found = 0
midindex = math.floor(len(arr) / 2)
highindex = len(arr)
num = int(input("what number are you trying to find? "))
while found == False:
    if num == arr[math.floor(midindex)]:
        foundindex = midindex
        found = True
    if num > arr[math.floor(midindex)]:
        lowindex = midindex
        midindex = (lowindex + highindex) / 2
    if num < arr[math.floor(midindex)]:
        highindex = midindex
        midindex = (lowindex + highindex) / 2
print("number found at index", int(foundindex))


# 2d data entry
arr = []
for j in range(3):
    arr.append([0,0,0])
for u in range(3):
    for g in range(3):
        print("enter data into index", u, ",", g, ": ", end="")
        arr[u][g] = int(input())
print(arr)


# #2d min and max
arr = [[2, -43, 2], [325, 2, 5], [1, 43, 7]]
max = -9999999999999999999999
min = 99999999999999999999999
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] > max:
            max = arr[i][j]
        if arr[i][j] < min:
            min = arr[i][j]
print("min:",min,"max:", max)


#2d bubble sort
arr = [[2, -43, 2], [325, 2, 5], [1, 43, 7]] 
flatarr = []
k = 0
for item in arr:
    for subitem in item:
        flatarr.append(subitem)
for i in range(len(flatarr)):
    for j in range(len(flatarr) - 1):
        if flatarr[j] > flatarr[j + 1]:
            flatarr[j], flatarr[j + 1] = flatarr[j + 1], flatarr[j]
for b in range(len(arr)):
    for c in range(len(arr[0])):
        arr[b][c] = flatarr[k]
        k += 1
print(arr)


#2d linear search
arr = [[2, -43, 2], [325, 325, 325], [1, 43, 7]]
num = int(input("Enter number to search for: "))
found = False
for i in range(3):
    if found == False:
        for j in range(3):
                if num == arr[i][j]:
                    print("num was found at index", i, ",", j)
                    found = True
                if found == True:
                    break
if found == False:
    print("number was not found")


# binary search (divides in half and searches more efficiently, only worked for sorted data)
arr = [-434, -23, 3, 31, 32, 32, 44, 65, 523, 5435, 12324, 2313124]
searchterm = int(input("Enter search term: "))
found = False
min = 0
max = len(arr)
mid = max // 2
while found == False:
    if searchterm == arr[mid]:
        found = True
    if searchterm < arr[mid]:
        max = mid
        mid = (max + min) // 2
    if searchterm > arr[mid]:
        min = mid
        mid = (max + min) // 2
    if min == mid:
        break
if found:
    print("found at index",mid)
else:
    print("not found")


#alternate binary search
import math
arr = [5, 7, 9, 20, 60, 80]
print("please enter search term", end=": ")
searchterm = int(input())
def binsearch():
    found = lowindex = middleindex = highindex = indexsearchitem = 0
    highindex = len(arr) - 1
    while highindex >= lowindex and found == 0:
        middleindex = math.floor((lowindex + highindex) / 2)
        if searchterm == arr[middleindex]:
            indexsearchitem = middleindex
            found = 1
        elif searchterm < arr[middleindex]:
            highindex = middleindex - 1
        else:
            lowindex = middleindex + 1
    if found == 0:
        print(searchterm, "not found")
    else:
        print(searchterm, "is found at index", indexsearchitem)
binsearch()


#insertion sort(like sorting playing cards)
arr = [3,44,32,523,31,65,-23,32,2313124,5435,12324,-434]
#we divide array into two parts(but it is still technically one array)
#we assume arr[0] is the first part with only one element and the rest of the array is the other part
#therefore the rest of the array starts with part 2
for i in range(1,len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key
print(arr)

########################2:

#recursive product
def factorial(x):
    if x == 1:
        return 1
    else:
        return factorial(x - 1) * x
print(factorial(5))


#recursive sum
def recursivesum(n):
    if n == 1:
        return 1
    else:
        return recursivesum(n - 1) + n
print(recursivesum(7))


########################3:

# add to queue = enqueue
# remove from queue = dequeue
# add to stack = stack append
# remove from stack = stack pop

# stack = last in, first out (the last item to be added to stack is the first to go out of it)
stack = ["*", "*","*","*","*","*"]
arr = []
while len(stack) != 1:
    arr.append(stack.pop())
    print(stack)
while len(arr) != 0:
    stack.append(arr.pop())
    print(stack)


# queue: first in is the first out
q = ["keem", "naruto", "bowie", "pamela", "obama", "eminem"]
while len(q) != 0:
    print(q.pop(0)) #queue.pop(0) >> pops the zeroth array from index/array/list

for i in range(7):
    q.append(input("Enter data here: "))
q.pop(0) 
q.pop(0)
q.pop(0)
q.pop()
q.pop()
q.pop()
print(q) #only the 4th/middle value is left now


#manual stack and queue
arrayQueue = [0] * 4
front = rear = 0

def insertIntoQueue(item):
    global front, rear, arrayQueue
    if rear == len(arrayQueue) - 1 :
        print("Overflow: Can't insert item, queue is full")
    else:
        if front == 0 and rear == 0:
            front = rear = 1
        else:
            rear += 1
        arrayQueue[rear] = item

def removefromQueue():
    global front, rear
    if front == 0:
        print("Underflow: can't delete, queue is empty")
    else:
        item = arrayQueue[front]
        if front == rear:
            front = rear = 0
        else:
            front += 1
        print(item, "has been deleted")

def finditem(SearchItem):
    global front, rear
    for count in range(rear, front, -1):
        if arrayQueue[count] == SearchItem:
            print(SearchItem, "is found at postion", count)
        else:
            pass

insertIntoQueue("Ali")
insertIntoQueue("Asim")
insertIntoQueue("Akram")
insertIntoQueue("Hadi")
print("Items in queue")

for count in range(rear, front - 1, -1):
    print(count , " " , arrayQueue[count])


print("Remove one item from Queue")

removefromQueue()
print("Insert an item into queue")
insertIntoQueue("New Name ABCDE")
print("search an Item in queue")
finditem("Akram")
print("Item in Queue")
for count in range(rear, front, -1):
    print(arrayQueue[count])
#################################

# print 2 0 0 0 0, 0 2 0 0 0, 0 0 2 0 0, 0 0 0 2 0, 0 0 0 0 2 naturally using for loops
position = 0
text ="0 0 0 0 0"
for i in range(5):
    h = text[:position] + '2' + text[(position + 1):]
    print(h)
    position += 2
        

# Write a program to calculate the electricity bill. The rates of electricity unit are as follows:

#If units >= 300 , cost per unit = 2, if units consumed are >300 and <= 500 then cpu = 5, and if units > 500 then cpu = 7. line cost of 150 is added and if bill greater than 2000 a tax of 5% is also added.

e = int(input("Enter electricity units: "))
if e <= 300:
    c = 2
elif e >= 300 and e <= 500:
    c = 5
else:
    c = 7
if e > 2000:
    print("cost is", (c * e) + 150, "ruppee")
else:
    print("cost is", c * e, "ruppee")

#########recursion and iteration

def recursive_sum(num):
    if num == 1:
        return 1
    return num * recursive_sum(num - 1)
print(recursive_sum(5))


def iterative_Sum(number):
    sum = 0
    for count in range(number, 0, -1):
        sum += count
    return sum
print(iterative_Sum(9))


#making factorial program on your own

def iterativefactorial(num):
    sum = 1
    for i in range(num, 0, -1):
        sum *= i
    return sum
num = int(input("Enter num: "))
print(num, "factorial is", iterativefactorial(num))

##############w/ recursive functions
def recursive_factorial(num):
    if num == 1:
        return 1
    else:
        return num * recursive_factorial(num - 1)
print(recursive_factorial(5))


def recursive_function(number):
    if number == 1:
        return 1
    return number * recursive_function(number - 1)
print(recursive_function(5))


#calculator
#every function in one main:
n1 = int(input("Enter First Number: "))
n2 = int(input("Enter Second Number: "))
op = input("Enter operator: ")
if op  == "+":
    print("Sum of numbers is:", n1 + n2)
elif op  == "-":
    print("Subtraction of numbers is:", n1 - n2)
elif op  == "*":
    print("Product of numbers is:", n1 * n2)
elif op  == "/":
    print("Division of numbers is:", n1 / n2)

#dividing into modules:
n1 = int(input("Enter First Number: "))
n2 = int(input("Enter Second Number: "))
op = input("Enter operator: ")

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def div(n1, n2):
    return n1 / n2

def mul(n1, n2):
    return n1 * n2

if op == "+":
    print("The sum is", add(n1, n2))
if op == "/":
    print("The division is", div(n1, n2))
if op == "-":
    print("The sum is", add(n1, n2))
if op == "*":
    print("The product is", mul(n1, n2))

#object oriented programming (OOP):

class calc: #a class is declared and named calc

    def add(n1, n2):
        return n1 + n2

    def sub(n1, n2):
        return n1 - n2

    def div(n1, n2):
        return n1 / n2

    def mul(n1, n2):
        return n1 * n2
    
n1 = int(input("Enter First Number: "))
n2 = int(input("Enter Second Number: "))
op = input("Enter operator: ")

if op == "+":
    print("The sum is", calc.add(n1, n2))
if op == "/":
    print("The division is", calc.div(n1, n2))
if op == "-":
    print("The sum is", calc.add(n1, n2))
if op == "*":
    print("The product is", calc.mul(n1, n2))

#acts similar to imported function
# import random is similar class calc
# random.randint is similar to calc.add
# (not in their purpose but in the way they are both classes and have subinstructions in each class)

#calculator program using inheritances
class calc: #class is declared and named calc
    def add(n1, n2):
        return n1 + n2

    def sub(n1, n2):
        return n1 - n2

class calc_child(calc): #class calc_child is declared AND inherits class calc (calc is parent class to calc.child)
    def div(n1, n2):
        return n1 / n2

class calc_child_child(calc_child): #class calc_child_child is declared AND inherits class calcz_child (calc is parent class to calc.child)
    def mul(n1, n2):
        return n1 * n2
    
n1 = int(input("Enter First Number: "))
n2 = int(input("Enter Second Number: "))
op = input("Enter operator: ")

if op == "+":
    print("The sum is", calc_child_child.add(n1, n2))
if op == "/":
    print("The division is", calc_child_child.div(n1, n2))
if op == "-":
    print("The sum is", calc_child_child.add(n1, n2))
if op == "*":
    print("The product is", calc_child_child.mul(n1, n2))


#sibling class demo
class parent:
    def one(x):
        if x == 1:
            return True
class child_1(parent): 
    def two(x):
        if x == 2:
            return True
class child_2(parent):
    def three(x):
        if x == 3:
            return True
x = int(input("Enter x: "))
try:
    child_2.one(x)
    print(child_2.one(x))
finally:
    pass
try:
    child_2.two(x)
    print(child_2.two(x)) #this(lines 506-510) will not work because the problem is nested.
finally:
    pass
try:
    child_2.three(x)
    print(child_2.three(x))
finally:
    pass
# child_2.one(x) ###we can also see by comparing colors how the sibling class works
# child_2.two(x)
# child_2.three(x)


# classes are public by default in python,
# Python provides conceptual implementation of public, protected, and private access modifiers,
# but not like other languages like C#, Java, C++. i.e class status is suggested but can be bypassed

#public classdemo

class nestle():
    water = True
class nestlevol(nestle):
    watervol = "3 litres"
obj = nestlevol() ##should succeed
print(obj.watervol)

#private classdemo , indicated by double underscore (__), only the print(__watervol)  inside the private class works, outside the class things fall apart

class nestle():
    water = True
class nestlevol(nestle):
    __watervol = "3 litres"
    milkvol = "4 litres"
    print(__watervol)
    print(milkvol)
obj = nestlevol()
class final(nestlevol):
    print(obj.milkvol)
    print(obj.__watervol) #<-------  program will error out here
    print(obj.milkvol)           #|
final() #------------------------|

#an object is a collection of classes

class person:
    species = "human"
    based = "carbon"
class alive(person):
    breathing = True

danial = alive() ########################## object danial being declared with base class alive which has inherited class species
print(danial)
print(person.species)
print(danial.species)
print(alive.species)
print(alive.breathing)
print(danial.breathing)


#input salary and grade, if grade is greater than 15 then add 50% bonus else add 25% bonus if grade is 15 or less. output total salary. do this using classes
return_bonus = 0

class a():
    def fun1(x):
        return x * 0.5
class b(a):
    def fun2(x):
        return x * 0.25
new_data = b()
salary = int(input("Enter Salary:"))
grade = int(input("Enter Grade:"))
if grade > 15:
    return_bonus = new_data.fun1(salary)
else:
    return_bonus = new_data.fun2(salary)
total_salary = salary + return_bonus
print("Total salary", total_salary)

#Write a program to calculate electricity bill, if units >= 300 , cost per ubnit = 2, if units consumed are >300 and <= 500 then cpu = 5, and if units > 500 then cpu = 7. line cost of 150 is added and if bill greater than 2000 a tax of 5% is also added. solve this usning classes

class A:
    def fun1(units):
        return units * 7
class B(A):
    def fun2(units):
        return units * 5
class C(B):
    def fun3(units):
        return units * 2
units = int(input("Please enter units: "))
if units > 500:
    return_cost = C.fun1(units)
elif units <= 300:
    return_cost = C.fun2(units)
else:
    return_cost = C.fun3(units)
returncostint = float(return_cost)
total_bill = (returncostint) + 150
if total_bill > 2000:
    total_bill += (0.05 * total_bill)
print("total bill:", total_bill)


#__init__ demo ; __varname__ means special method

class classe:
    def __init__(self, CPU, RAM): ################ __init__ is passed automatically even if not referred to
        print("init innit")
        self.CPU = CPU
        self.RAM = RAM
    def call():
        print("this function will never be ruin unless called directly upon")
pc = classe("i5", "8GB")
print(pc.RAM)
print(pc.CPU)
###the print("init innit") runs too even though it wasnt directly called


#constructor call

class a: ## the constrctor __init__ is being invoked implicitly here
    name = "Danial" ##
    age = 18 ##
obj = a()
print(obj.name)
print(obj.age)

#now doing it explicitly,

class A:
    def __init__(self, name, age):
        self.name = "Danial"
        self.age = 17
obj = a() 
print(obj.name)
print(obj.age)


# function overloading demo,, doesent work in python

# First product function.
def product(a, b):
    p = a * b
    print(p)
      
# Second product function
def product(a, b, c):
    p = a * b* c
    print(p)
  
# Uncommenting the below line shows an error    
# product(4, 5)
  
# This line will call the second product method
#therefore it is proven that method overloading is not natively supported in python and that the latest method/function to bear a name is chosen

# difference between strip(), rstrip(), and lstrip()
# strip(): returns a new string after removing any leading and trailing whitespaces including tabs (\t).
# rstrip(): returns a new string with trailing whitespace removed. It’s easier to remember as removing white spaces from “right” side of the string.
# lstrip(): returns a new string with leading whitespace removed, or removing whitespaces from the “left” side of the string.

term = str("   dhsbdhsbvdhsavbdhy   \n")
print(term.strip())
print(term.lstrip())
print(term.rstrip())


# file handling

max = -999999999999999999
min = 999999999999999999
avg = 0
file = open("G:\CSCLASS\handling.txt", "w") #write mode so all previous data is cleared (not neccesary but makes it more convinient)
for i in range(5):
    print("Enter data to enter at index", i + 1, ": ", end="")
    print(input(), file = file)  ##########  we can use file.write but file.write only accepts one parameter and thus would require multiple f.writes)
file.close()

file = open("G:\CSCLASS\handling.txt", "r") ###file is opened in reading mode and pointer is at line #0, so it can carry out min,max , avg functions from start
for line in file: ####line isnt  a command, it can be anything e.g for cheetos in file:
    refinedline = int(line.rstrip()) ##any possible newline (\n) is stripped and the value is "refined"
    if refinedline > max:
        max = refinedline
    if refinedline < min:
        min = refinedline
    avg += refinedline
file.close()

file = open("G:\CSCLASS\handling.txt", "a")
print("min: ", min, file=file)
print("max: ", max, file=file)  ###instead of writing print output to sys.stdout we are instead writing to the file(where it says file = file, where the second file is the filename )
print("avg: ", avg / 5, file=file)
file.close() ##python automatically closes files sometimes so you should still use file.close( whenever appropriate)

#write the table of any number which is input  up to 10 (e.g i * 10 = 10i)
file = open("G:\CSCLASS\handling.txt", "w")
t = int(input("Enter number of table that you want to print: "))
for i in range(1, 11):
    print(t, "x", i, "=", i*t, file = file)
    

##difference between static and dynamic loop:
#A STATIC LOOP AHS A SET VALUE TO LOOP TO E.G IN THE CASE OF A FOR LOOP
for i in range(5):
    pass
#this starts from 0 to 4, has fixed values, number of executions of loops are decided before the program runs
#a dynamic loop has its values set upn first launching a program
#e.g
a = int(input("Enter value to start from"))
b = int(input("Enter value to end at"))
for i in range(a,b):
    pass #whatever

#task: write the table program but with a dynamic loop
file = open("E:\CSCLASS\handling.txt", "w")
a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))
table = int(input("Enter table: "))
for i in range(a, b + 1):
    print(table, "x", i, "=", i * table, file= file)


#save first 50 even numbers to a file and their sum
total = 0
file = open("E:\CSCLASS\handling.txt", "w")
for i in range(50):
    print(2* (i + 1), file = file)
file = open("E:\CSCLASS\handling.txt", "r+")  ###using r+ because after reading we write too
for pee in file:
    total += int(pee.rstrip())
print("sum: ", total, file = file)


# writing previous code in pseudocode:
# procedure fiftyevensum()
# DECLARE total: integer <-- 0
# OpenFile "handling.txt" FOR Write
# FOR Count <-- 1 to 50 Step 1
#     WriteFile ("handling.txt", 2 * Count)
#     total = total + 2
# WriteFile("handling.txt", "total: ", total)


#enter any 20 numbers and check how any are even, how many are odd amd how many are 0
even = odd = zero = 0
chungose = open("D:\CS\handling.txt", "w")
for i in range(20):
    print("Enter number", i + 1, end =": ")
    t = int(input())
    chungose.write(str(t) + "\n")
chungose.close()

chungose = open("D:\CS\handling.txt", "r+")
for big in chungose:
    if int(big.rstrip()) == 0:
        zero += 1
    if int(big.rstrip()) // 2 == int(big.rstrip()) / 2:
        even += 1
    else:
        odd += 1
print("even: ", even, "\nodd: ", odd, "\nzeros: ", zero, file = chungose)


#file searching
def writedata():
    file = open("D:\CS\handling.txt", "w")
    for i in range(10):
        print("Enter number", i + 1, end=": ")
        number = input()
        print(number, file=file)
def readdata():
    file = open("D:\CS\handling.txt", "r")
    lineno = 1
    found = False
    usersearch = input("Enter number to look for: ")
    for line in file:
            if found == True:
                pass
            else:
                if line.strip() == usersearch:
                    foundlinenumber = lineno
                    found = True
                else:
                    lineno += 1
    if found == True:
        print("data has been first found at line number: ", foundlinenumber)

writedata()
readdata()


# Search through a txt file which had ids and emails. The user entered an Id and if the id was found then the email corresponding to that id was to be written in another results text file. If the id was not found then just write something like “id not found” in the results txt file.
# At the end print the number of ids not found on the console, And the user can search through the file 5 times

chungose = open("G:\CSCLASS\handling.txt", "r") ##open source file for read
file2 = open("G:\CSCLASS\handling2.txt", "w") #open destination file for write
foundnum = 0
for i in range(5):
    found = False
    string = str(input("Enter ID to search for: "))
    for biggest in chungose:
        big = str(biggest.strip()) #strip all characters like \n newline
        if string == big[:4]:
            email = big[5:]
            found = True
    if found == True:
        print(email, file = file2)
        foundnum += 1
    if found == False:
        print("id", string, "not found", file = file2)
    chungose.seek() ##the pointer is moves back to the to of the file so that it starts from index 0/line 1 again
print("IDs found:", foundnum, "IDs not found:", 5 - foundnum)

###

# Check if a number is even or odd
num = int(input("Enter number to check if even or odd: "))
if num // 2 == num / 2:
    print(num, "is even")
else:
    print(num, "is odd")

#Array data entry until -1 is entered
a = 0
array = []
while a != -1:
    a = int(input("Enter any number, it will be added to an array until you enter -1: "))
    array.append(a)
print(array)

#Write a Python program to reverse the order of the items in the array
arr1 = ["zan", "ram", "ial", "dan"]
arr2 = []
for i in range(len(arr1), 0, -1):
    arr2.append(arr1[i - 1])
print(arr2)


#Write a Python program to remove all duplicate elements from a given array and returns a new array.
arr =[1, 5, 2342, 534, 3, 5, 3, 5] #//too easy
arr2 = list(dict.fromkeys(arr))
print(arr2)

#using more logical method

arr =[1, 5, 2342, 534, 3, 5, 3, 5]
print ("The original list is :", arr)
arr2 = []
for element in arr:
    if element not in arr2:
        arr2.append(element)
print(arr2)


#search for an item in an array, output the first and last index it is found at, and the count of that number
arr =[1, 5, 2342, 534, 3,8,3, 17, 45]
found = False
count = findex = lindex = 0
int = int(input("Enter term you are looking for: "))
for i in range(len(arr)):
    if int == arr[i]:
        if found == False:
            findex = i
            found = True
        lindex = i
        count += 1
if findex == lindex:
    print("The item was only found one time in the array, at index", findex)
else:
    print("First index: ", findex, ", Last index: ", lindex, ", element occured", count, "times")

#########Performing Python tasks:
################################

# #Task # 1 : Input the length and width of a rectangle and print the area and perimeter.
length = float(input("Enter Length of Rectangle: "))
width = float(input("Enter Width of Rectangle: "))
print("Area:", length * width, "cm^2 ")
print("Perimeter:", 2* (length + width), "cm")

#Task # 2 : Input the time in hours, minutes and second. Convert this time in to seconds and print the time in seconds.
#Input the time in hours, minutes and second. Convert this time in to seconds
#and print the time in seconds
hours = int(input("Enter current hour: "))
minutes = int(input("Enter current minute: "))
seconds = int(input("Enter current second: "))
minsecs = 60 * minutes
hoursecs = 3600 * hours
totalsecs = minsecs + hoursecs + seconds
print("The time is currently", totalsecs, "seconds")

#Task # 3 : Input two numbers a and B, Swap and print them.
A = int(input("Number A: "))
B = int(input("Number B: "))
A, B = B, A
print("Number A:", A)
print("Number B:", B)

#Task # 4 : Input the marks obtained by a students in three tests. Input the Maximum  obtainable marks also. Print the Total Marks, Total Percentage and Average Marks of the Student. Your output must all be in one print statement using concatenation of variables and string constants.
A = int(input("Test 1 Marks: "))
B = int(input("Test 2 Marks: "))
C = int(input("Test 3 Marks: "))
M = int(input("Max Obtainable : "))
T = A + B + C
TP = (T / (3 * M) * 100)
AM = T / 3
print ("Total: ", T, ", Percentage::", TP, "%, Average Marks: ", AM )

#Task 5: Enter the price of an item, the amount of the item, apply 17.5% tax on it and output total payable.
price = int(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))
t = price * quantity
tax = 0.175 * t
print("Total:",t,"\nTax:",tax,"\nTotal Payable:",t+tax)

#Task 6: Convert Celcius to Fahrenheit.
cel=int(input("Enter Temperature in Celcius: "))
fah = cel * 2.12
print("Temperature in Fahrenheit is:",fah)

#Task 7: Enter a students name, marks and max obtainable marks. Then output their percentage and a pass/fail.
#A = int(input("Test Marks: "))
#M = int(input("Max Obtainable : "))
#N = str(input("Student Name : "))
#PF = A / M 
#if PF < 0.5:
#    print(N, "has failed with ", (100 * PF), "% marks")
#elif PF > 0.5:
#    print(N, "has passed with ", (100 * PF), "% marks")

#Task # 8: Input a year and print if it is a leap year or not.

# Method 1
def LeapYear(year):
    ly = False
    if year // 4 == year / 4:
        if (year // 100 != year / 100) or (year // 400 == year / 400):
            print(year, "is a leap year")
            ly = True
    if ly == False:
        print(year, "is not a leap year")
LeapYear(2024)

#Method 2
def LeapYear(year):
    LEAPYEAR = 2000
    if abs(LEAPYEAR - year) % 4 == 0:
        print(year, "is a leap year.")
    else:
        print(year, "isn't a leap year.") 
LeapYear(248274828)

# Task # 9
# Input the hourly rate and hours worked of an employee. The employees who 
# 	work for more than 40 hours are eligible for overtime pay along with normal pay
# 	and others will get only normal pay. The rate of over time pay is thrice the 
# 	normal hourly rate. You must show the output in the given way	
# 		Name                	: XXXXXXX
# 		Normal Salary       	: XXXXXXX
# 		OverTime Salary		: 0.00
# 		Total			: XXXXXXX

name = input("Enter name of employee: ")
hours = int(input("Enter hours of employee: "))
rate = int(input("Enter hourly rate of employee: "))
if hours > 40:
	over = "true"
	overtimehours = hours - 40
	overpay = (3 * rate * overtimehours)
	pay = (40 * rate)
else:
	pay = (hours * rate)
	overpay = 0 
	pass
total = pay + overpay
print("Name: ", name)
print("Normal Salary: ", pay)
print("Overtime Salary: ", overpay)
print("Total: ", total)

# #Task # 10: Input the marks obtained by a student in 2 test. Ouptut the grade
# 		you dont need to do any validation
# 		Distinction if both are above 80.
# 		Merit if total of both is above 160 
# 		Credit if Total of both tests is above 120
# 		Pass if above 100
# 		Fail otherwise which means total is below OR EQUAL 100
# 		82,83	=> Distinction
# 		100,79	=> Merit
# 		70,75   => Credit
# 		60,62   => Pass
# 		90,2    => Fail

a = int(input("Enter Test 1 Marks: "))
b = int(input("Enter Test 2 Marks: "))
d = ""
if a + b >= 100:
     d = d + "pass, "
     if a + b >= 120:
        d = d + "credit, "
        if a + b >= 160:
            d = d + "merit, "
            if a >= 80 and b >= 80:
                d = d + "distinction."
else:
    d = d + "fail."
print("You have acheived", d)

# Task # 11 : Input a character and print its category.
char = input("Enter a character ")
asc_code = ord(char)
if asc_code >= 65 and asc_code<= 90:
    print ("Capital letter")
elif asc_code >= 97 and asc_code <= 122 :
    print ("Lower case")
elif asc_code >= 48 and asc_code <= 57:
    print ("Digit")
else:
    print ("Special Character")


# Task # 12 : Input a number and print if it is special or ordinary
# 	Special numbers are the ones that are in the following ranges inclusive: 20 - 30, 50 - 60, 80 - 90 

N = int(input("Enter number: "))
if -1 < N < 101:
     if 19 < N < 31 or 49 < N < 61 or 79 < N < 91:
           print("Special Number!")
     else:
           print("Number is not special!")
else:
     print("Error, please try again")


# Task # 13: Input the Carbon Contents, tensile strength and hardness of a steel.
# 	Output the grade of steel using nested IF statements

# 	Carbon Contents < 1.6
# 	Tensile Strength > 1600
# 	Hardness > 8

# 	Grade is 10 if all three are true
# 	Grade is 9 if (i) and (ii) are True
# 	Grade is 8 if (i) and (iii) are True
# 	Grade is 7 if (ii) and (iii) are True
# 	Grade is 6 if either one is True
# 	Grade is 5 otherwise { all are False }

a = float(input("Input Carbon Contents: "))
b = float(input("Input Tensile Strength: "))
c = float(input("Input Hardness of Steel: "))
Carbon = Tensile = Hardness = False
if a < 1.6:
     Carbon = True
if b > 1600:
     Tensile = True
if c > 8:
     Hardness = True
if (not Carbon) and (not Tensile) and (not Hardness):
    print("Steel is Grade 5")
else:
    if Carbon:
        if Tensile and Hardness:
            print("Steel is Grade 10")
        elif Tensile:
                print("Steel is Grade 9")
        elif Hardness:
            print("Steel is Grade 8")
        else:
            print("Steel is Grade 6")
    elif Tensile:
        if Hardness:
            print("Steel is Grade 7")
        elif not Carbon:
            print("Steel is Grade 6")
    else:
        print("Steel is Grade 6")

# Task # 14 : Input a 3-digit number and print if it is an armstrong number or not. 
num = int(input("Enter a three digit number: "))
while num > 999 or num < 100:
    num = int(input("Error, Please enter a 3 digit number: "))
numstr = str(num)
if num == (int(numstr[0]) ** 3) + (int(numstr[1]) ** 3) + (int(numstr[2]) ** 3):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")

#Task # 15 : Input a character and print if it is a vowel or consonant. Make sure the input is a character.
#Upper and lower case both are allowed, but nothing else other than a character should be allowed.
char = str(input("Enter a character: "))
ord = ord(char)
if ord == 97 or ord == 65 or ord == 101 or ord == 73 or ord == 69 or ord == 79 or ord == 85 or ord == 105 or ord == 111 or ord == 117:
   print(char, "is a vowel")  ##all the ascii codes for vowels
elif (ord >= 97 and ord <= 122) or (ord >= 65 and ord <= 90):
   print(char, "is a consonant")
else:
    print("Please enter a character!")

# #Task 16 : Input a 5 digit number and print if it is a palindrome or not. 
num = int(input("Enter 5 digit Number: "))
while len(str(num)) != 5:
    num = int(input("Error! Enter 5 digit number: "))
numrev = ""
for i in range(len(str(num)) - 1 , -1, -1):
    numrev += (str(num))[i] ###lines 1103-1105 can be replaced with splicing i.e num[::-1]
if numrev == str(num):
    print(num, "is a pallindrome.")
else:
    print(num, "is not a pallindrome.")

# #Task # 17 : Generate a random number between 1 and 10 inclusive using the library random. 
# Ask the user to guess it, if the guess is exactly the number print "Bingo". If it is one above or below 
# print "Too Close", if it is 2 below or 2 above then print "Close" otherwise print "You Lose".

import random
r = random.randrange(1,10)
a = int(input("enter number between 1-10: "))
if a == r :
   print("Bingo")
elif abs(r-a) == 1:
   print("Too Close")
elif abs(r-a) == 2:
   print("Close")
else:
    print("You Lose")
#******************************** ITERATION / LOOP ********************************

#Task # 18 : Input a number and print it Factorial. 

num = int(input("Enter number to find factorial of: "))
while num < 0:
    num = int(input("Enter number to find factorial of(-ve not allowed): "))
n = int = num
if num != 0:
    while n != 1:
        n -= 1
        int *= n
    print("Factorial of", num, "is", int)
else:
    print("Factorial of", 0, "is", 1)


# Task # 19 : Input two numbers and print the product without using the multiplication operator (*)
print("Note: if one of the numbers being multiplied is negative the it should be entered as the first number.")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = 0
for i in range(b):
    c += a
print(c)

#Task # 20 : Input two numbers Base and Power. Find Base raised to the power "Power" without using the ** operator.
a = int(input("Enter Base number: "))
b = int(input("Enter Power number: "))
c = 1
for i in range(b):
    c *= a
print(c)

# Task # 21 : Input two numbers A and B. Find the product of all numbers between A and B inclusive. 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = 1
for i in range(a , b + 1):
    c *= i
print("Product: ", c)

#Task # 22 : Input a denary number and convert and print its binary equivalent.
#You cannot put any limit, your logic must work for any positive number.
denary = int(input("Input a denary number:"))  
binary=""  
while denary > 0:    
 binary = str(denary % 2) + binary  
 denary = denary // 2  
print("Your binary number is: " + binary)

# Task # 23 : Input numbers and stop when zero is entered. Print the Largest and smallestvnumber (positive) 
# entered by the user. Print the percentage of negative numbers entered. NO validation.


a = int(input("Enter Number: ")) ###input
b = a #biggest
c = a #smallest
negative = 0
count = 0
if a < 0:
 count += 1
 negative += 1
if a > 0:
 count += 1
while a != 0:
 a = int(input("Enter Number: "))
 if b > a:
   b = a
 if c < a:
   c = a
 if a < 0:
   negative += 1
 if a != 0:
   count += 1
negpercent = (100 * negative / count)
print("Smallest:", b, "Biggest:", c, "Percentage of negative numbers: ", negpercent, "%")

# Task # 24 : Input a binary number and convert it to a denary number with 
# the asssumption that the user will only enter zero and ones. 

bin = input("Enter Binary Number: ")
a = 0
for i in range(len(bin)):
    if bin[i] == "1":
        a += (2 ** (len(bin) - i - 1))
print(bin, "in base 10 is:", a)


# Task # 25 : Input a number and print if it is a Prime number or not.Your program should work with logically any positive number(no limit). 

n = int(input("Enter a number to check if prime: "))
composite = False
i = 2
while composite == True or i < n:
    if n % i != 0:
        i += 1
    else:
        composite = True
        break
if composite:
    print(n, "is composite.")
else:
    print(n, "is prime.")

# Task # 26: Input two numbers. Find the sum of all numbers between these two numbers including the entered ones. 
# Do not include any number that is a factor of 3 or 5. But if it is a factor of both then include it.
a = int(input("Enter Number A: "))
b = int(input("Enter Number B: "))
temp = []
if a > b:
    a,b = b,a
arr = list(range(a, b+1))
for j in list(arr):
   if ((j // 3 == j / 3) and (j // 5 == j / 5)):
       temp.append(j)
for i in list(arr):
   if (i // 3 == i / 3) or (i // 5 == i / 5):
       arr.remove(i)
print ("The sum is", sum(arr + temp))

#***************************************** WORKING WITH STRINGS *****************************************

# Task#27: Input a Full name for example. Extract the first and last name from the name.
# Save in different variables and print both in two different lines.

name = input("Input first and last name: ")
space = name.find(" ")
fname, lname = name[:space], name[space + 1:]
print("First Name:", fname, "\nLast name:", lname)

# Task#28: Input a String for example "Hello" Now print what is shown below one by one 
# using six different loops.

# (1)
# 	h
# 	e
# 	l
# 	l
# 	o
# (2)
# 	o
# 	l
# 	l
# 	e
# 	h
# (3)
# 	h
# 	he
# 	hel
# 	hell
# 	hello
# (4)
# 	o
# 	lo
# 	llo
# 	ello
# 	hello
# (5)
# 	hello
# 	hell
# 	hel	
# 	he
# 	h
# (6)
# 	hello
# 	ello
# 	llo
# 	lo
# 	o


#loop 1
from http.client import FOUND


word = str(input("Enter: "))
var = 0
while var != len(word):
   if var <= len(word):
       print(word[var])
       var += 1
#loop 2 
word = (str(input("Enter: "))[::-1])
var = 0
while var != len(word):
   if var <= len(word):
       print(word[var])
       var += 1
#loop 3 
word = str(input("Enter: "))
var = 0
while var != (len(word) + 1):
   if var <= len(word):
       print(word[0:var])
       var += 1
#loop 4
word = str(input("Enter: "))
var = len(word)
while var != 0:
   if var >= 0:
       var_1 = word[0:(var - 1)]
       print(word.replace(var_1,""))
       var -= 1
#loop 5
word = str(input("Enter: "))
var = len(word)
while var != 0:
   if var >= 0:
       print(word[0:var])
       var -= 1
#loop 6
word = str(input("Enter: "))[::-1]
var = len(word)
while var != 0:
   if var >= 0:
       var_1 = word[0:var]
       var -= 1
       print(var_1[::-1])

#Task # 29: Input a String and a character, Search whether the character exists in the 
#input string or not. Make use of a boolean variable "Found".
found = False
a = input("Enter a string:  ")
b = input("Input character you want to find in the string: ")    
for j in range(len(a)):
    if b == a[j]:
        found = True
    if found == True:
        break
if found == True:
    print("Character found in string")
else:
    print("Character not found in string")

# #Task# 30: Input a string and a character, find how many occurrances of this character
# are found in the given string. for example in the string "Mississippi" if we search "s"
# the answer should be 4. 

A = input("Enter a string:  ")
B = input("Input character you want to find in the string: ")    
var = A.count(B)  
print ("Count of", B, "in", A, " is: " +  str(var))


#######I am switching to functions from now on

# Task#31: Input a String and print the check sum value of it. Check sum is the sum of 
# Ascii Codes of all charcaters. Divide the sum by 256, the remainder is the checksum.

def checksum(word):
    checksum = 0
    for i in range(len(word)):
        checksum += ord(word[i])
    if checksum > 256:
        checksum = checksum % 256
    else:
        pass
    print(checksum)
checksum("AAAA")

# Task#32: Input a HexaDecimal String. For Example "FA2B". Now convert this hex string
# to a denary number. The built in function you might need are len(), int() or any other.
def Hexadecimal(hex):
    a = b = 0
    for i in range(len(hex)):
        if hex[i] != "0":
            if hex[i] == "a" or hex[i] == "A":
                b = 10
            elif hex[i] == "b" or hex[i] == "B":
                b = 11
            elif hex[i] == "c" or hex[i] == "C":
                b = 12
            elif hex[i] == "d" or hex[i] == "D":
                b = 13
            elif hex[i] == "e" or hex[i] == "E":
                b = 14
            elif hex[i] == "a" or hex[i] == "F":
                b = 15
            else:
                b = int(hex[i])
            a += (b * (16 ** (len(hex) - i - 1)))
    print(hex, "in base 10 is:", a)
Hexadecimal("a325")

#OR// USING A BUILT IN FUCNTION, 
def Hexadecimal(string):
    return(int(string, 16))

# Task # 33 : Input a number N and print a grid of stars with N number of rows and 
# N number of Columns. 
def task33(N):
    for i in range(N):
        for j in range(N):
            print("*", end = "")
        print("\n")
task33(5)

# Task # 34 : input a number N and print this for example N = 5
# 	*
# 	* *
# 	* * * 
# 	* * * *
# 	* * * * *

def task34(width):
    grid = []
    for i in range(width):
        grid.append("*")
        print(grid)
task34(5)

# Task # 35 :
# 	* * * * *
# 	* * * *
# 	* * *
# 	* *
# 	*

def task35(width):
    grid = ["*"]
    for i in range(width):
       grid.append("*")
    for i in range(width):
       grid.remove("*")
       print(grid)

task35(5)

# Task # 36:
# 	* 
# 	* *
# 	* * *
# 	* * * *
# 	* * * * *
# 	* * * * 
# 	* * * 
# 	* * 
# 	*

def task36(width):
    grid = ["*"]
    for i in range(width):
       grid.append("*")
       print(grid)
    for i in range(width):
       grid.remove("*")
       print(grid)
task36(5)


# Task #37
# 	* * * * *
# 	* * * *
# 	* * *
#   * *
# 	* 
# 	* *
# 	* * *
# 	* * * *
# 	* * * * *

def task37(width):
    grid = ["*"]
    for i in range(width):
       grid.append("*")
    for i in range(width):
       grid.remove("*")
       print(grid)
    for i in range(width):
       grid.append("*")
       print(grid)
task37(5)

# Task # 38: Input a number N. Print
# 	1
# 	2 2
# 	3 3 3 
# 	4 4 4 4
# 	5 5 5 5 5

def task38(width):
   tempcount = count = 1
   grid = []
   for i in range(width):
      while tempcount != 0:
         grid.append(i + 1)
         tempcount -= 1
      print(grid)
      count += 1
      tempcount = count
      grid.clear()
task38(5)

# Task # 39 Input a number N , say 5

# 	1
# 	1 2
# 	1 2 3 
# 	1 2 3 4 
# 	1 2 3 4 5

def task39(width):
   count = 1
   grid = []
   for i in range(width):
      grid.append(count)
      count += 1
      print(grid)
task39(6)

# Task # 40: Input a number N say 5

# 	1 2 3 4 5
# 	1 2 3 4 
# 	1 2 3
# 	1 2
# 	1

def task40(width):
   count = 1
   grid = []
   for i in range(width):
      grid.append(count)
      count += 1
   for i in range(width - 1):
         grid.pop()
         print(grid)
task40(153)


# Task # 41: Input a number N say 5
# 	1
# 	1 2
# 	1 2 3 
# 	1 2 3 4 
# 	1 2 3 4 5
# 	1 2 3 4
# 	1 2 3 
# 	1 2 
# 	1

def task41(width):
   count = 1
   grid = []
   for i in range(width):
      grid.append(count)
      print(grid)
      count += 1
   for i in range(width - 1):
         grid.pop()
         print(grid)
task41(15)

# Task # 42 : Input a number N say 5

# * * * * *
#   * * * *
#     * * *
#       * *
#         *

def task42(width):
    P = width
    count = 0
    while width != 0:
        M = P * "*"
        O = M.replace("*", " ", count )
        width -= 1
        count += 1
        print(O)
task42(5)

# Task 43:  Input a number say 5

# * * * * *
#   * * * *
#     * * *
#       * *
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

def task43(width):
    P = width
    count = 0
    while width != 0:
       M = P * "*"
       O = M.replace("*", " ", count )
       width -= 1
       count += 1
       print(O)
    count -= 1
    width =- 1
    while width != P:
       M = P * "*"
       O = M.replace("*", " ", count )
       width += 1
       count -= 1
       print(O)
task43(5)


# Task # 44 : Input a number say 5
# 	1
# 	2 3
# 	4 5 6
# 	7 8 9 10
# 	11 12 13 14 15 

def task44(rows):
    currentNumber = 1
    stop = 2
    for i in range(rows):
       for column in range(1, stop):
           print(currentNumber, end=' ')
           currentNumber += 1
       print("")
       stop += 1
task44(10)

# Task # 45 : Input a number and print its digital Roots. A digit roots is the sum of its
# digits until you get a one digits number

def digitalroot(a):
    p = a
    if len(str(a)) == 1:
       return a
    else:
        sum = 0
        for i in str(a):
            sum += int(i)
        a = str(sum)
        return digitalroot(a)
print("The digital root is", digitalroot(16232453))

# Task # 46 : Print the First 1000 Prime Numbers.

def thousandprimes():
    count = composite = 0
    i = 2
    while count != 1000:
        for j in range(2, i):
            composite = False
            if i % j == 0:
                composite = True
            if composite:
                break
        if not composite:
            print(i)
            count += 1 ####edit this line to edit the amount of primes to print
        i += 1
thousandprimes()

# Task # 47 : Input a number and print all Niven numbersbelow this number. A number N is a Niven number if N is 
# completly divisble by the sum of its digits e.g 18 is a Niven number because 18 is divisible by 9(sum of 1 and 8). 

def NivenNumbers(N):
    print("The Niven Numbers <= Number N are: ")
    while N != 0:
       while len(str(N)) >= 2:
           var1 = [int(x) for x in str(N)]
           var2 = sum(var1)
           if N % var2 == 0:
               print(N)
           N -= 1    
NivenNumbers(14242)

# #Task 48: Collatz Problem // Enter a number, if the number is even divide it by two, otherwise multiply by 3 and add 1.
#Keep doing this until number reaches 1. Show progression in an array/list and output total steps and max value.

def Collatz(i):
    n = i
    count = 1
    prog = [n]
    max = 1
    while n != 1:
        if max < n:
            max = int(n)
        if n % 2 == 0:
            n = n / 2
            count += 1
        else:
            n = (3 * n) + 1
            count += 1
        prog.append(int(n))
    print("stopping time:", count, "\nprogression:", prog,", max value:", max)
Collatz(13)
#####################FIN#####################