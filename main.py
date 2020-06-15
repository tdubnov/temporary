import argparse

def parse_input():
    """
    prints from 0 to first_number-1 the number and it's square
    Parses the input: first_number
    :return: NONE
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('first_number', type=int, nargs='?')
    args = parser.parse_args()
    if args.first_number is None:
        parser.error("too few arguments")
    for i in range(args.first_number):
        print(str(i) + " " + str(i*i))


def main():
    parse_input()


if __name__ == "__main__":
    main()
