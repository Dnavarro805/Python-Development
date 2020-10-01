################################################################################
## Student Name: Daniel Navarro                      Summer of 2016           ##
## Program Name: MasterMenu.py                       Ventura College          ##
## Comments    : Studying for Final.                 CS V11                   ##
##               Lecture Notes.                      Programming Fundamentals ##
##                                                   Engr. R.M. Polito        ##
################################################################################


import     os
from     math import *
from   random import *
from graphics import *


def Clear():
    os.system("cls")

def EjectTheLine(A): # How many lines (A) to go down
    Present = 0
    while Present < A:
        print()
        Present = Present + 1

def MarginLeft(A): # How many spaces (A) to move to the right
    Past = 0
    while Past < A:
        print (""),
        Past = Past + 1

def CenterTheDude(A,B): # The A is the TEXT reciever
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
    print ("[A] - Formula Interpretation")

    EjectTheLine(2)
    MarginLeft(20)
    print ("[B] - Do Generation using for x in range(N)")

    EjectTheLine(2)
    MarginLeft(20)
    print ("[C] - Do random 3-digit NOT divisible by 1,2,3,5,7,11")

    EjectTheLine(2)
    MarginLeft(20)
    print ("[D] - Do String Manipulation")

    EjectTheLine(2)
    MarginLeft(20)
    print ("[E] - Do graphics")

    EjectTheLine(2)
    MarginLeft(20)
    print ("[Q] - Quit Quit Quit")

def DoTheFirstReview(): # Formula Interpretation 
    EjectTheLine(2)
    A = 1
    B = 2
    C = 3
    MarginLeft(3)
    print ("When A =",A,"and B =",B,"and C =",C,"then formula =",(A/(1.0*B/C) - C/(1.0*B/A)) / (1.0*1/B - 1.0*C /(A*B)))

    
    EjectTheLine(1)
    MarginLeft(24)
    os.system("pause")

def DoTheSecondReview(): # Number generation using for x in range(A) ONLY

    EjectTheLine(2)
    for k in range (10):
        MarginLeft(40)
        print (128-2**k)

    EjectTheLine(1)
    MarginLeft(24)
    os.system("pause")

def DoTheExitCommand(): # EXIT Command 
    EjectTheLine(2)
    MarginLeft(24)
    print ("Sayanara.. hasta la vista..baby!!!")

def DoTheFirstWhileCommand(): # Created 20 random numbers and printed the biggest and smallest 
    A = []
    k = 0
    while k < 10:
        Holder = int(random()*10000)
        if Holder > 99 and Holder < 1000 and Holder % 2 != 0 and Holder % 3 != 0 and Holder % 5 != 0 and Holder % 7 != 0 and Holder % 11 != 0:
            A.append(Holder)
            k = k + 1

    EjectTheLine(2)
    for k in range(len(A)):
        MarginLeft(40)
        print (A[k])

    EjectTheLine(1)
    MarginLeft(24)
    os.system("pause")

def DoTheFirstStringCommand(): # String manipulation using input command
    EjectTheLine(2)
    MarginLeft(12)
    A = input("Give me a string: ") # len(A) == 5, and -1 == 4,and - k == 0,1,2,3,4,5...
    EjectTheLine(1)

    EjectTheLine(2)
    for k in range(len(A)):
        MarginLeft(45-k)
        print (A[len(A)-1-k],"",A[k])
 
    EjectTheLine(1)
    MarginLeft(24)
    os.system("pause")

def DoTheFirstDrawing(): 
    global Row,Col,Offset,MyWindow,DrawTheLine

    Row = 1100
    Col = 680
    Offset = Col / 32

    MyWindow = GraphWin("Graphics",Row,Col,True)

def DrawTheCrossHairs():
    PointA = Point(0      , Col/2)
    PointB = Point(Row    , Col/2)
    PointC = Point(2*Row/3,     0)    
    PointD = Point(2*Row/3,   Col)
    PointE = Point(Row/3  ,     0)    
    PointF = Point(Row/3  ,2*Col )

    DrawTheLine(PointA,PointB,color_rgb(255,0,0),2)
    DrawTheLine(PointC,PointD,color_rgb(255,0,0),2)
    DrawTheLine(PointE,PointF,color_rgb(255,0,0),2)

def DrawTheLine(PointX,PointY,MuhColor,MuhWidth):
    MuhLine = Line(PointX,PointY)
    MuhLine.setOutline(MuhColor)
    MuhLine.setWidth(MuhWidth)
    MuhLine.draw(MyWindow)

