my_array = list()
sum = 0
num = input("enter elements")
print("Enter numbers in array: ")
for i in range(int(num)):
    n = input("num :")
    my_array.append(int(n))
print("ARRAY: ", my_array)
my_array.sort()
print("sorted array is:", my_array)
sum(num for num in my_array if not num % 2)
i  # f my_array[i] % 2 == 0:
#  print(my_array[i])
# sum += i
print(sum)
