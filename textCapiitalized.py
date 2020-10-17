
__author__ = "Atanu Jana"


def cap(s):
    l = s.split(" ")
    a = [i.capitalize() for i in l]
    return " ".join(a)


s = input()
print(cap(s))