def DrawTheHexagon():
    H     = (Col / 2 - 2 * Offset)/2 
    Side  = int(2* sqrt(3) * H /3)

    PointA = Point(Row/6-Side/2,3*Col/4-H)
    PointB = Point(Row/6+Side/2,3*Col/4-H)
    PointC = Point(Row/6+Side    ,3*Col/4)
    PointD = Point(Row/6+Side/2,3*Col/4+H)
    PointE = Point(Row/6-Side/2,3*Col/4+H)
    PointF = Point(Row/6 -Side ,3*Col/4  )

    DrawTheLine(PointA,PointB,'blue',2)
    DrawTheLine(PointB,PointC,'blue',2)
    DrawTheLine(PointC,PointD,'blue',2)
    DrawTheLine(PointD,PointE,'blue',2)
    DrawTheLine(PointE,PointF,'blue',2)
    DrawTheLine(PointF,PointA,'blue',2)

def DrawTheSquare():
    Side = Col / 2 - 2 * Offset

    PointA = Point(5*Row/6-Side/2,3*Col/4-Side/2)
    PointB = Point(5*Row/6+Side/2,3*Col/4-Side/2)
    PointC = Point(5*Row/6+Side/2,3*Col/4+Side/2)
    PointD = Point(5*Row/6-Side/2,3*Col/4+Side/2)

    DrawTheLine(PointA,PointB,'blue',2)
    DrawTheLine(PointB,PointC,'blue',2)
    DrawTheLine(PointC,PointD,'blue',2)
    DrawTheLine(PointD,PointA,'blue',2)

def DrawTheTriangle():
    H = Col / 2 - 2 * Offset
    Side = int(2 *sqrt(3) * H / 3)
    
    PointA = Point(Row/2         ,Col/4-H/2)
    PointB = Point(Row/2 + Side/2,Col/4+H/2)
    PointC = Point(Row/2 - Side/2,Col/4+H/2)

    DrawTheLine(PointA,PointB,'blue',2)
    DrawTheLine(PointB,PointC,'blue',2)
    DrawTheLine(PointC,PointA,'blue',2)

def DrawTheRectangle():
    L = 3*(Row/2)/4 
    W = Col/2 - 2 * Offset

    PointA = Point(Row/4-L/2 ,3*Col/4-W/2) 
    PointB = Point(Row/4+L/2 ,3*Col/4-W/2)
    PointC = Point(Row/4+L/2 ,3*Col/4+W/2)
    PointD = Point(Row/4-L/2 ,3*Col/4+W/2)

    DrawTheLine(PointA,PointB,'blue',2)
    DrawTheLine(PointB,PointC,'blue',2)
    DrawTheLine(PointC,PointD,'blue',2)
    DrawTheLine(PointD,PointA,'blue',2)

def DrawTheCircle():
    Diameter = Col / 2 - 2* Offset 
    PointA = Point(3*Row/4,Col/4)

    CircleA = Circle(PointA, Diameter/2)
    CircleA.setFill('blue')
    CircleA.draw(MyWindow)

def DrawTheStar():
    Diameter = Col/2  - 2 * Offset
    Radius = Diameter / 2
    
    PointA = Point(3*Row/4 + Radius * cos( 18*pi/180),Col/4 - Radius*sin( 18*pi/180))
    PointB = Point(3*Row/4 + Radius * cos( 90*pi/180),Col/4 - Radius*sin( 90*pi/180))
    PointC = Point(3*Row/4 + Radius * cos(162*pi/180),Col/4 - Radius*sin(162*pi/180))
    PointD = Point(3*Row/4 + Radius * cos(234*pi/180),Col/4 - Radius*sin(234*pi/180))
    PointE = Point(3*Row/4 + Radius * cos(306*pi/180),Col/4 - Radius*sin(306*pi/180))

    # Drawing will be from D-B,B-E,E-C,C-A,A-D
    DrawTheLine(PointD,PointB,'black',2)
    DrawTheLine(PointB,PointE,'black',2)
    DrawTheLine(PointE,PointC,'black',2)
    DrawTheLine(PointC,PointA,'black',2)
    DrawTheLine(PointA,PointD,'black',2)

def MenuCaller():
    Response = ''
    while Response != 'Q':
        Heading()
        MyMenu()
        EjectTheLine(2)
        MarginLeft(35)
        Response = input("Please enter A,B,C,D,E,Q: ")
        if Response == 'A' or Response == 'a':
            DoTheFirstReview()
        if Response == 'B' or Response == 'b':
            DoTheSecondReview()
        if Response == 'C' or Response == 'c':
            DoTheFirstWhileCommand()
        if Response == 'D' or Response == 'd':
            DoTheFirstStringCommand()
        if Response == 'E' or Response == 'e':
            DoTheFirstDrawing()
            DrawTheCrossHairs()
            DrawTheHexagon()
            DrawTheSquare()
            DrawTheTriangle()
        if Response == 'Q' or Response == 'q':
            DoTheExitCommand()        


def main():
    MenuCaller()
