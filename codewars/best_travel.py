import itertools


def choose_best_sum(t, k, ls):
    combinations = list(itertools.combinations(ls, k))
    print(len(combinations))
    max_combination = [0, 0, 0]
    for combination in combinations:
    	if sum(combination) > sum(max_combination) and sum(combination) <= t:
    		max_combination = combination
    if sum(max_combination) == 0:
        return None
    else:
        return sum(max_combination)


xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
print(choose_best_sum(430, 8, xs))



