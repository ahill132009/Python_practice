def solution(arr):
    count_all = 0 if len(arr) > 1 else 1
    count_local = 1
    print(count_all)
    for x in range(1,len(arr)):
    	if arr[x] == arr[x-1]:
    		count_local += 1
    	else:
    		count_all = max(count_local, count_all)
    		count_local = 1
    return count_all

