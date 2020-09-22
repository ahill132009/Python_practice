def solution(total):
	hours = total // 60
	if hours > 23:
	    hours = hours % 24
	return f'{hours} {total % 60}'

