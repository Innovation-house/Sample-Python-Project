def main():
    print("Welcome to the Sample Project!")
    from utils import add, multiply

    a, b = 5, 10
    print(f"Adding {a} and {b}: {add(a, b)}")
    print(f"Multiplying {a} and {b}: {multiply(a, b)}")

if __name__ == "__main__":
    main()

# File: utils.py

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y
