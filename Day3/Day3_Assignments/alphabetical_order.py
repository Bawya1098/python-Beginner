def check_alphabetical_order():
    print("word to check:")
    word = str(input("enter the word: "))
    list = ()
    a = sorted(word)
    for i in word:
        list.append(a)
        if list == word:
            print("true")
    else:
        print("false")

check_alphabetical_order()