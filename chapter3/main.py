# Week 3: Functions

# 1. Defining Functions
def greet(name):
    return f"Hello, {name}!"

# Calling the function
message = greet("Alice")
print(message)

# 2. Functions with Multiple Arguments
def add_numbers(a, b):
    return a + b

sum_result = add_numbers(5, 10)
print(sum_result)

# 3. Default Arguments
def greet_with_default(name="Guest"):
    return f"Hello, {name}!"

print(greet_with_default())  # Using default value
print(greet_with_default("Bob"))  # Using custom value
