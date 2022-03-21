# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd_optimized(a, b):
    current_gcd = 1
    
    if min(a,b) > 0:
        a_prime = max(a,b) % min(a,b)
        # print(a_prime, min(a,b))
        current_gcd = gcd_optimized(a_prime, min(a,b))
    else:
        current_gcd = max(a,b)

    return current_gcd

def lcm_optimized(a, b):
    lcm = (a*b)/gcd_optimized(a, b)
    
    return int(lcm)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_optimized(a, b))

