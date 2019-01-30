number = int(input("enter the elements in list:"))
my_array = list()
print("enter number in array:")
for i in range(0, int(number)):
    n = int(input("enter num:"))
    my_array.append(int(n))
    print("List is:", my_array)
my_array.sort()
print("sorted list is:", my_array)
for i in range(len(my_array) - 1):
    if my_array[i] == my_array[i + 1]:
        print(my_array[i])
        print(my_array.count(my_array[i]))


        # rint(my_array.count(2))
