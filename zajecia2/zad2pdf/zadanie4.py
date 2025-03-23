def fibbonaci_generator():
    a = 0
    b = 1
    while True:
        yield a
        c = a
        a = b
        b = a + c


fib = fibbonaci_generator()

for i in range(10):
    print(next(fib))