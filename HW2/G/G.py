# Пока не смог решить

def solution(a, b):
	c = 0
	count_a = 0
	count_b = 0
	res = []
	while count_a != len(a) or count_b != len(b):
		if a[count_a] < b[count_b]:
			res.append(a[count_a])
			count_a += 1
		else:
			if b[count_b] not in a:
				res.append(b[count_b])
				count_b += 1
			else:
				count_b += 1
	return res
print(solution(a,b))

    