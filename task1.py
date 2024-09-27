import random

def choose_word():
    # List of words to choose from
    word_list = ['python', 'hangman', 'programming', 'challenge', 'computer']
    return random.choice(word_list)

def display_word(word, guessed_letters):
    # Display the current state of the word
    display = ''.join(letter if letter in guessed_letters else '_' for letter in word)
    return display

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts_left = 6  # Number of incorrect attempts allowed
    used_letters = set()

    print("Welcome to Hangman!")
    
    while attempts_left > 0:
        print("\nCurrent word: ", display_word(word, guessed_letters))
        print("Used letters: ", ' '.join(sorted(used_letters)))
        print("Attempts left: ", attempts_left)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in used_letters:
            print("You've already guessed that letter.")
            continue

        used_letters.add(guess)

        if guess in word:
            guessed_letters.add(guess)
            if set(word) == guessed_letters:
                print("\nCongratulations! You've guessed the word:", word)
                break
        else:
            attempts_left -= 1
            print(f"Incorrect! The letter '{guess}' is not in the word.")
        
        if attempts_left == 0:
            print("\nGame over! The word was:", word)

if __name__ == "__main__":
    hangman()
