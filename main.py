a = "hi dad"
print(a)
b = range(101)
for number in b:
    print(number)
    c = number % 10
    if c == 0:
        print("ten")
    else:
        print("not ten")
        c = 10

c = c +11
