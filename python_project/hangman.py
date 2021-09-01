import dictionary_parser
import random
import scores_parser


def choose_category(categories):
    """Print the categories in a readable format and let the user choose one of them."""
    for i, category in enumerate(categories):
        print(f'{i}.{category}')
    num = -1
    while num < 0 or num >= len(categories):
        num = int(input('Enter the number corresponding to your desired category: '))
    print('------------------------------------------------')
    for i, category in enumerate(categories):
        if num == i:
            return category


def choose_random_word(chosen_category):
    """Pick a random word from a given category."""
    words = dictionary_parser.get_words_from_category(chosen_category)
    return random.choice(words)


def set_allowed_failed_guesses(chosen_word):
    """Set the maximum allowed number of failed guesses for a specific word length."""
    if len(chosen_word) < 10:
        return 4
    elif len(chosen_word) < 20:
        return 6
    else:
        return 8


def game(word, guesses):
    """Main instance of the game.
    Based on the chosen word, generate its censored version.

    After each guess, update the game window depending on the outcome (correct or wrong).
    If the guessed letter is found in the word, the censored version is updated accordingly.
    Otherwise, the number of guesses left decreases by one.

    The game ends when either the word is found or the number of guesses left is zero.
    """
    wrong_guesses = 0
    censored_word = word
    already_guessed_letters = []
    for i in range(0, len(censored_word)):
        if censored_word[i].isalnum():
            censored_word = censored_word[:i] + '-' + censored_word[i + 1:]
    while guesses > 0 and '-' in censored_word:
        # print(censored_word)
        guessed_letter = display_game(censored_word, guesses)
        for i in range(0, len(word)):
            if word[i] == guessed_letter:
                censored_word = censored_word[:i] + guessed_letter + censored_word[i + 1:]
        if guessed_letter in already_guessed_letters:
            guesses -= 1
            wrong_guesses += 1
        else:
            already_guessed_letters.append(guessed_letter)
        if guessed_letter not in word:
            guesses -= 1
            wrong_guesses += 1
        if censored_word == word and guesses > 0:
            print(f'You won! The word was \'{word}\'')
            print('------------------------------------------------')
            scores_parser.add_score(word, wrong_guesses, 'won')
            break
        elif censored_word != word and guesses == 0:
            print(f'You lost! The word was \'{word}\'')
            print('------------------------------------------------')
            scores_parser.add_score(word, wrong_guesses, 'lost')
            break


def display_game(word, guesses):
    """Prints a new instance of the game after every guess."""
    print(f'Guesses left: {guesses}')
    print(f'Current word: {word}')
    current_guess = input('Enter your current guess: ')
    while not current_guess.isalnum():
        current_guess = input('Enter your current guess: ')
    print('------------------------------------------------')
    return current_guess


if __name__ == '__main__':
    playing = True
    while playing:
        print('Choose your option:')
        print('1. Play')
        print('2. See previous scores')
        print('3. Exit')
        opt = input('Enter your number: ')
        print('------------------------------------------------')
        if opt == '1':
            cat = choose_category(dictionary_parser.get_categories())
            w = choose_random_word(cat)
            allowed_failed_guesses = set_allowed_failed_guesses(w)
            game(w, allowed_failed_guesses)
        elif opt == '2':
            scores_parser.get_scores()
        elif opt == '3':
            break
