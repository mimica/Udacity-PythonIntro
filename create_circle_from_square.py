import turtle

def draw_square(aTurtle):
	for i in range(1, 5):
		aTurtle.forward(100)
		aTurtle.right(90)

def draw_art():
	turtle.setup(1024, 768)
	window = turtle.Screen()
	window.bgcolor("lightgreen")
	window.title("Hello little baby")

	toto = turtle.Turtle()
	toto.shape("turtle")
	toto.shapesize(3, 3, 3)
	toto.color("blue")
	toto.speed(6)
	for i in range(1, 37):
		draw_square(toto)
		toto.right(10)


draw_art()
