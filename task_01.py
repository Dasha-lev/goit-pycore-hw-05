def caching_fibonacci():
    # Create an empty dictionary to store cached Fibonacci values
    cache = {}

    def fibonacci(n):
        # Check for basic cases
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        
        # If the value is already in the cache, return it
        if n in cache:
            return cache[n]
        
        # Calculate the value recursively and store it in the cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # Return the inner function that calculates Fibonacci numbers
    return fibonacci

# Get the fibonacci function from caching_fibonacci
fib = caching_fibonacci()

# Use the fibonacci function to calculate Fibonacci numbers
print(fib(10))  
print(fib(15))  
