def Fibonacci(n):
    """
	Returns nth number in fib seq
    """
    if n < 2:
        return n
    else:
	return Fibonacci(n-1) + Fibonacci(n-2)
    
    
    
