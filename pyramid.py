print("Enter the height of the pyramid")
h = int(input("height"))
for i in range(0, h):
    for j in range(0, i + 1):
        print("#",end=' ')
    print(" ")