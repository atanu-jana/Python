# Output: 5 = 120

def factorial(a):
    if a==0:
        return 1
    return a*factorial(a-1)

number = int(input("Enter the number: "))
print(factorial(number))
