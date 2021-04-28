import random
from hangman_words import word_list
from art import logo, stages


def main():
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    lives = 6
    print(logo)
    display = []

    for _ in range(word_length):
        display += "_"

    end_of_game = False
    while not end_of_game:
        guess = input("Guess a letter: ").lower()
        if guess in display:
            print(f"You have already guessed this letter {guess}")
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        if guess not in chosen_word:
            print(f"The letter {guess} is not in the word.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print(f"You lose. The word is {chosen_word}")
        print(f"{' '.join(display)}")
        if "_" not in display:
            end_of_game = True
            print("You win.")
        print(stages[lives])


if __name__ == '__main__':
    main()

