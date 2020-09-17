#########################################################################
## Student Name: Daniel Navarro               Summer of 2016           ##
## Program Name: FirstProgram.py              Ventura College          ##
## Comments    : My first Python Program      CS V11                   ##
##                                            Programming Fundamentals ##
##                                            Professor RM Polito      ##
#########################################################################


import sys
import  os


def ClearTheScreen():
    os.system("cls")

def Heading():
    print ("\t\t   VENTURA COUNTY COMMUNITY COLLEGE DISTRICT")
    print ("\t\t\t\tVentura College")
    print ("\n\t\t    Programing Fundamentals - Summer of 2016")
    print ("\t\t\t\t     CS V11")
    print ("\t\t\t\t Daniel Navarro")

def CenterMessage():
    print ("\n\n\n\n\n\n\n\t\t  Welcome to Python Programmig...Best of Luck!\n\n")


def main():
    ClearTheScreen()
    Heading()
    CenterMessage()
