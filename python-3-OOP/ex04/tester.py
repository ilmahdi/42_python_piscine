from ft_calculator import Calculator


def main():
    try:
        a = [5, 10, 2]
        b = [2, 4, 3]
        Calculator.dotproduct(a, b)
        Calculator.add_vec(a, b)
        Calculator.sous_vec(a, b)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
