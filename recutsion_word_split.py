def word_split(phrase, list_of_words, output=None):

    if output is None:
        output = []
        print("inside first if ")

    i =0
    for word in list_of_words:
        print("inside for loop", i, word, phrase)
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):], list_of_words, output)
        i += 1

    return True if len(output) == len(list_of_words) else False


print(word_split("iLoveIndia", ["i", "India", "Love"]))


# debug message for better understanding:
# inside first if

# inside for loop 0 i iLoveIndia

# inside for loop 0 i LoveIndia
# inside for loop 1 India LoveIndia
# inside for loop 2 Love LoveIndia

# inside for loop 0 i India
# inside for loop 1 India India

# inside for loop 0 i
# inside for loop 1 India
# inside for loop 2 Love

# Finally : True
