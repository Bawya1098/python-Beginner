# string = str(input("enter the string"))
# print(string)
string1 = "thought"
string2 = "works"
substring = "thought"
print(string1.capitalize() + string2.capitalize())
print(string1.casefold() + string2.casefold())
print(string1.center(12, "_") + string2.center(10, "_"))
print(string1.count(substring))
print(string1.encode(string2="works", string="kows"))