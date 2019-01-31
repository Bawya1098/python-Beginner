print("Enter the height of the pyramid")
h = int(input("height"))


def upper_triangle():
    for lower in range(1, h + 1):
        for upper in range(1, lower + 1):
            print("#", end=' ')

        print()


def lower_triangle():
    for lower in range(h + 1, 1, -1):
        for upper in range(0, lower - 1):
            print("#", end=' ')

        print()


upper_triangle()
lower_triangle()
