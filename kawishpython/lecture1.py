import turtle
canvas=turtle.Screen()
v_pen = turtle.Turtle()
for _ in range(33):
    v_pen.forward(200)
    v_pen.right(190)
v_pen.hideturtle()
canvas.exitonclick()