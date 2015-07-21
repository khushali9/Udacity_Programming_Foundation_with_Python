# -*- coding: utf-8 -*-
import turtle
def draw_square():
	window=turtle.Screen()
	window.bgcolor("black")
	brad = turtle.Turtle()
	#So when we write turtle.Turtle() we r calling function init() of the class it creates space for the instance of the class

	brad.forward(100)
	brad.right(100)
	brad.shape("turtle")
	brad.color("red")
	brad.speed()
	window.exitonclick()
#So when we write turtle.Turtle() we r calling function init() of the class it creates space for the instance of the class
#For loop that will work 4 time —>for i in range (1,5):
#for drawing we need window so which is

draw_square()

