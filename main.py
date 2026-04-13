# meow! meow! meow! :3
from turtle import *
# screen stuff meow
screen = Screen()
screen.bgcolor("black")
screen.title("name project meow")
screen.setup(width=1000, height=400)
# turtle setup time! meow
tt = Turtle("turtle")
rt = Turtle("turtle")
at = Turtle("turtle")
vt = Turtle("turtle")
it = Turtle("turtle")
st = Turtle("turtle")
tt.color("purple")
rt.color("yellow")
at.color("pink")
vt.color("green")
it.color("red")
st.color("orange")
# tutle move time! meow

# Letter T
tt.pensize(5)
tt.penup()
tt.goto(-400,-100)
tt.pendown()
tt.goto(-400,150)
tt.goto(-475,150)
tt.goto(-325,150)

# Letter R
rt.pensize(5)
rt.penup()
rt.goto(-275,-100)
rt.pendown()
rt.left(90)
rt.forward(250)
rt.right(90)
for i in range(18):
    rt.forward(10)
    rt.right(10)
rt.forward(8)
rt.left(115)
rt.forward(150)

# Letter A
at.pensize(5)
at.penup()
at.goto(-150,-100)
at.pendown()
at.left(90)
at.forward(180)
for i in range(18):
    at.forward(10)
    at.right(10)
at.forward(180)
at.right(180)
at.forward(120)
at.left(90)
at.forward(110)

# Letter V
vt.pensize(5)
vt.penup()
vt.goto(20,150)
vt.pendown()
vt.right(80)
vt.forward(250)
vt.left(155)
vt.forward(250)

# Letter I
it.pensize(5)
it.penup()
it.goto(150,-100)
it.pendown()
it.forward(100)
it.right(180)
it.forward(50)
it.right(90)
it.forward(250)
it.left(90)
it.forward(50)
it.right(180)
it.forward(100)

# Letter S
st.pensize(5)
st.penup()
st.goto(290,-40)
st.pendown()
st.right(90)
for i in range(22):
    st.forward(10)
    st.left(10)
st.forward(100)
for i in range(22):
    st.forward(10)
    st.right(10)

# ok done baii baii




















# weird exit on click thing. a bit redundant no? i feel like you'd want the window to stay open so you can see the final product...
screen.exitonclick()
