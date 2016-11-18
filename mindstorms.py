import turtle

def draw_square():
	window = turtle.Screen()
	window.bgcolor("red")

	toto = turtle.Turtle()
	toto.shape("turtle")
	toto.color("blue")
	toto.speed(1)
	toto.forward(100)
	toto.right(90)
	toto.forward(100)
	toto.right(90)
	toto.forward(100)
	toto.right(90)
	toto.forward(100)
	toto.right(90)

	window.exitonclick()


draw_square()
