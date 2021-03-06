#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic",
"arrow", "turtle", "circle", "square", "triangle", "classic",
"arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold",
"red", "blue", "green", "orange", "purple", "gold",
"red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.penup()
  t.color(turtle_colors.pop())
  my_turtles.append(t)

 

#this tells it where to start drawing
startx = 0
starty = 0
direction= -45
length=50

# this makes each turtle do sequence of commands. So it moves out some distance,turns, goes forward, and stops.
for t in my_turtles:
  t.goto(startx, starty)
  t.pendown()
  t.right(direction)     
  t.forward(length)




#	This changes how the other turtle starts
  startx = t.xcor()
  starty = t.ycor()
  direction= direction+45
  length=length+3



wn = trtl.Screen()
wn.mainloop()
