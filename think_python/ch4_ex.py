"""
Exercise 1

Download the code in this chapter from http://thinkpython2.com/code/polygon.py.
- Draw a stack diagram that shows the state of the program while executing circle(bob, radius). You can do the arithmetic by hand or add print statements to the code.
- The version of arc in Section 4.7 is not very accurate because the linear approximation of the circle is always outside the true circle. As a result, the Turtle ends up a few pixels away from the correct destination. My solution shows a way to reduce the effect of this error. Read the code and see if it makes sense to you. If you draw a diagram, you might see how it works.
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
