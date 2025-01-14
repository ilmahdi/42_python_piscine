import sys


def main():
    try:
        if len(sys.argv) < 2:
            return
        elif len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        number = int(sys.argv[1])
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

    except ValueError:
        print("AssertionError: argument is not an integer")
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
