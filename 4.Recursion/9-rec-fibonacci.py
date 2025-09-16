def fibonacci(n):
    if n <= 1:      # f(n) = f(n-1) + f(n-2)
        return n
    last = fibonacci(n-1)  # 1st 
    slast = fibonacci(n-2) # 2nd
    return last + slast


def main():
    n = 5       
    for i in range(n + 1):
        print(fibonacci(i), end=' ')
    
main()