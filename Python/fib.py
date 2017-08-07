def fib (n): # Another recursive solution to the fibonacci sequence...
	if n <= 2:
		return 1
	return fib(n-2) + fib(n-1)
	

print fib(7) # 13 (0.7s!)