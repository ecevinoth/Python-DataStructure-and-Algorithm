def word_split(phrase, list_of_words, output=None):

    if output is None:
        output = []
        print("inside if condition")

    i = 0
    for word in list_of_words:

        if len(phrase) == 0:
            break
        print("inside for loop : ", i, "word :", word, ", input phrase :", phrase)
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):], list_of_words, output)
        i += 1

    return True if len(output) == len(list_of_words) else False


print(word_split("iLoveIndia", ["i", "India", "Love"]))

# # # debug message for better understanding

# # # 1st iteration
# inside if condition
# inside for loop :  0 word : i , input phrase : iLoveIndia

# # # 2nd iteration
# inside for loop :  0 word : i , input phrase : LoveIndia
# inside for loop :  1 word : India , input phrase : LoveIndia
# inside for loop :  2 word : Love , input phrase : LoveIndia

# # # 3td iteration
# inside for loop :  0 word : i , input phrase : India
# inside for loop :  1 word : India , input phrase : India

# # Finally : True
