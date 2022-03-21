# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def F_sum(F_seq_mod_10, n, pisano_period):
    
    F_seq_mod_sum = sum(F_seq_mod_10)
    remainder = (n+1)%pisano_period
    multiplier = int((n+1)/pisano_period)
    # print(multiplier, remainder)
    F_seq_mod_sum_remainder = sum(F_seq_mod_10[:remainder])
        
    return (multiplier*F_seq_mod_sum + F_seq_mod_sum_remainder)%10
    

def fibonacci_sum_efficient(n):
    
    if (n <= 1):
        return n
    
    # Since we need last digit of sum
    m = 10
    previous = 0
    current  = 1
    pisano_period = 1
    F_seq_mod_10 = [0, 1]
    
    while True:
         
        curr_new = (previous + current)%m
        previous = current
        current = curr_new
        
        # cycle always starts with 01
        if previous==0 and current==1:
            break
        F_seq_mod_10.append(current)
        pisano_period += 1
    
    # print('pissano: ', pisano_period)
    # print('F_seq_moded: ', F_seq_mod_10)
    output = F_sum(F_seq_mod_10, n, pisano_period)
    
    # print(output)
    return output

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_efficient(n))
