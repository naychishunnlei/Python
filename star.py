def print_pattern(n):
    while n >= 1:
        for i in range(1, n + 1):
            print('*' * i)
        for i in range(n - 1, 0, -1):
            print('*' * i)
        n -= 1

try:
    num = int(input("Enter an integer greater than or equal to 1: "))
    if num >= 1:
        print_pattern(num)
    else:
        print("Please enter a valid integer greater than or equal to 1.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
