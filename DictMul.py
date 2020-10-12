# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

number  = int(input("Enter the number: "))

d = dict()
for i in range(1,number+1):
    d[i] = i*i
print(d)
