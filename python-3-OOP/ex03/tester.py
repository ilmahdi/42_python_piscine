from ft_calculator import Calculator


def main():
    try:
        v1 = Calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        v1 + 5
        print("---")
        v2 = Calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        v2 * 5
        print("---")
        v3 = Calculator([10.0, 15.0, 20.0])
        v3 - 5
        v3 / 0
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
