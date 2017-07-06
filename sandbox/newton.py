
def find_square_root_newton_raphson(s, epsilon=0.00000000001):
	x = s
	while True:
		print(x)
		if abs(x**2 - s) <= epsilon:
			break
		x = (x + s/x) / 2
	return x

# find_square_root_newton_raphson(4)