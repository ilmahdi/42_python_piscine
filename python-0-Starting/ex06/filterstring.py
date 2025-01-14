import sys
from ft_filter import ft_filter


def main() -> int:
    try:
        if len(sys.argv) == 3:
            try:
                s = sys.argv[1].split()
                n = int(sys.argv[2])
                # Use the lambda directly in the ft_filter call
                print(list(ft_filter(lambda w: len(w) >= n, s)))
            except ValueError:
                raise AssertionError("the arguments are bad")
        else:
            raise AssertionError("the arguments are bad")
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
