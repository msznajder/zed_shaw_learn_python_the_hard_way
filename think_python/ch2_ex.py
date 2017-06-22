"""
Exercise 1
"""

# 42 = n
# SyntaxError: can't assign to literal

# How about x = y = 1?
# Legal

# In some languages every statement ends with a semi-colon, ;. What happens if you put a semi-colon at the end of a Python statement?
# Legal. Can use multiple statements in one line.

# What if you put a period at the end of a statement?
# Creates a tuple.

# In math notation you can multiply x and y like this: x y. What happens if you try that in Python?
# SyntaxError: invalid syntax


"""
Exercise 2  
"""

# The volume of a sphere with radius r is 4/3 π r3. What is the volume of a sphere with radius 5?

import math

r = 5
vol = 4/3 * math.pi * r**3
print(vol)


# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
price = 24.95
discount = 0.4
shipping_first = 3
shipping_additional = 0.75
copies = 60

total_price = copies * price * (1 - discount) + shipping_first + shipping_additional * (copies - 1)
print(total_price)


# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
start_time_h = 6
start_time_m = 52
start_time_s = 0

easy_pace_m = 8
easy_pace_s = 15

fast_pace_m = 7
fast_pace_s = 12

run_time_m = 1 * easy_pace_m + 3 * fast_pace_m + 1 * easy_pace_m
run_time_s = 1 * easy_pace_s + 3 * fast_pace_s + 1 * easy_pace_s

total_time_h = start_time_h
total_time_m = start_time_m + run_time_m 
total_time_s = start_time_s + run_time_s 

print(total_time_h, total_time_m, total_time_s)

total_time_m = total_time_m + total_time_s // 60
total_time_h = total_time_h + total_time_m // 60

print(total_time_h, total_time_m % 60, total_time_s % 60)
