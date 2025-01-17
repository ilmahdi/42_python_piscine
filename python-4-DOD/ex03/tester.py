from new_student import Student


def main():
    student = Student(name="Edward", surname="agle")
    print(student)

    try:
        student = Student(name="Edward", surname="agle", id="toto")
    except TypeError as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
