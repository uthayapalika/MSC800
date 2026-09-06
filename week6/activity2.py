def decorator_function(original_function):
    def wrapper(*args, **kwargs):
        print("Function is starting")
        result = original_function(*args, **kwargs)
        print("Function is finished")
        return result
    return wrapper

@decorator_function
def add(a, b):
    return a + b

result = add(10, 20)
print(result)