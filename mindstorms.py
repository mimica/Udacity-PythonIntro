import turtle

def draw_square():
	turtle.setup(1024, 768)
	window = turtle.Screen()
	window.bgcolor("lightgreen")
	window.title("Hello little baby")

	toto = turtle.Turtle()
	toto.shape("turtle")
	toto.shapesize(3, 3, 3)
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

	pipo = turtle.Turtle()
	pipo.shape("arrow")
	pipo.color("red")
	pipo.shapesize(3, 3, 3)
	toto.speed(6)
	pipo.circle(200)

	bebe = turtle.Turtle()
	bebe.shape("classic")
	bebe.shapesize(3, 3, 3)
	bebe.color("black")
	bebe.speed(3)
	bebe.forward(300)
	bebe.left(120)
	bebe.forward(300)
	bebe.left(120)
	bebe.forward(300)

	window.exitonclick()


draw_square()
