import turtle          
win = turtle.Screen()
win.title("Initials")

# Create the initials attribute and add the display option
t = turtle.Turtle()     
t.pensize(5)
t.pencolor("blue")
t.shape("turtle")

# Draw the first initial D
t.left(90)
t.fd(100)
t.right(90)
t.circle(-50,180)
t.penup()

# Draw the seconf initial G
t.bk(110)
t.pendown()
t.right(180)
t.fd(30)
t.circle(20,220)
t.penup()
t.circle(20,140)
t.pendown()
t.bk(40)
t.left(90)
t.fd(70)
t.circle(-30,150)

# end commands
win.mainloop()             # Wait for user to close window
