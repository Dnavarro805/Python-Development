################################################################################
## Student Name: Daniel Navarro                      Summer of 2016           ##
## Program Name: Lists&Strings.py                    Ventura College          ##
## Comments    : Studying Lists and Strings.         CS V11                   ##
##                                                   Programming Fundamentals ##
##                                                   Engr. R.M. Polito        ##
################################################################################


import sys
import  os
from math   import *
from random import *


def Clear():
    os.system("cls")

def Heading():
    print ("\t\t\t   Testing on Strings and Lists\n\n")

def StringOne():
    A = "hello dolly, won't you come to me baby"
    
    # I want to print just hello..
    print ("\t\t\t\t     ",A[0:5])
    
    # I want to print just come to me...
    print ("\n\t\t\t\t   ",A[23:33])
    
    # I want to print them all centered one letter at a time...
    for k in range(len(A)):
        print ("\t\t\t\t\t",A[k])

    # Now for the upper,lower, capitalize, etc....
    print ("\n\t\t\t",A.upper())
    print ("\n\t\t\t",A.lower())
    print ("\n\t\t\t",A.capitalize())
    print ("\n\t\t\t",A.title())
    
    # How do you prove that the string is immutable.. can NOT change.
    # A[2] = 'p'
    # print ("\n\t",A.upper())
    # TypeError: 'str' object does not support item assignment

    # Print all centered one letter at a time using while loop
    k = 0
    while k < len(A):
        print ("\t\t\t\t\t",A[k])
        k = k + 1

def StringTwo(): # Suppose I want to count vowels in a string..aeiou
    A = "This Is Just The Beginning Of Programming"
    VowelCounter = 0
    k = 0
    while k < len(A):
        if A[k] == 'a' or A[k] == 'e' or A[k] == 'i' or A[k] == 'o' or A[k] == 'u' or A[k] == 'A' or A[k] == 'E' or A[k] == 'I' or A[k] == 'O' or A[k] == 'U':
            VowelCounter = VowelCounter + 1  
        k = k + 1
    print ("\n\t\t\t     The number of vowels is:", VowelCounter)

def ListOne():
    A = [] # To Declare or Initialize a LIST
    A.append("January")
    A.append("February")
    
    # I want to append 5, 10, 100
    A.append(5)
    A.append(10)
    A.append(100)
    A.append(sqrt(2))
    
    # I want to append 1,2,3,4,5,6,7,8,9,10
    for x in range(10):
        A.append(x+1)
        
    for k in range(len(A)):
        print ("\n\t\t\t\t",A[k])

    # I am going to delete 10 the last item = pop command
    for x in range(5):
        A.pop()

    for k in range(len(A)):
        print("\n\t\t\t\t",A[k])

def ListTwo():# Populate a List with ten random numbers two-digit, EVEN
    A = []
    k = 0
    while k < 10:
        RandomNumber = int(random()*100)
        if RandomNumber > 9 and RandomNumber < 100 and RandomNumber % 2 == 0:
            A.append(RandomNumber)
            k = k + 1

    for k in range(len(A)):
        print ("\n\t\t\t\t",A[k])

    A.sort() # Python sort()
    print ("\n\t\tThe biggest number is =",A[9])
    print ("\n\t\tThe smallest number is =",A[0])
    
    # I want the AVERAGE
    Sum = 0
    for k in range(10):
        Sum = Sum + A[k]
    print ("\n\t\tThe average number is =",Sum/10)

    for k in range(len(A)):
        print ("\n\t\t\t\t",A[k])

    print("\n\n\n\t\tReverse Display\n\n")
    A.reverse()
    for k in range(len(A)):
        print ("\n\t\t\t\t",A[k])

                   
def main():
    Clear()
    Heading()
    StringOne()
    StringTwo()
    ListOne()
    ListTwo()
    
