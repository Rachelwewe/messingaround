import random

# Word list
words = ['python', 'hangman', 'challenge', 'programming', 'computer', 'artificial', 'intelligence']

# Choose a random word
word = random.choice(words)
word_letters = set(word)  # unique letters in the word
guessed_letters = set()
tries = 6  # number of allowed wrong attempts

print("Welcome to Hangman!")

# Game loop
while tries > 0 and word_letters != guessed_letters:
    print("\nWord: ", ' '.join([letter if letter in guessed_letters else '_' for letter in word]))
    print(f"Tries left: {tries}")
    print("Guessed letters:", ' '.join(sorted(guessed_letters)))

    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Invalid input. Enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word_letters:
        print("Good guess!")
    else:
        print("Wrong guess!")
        tries -= 1

# Game result
if word_letters == guessed_letters:
    print(f"\nCongratulations! You guessed the word: {word}")
else:
    print(f"\nGame Over! The word was: {word}")
