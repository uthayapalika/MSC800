print("Hello Python")
a=10;
b=20;
c=a+b;
print("The sum of a and b is:", c)

# Function to print Fibonacci series
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b

# Function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Main function
def main():
    N = int(input("Enter a number: "))

    print("Fibonacci series up to", N, ":")
    fibonacci(N)

    print("\nFactorial of", N, "is:", factorial(N))

main()
