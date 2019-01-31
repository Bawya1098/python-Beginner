word = input("enter the string:")
length = len(word)


def non_repeating():
    for i in range(0, length + 1):
        if i == 0:
            if word[i] != word[i + 1]:
                print(word[i])
                break
        elif i == length + 1:
            if word[i] != word[i - 1]:
                print(word[i])
                break
        else:
            if word[i] != word[i + 1] and word[i] != word[i - 1]:
                print(word[i])
                break


non_repeating()
