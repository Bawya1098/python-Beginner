word = str(input("words to be separated by hypen:"))
separated_word = word.split('-')
sorted_separated_word = ('-'.join(sorted(separated_word)))
print("word is: ", word)
print("separated_word is:", separated_word)
print("sorted_separated_word is: ", sorted_separated_word)