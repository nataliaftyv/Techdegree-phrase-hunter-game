import random
from phrasehunter.phrase import Phrase

# TODO: catch value errors
# TODO: prevent repeat guesses of same letter


class Game:

    def __init__(self):
        self.missed = 0
        self.allowed_misses = 1
        self.phrases = [
            'The Remains of the Day',
            'A Pale View of Hills',
            'An Artist of the Floating World ',
            'Never Let Me Go',
            'The Buried Giant'
        ]
        self.active_phrase = None
        self.guesses = []
        # a list that contains the letters guessed by the user.
        self.correct_guesses = []

    def start(self):
        self.welcome()
        # creates the game loop,
        self.active_phrase = self.get_random_phrase()
        print(f'Active Phrase is {self.active_phrase}')
        # TODO: for testing purposes, remove print when done

        while self.missed < self.allowed_misses:
            self.active_phrase.display(self.correct_guesses)
            letter = self.get_guess()
            self.active_phrase.check_letter(letter)
            if self.active_phrase.check_letter(letter) is False:
                self.missed += 1
                print(f'Wrong Guess! You have {self.allowed_misses - self.missed} of {self.allowed_misses} lives left')

            else:
                self.correct_guesses.append(self.active_phrase.check_letter(letter))
                print('Good guess!')
                self.active_phrase.display(self.correct_guesses)
                self.active_phrase.check_complete()

        self.game_over()
        print('Game over')

    def get_random_phrase(self):
        phrase_choice = random.choice(self.phrases)
        current_phrase = Phrase(phrase_choice)
        return current_phrase

    @staticmethod
    def welcome():
        print('Welcome to the Phrase Hunt Game! Can you guess the hidden phrase?')

    def get_guess(self):
        # gets the guess from a user and records it in the guesses attribute
        guess = input('Guess a letter > ')
        guess = guess.lower()
        self.guesses.append(guess)
        print(self.guesses)
        print(f' user letter is: {guess}')
        return guess
        # TODO: for testing purposes, remove print when done

    def game_over(self):
        # this method displays a friendly win or loss message and ends the game.
        self.active_phrase.check_complete()
        if Phrase.check_complete:
            print('You won!')
        elif self.missed > self.allowed_misses:
            print('You lost!')

