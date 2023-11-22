from git_test.real_code import hello_world


def add_numbers(number, another_number):
    return number + another_number


def main():
    hello_world()

    print(add_numbers(1, 2))


if __name__ == "__main__":
    main()
