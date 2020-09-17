################################################################################
## Student Name: Daniel Navarro                      Programming Fundamentals ##
## program name: Formulas.py                          CS V11                  ##
## Comment     : Covering Chapter 2 Assingment       Summer of 2016           ##
##               More on print command               Ventura College          ##
##                                                   Professor RM Polito      ##
################################################################################


import  sys
import   os
import math
from random import *


def ClearTheScreen():
    os.system("cls")

def Heading():
    print ("\t\t  MATH AND SCIENCE DIVISION OF VENTURA COLLEGE")
    print ("\t\t\t  Computer Scinece Department\n")
    print ("\t\t       CS V11 - Programming Fundamentals")
    print ("\t\t\t\t Daniel Navarro\n\n\n")

def FormulaOne():
    print ("\t\t Performing FormulaOne:\n\n")
    A = 1
    B = 3
    C = 5
    D = 2
    E = 1.*(A + B) / (C - D) # Instead of using float, use (1.*) to get decimals
    print("\t\t\tThe value of E = ", round(E,3))

def FormulaTwo():
    print ("\n\n\t\t Performing FormulaTwo:\n\n")
    A = 4.3
    B = 3.1
    C = 2.1
    D = 6.5
    E = (A*B - C/D) / (A + B/C) # Since given all floats (non integers) there is no need for 1.0*
    print (" When A =", A," and B =",B," and C =",C," and D =",D,"then FormulaTwo =",round(E,2))

def FormulaThree(): # print #'s: 3,5,7,9...21
    print ("\n\n\t\tPerforming FormulaThree:\n")
    for k in range(10):
        print ("\t\t\t\t\t",2*k+3)

def FormulaFour(): # print #'s: 95,90,85,80...50
    print ("\n\n\t\tPerforming FormulaFour:\n")
    for k in range(10):
        print ("\t\t\t\t\t",95-k*5)
        
def FormulaFive(): # print #'s: 1,2,4,8...1024
    print ("\n\n\t\tPerforming FormulaFive:\n")
    for k in range(11):
        print ("\t\t\t\t\t",2**k)

def FormulaSix(): # print #'s: 1,2,4,8...1024
    print ("\n\n\t\t Performing FormulaSix:\n")
    for k in range(11):
        print ("\t\t\t\t\t",(-2)**k)

def FormulaSeven(): # I will perform the square root of A
    print ("\n\n\t\tPerforming FormulaSeven:\n\n")
    A = 144
    B = math.sqrt(A) 
    print ("\t\t\tThe square root of",A," is equal to",B,"\n\n")

def FormulaEight(): # We will solve the Ideal Gas Formula PV = nRT(T+273). Find formula for n?
    P = 100
    V = 44.8
    R = 833
    T = 100
    n = P*V/(R*(T+273))
    print("\n\n\t\tPerforming FormulaEigth:\n\n")
    print("\t\t\tThe value of n =", round(n,3))
    
def FormulaNine():
    V = 1000
    r = math.sqrt(3*V/(4*math.pi))**(1./3)
    print("\n\n\t\t Performing FormulaNine:\n\n")
    print("\t\t\tThe value of r =", round(r,3))

def FormulaTen(): # P = Deposit(1+R)^n. Solve for n? 
    P = 200000
    D = 5000
    r = 0.09
    n = (math.log(P) - math.log(D)) / math.log(1+r)
    print("\n\n\t\t  Performing FormulaTen:\n\n")
    print("\t\t\tThe value of n =", round(n,3))
    print("\n\n")
    
def HarderOne(): # generate 10 random numbers that are two-digit and EVEN
    C = 0
    while C < 10:
        Numbers = int(random()*10000)
        if Numbers > 9 and Numbers < 100 and Numbers % 2 == 0:
            print ("\t\t\t\tThe numbers are:", Numbers)
            C = C + 1

def HarderTwo(): # Generate 17 #'s 4-digit ODD and divisible by 7
    A = 0
    while A < 17:
        Numbers = int(random()*10000)
        if Numbers > 999 and Numbers < 10000 and Numbers % 7 == 0 and Numbers % 2 != 0:
            print ("\t\t\t\tThe numbers are:", Numbers)
            A = A + 1

    
def main():
    ClearTheScreen()
    Heading()
    FormulaOne()
    FormulaTwo()
    FormulaThree()
    FormulaFour()
    FormulaFive()
    FormulaSix()
    FormulaSeven()
    FormulaEight()
    FormulaNine()
    FormulaTen()
    HarderOne()
    HarderTwo()
