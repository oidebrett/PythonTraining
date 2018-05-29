import turtle

#Create a turle object and call it 'pen'
pen = turtle.Turtle()

#Create a window for turtle
window = turtle.Screen()

pen.shape("square")

pen.forward(50) #move forward 50 units
pen.left(90)     #turn left by 90 degrees
pen.forward(100) #move forward 100 units
pen.right(90)    #turn right by 90 degrees
pen.hideturtle()
pen.forward(150)  #move forward 50 units
pen.showturtle()
pen.left(90)     #turn left by 90 degrees
pen.forward(100) #move forward 100 units

#Keep looping until window is closed
window.mainloop()


