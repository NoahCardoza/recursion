def permute(arr): # This fuction dose exactly what it says. It permutes a list.
	if len(arr) == 1:
		return [arr]
	else:
		perms = []
		for i in range(len(arr)):
			for p in permute(arr[:i] + arr[i+1:]):
				perms.append([arr[i]] + p)
		return perms

print permute([1, 2, 3]) # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
