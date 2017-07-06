def bisection_search(l, target):
	low = 0
	high = len(l) - 1
	while True:
		if low > high:
			return -1
		m = int((low + high) / 2)
		if target > l[m]:
			low = m + 1
		elif target < l[m]:
			high = m -1
		if target == l[m]:
			return m


print(bisection_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))