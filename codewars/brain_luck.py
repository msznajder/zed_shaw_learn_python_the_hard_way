"""
https://www.codewars.com/kata/526156943dfe7ce06200063e
https://fatiherikli.github.io/brainfuck-visualizer/#LD4sPFs+Wy0+Kz4rPDxdPj5bLTw8Kz4+XTw8PC1dPj4u
"""

def brain_luck(code, input):

	input_bytes_array = [ord(ch) for ch in input]
	print(input_bytes_array)
	
	inst_pointer_idx = 0
	data_pointer_idx = 0 # not sure hot to initialise
	data_pointer_val = 0 # not sure hot to initialise
	res_array = [] 

	counter = 0

	while True:
		instruction = code[inst_pointer_idx]
		# print("inst_pointer_idx", inst_pointer_idx)
		if instruction == '>':
			print(">")
			data_pointer_idx += 1
			if data_pointer_idx > len(input_bytes_array)-1:
				data_pointer_idx = len(input_bytes_array)-1
			inst_pointer_idx += 1
		elif instruction == '<':
			print("<")
			data_pointer_idx -= 1
			if data_pointer_idx < 0:
				data_pointer_idx = 0
			inst_pointer_idx += 1
		elif instruction == '+':
			print("+")
			data_pointer_val = (data_pointer_val + 1) % 256
			inst_pointer_idx += 1
		elif instruction == '-':
			print("-")
			data_pointer_val = (data_pointer_val - 1) % 256
			inst_pointer_idx += 1
		elif instruction == '.':
			print(".")
			res_array.append(chr(data_pointer_val))
			data_pointer_val = 0 # not sure if I should do that here
			inst_pointer_idx += 1
		elif instruction == ',':
			print(",")
			data_pointer_val = input_bytes_array[data_pointer_idx] # this should be converted to ascii - how?
			inst_pointer_idx += 1
			data_pointer_idx += 1
		elif  instruction == '[':
			print("[")
			if data_pointer_val == 0:
				inst_pointer_idx = inst_pointer_idx + code[inst_pointer_idx:].find(']') + 1
			else:
				inst_pointer_idx += 1
			print(inst_pointer_idx)
		elif instruction == ']':
			print("]")
			if data_pointer_val != 0:
				print(code[:inst_pointer_idx])
				inst_pointer_idx = code[:inst_pointer_idx].rfind('[') + 1
			else:
				inst_pointer_idx += 1
			print(inst_pointer_idx)

		
		# print("data_pointer_idx", data_pointer_idx)
		# print("data_pointer_val", data_pointer_val)
		# print("res_array", res_array)

		if inst_pointer_idx >= len(code):
			break

		print(inst_pointer_idx)
		counter += 1
		if counter >= 345:
			break

	return "".join(res_array)


# print(brain_luck(',+[-.,+]', 'Codewars' + chr(255)))

# print(brain_luck(',[.[-],]', 'Codewars' + chr(0)))

print(brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)))


# print(brain_luck(',+[-.,+]', 'Codewars' + chr(255)))
# brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)), chr(72)

# Echo until byte(255) encountered
# assert brain_luck(',+[-.,+]', 'Codewars' + chr(255)), 'Codewars'

# # Echo until byte(0) encountered
# assert brain_luck(',[.[-],]', 'Codewars' + chr(0)), 'Codewars'

# # Two numbers multiplier
# assert brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)), chr(72)
