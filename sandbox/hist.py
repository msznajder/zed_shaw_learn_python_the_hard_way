FILENAME = "readme.txt"

def words_hist(filename):
	hist = {}
	with open(filename) as fin:
		for line in fin:
			for word in line.strip().split():
				hist[word] = hist.get(word, 0) + 1

	for key, val in hist.items():
		print(key, val)

words_hist(FILENAME)