## Chapter 13  Case study: data structure selection

## 13.2  Random numbers

# The function random returns a random float between 0.0 and 1.0 (including 0.0 but not 1.0).

 # Each time you call random, you get the next number in a long series.

import random

for i in range(10):
	x = random.random()
	print(x)


# The function randint takes parameters low and high and returns an integer between low and high (including both).
random.randint(5, 10)


# To choose an element from a sequence at random, you can use choice.
t = [1, 2, 3]
random.choice(t)
