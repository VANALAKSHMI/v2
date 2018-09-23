#29
print("to print time")
m = int(input("n="))
i=0
s=0
for x in range(1,25):
    for y in range(1,61):
        s = s + 1
        if (m == s):
            print(i, ":", y)
            break

    i = i + 1
