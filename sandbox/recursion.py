def fact(n):
	if n == 0:
		return 0
	else:
		return n * fac(n-1)

def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)


def print_n(n):
	if n == 0:
		print(n)
	else:
		print(n)
		print_n(n-1)

def print_n2(n):
	for i in range(n):
		print(i)

print_n(3)