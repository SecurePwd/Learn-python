# Week 4: Data Structures

# 1. Lists (Mutable)
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Adding an element to the list
print(fruits)

# 2. Tuples (Immutable)
coordinates = (10.0, 20.0)
# coordinates[0] = 15.0  # This will raise an error because tuples are immutable
print(coordinates)

# 3. Sets (Unordered, no duplicates)
unique_numbers = {1, 2, 3, 3, 4}
print(unique_numbers)  # {1, 2, 3, 4}

# 4. Dictionaries (Key-Value Pairs)
person = {"name": "Alice", "age": 30, "city": "New York"}
print(person["name"])  # Accessing value using key

# 5. List Comprehensions (Shorter syntax for creating lists)
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
print(squares)
