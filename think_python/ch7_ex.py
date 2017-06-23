"""
Exercise 1  
Copy the loop from Section 7.5 and encapsulate it in a function called mysqrt that takes a as a parameter, chooses a reasonable value of x, and returns an estimate of the square root of a.
To test it, write a function named test_square_root that prints a table like this:

a   mysqrt(a)     math.sqrt(a)  diff
-   ---------     ------------  ----
1.0 1.0           1.0           0.0
2.0 1.41421356237 1.41421356237 2.22044604925e-16
3.0 1.73205080757 1.73205080757 0.0
4.0 2.0           2.0           0.0
5.0 2.2360679775  2.2360679775  0.0
6.0 2.44948974278 2.44948974278 0.0
7.0 2.64575131106 2.64575131106 0.0
8.0 2.82842712475 2.82842712475 4.4408920985e-16
9.0 3.0           3.0           0.0
The first column is a number, a; the second column is the square root of a computed with mysqrt; the third column is the square root computed by math.sqrt; the fourth column is the absolute value of the difference between the two estimates.
"""
import math 


def custom_sqrt(a):
	"""Calculates squre root value for given number.

	a: non-negative integer
	"""
	x = a
	epsilon = 0.0000001
	while True:
		y = (x + a/x) / 2
		if abs(x-y) < epsilon:
			break
		x = y
	return y


def test_square_root():
	for a in range(1, 10):
		print(a, custom_sqrt(a), math.sqrt(a), abs(custom_sqrt(a)-math.sqrt(a)))


test_square_root()


"""
Exercise 2  
The built-in function eval takes a string and evaluates it using the Python interpreter. For example:
>>> eval('1 + 2 * 3')
7
>>> import math
>>> eval('math.sqrt(5)')
2.2360679774997898
>>> eval('type(math.pi)')
<class 'float'>
Write a function called eval_loop that iteratively prompts the user, takes the resulting input and evaluates it using eval, and prints the result.
It should continue until the user enters 'done', and then return the value of the last expression it evaluated.
"""
def eval_loop():
	last_res = None
	while True:
		inst = input()
		if inst == "done":
			return last_res
			break
		last_res = eval(inst)
		print(last_res)


# print(eval_loop())


"""
Exercise 3  
The mathematician Srinivasa Ramanujan found an infinite series that can be used to generate a numerical approximation of 1 / π:
 
Write a function called estimate_pi that uses this formula to compute and return an estimate of π. It should use a while loop to compute terms of the summation until the last term is smaller than 1e-15 (which is Python notation for 10−15). You can check the result by comparing it to math.pi.
Solution: http://thinkpython2.com/code/pi.py.
"""
import math


def estimate_pi():
	"""
	Computes an estimate of pi.

	Algorithm due to Srinivasa Ramanujan,
	from http://en.wikipedia.org/wiki/Pi.
	"""
	k = 0
	break_condition = 1e-15
	series = 0
	while True:
		numerator = math.factorial(4*k) * (1103 + 26390*k)
		denominator = math.factorial(k)**4 * 396**(4*k)
		term = (numerator) / (denominator)
		series += term
		if abs(term) < break_condition:
			break
		k += 1

	scale = (2 * math.sqrt(2)) / 9801
	
	return scale * series

print(estimate_pi())
print(1 / math.pi)
