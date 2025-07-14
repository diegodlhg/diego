import argparse


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


OPERATIONS = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide,
}


def parse_args():
    parser = argparse.ArgumentParser(description="Simple calculator")
    parser.add_argument('operation', choices=OPERATIONS.keys(), help="Operation to perform")
    parser.add_argument('a', type=float, help="First operand")
    parser.add_argument('b', type=float, help="Second operand")
    return parser.parse_args()


def main():
    args = parse_args()
    func = OPERATIONS[args.operation]
    result = func(args.a, args.b)
    if result.is_integer():
        result = int(result)
    print(result)


if __name__ == '__main__':
    main()
