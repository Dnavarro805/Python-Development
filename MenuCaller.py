################################################################################
## Student Name: Daniel Navarro                      Summer of 2016           ##
## Program Name: MenuCaller.py                       Ventura College          ##
## Comments    : Studying the while command.         CS V11                   ##
##                                                   Programming Fundamentals ##
##                                                   Engr. R.M. Polito        ##
################################################################################


import   os
import  sys
from   math import *
from random import *


def Clear():
    os.system("cls")

def EjectTheLine(A):
    Present = 0
    while Present < A:
        print ()
        Present = Present + 1

def MarginLeft(A):
    Past = 0
    while Past < A:
        print ()
        Past = Past + 1

def CenterTheDude(A,B):
    EjectTheLine(B)
    k = len(A)
    k = (80-k)/2
    MarginLeft(k)
    print (A)

def Heading():
    Clear()
    CenterTheDude("UNITED STATES OF AMERICA",0)
    CenterTheDude("Washinton DC",0)
    CenterTheDude("Programming Fundamentals - Summer of 2016",1)
    CenterTheDude("Submitted by",1)
    CenterTheDude("Daniel Navarro",0)

def MyMenu():
    EjectTheLine(3)
    MarginLeft(20)
    print ("[A] - Do the for x in range (10) sample command")

    EjectTheLine(2)
    MarginLeft(20)
    print ("[B] - Three-digit EVEN on First While Loop Command")

    EjectTheLine(2)
    MarginLeft(20)
    print ("[C] - Two-digit ODD on the Second While Loop Command")

    EjectTheLine(2)
    MarginLeft(20)
    print ("[D] - Do the First List")
    
    EjectTheLine(2)
    MarginLeft(20)
    print ("[E] - Do the Second List")

    EjectTheLine(2)
    MarginLeft(20)
    print ("[Q] - Quit Quit Quit!")

def DoTheRangeCommand():
    EjectTheLine(2)
    for x in range(10):
        MarginLeft(40)
        print (2**x)
    EjectTheLine(1)
    MarginLeft(24)
    os.system("pause")

def DoTheFirstFormula():
    A = 2
    B = 3
    C = 4
    EjectTheLine(2)
    MarginLeft(24)
    print ("When A =",A,"and B =",B,"and C =",C,"then Formula One =",(1.*1/(A*B)+1.*C/(A*B))/(1-1.*A*B/C))
    EjectTheLine(1)
    MarginLeft(24)
    os.system("pause")

def DoTheExitCommand():
    EjectTheLine(2)
    MarginLeft(24)
    print ("Goodbye!!!")

def DoTheFirstWhileLoop():
    EjectTheLine(2)
    x = 0
    while x < 10:
        Zena = int(random()*1000)
        if Zena > 99 and Zena < 1000 and Zena % 2 == 0:
            MarginLeft(40)
            print (Zena)
            x = x + 1
    EjectTheLine(1)
    MarginLeft(24)
    os.system("pause")

def DoTheSecondWhileLoop():
    EjectTheLine(2)
    x = 0
    while x < 10:
        Zena = int(random()*1000)
        if Zena > 9 and Zena < 100 and Zena % 2 != 0:
            MarginLeft(40)
            print (Zena)
            x = x + 1
    EjectTheLine(1)
    MarginLeft(24)
    os.system("pause")

def DoTheFirstList():
    EjectTheLine(2)
    MarginLeft(24)
    print ("I am doing the First Sample on Lists: ")
    EjectTheLine(2)

    A =[]
    k = 0
    while k < 10:
        Holder = int(random()*1000)
        A.append(Holder)
        k = k + 1       

    EjectTheLine(2)
    for x in range(len(A)):
        MarginLeft(37)
        print (A[x])

    A.sort()
    EjectTheLine(2)
    MarginLeft(24)
    print ("The Biggest Number Is =",A[9])

    A.sort()
    EjectTheLine(2)
    MarginLeft(24)
    print ("The Smallest Number Is =",A[0])
    EjectTheLine(2)
         
    EjectTheLine(1)
    MarginLeft(24)
    os.system("pause")

def DoTheSecondList():
    EjectTheLine(2)
    MarginLeft(24)
    print ("I am doing the Second List Sample: ")
    EjectTheLine(2)

    A = [] # This declares an EMPTY LIST
    # I want to populate with random integers
    k = 0
    while k < 10:
        Holder = int(random()*1000)
        A.append(Holder)
        k = k + 1

    EjectTheLine(2)
    for x in range(len(A)):
        MarginLeft(38)
        print (A[x])

    A.sort()
    EjectTheLine(2)
    for x in range(len(A)):
        MarginLeft(38)
        print (A[x])

    A.reverse()
    EjectTheLine(2)
    for x in range(len(A)):
        MarginLeft(38)
        print (A[x])

    EjectTheLine(1)
    MarginLeft(24)
    os.system("pause")

def MenuCaller():
    Response = ''
    while Response != 'Q':
        Heading()
        MyMenu()
        EjectTheLine(2)
        MarginLeft(35)
        Response = input("Please enter A,B,C,D,E,Q: ")
        if Response == 'A' or Response == 'a':
            DoTheRangeCommand()
        if Response == 'B' or Response == 'b':
            DoTheFirstWhileLoop()
        if Response == 'C' or Response == 'c':
            DoTheSecondWhileLoop()
        if Response == 'D' or Response == 'd':
            DoTheFirstList()
        if Response == 'E' or Response == 'e':
            DoTheSecondList() 
        if Response == 'Q' or Response == 'q':
            DoTheExitCommand()

            
def main():
    MenuCaller()
    
