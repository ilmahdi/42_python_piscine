from load_image import ft_load


def main() -> int:
    try:
        print(ft_load("./landscape.png"))
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
