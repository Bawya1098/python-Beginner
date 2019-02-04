word = input("enter the string:")
length = len(word)

def non_repeating():
    for i in range(0, length+1):
        val = {0: word[i] != word[i + 1], length + 1:word[i] != word[i - 1], word[i] != word[i + 1] and word[i] != word[i - 1]:print(word[i])}

        return(val)


non_repeating()