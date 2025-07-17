import argparse
import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def main():
    parser = argparse.ArgumentParser(description='Simple command line calculator')
    parser.add_argument('num1', type=float, nargs='?', help='First number')
    parser.add_argument('op', type=str, nargs='?', help='Operation (+,-,*,/)')
    parser.add_argument('num2', type=float, nargs='?', help='Second number')
    args = parser.parse_args()

    if args.num1 is None or args.op is None or args.num2 is None:
        print('Interactive mode')
        try:
            args.num1 = float(input('Enter first number: '))
            args.op = input('Enter operation (+,-,*,/): ')
            args.num2 = float(input('Enter second number: '))
        except ValueError:
            print('Invalid input.')
            return

    if args.op not in ops:
        print('Unsupported operation')
        return

    try:
        result = ops[args.op](args.num1, args.num2)
    except ZeroDivisionError:
        print('Error: division by zero')
        return
    print(f'{args.num1} {args.op} {args.num2} = {result}')

if __name__ == '__main__':
    main()
