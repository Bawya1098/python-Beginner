print("Guess the number")
a = 45
while True:
    num = int(input("enter the number"))
    if num == a:
        print("you won")
        break
    if num < a:
        print("guess higher")
    else:
        print("guess lower")
