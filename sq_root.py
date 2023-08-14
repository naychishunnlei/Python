def square_root_approximation(n, iterations):
    guess = n / 2.0
    for _ in range(iterations):
        temp = n / guess
        guess = (guess + temp) / 2.0
    return guess

number = float(input("Enter a number to find its square root: "))

for iterations in range(5, 8):
    approximation = square_root_approximation(number, iterations)
    print(f"Approximation with {iterations} iterations: {approximation:.3f}")
