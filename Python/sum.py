def rec_sum(l): # Say it out loud a few times... This function adds all the elements of a numerical list no matter how manny sublists deep
	if l:
		if type(l[0]) == list: 
			return rec_sum(l[0]) + rec_sum(l[1:])
		return l[0] + rec_sum(l[1:])
	return 0

print rec_sum([1, 2, [3,4], [5,6]]) # 21