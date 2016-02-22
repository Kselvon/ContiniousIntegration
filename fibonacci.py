def fibonacci(n):
    """
	Returns nth number in fib seq
    """
    if n < 0:
        raise ValueError("n<0 not valis")
    elif round(n) != n:
        raise ValueError("fractional n not allowed")
    elif n < 2:
        return n
    else:
        return 1+fibonacci(n-1) + fibonacci(n-2)
    
    
    
