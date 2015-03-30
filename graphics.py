"""
This module contains functions for all the graphics required for eXtreme tic-tac-toe.
"""

from turtle import *

def gamecanvas():
	"""
	Initializes the game board for play, and a system turtle.

	Outputs a turtle.
	"""

	# Creates a blank canvas of the appropriate size.
	setup(width = 1200, height = 1000, startx = 0, starty = 0)
	world = Screen()
	world.screensize(canvheight = 1000, canvwidth = 1200, bg = "white")
	screen_x, screen_y = world.screensize()
 	world.setworldcoordinates(0,0,screen_x,screen_y)

def systemturtle():
	"""
	Creates a system turtle with which to draw board elements.
	"""

	# Creates a system turtle.
	sys_turtle = Turtle()
	sys_turtle.speed(0)

	return sys_turtle

def draw_bigsquare(turtle):
	"""
	Draws a major square of the big tic-tac-toe board.
	"""

	# Faces the turtle east.
	turtle.setheading(0)
	
	# Sets the width of the pen to 5.
	turtle.pensize(5)
	
	side_len = 306

	for i in range(4):
		turtle.fd(side_len)
		turtle.lt(90)

def draw_bigboard(turtle):
	"""
	Draws the big tic-tac-toe board.
	"""
	
	x_pos = [40.0, 345.0, 650.0]
	y_pos = [40.0, 345.0, 650.0]

	for j in y_pos:
		for i in x_pos:
			turtle.pu()
			turtle.setpos(x = i, y = j)
			turtle.pd()
			draw_bigsquare(turtle)

def draw_smallboard(turtle):

	# Faces the turtle east.
	turtle.setheading(0)
	
	# Sets the width of the pen to 5.
	turtle.pensize(1)

	side_len = 306

	turtle.pd()

	for i in range(2):
		turtle.fd(side_len/3.0)
		turtle.lt(90)
		turtle.fd(side_len)
		turtle.bk(side_len)
		turtle.rt(90)

	turtle.fd(side_len/3.0)
	turtle.lt(90)

	for i in range(2):
		turtle.fd(side_len/3.0)
		turtle.lt(90)
		turtle.fd(side_len)
		turtle.bk(side_len)
		turtle.rt(90)

def draw_gameboard():
	
	gamecanvas()
	sys_turtle = systemturtle()
	draw_bigboard(sys_turtle)

	x_pos = [40.0, 345.0, 650.0]
	y_pos = [40.0, 345.0, 650.0]

	for j in y_pos:
		for i in x_pos:
			sys_turtle.pu()
			sys_turtle.setpos(x = i, y = j)
			sys_turtle.pd()
			draw_smallboard(sys_turtle)

	exitonclick()

def draw_xsmall(turtle,x_coord,y_coord):
	"""
	Draws a small x for the small boards.
	"""

	turtle.setpos(x_coord + 50, y_coord + 50)
	turtle.setheading(45)
	turtle.pensize(3)

	for i in range(4):
		turtle.fd(30)
		turtle.bk(30)
		turtle.lt(90)

def draw_xlarge(turtle,x_coord,y_coord):
	"""
	Draws a large x for the big board.
	"""

	turtle.setpos(x_coord + 150, y_coord + 150)
	turtle.setheading(45)
	turtle.pensize(10)
	
	for i in range(4):
		turtle.fd(200)
		turtle.bk(200)
		turtle.lt(90)

def reg_polygon(t,sides,len):
	angle = (360.0/float(sides))
	for i in range(sides):
		fd(t,len)
		lt(t,angle)

def circle(t,radius):
	
	circum = 3.141*2.0*float(radius)
	n = int(circum / 3) + 1
	len = circum / n
	reg_polygon(t,n,len)

def draw_osmall(turtle,x_coord,y_coord):
	"""
	Draws a small o for the small boards.
	"""

	# Sets the turtle into position.
	turtle.setpos(x_coord + 50, y_coord + 50)
	turtle.setheading(0)
	turtle.fd(30)
	turtle.lt(90)
	turtle.pensize(3)

	# Draws the circle.
	circle(turtle,30)

def draw_olarge(turtle,x_coord,y_coord):
	"""
	Draws a large x for the big board.
	"""

	# Sets the turtle into position.
	turtle.setpos(x_coord + 150, y_coord + 150)
	turtle.setheading(0)
	turtle.fd(200)
	turtle.lt(90)
	turtle.pensize(3)

	# Draws the circle.
	circle(turtle,200)
