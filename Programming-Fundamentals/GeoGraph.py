################################################################################
## Student Name: Daniel Navarro                      Summer of 2016           ##
## Program Name: GeoGraph.py                         Ventura College          ##
## Comments    : Studying GEOMETRIC GRAPHICS.        CS V11                   ##
##                                                   Programming Fundamentals ##
##                                                   Engr. R.M. Polito        ##
################################################################################


from math     import *
from graphics import *


def DeclareGlobals():
    global Row,Col,Offset,MyWindow,DrawTheLine

    Row = 1100
    Col = 680
    Offset = Col / 32

    MyWindow = GraphWin("Graphics",Row,Col,True) 

def DrawTheCrossHairs():
    PointA = Point(0    , Col/2)
    PointB = Point(Row  , Col/2)
    PointC = Point(Row/2,     0)    
    PointD = Point(Row/2,   Col)

    DrawTheLine(PointA,PointB,color_rgb(255,0,0),2)
    DrawTheLine(PointC,PointD,color_rgb(255,0,0),2)  

def DrawTheBigStar():
    Diameter  = Col - 2 * Offset
    MyRadius  = Diameter/2
    MyCenterX = Row/2
    MyCenterY = Col/2
    
    DrawTheStar(MyCenterX,MyCenterY,MyRadius,color_rgb(0,255,0),2)
    
def DrawStarsInQuadrants():
    Diameter = Col / 2 - 2 * Offset
    MyRadius = Diameter / 2
    
    MyCenterX = 3*Row / 4
    MyCenterY = Col/4
    DrawTheStar(MyCenterX,MyCenterY,MyRadius,color_rgb(0,255,0),2)

    MyCenterX = Row / 4
    MyCenterY = Col/4
    DrawTheStar(MyCenterX,MyCenterY,MyRadius,color_rgb(0,255,0),2)

    MyCenterX = Row / 4
    MyCenterY = 3*Col/4
    DrawTheStar(MyCenterX,MyCenterY,MyRadius,color_rgb(0,255,0),2)

    MyCenterX = 3*Row / 4
    MyCenterY = 3*Col / 4
    DrawTheStar(MyCenterX,MyCenterY,MyRadius,color_rgb(0,255,0),2)
    
def DrawTheStar(CenterX,CenterY,Radius,MyColor,MyWidth):
    
    PointA = Point(CenterX + Radius * cos( 18*pi/180),CenterY - Radius*sin( 18*pi/180))
    PointB = Point(CenterX + Radius * cos( 90*pi/180),CenterY - Radius*sin( 90*pi/180))
    PointC = Point(CenterX + Radius * cos(162*pi/180),CenterY - Radius*sin(162*pi/180))
    PointD = Point(CenterX + Radius * cos(234*pi/180),CenterY - Radius*sin(234*pi/180))
    PointE = Point(CenterX + Radius * cos(306*pi/180),CenterY - Radius*sin(306*pi/180))

    #### Drawing will be from D-B,B-E,E-C,C-A,A-D
    DrawTheLine(PointD,PointB,MyColor,MyWidth)
    DrawTheLine(PointB,PointE,MyColor,MyWidth)
    DrawTheLine(PointE,PointC,MyColor,MyWidth)
    DrawTheLine(PointC,PointA,MyColor,MyWidth)
    DrawTheLine(PointA,PointD,MyColor,MyWidth)

    CircleA = Circle(Point(CenterX,CenterY),Radius)
    CircleA.setOutline(MyColor)
    CircleA.setWidth(MyWidth)
    CircleA.draw(MyWindow)

def DrawTheLine(PointX,PointY,MyColor,MyWidth):
    MyLine = Line(PointX,PointY)
    MyLine.setOutline(MyColor)
    MyLine.setWidth(MyWidth)
    MyLine.draw(MyWindow)

    
def main():
    DeclareGlobals()
    DrawTheCrossHairs()
    #DrawTheBigStar()
    DrawStarsInQuadrants()
    
