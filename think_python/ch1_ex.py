## Exercise 1  

# You can use a minus sign to make a negative number like -2. What happens if you put a plus sign before a number? What about 2++2?
# 4

# In math notation, leading zeros are ok, as in 02. What happens if you try this in Python?
  
# What happens if you have two values with no operator between them?
# SyntaxError: invalid token

"""
Exercise 2
"""

# How many seconds are there in 42 minutes 42 seconds?
seconds = 42 * 60 + 42

# How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
miles = 10 / 1.61

# If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? 
avr_s_per_m = seconds / miles
print("{}:{}".format(int(avr_s_per_m // 60), int(round(avr_s_per_m % 60))))

# What is your average speed in miles per hour?
avr_speed = miles / (seconds / 60 / 60)
print(avr_speed)
