import sys


def ispunctuation(c) -> bool:
    """
    Checks if a character is a punctuation mark.

    Args:
        c (str): A single character.

    Returns:
        bool: `True` if `c` is a punctuation mark, `False` otherwise.
    """
    return c in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"


def count_text_chars(s: str) -> None:
    """
    Counts the number of upper letters, lower letters, punctuation
    marks, spaces, and digits in a given string.

    Args:
        s (str): The input string.

    Returns:
        None: The function prints the counts to the console.
    """
    case_counts = {
        "upper letters": [0, str.isupper],
        "lower letters": [0, str.islower],
        "punctuation marks": [0, ispunctuation],
        "spaces": [0, str.isspace],
        "digits": [0, str.isdigit],
    }

    for c in s:
        for key, (_, func) in case_counts.items():
            if func(c):
                case_counts[key][0] += 1
                break

    print(f"The text contains {len(s)} characters:")
    for key, (count, _) in case_counts.items():
        print(f"{count} {key}")


def main() -> int:
    try:
        if len(sys.argv) < 2:
            print("What is the text to count?")
            s = sys.stdin.readline()
        elif len(sys.argv) < 3:
            s = sys.argv[1]
        else:
            raise AssertionError("Too many arguments provided")
        count_text_chars(s)
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
