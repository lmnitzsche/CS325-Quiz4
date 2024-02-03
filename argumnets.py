import argparse

def main():
    parser = argparse.ArgumentParser(description='Argument Parser Example')
    parser.add_argument('string_arg', type=str, help='A string input')
    parser.add_argument('int_arg', type=int, help='An integer input')
    parser.add_argument('float_arg', type=float, help='A float input')
    args = parser.parse_args()

    print(f'String: {args.string_arg}')
    print(f'Integer: {args.int_arg}')
    print(f'Float: {args.float_arg}')

if __name__ == "__main__":
    main()