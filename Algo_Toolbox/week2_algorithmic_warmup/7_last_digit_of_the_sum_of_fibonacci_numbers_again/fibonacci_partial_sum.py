# Uses python3
import sys
# import time

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10

def F_sum(F_seq_mod_10, n, pisano_period):
    
    F_seq_mod_sum = sum(F_seq_mod_10)
    remainder = (n+1)%pisano_period
    multiplier = int((n+1)/pisano_period)
    # print(multiplier, remainder)
    F_seq_mod_sum_remainder = sum(F_seq_mod_10[:remainder])
        
    return (multiplier*F_seq_mod_sum + F_seq_mod_sum_remainder)
    

def fibonacci_partial_sum_efficient(from_, n):
    
    
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
    F_n = F_sum(F_seq_mod_10, n, pisano_period)
    F_m_1 = F_sum(F_seq_mod_10, from_-1, pisano_period)
    output = (F_n-F_m_1)%10
    # print(output)
    return output

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    # start_t = time.time()
    # print(fibonacci_partial_sum_naive(from_, to))
    # print('Naive time taken: ', time.time()-start_t)
    
    # start_t = time.time()
    print(fibonacci_partial_sum_efficient(from_, to))
    # print('Efficient time taken: ', time.time()-start_t)