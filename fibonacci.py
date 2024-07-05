def fibonacci_gen():
    a,b = 0,1
    while True:
        yield a     #points the currunt value of a
        a,b = b,a+b
fibonnaci=fibonacci_gen()
for _in range(10):
    print(next(fibonnaci))