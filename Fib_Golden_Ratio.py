def fib(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    
    return fib(x-1) + fib(x-2)

def fib_seq(n):
    for i in range(n):
        print(fib(i))
        

# Function to approximate golden ratio using fibbonacci numbers, GR=1.618033988749895
def golden_ratio_approx(n):
    if n<2:
        return None
    
    fib_n=fib(n)
    fib_n_plus1=fib(n+1)
    
    if fib_n==0:
        return None
    
    return fib_n_plus1/fib_n

n=int(input("Enter n:"))
print("Fibbonaci sequence for first",n,"terms is:")
fib_seq(n)
print("Fibonacci of number",n,"=",fib(n))
print("Approximated golden ratio using fibonacci of number",n,"=",golden_ratio_approx(n))
