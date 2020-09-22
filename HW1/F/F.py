def solution(n):
   	list_of_twos = [1]
   	numb = 1
   	while n > numb:
   		numb *= 2
   		if n >= numb:
   			list_of_twos.append(numb)
   	return list_of_twos

print(solution(5))