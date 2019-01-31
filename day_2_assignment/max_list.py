number = int(input("enter size"))
my_array = list()
print("Enter numbers in list: ")
for i in range(0, number):
    n = input("num :")
    my_array.append(int(n))
print("ARRAY: ", my_array)
print("max is: ", max(my_array))
print(" min is: ", min(my_array))
