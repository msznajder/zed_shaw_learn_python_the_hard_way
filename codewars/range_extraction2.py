"""
http://www.codewars.com/kata/range-extraction
"""


def solution(args):
    sequences = []
    current_seq = []
    for idx, val in enumerate(args):
        if idx == 0:
            current_seq.append(str(val))
            continue
        if val - args[idx-1] != 1:
            sequences.append(current_seq)
            current_seq = []
        current_seq.append(str(val))
    sequences.append(current_seq)
    print(sequences)

    res = ""
    for seq in sequences:
        if len(seq) == 1:
            res += "".join(seq) + ","
        elif len(seq) == 2:
            res += ",".join(seq) + ","
        elif len(seq) >= 3:
            res += seq[0] + "-" + seq[-1] + ","
    return res[:-1]





solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])
# '-6,-3-1,3-5,7-11,14,15,17-20'

[[-6], [-2, -1, 0, 1], [4, 5], [8, 9, 10, 11], [15]]