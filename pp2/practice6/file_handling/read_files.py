with open("test.txt", "w") as f:
    f.write("apple\nbanana\ncherry\norange\ngrape")

# 1. Reading the entire file
with open("test.txt", "r") as f:
    print(f.read())

# 2. Reading one line
with open("test.txt", "r") as f:
    print(f.readline())

# 3. Reading all lines into a list
with open("test.txt", "r") as f:
    print(f.readlines())

# 4. Reading lines in a loop
with open("test.txt", "r") as f:
    for line in f:
        print(line.strip())

# 5. Reading the first 5 characters
with open("test.txt", "r") as f:
    print(f.read(5))

# 6. Counting the number of lines
with open("test.txt", "r") as f:
    print(len(f.readlines()))

# 7. Searching for a line containing a word
with open("test.txt", "r") as f:
    for line in f:
        if "banana" in line:
            print("Found:", line.strip())

# 8. Reading and removing whitespace
with open("test.txt", "r") as f:
    lines = [line.strip() for line in f]
print(lines)

# 9. Reading in uppercase
with open("test.txt", "r") as f:
    print(f.read().upper())

# 10. Error handling — file not found
try:
    with open("nofile.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")
