# Question:

# Define a class which has at least two methods:

# getString: to get a string from console input
# printString: to print the string in upper case.
# Output:
# atanu ATANU

class IOstring():
    def __init__(self):
        pass
    def getString(self):
        self.s = input()
    def printString(self):
        print(self.s.upper())

string = IOstring()
string.getString()
string.printString()