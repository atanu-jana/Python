



__author__ = "Atanu Jana"


def swap_case(s):
    a = ""
    for word in s:
        if word.isupper() == True:
            a += (word.lower())
        else:
            a += (word.upper())
    return a


s = "Atanu.Jana"

print(swap_case(s))
