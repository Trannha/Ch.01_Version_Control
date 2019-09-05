'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
yoda=turtle.Turtle()
yoda.shape=turtle
screen=turtle.Screen() # makes a screen object
screen.bgcolor('black') # colors the screen
yoda.pensize(3) # width of pen line
yoda.speed(20)  # speed of drawing. Go fast to not waste time.
yoda.color("#00FF00")
yoda.circle(100)  #head
yoda.penup()
yoda.setpos(50,185) #right ear
yoda.pendown()
yoda.circle(50)
# yoda.goto(200,210)
# yoda.goto(88,145)
# yoda.penup()
yoda.setpos(-50,185)  #left ear
yoda.pendown()
yoda.circle(50)
yoda.penup()
#yoda.goto(-200,210)
# yoda.goto(-88,145)
yoda.goto(45,190)
yoda.pendown()
yoda.circle(15)
yoda.penup()
yoda.goto(-45,190)
yoda.pendown()
yoda.circle(15)
#yoda.fillcolor('white')
yoda.penup()
yoda.setpos(200,-300)
yoda.pendown()
yoda.pencolor('#00FF00')
yoda.write('Nha Tran',font=("Arial", 12, "normal"))
yoda.penup()
yoda.goto(50,40)
yoda.pendown()
yoda.left(90)
yoda.circle(40, 180)



turtle.exitonclick() #Keeps pycharm window open
