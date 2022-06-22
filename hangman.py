from random import choice
from string import ascii_lowercase

alphabet = ascii_lowercase
words = 'python', 'java', 'swift', 'javascript'
scoreboards = [0, 0]

print("H A N G M A N")
status = " "
while status not in "exit":
    status = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if status == "play":
        print()
        attempts = 8
        used_letter = set()
        word = choice(words)
        secret_word = '-' * len(word)
        while attempts > 0:
            print(secret_word)
            letter = input("Input a letter: ")
            if letter not in alphabet and len(letter) == 1:
                print("Please, enter a lowercase letter from the English alphabet.")
            elif len(letter) != 1:
                print("Please, input a single letter.")
            else:
                if letter in used_letter:
                    print("You've already guessed this letter.")
                elif letter in word:
                    index = word.find(letter)
                    for _ in range(word.count(letter)):
                        secret_word = secret_word[:index] + letter + secret_word[index + 1:]
                        index = word.find(letter, index + 1)
                    if secret_word == word:
                        break
                else:
                    print("That letter doesn't appear in the word.")
                    attempts -= 1
                used_letter.add(letter)
            print()
        if not attempts:
            scoreboards[1] += 1
            print("You lost!")
        else:
            scoreboards[0] += 1
            print(f"You guessed the word {secret_word}!")
            print("You survived!")
    elif status == "results":
        print(f"You won: {scoreboards[0]} times.")
        print(f"You lost: {scoreboards[1]} times.")
