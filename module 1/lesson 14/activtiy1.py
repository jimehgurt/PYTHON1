import turtle 
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
hexagon = turtle.Turtle()
numsides = 6
length = 70
angle = 360 / numsides
for i in range(numsides) :
    hexagon.forward(length)
    hexagon.right(angle)
turtle.done()