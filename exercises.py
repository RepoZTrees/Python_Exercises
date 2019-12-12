# This is a master file for all Python exrcises.
# To add changes for commit/once you made your local commits, you can then push it to your remote GitHub.
   # git add . # Will add all the files from the folder
   # git add filename # Will add only those files
   # git commit -m "write some message"
   # git push

# To run this module from bash:
# $ python3
# >>>import module /module means filename.py file
# >>>filename.module /function name
# Select line, Select word, Select Sentence, Select Paragraph
#

#-------------*******-----------------*****----------------

# Q1 Return number of digits in number

def digits(n):
    a = str(n)
    print(a)
    print(len(a))
#digits(n)

#Q1a. evenOdd function
def evenOdd(x):
    if(x % 2 == 0):
        print("Even")
    else:
        print("Odd")
#evenOdd(x)

# Q2 - Return number of words in a sensentence

def words(s):
    a = s.split(" ")
    print(a)
    #"Returns number of words in sentences"
    return len(a)
#words(s)

# Q2a - Return number of letters in a sentence

def letters(s):
    a = list(s)
    print(a)
    return len(a)
#letters(s) 
        

# Q3 Tables
#tables(3,10)
# 3 * 1 = 3
# 3 * 2 = 6
# 3 * 3 = 9
# 3 * 4 = 12
# .
# .
# .
# 3 * 10 = 30

def tables(m, n):
    for a in range(m, m+1):
        for i in range(1, n+1):
            b = a*i
            print(f"{a} * {i} = {b}")
#tables(m,n)

# Q4
# tables2(5)
# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20
# 5 10 15 20 25

# Logic for the above table:
# | i | j | i*j | q   | row |
# |---+---+-----+-----+-----+
# | 1 | 1 | 1   | '1' | ['1']
# | 1 | 2 | 2   | '2' | ['1','2']
# | 1 | 3 | 3   | '3' | ['1','2','3']
# | 1 | 4 | 4   | '4' | ['1',2','3','4']
# | 1 | 5 | 5   | '5' | ['1','2','3','4','5']
# | 2 | 1 | 2   | '2' | ['2']
# | 2 | 2 | 4   | '4' | ['2','4']
# | 2 | 3 | 6   | '6" | ['2','4','6']


def tables2(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print (f"{i*j}", end="  ")
        print()
    print()
#tables2()
        

# Q5 FizBizz
# Write a function fizzbizz that takes a number n as input
# It should print numbers from 1 to n with the following rules.
# 1. If it's a multiple of 3, it should print fizz
# 2. If it's a multiple of 5, it should print bizz
# 3. If it's a multiple of 15, it should print fizzbizz
# 4. Otherwise, it should just print the number.
# Example output:
# fizzbizz(15)
# should print
# 1
# 2
# fizz
# 4
# bizz
# fizz
# .
# .
# .
# 13
# 14
# fizzbizz

# modulo operator
def fizzbizz(o):
    for i in range(1, o+1):
        if i%15 == 0:
            print('fizzbizz')
        elif i%3 == 0:
            print('fizz')
        elif i%5==0:
            print('bizz') 
        else:
            print(f"{i}")
#fizzbizz(o)

#Q6 Write a program biggest which will retrun the largest element of a
# list of numbers
# e.g.
#     biggest ([1,5,9,20,7,-5,23,4,12])
# will return
#     23
#-----***------

def biggest(l):
    biggest_num = l[0]
    for i in l:
        if i > biggest_num:
            biggest_num = i
   # print(f"the biggest number is:{biggest_num}")
    return biggest_num

#biggest(l)


#Q7 Write a program biggest2 which will return the largest 2 elements of
# a list of numbers
# e.g.
#    biggest2([1,5,9,20,7,-5,23,4,12])
# will return
#    [20,23]

def biggest2(l):
    numbers = l
    if numbers[0]>numbers[1]:
        largest, second_largest = numbers[0], numbers[1]
        #print(largest, second_largest)
    else:
        largest, second_largest = numbers[1], numbers[0]
        #print(largest, second_largest)

    for i in numbers[2:]:
        if i>second_largest:
            if i>largest:
                second_largest, largest = largest, i
                #print(second_largest, largest)
            else:
                second_largest = i
                #print(second_largest)
            #print(second_largest, largest)
    return second_largest, largest



#Q8 A panagram is a sentence that contains all letters of the alphabet.
# e.g. ' The quick brown fox jumps over the lazy dog'
# Implement a function called 'panagram' which takes a string s as input
# and will return True if s is a panagram and False if not.
# e.g.
#panagram("the quick brown fox jumps over the lazy dog") # > True
#panagram("the quick brown fox jumped over the lazy dog") # > False
# "sphinx" of black quartz, judge my vow"

def panagram(s):
#"Will return True if s is a panagram. False otherwise"
#s = "the quick brown fox jumps over the lazy dog"

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in alphabet:
        if i not in s.lower():
            return False
    return True

# Q9 Write a function called "freq" which will take a string s as
# input and return a dictionary that contains the number of times each
#letter occurs  in s.
#e.g. freq("six sick sheep") will return:
# {'s':3, ' ':2, 'e':2,'i':2, 'c':1, 'h':1, 'k':1, 'p':1, 'x':1}

"""
Logic:

{'s': 1}
{'s': 1, 'i': 1}
{'s': 1, 'i': 1, 'c': 1}
{'s': 1, 'i': 1, 'c': 1, 'k': 1}
{'s': 1, 'i': 1, 'c': 1, 'k': 1, ' ': 1}
{'s': 2, 'i': 1, 'c': 1, 'k': 1, ' ': 1}
{'s': 2, 'i': 2, 'c': 1, 'k': 1, ' ': 1}
{'s': 2, 'i': 2, 'c': 1, 'k': 1, ' ': 1, 'x': 1}
{'s': 2, 'i': 2, 'c': 1, 'k': 1, ' ': 2, 'x': 1}
{'s': 3, 'i': 2, 'c': 1, 'k': 1, ' ': 2, 'x': 1}
{'s': 3, 'i': 2, 'c': 1, 'k': 1, ' ': 2, 'x': 1, 'h': 1}
{'s': 3, 'i': 2, 'c': 1, 'k': 1, ' ': 2, 'x': 1, 'h': 1, 'e': 1}
{'s': 3, 'i': 2, 'c': 1, 'k': 1, ' ': 2, 'x': 1, 'h': 1, 'e': 2}
{'s': 3, 'i': 2, 'c': 1, 'k': 1, ' ': 2, 'x': 1, 'h': 1, 'e': 2, 'p': 1}
's':3 'i':2 ' ':2 'e':2 >>> 
"""

def freq(s):
    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
        #print(count) / will print the logic table

    for key in count:
        if count[key] > 1:
            print (f"'{key}':{count[key]}",end=" ")

# Q10 Write a function 'breakdown' which will take an amount as an input and
# give the breakdown of number of currency notes required.
# We have 2000, 500, 200,100, 50, 20, 10, 5, 2, 1 notes in denominations.

def breakdown(amt):
    denominations = [2000,500,200,100,50,20,10,5,2,1]
    for denomination in denominations:
        number_of_notes = amt // denomination
        sub_amount = number_of_notes * denomination
        amt = amt - sub_amount
        if number_of_notes >= 1:
            print(f'\t{denomination}\t* {number_of_notes} = {sub_amount}')
