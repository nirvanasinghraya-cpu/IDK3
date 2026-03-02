from turtle import *
from colorsys import *

# Speed up the turtle
tracer(10)  # Changed back to 30 for smooth animation
bgcolor("black")

# Increase pen size for more vibrant look
pensize(2)

h = 0
step = 0.000002

# Make the turtle faster
speed(0)

shape_center_x = 0
shape_center_y = 0

for i in range(1000):
    h += step
    
    if i % 10 == 0:
        color(hsv_to_rgb(h, 1, 1))
    else:
        color(hsv_to_rgb(h, 0.8, 1))
    old_x, old_y = pos()
# Start at a reasonable position
penup()
goto(0, 0)
pendown()

for i in range(1000):
    h += step
    
    if i % 10 == 0:
        color(hsv_to_rgb(h, 1, 1))
    else:
        color(hsv_to_rgb(h, 0.8, 1))
    
    # Your original pattern - no camera tricks
    if i % 5 == 0:
        right(5)
        forward(165)
        circle(50, 180)
        right(360/5)
    
    if i % 50 == 0:
        for _ in range(8):
            forward(100)
            left(45)
            
            new_x, new_y = pos()

            shape_center_x = shape_center_x * 0.95 + new_x * 0.05
            shape_center_y = shape_center_y * 0.95 + new_y * 0.05

            if i % 5 == 0:
                offset_x = -shape_center_x
                offset_y = -shape_center_y

hideturtle()
done()
