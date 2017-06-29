def count_down(n):
	if n == 0:
		print("Blastoff!")
	else:
		print(n)
		count_down(n-1)


count_down(10)


def print_n(n):
	while n > 0:
		print(n)
		n -= 1


print_n(10)


def print_n2(n):
	if n == 0:
		print(n)
	else:
		print(n)
		print_n2(n-1)


print_n2(10)


def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)


def fac(n):
	if n == 0:
		return 1
	else:
		return n*fac(n-1)

print(fac(3))
