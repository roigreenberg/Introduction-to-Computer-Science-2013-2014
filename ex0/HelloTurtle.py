#####################################################################
# FILE : HelloTurtle.py
# WRITER : Roi Greenberg + roigreenberg + 305571234
# EXERCISE : intro2cs ex0 20013-2014
# DESCRIPTION:
# A simple program that print "Hello world" using Turtle graphics
#####################################################################

import turtle

# title for the display window
turtle.title ("fun with Turtle Graphics and Python")

turtle.up()         # lift the pen up, no drawing
turtle.goto(-100,-100)
turtle.down()       # pen is down, drawin now

# draw a square
turtle.goto(100,-100)
turtle.goto(100,100)
turtle.goto(-100,100)
turtle.goto(-100,-100)

# draw a circle
turtle.up()
turtle.goto(0,-100)
turtle.down()
turtle.circle(100)

# go to the center, leave a message
turtle.up()
turtle.goto(-70,-5)
turtle.write("Hello World",font=("Ariel", 20, "normal"))
turtle.done()
