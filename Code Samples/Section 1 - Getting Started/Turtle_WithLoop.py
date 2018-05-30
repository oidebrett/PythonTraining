import turtle

#Create a turle object and call it 'pen'
pen = turtle.Turtle()

#Create a window for turtle
window = turtle.Screen()

for i in range(4):
    pen.forward(100) #move forward 100 units
    pen.left(90)     #turn left by 90 degrees

#Keep looping until window is closed
window.mainloop()


