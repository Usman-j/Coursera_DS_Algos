# Uses python3
def calc_fib(n):
    
    if (n <= 1):
        return n
    F_seq = [0 for i in range(n+1)]
    F_seq[1] = 1
    for i in range(2,n+1):
        F_seq[i] = F_seq[i-1] + F_seq[i-2]
        
    # print(F_seq)
    return F_seq[n]
    
    
    # return calc_fib(n - 1) + calc_fib(n - 2)
    

n = int(input())
print(calc_fib(n))
