import math
N, P = map(int, input().split(" "))

def factorial_for(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret

print(factorial_for(N) % P)