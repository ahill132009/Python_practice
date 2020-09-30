# Case 38 failed

def solution(line):
	if 'h' in line:
		first_h = line.index('h')
		last_h = len(line) - 1 - line[::-1].index('h')
		line = line[:first_h+1] + line[first_h+1:last_h].replace('h', 'H') + line[last_h:]
	list_line = list(line)
	for x in range((len(list_line)-1), 1, -1):
		if x % 3 == 0:
			list_line.pop(x)
	line = ''.join(list_line)
	line = line.replace('1', 'one')
	return line

