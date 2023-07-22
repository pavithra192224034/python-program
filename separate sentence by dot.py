sentence = "this is a cat"

words = sentence.split()

capitalized_words = [word.capitalize() for word in words]

new_sentence = ' '.join(capitalized_words) + '.'

print("The new sentence is:", new_sentence)
