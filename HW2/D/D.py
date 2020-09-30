import sys
sys.setrecursionlimit(30000)


def solution(n,k):
	if n == 1:
		return 1
	else:
		return (solution(n - 1, k) + k - 1) % n + 1


'''k -= 1
start = 0
list_nums = list(range(7))
while len(list_nums) > k:
	list_nums = list_nums[start:]
	popped = list_nums.pop(k)
	list_nums = list_nums[k:] + list_nums[:k]

if k % 2 == 1:
	list_nums.pop(1)
else:
	list_nums.pop(0)
return list_nums[0] + 1'''