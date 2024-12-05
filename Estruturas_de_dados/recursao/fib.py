import sys
import functools
contador = 0

@functools.lru_cache()
def fibonacci( n ):
    global contador
    contador += 1
    if ( n < 0 ):
        return -1
    if ( n == 0 or n == 1 ):
        return 1
    else:
        return ( fibonacci(n-1) + fibonacci(n-2) )

# print(sys.argv)
print(fibonacci(int(sys.argv[1])))
print(f"Contador: {contador}")
