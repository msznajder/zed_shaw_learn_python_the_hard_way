"""
http://www.codewars.com/kata/range-extraction
"""


def solution(args):
	res = []
	holder = ""
	print(len(args)-2)
	for idx in range(len(args)-1):
		print(idx, args[idx])
		if idx == 0 and args[idx+1] - args[idx] != 1:
			res.append(str(args[idx]))
			continue
		elif args[idx+1] - args[idx] == 1 and holder == "":
			print("in1")
			holder = str(args[idx]) 
		elif args[idx+1] - args[idx] == 1 and holder != "":
			pass
		elif args[idx+1] - args[idx] != 1 and holder != "":
			print("in3")
			holder += "-" + str(args[idx])
			res.append(holder)
			holder = ""
		elif args[idx+1] - args[idx] != 1 and holder == "":
			print("in4")
			res.append(str(args[idx]))
		elif idx == len(args)-2:
			print("int5")

	print(res)




# solution([1, 2, 3, 4, 5, 7])
solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])