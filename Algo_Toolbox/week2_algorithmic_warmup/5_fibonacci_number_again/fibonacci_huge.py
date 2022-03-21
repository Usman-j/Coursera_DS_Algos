# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def F_mod(n, m):
    
    previous = 0
    current  = 1
    for _ in range(n - 1):
         
        curr_new = (previous + current)%m
        previous = current
        current = curr_new
        
    return current
    

def get_fibonacci_huge_efficient(n, m):
    
    if (n <= 1):
        return n
    
    previous = 0
    current  = 1
    pisano_period = 1
    # Can also populate a list here so that <F_mod> is not needed
    while True:
         
        curr_new = (previous + current)%m
        previous = current
        current = curr_new
        
        # cycle always starts with 01
        if previous==0 and current==1:
            break
        
        pisano_period += 1
    
    # print('pissano: ', pisano_period)
    F_target = n%pisano_period
    output = F_mod(F_target, m)
    
    # print(output)
    return output
        
if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_efficient(n, m))
