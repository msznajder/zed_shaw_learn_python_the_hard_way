## Chapter 9  Case study: word play

## 9.1  Reading word lists

fin = open("words.txt")

# fin is a common name for a file object used for input. 

# print(fin.readline().strip())
# print(fin.readline().strip())

for line in fin:
	word = line.strip()
	# print(word)

fin.close()


## 9.6  Glossary

# file object:
# A value that represents an open file.

# reduction to a previously solved problem:
# A way of solving a problem by expressing it as an instance of a previously solved problem.

# special case:
# A test case that is atypical or non-obvious (and less likely to be handled correctly).
