
__author__ = "Atanu Jana"


def print_full_name(a, b):
    print("Hello {0}{1}! You just awesome.".format(a, b))


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
