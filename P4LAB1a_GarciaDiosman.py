import turtle          
win = turtle.Screen()
win.title("Square & Triangle")

# Create the triangle attribute and add the display options
t = turtle.Turtle()     
t.pensize(5)
t.pencolor("blue")
t.shape("triangle")

# draw the triangle
for i in (1,2,3):
    t.forward(80)
    t.left(120)

# Create the square attribute and add the display options
s = turtle.Turtle()     
s.pensize(5)
s.pencolor("red")
s.shape("square")

# draw the square
for i in (1,2,3,4):
    s.forward(50)
    s.left(90)

# end commands
win.mainloop()             # Wait for user to close window
