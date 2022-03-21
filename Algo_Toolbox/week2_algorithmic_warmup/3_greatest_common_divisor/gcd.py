# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_optimized(a, b):
    current_gcd = 1
    
    if min(a,b) > 0:
        a_prime = max(a,b) % min(a,b)
        # print(a_prime, min(a,b))
        current_gcd = gcd_optimized(a_prime, min(a,b))
    else:
        current_gcd = max(a,b)

    return current_gcd
    

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_optimized(a, b))
