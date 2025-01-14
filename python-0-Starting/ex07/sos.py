import sys


def main() -> int:
    MORSE_DICT = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
        " ": "/ ",
    }
    try:
        if len(sys.argv) == 2:
            try:
                s = sys.argv[1].upper()
                print(" ".join([MORSE_DICT[c] for c in s]))
            except KeyError:
                raise AssertionError("the arguments are bad")
        else:
            raise AssertionError("the arguments are bad")

    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
