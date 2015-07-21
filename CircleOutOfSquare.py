# -*- coding: utf-8 -*-
import turtle
def move_turtle(turtle_in):
	for i in range(1,5):
		turtle_in.forward(100)
		turtle_in.right(90)#not 100 give 90 degree

def draw_square():
	window=turtle.Screen()
	window.bgcolor("black")
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("red")
	brad.speed(2)
	#So when we write turtle.Turtle() we r calling function init() of the class it creates space for the instance of the class
	for i in range(1,37):
		move_turtle(brad)
		brad.right(10)
	
	window.exitonclick()
#So when we write turtle.Turtle() we r calling function init() of the class it creates space for the instance of the class
#For loop that will work 4 time —>for i in range (1,5):
#for drawing we need window so which is

draw_square()

#for cirlce
#brad1 = turtle.Turtle()
#brad1.shape("arrow")
#brad1.color("red")
#brad1.circle(100)
