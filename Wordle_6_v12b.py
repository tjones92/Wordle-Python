import random

words = open('sixletterwordlist.txt', 'r')
wordlist = words.read()

wordarray = wordlist.split("\n")

word = random.choice(wordarray)

def word_check(guess):
    result = ""
    for x in range(0, 6):
        if guess[x] == word[x]:
            result += "o"
        elif guess[x] in word:
            result += "x"
        elif guess[x] not in word[x]:
            result += "_"
            continue
    print(result)

count = 0

while True:
        guess = input("Enter a six-letter word: ")
        if len(guess.lower()) < 6:
            print("Please enter a six-letter word.")
            continue
        if len(guess.lower()) > 6:
            print("Please enter a six-letter word.")
            continue
        if guess.lower() not in wordarray:
            print("Guess not in wordlist.")
            continue
        else:
            word_check(guess.lower())
            if  guess == word:
                print("Correct!")
                break
            else:
                count += 1
                if count >= 6:
                    print("The word was " + word)
                    print("Try again.")
                    break

