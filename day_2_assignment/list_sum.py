number = input("enter elements")
my_array = list()
sum = 0
print("Enter numbers in array: ")
for i in range(int(number)):
    n = input("num :")
    my_array.append(int(n))
print("ARRAY: ", my_array)
for num in my_array:
    sum = sum + num
print("sum is:", sum)
