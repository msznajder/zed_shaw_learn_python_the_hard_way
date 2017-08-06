"""
Exercise 1  
Write a function called sed that takes as arguments a pattern string, a replacement string, and two filenames; it should read the first file and write the contents into the second file (creating it if necessary). If the pattern string appears anywhere in the file, it should be replaced with the replacement string.
If an error occurs while opening, reading, writing or closing files, your program should catch the exception, print an error message, and exit. Solution: http://thinkpython2.com/code/sed.py.
"""
def sed(pattern, replacement, fin, fout):
	try:
		file_in = open(fin)
		file_out = open(fout, "w")
	except IOError as e:
		print(e)
	data = file_in.read()
	data = data.replace(pattern, replacement)
	file_out.write(data)

	file_in.close()
	file_out.close()

# sed("abba", "ddd", "in.txt", "out.txt")
		

"""
Exercise 3  
In a large collection of MP3 files, there may be more than one copy of the same song, stored in different directories or with different file names. The goal of this exercise is to search for duplicates.
Write a program that searches a directory and all of its subdirectories, recursively, and returns a list of complete paths for all files with a given suffix (like .mp3). Hint: os.path provides several useful functions for manipulating file and path names.
"""
import os

def find_all_files_with_suffix(suffix):
	files_with_suffix = []
	for cur, dirs, files in os.walk("."):
	        for file in files:
	        	if suffix == "." + file.rpartition(".")[2]:
	        		files_with_suffix.append(os.path.join(cur, file))
	return files_with_suffix


print(find_all_files_with_suffix(".mp3"))

















