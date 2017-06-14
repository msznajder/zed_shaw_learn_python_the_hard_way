"""
Exercise 1
"""

# __main__:
# 	radius -> 100

# circle:
# 	t -> bob
# 	r -> 100

# arc:
# 	t -> bob
# 	r -> 100
# 	angle -> 360

# 	arc_length -> 628.3185307179587
# 	n -> 158
# 	step_length -> 3.9766995615060674
# 	step_angle -> 2.278481012658228

# polyline:
# 	t -> bob
# 	n -> 158
# 	length -> 3.9766995615060674
# 	angle -> 2.278481012658228


"""
Exercise 2
"""

import polygon
import turtle


def petal(t, radius, angle):
	polygon.arc(t, radius, angle)
	t.lt(90)
	polygon.arc(t, radius, angle)
	t.lt(angle*2)
	

if __name__ == "__main__":
	bob = turtle.Turtle()

	radius = 50
	angle = 90

	# polygon.circle(bob, radius)
	# flower(bob, radius, 4)

	petal(bob, radius, angle)
	# polygon.arc(bob, radius, 90)

	turtle.mainloop()
