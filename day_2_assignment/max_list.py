def list_1(list()):
number = input("enter elements")
my_array = list()
print("Enter numbers in array: ")
for i in range(int(number)):
    n = input("num :")
    my_array.append(int(n))
print("ARRAY: ", my_array)


def higher_num(my_array1):
    max_number = my_array1[0]
    for a in my_array1:
        if a > max_number:
            max_number = a
            return a


my_array1 = my_array()

