# example_program.py

def greet(name):
    return f"Hello, {name}! Welcome to my example program!"

def add(a, b):
    if a < 0 or b < 0:
        return "Error: Cannot add negative numbers :("
    return a + b

if __name__ == "__main__":
    print(greet("Alice"))
    print(f"2 + 3 = {add(2, 3)}")
