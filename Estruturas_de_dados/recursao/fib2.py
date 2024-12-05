import sys

def fib(n):
    if n in (0, 1):
        return 1
    c = 1
    a = 1
    b = 1
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return c

print(fib(int(sys.argv[1])))
