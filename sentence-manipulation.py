#DAY-11
# input sentence
print("Enter a sentence of your choice: ")
response = input()

#output sentence
words = response.split()
first_word = words[0]
last_word = words[-1]
print(len(response))
print(words)
print(len(words))
print(first_word)
print(last_word)

#indexing and slicing
first_three_characters = response[:3]
last_three_characters = response[-3:]
reversed_sentence = response[::-1]
print(first_three_characters)
print(last_three_characters)
print(reversed_sentence)

#modify the sentence
uppercase = response.upper()
lowercase = response.lower()
hyphens = response.replace(" ", "-")
print(uppercase)
print(lowercase)
print(hyphens)
