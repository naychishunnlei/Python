def f(n):
    if n==0:
        return 0
    elif n % 2 == 0:
        return 2 * f(n/2) + 1
    else:
        return 0
    
def display_f(n, count = 0):
    if count > n:
        return
    result = f(count)
    print(f"f({count}) = {result}")
    display_f(n, count + 1)

n = 2
display_f(n)