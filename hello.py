print("Hello Python")
a=10;
b=20;
c=a+b;
print("The sum of a and b is:", c)

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print("Fibonacci series up to {n} terms is printed.") # for a new line after printing the sequence)