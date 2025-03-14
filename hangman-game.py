#DAY-31
import random

def hangman():
    word_list = ["bread", "python", "commando", "purple", "monday"]
    word = random.choice(word_list)
    guessed_word = ['_'] * len(word)
    attempts = 5

    print("Welcome to Hangman!")
    print("Guess a word: ")
    print(" ".join(guessed_word))

    while attempts > 0:
        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letter.")
            continue

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
            print("Good try!")

        else: 
            attempts -= 1
            print(f"Incorrect. {attempts} attempts left.")

        print(" ".join(guessed_word))

        if "_" not in guessed_word:
            print("\nYou won! The wordis:", word)
            break
    else:
        print("\nYou lost! The word was:", word)

hangman()
