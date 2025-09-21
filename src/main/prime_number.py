def is_prime_naive(n):
    """Return True if n is prime (naive test)."""
    is_prime  = True
    if n <= 1:
        is_prime = False
        
    else:
        for d in range(2, n):           # tests 2,3,...,n-1
            if n % d == 0: 
                is_prime = False
                break       
    return "Given number {}, is {}".format(n, "prime" if is_prime else "not prime")

is_prime = is_prime_naive(44)
print(is_prime)
