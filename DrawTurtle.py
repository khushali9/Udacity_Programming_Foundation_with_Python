# -*- coding: utf-8 -*-
import turtle
def draw_square():
	window=turtle.Screen()
	window.bgcolor("black")
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("red")
	brad.speed(2)
	#So when we write turtle.Turtle() we r calling function init() of the class it creates space for the instance of the class

	brad.forward(100)
	brad.right(90) #not 100 give 90 degree
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(100)
	brad.forward(100)
	brad.right(90)
	
	window.exitonclick()
#So when we write turtle.Turtle() we r calling function init() of the class it creates space for the instance of the class
#For loop that will work 4 time —>for i in range (1,5):
#for drawing we need window so which is

draw_square()

