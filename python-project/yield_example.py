def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Print all the numbers of the Fibonacci sequence that are lower than 1000
for i in fibonacci_gen():
    if i > 1000:
        break
    print(i)