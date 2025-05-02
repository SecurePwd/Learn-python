# Week 8: File I/O

# 1. Writing to a File
with open("file.txt", "w") as file:
    file.write("Hello, this is a test.\n")
    file.write("Writing to files is fun!")

# 2. Reading from a File
with open("file.txt", "r") as file:
    content = file.read()
    print(content)

# 3. Working with CSV Files
import csv

# Writing CSV
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 30])
    writer.writerow(["Bob", 25])

# Reading CSV
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
