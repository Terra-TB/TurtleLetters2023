from turtle import *






#draw the letter C
def drawC():
  pendown()
  left(180)
  for i in range (180):
    forward(1)
    right(1)
  penup()
  forward(30)

#draw the letter G
def drawG():
  forward(50)
  pendown()
  for i in range (180):
    backward(1)
    left(1)
  right(90)
  forward(50)
  left(90)
  forward(30)
  
  



def drawH():
  penup()
  goto(-50, -50)
  pendown()
  forward(125)
  left(90)
  forward(75)
  right(180)
  forward(150)
  right(180)
  forward(75)
  left(90)
  forward(125)
  right(90)
  forward(75)
  right(180)
  forward(150)
  penup()

def drawW():
  goto(125,-50)
  pendown()
  left(45)
  forward(75)
  left(95)
  forward(70)
  right(95)
  forward(75)
  left(95)
  forward(75)
  
def drawC():
  goto(0, 0)
  penup()
  backward(50)
  left(90)
  forward(25)
  forward(20)
  pendown()
  for i in range(17):
    left(20)
    forward(20)

def drawL():
  penup()
  goto(0, -20)
  left(20)
  pendown()
  forward(105)
  penup()
  goto(0, -20)
  right(90)
  pendown()
  forward(75)

def drawD():
  forward(50)
  penup()
  right(180)
  forward(80)
  pendown()
  right(90)
  forward(60)
  left(90)
  for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    forward(20)
    left(20)
  left(70)
  forward(60)


def upperT():
    pendown()
    forward(95)
    penup()
    right(180)
    forward(47.5)
    left(90)
    pendown()
    forward(100)
    penup()
    right(180)
    forward(100)
    right(90)
    forward(100)
    return
def upperJ():
    pendown()
    right(90)
    forward(75)
    penup()
    right(90)
    forward(50)
    pendown()
    right(270)
    circle(25,180)
    return

def drawN():
  left(90)
  pendown()
  forward(100)
  right(150)
  forward(115)
  left(150)
  forward(100)

def drawB():
  pendown()
  forward(100)
  right(90)
  forward(20)
  right(40)
  forward(40)
  right(100)
  forward(40)
  left(100)
  forward(40)
  right(100)
  forward(40)
  right(40)
  forward(20)


def drawA():
  pendown()
  forward(200)
  right(150)
  forward(200)
  left(180)
  forward(100)
  left(75)
  forward(60)


def drawR():
  right(90)
  forward(50)
  right(180)
  forward(200)
  right(90)
  for i in range(90):
    right(2)
    forward(2)
  left(120)
  forward(100)

def drawG():
  penup()
  goto(-50,100)
  pendown()
  left(180)
  forward(150)
  left(90)
  forward(200)
  left(90)
  forward(150)
  left(90)
  forward(75)
  left(90)
  forward(100)
  right(180)

def drawF():
  penup()
  goto(150, 100)
  pendown()
  left(180)
  forward(150)
  left(90)
  forward(75)
  left(90)
  forward(100)
  right(180)
  forward(100)
  left(90)
  forward(125)
  left(90)


def drawR():
  penup()
  goto(-300, -100)
  pendown()
  setheading(90)
  forward(250)
  right(90)
  forward(100)
  right(90)
  forward(100)
  right(90)
  forward(100)
  left(125)
  forward(180.27)

def drawW():
  penup()
  goto(-150, 100)
  pendown()
  setheading(-65)
  forward(254)
  left(130)
  forward(254)
  right(130)
  forward(254)
  left(130)
  forward(254)

def A():
  penup()
  pencolor('#111166')
  goto(-200, 100)
  pendown()
  goto(-100, -100)
  goto(-150, 0)
  goto(-250, 0)
  goto(-200, 100)
  goto(-300, -100)
  penup()
def S():
  goto(200, 100)
  pendown()
  goto(100, 100)
  goto(100, 0)
  goto(200, 0)
  goto(200, -100)
  goto(100, -100)

def drawY():
  penup()
  goto(-50,0)
  pendown()
  goto(0,50)
  penup()
  goto(-25,25)
  pendown()
  goto(-50,50)
def drawP():
  penup()
  goto(75,0)
  pendown()
  goto(75,50)
  goto(100,50)
  goto(100,25)
  goto(75,25)


def drawN():
  right(180)
  penup()
  goto(150,0)
  pendown()
  left(90)
  forward(100)
  right(150)
  forward(115)
  left(150)
  forward(100)



def createA():
   left(90)
   forward(100)
   right(90)
   forward(50)
   right(90)
   forward(100)
   right(90)
   forward(10)
   right(90)
   forward(50)
   left(90)
   forward(30)
   left(90)
   forward(50)
   right(90)
   forward(10)
   penup()
   right(90)
   forward(70)
   right(90)
   forward(10)
   pendown()
   forward(30)
   left(90)
   forward(15)
   left(90)
   forward(30)
   left(90)
   forward(15)
   penup()
   forward(100)

def createM():
  left(90)
  forward(70)
  left(90)
  forward(30)
  pendown()
  forward(100)
  right(135)
  forward(100)
  left(90)
  forward(100)
  right(135)
  forward(100)
  right(90)
  forward(15)
  right(90)
  forward(60)
  left(135)
  forward(75)
  right(90)
  forward(75)
  left(135)
  forward(60)
  right(90)
  forward(20)


def drawB ():
  penup()
  goto(-50,-50)
  pendown()
  forward(100)
  left(90)
  forward(100)
  left(90)
  forward(100)
  left(90)
  forward(100)
  left(180)
  forward(200)
  

def drawR ():
  penup()
  goto(-50,-50)
  pendown()
  left(90)
  forward(200)
  right(90)
  forward(90)
  right(25)
  forward(26)
  right(25)
  forward(26)
  right(25)
  right(25)
  forward(26)
  right(25)
  forward(26)
  right(25)
  forward(26)
  right(25)
  forward(26)
  forward(50)
  left(120)
  forward(125)

def writeV():
  penup()
  goto(-200,0)
  pendown()
  left(135)
  forward(-200)
  right(45)
  forward(200)

def writeC():
  penup()
  goto(100,50)
  pendown()
  left(90)
  forward(150)
  left(90)
  forward(175)
  left(90)
  forward(150)


def drawD ():
  #Draw D
  penup()
  goto (-100,0)
  pendown()
  left(90)
  forward(80)
  right(120)
  forward(100)
  right (135)
  forward (100)  
  
def drawP ():
  #Draw P
  penup()
  setheading(90) 
  goto (40,0)
  pendown()
  forward (80)
  right (125)
  forward (60)
  right (125)
  forward (60)

def drawE():
  pendown()
  forward(75)
  left(180)
  forward(75)
  left(90)
  forward (50)
  left(90)
  forward(75)
  left(180)
  forward(75)
  left(90)
  forward (50)
  left(90)
  forward(75)

def drawS():
  penup()
  forward(30)
  pendown()
  forward(75)
  left(90)
  forward(50)
  left(90)
  forward(75)
  right(90)
  forward(50)
  right(90)
  forward(75)

def drawN():
  pendown()
  right(90)
  forward(100)
  right(135)
  forward(130)
  left(135)
  forward(100)
  penup()
def drawV():
  left(90)
  forward(150)
  left(90)
  forward(100)
  right(155)
  pendown()
  forward(100)
  left(135)
  forward(100)






