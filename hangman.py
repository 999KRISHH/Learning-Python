#Step 5

import random
import hangman_art
# import hangman_words
import movies

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
if type == 1:
    word_list = (movies.bollywood_movies)
    word = random.choice(word_list)
elif type == 2:
    word_list = (movies.hollywood_movies)
    word = random.choice(word_list)
else:
    word_list = (movies.movies)
    word = random.choice(word_list)
chosen_word = word.lower()
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)
type = input(
    "Welcome to Hangman!\nType '1' for Bollywood or Type '2' for Hollywood or just press 'Enter' for a mix of  both Bollywood and Hollywood: "
)
#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print("".join(display))
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    if guess in display:
        print(f"You've already guessed {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose.\nThe word is {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(hangman_art.stages[lives])

    # print(stages[lives])
# print(word_list)
