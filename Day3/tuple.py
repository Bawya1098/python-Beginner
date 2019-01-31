# tuple = ((12, 34), (23, 78)]
# rint(tuple)


def mutable_list(string):
    print(hex(id(string)))
    string = string.replace("st", "ST")
    print(hex(id(string)))


def immutable_list(numbers):
    print(hex(id(numbers)))


immutable_list(12)


def mutable_list1(list):
    print(hex(id(list())))


mutable_list1(1, 2, 3)
