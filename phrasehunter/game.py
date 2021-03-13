import random
from phrasehunter.phrase import Phrase
# TODO: remove all test print statements


class Game:

    def __init__(self):
        self.missed = 0
        self.allowed_misses = 5
        self.phrases = [
            'The Remains of the Day',
            'A Pale View of Hills',
            'An Artist of the Floating World ',
            'Never Let Me Go',
            'The Buried Giant'
        ]
        self.allowed_chars = list('abcdefghijklmnopqrstuvwxyz')
        self.active_phrase = None
        self.guesses = []
        # a list that contains unique letters guessed by the user, duplicates not recorded

    def start(self):
        self.welcome()
        self.active_phrase = self.get_random_phrase()
        print(f'Your phrase is: {self.active_phrase.convert_to_hidden()}')

        while self.missed <= self.allowed_misses:
            letter = self.get_guess()
            if letter == 'Duplicate':
                print('Oops! You already tried this letter! Try again!')
                letter = self.get_guess()
            while letter not in self.allowed_chars:
                print('Oops! This character is not allowed! Must be a single letter of English alphabet! Try again!')
                letter = self.get_guess()
            if self.active_phrase.check_letter(letter):
                print('Good guess!')
                self.active_phrase.display(letter)
                if self.active_phrase.check_complete():
                    break
            else:
                self.missed += 1
                print(f'Wrong Guess! You have used {self.missed} of {self.allowed_misses} allowed misses!')

        self.game_over()
        print('This Game is over!')

    def get_random_phrase(self):
        phrase_choice = random.choice(self.phrases)
        current_phrase = Phrase(phrase_choice)
        return current_phrase

    @staticmethod
    def welcome():
        print('Welcome to the Phrase Hunt Game! Can you guess the hidden phrase?')

    def get_guess(self):
        # gets the guess from a user and records it in the guesses attribute, unless it is a repeat guess
        # in case of repeat guess, returns string 'Duplicate' for future handling in Game class

        guess = input('Guess a letter > ').lower()
        if guess not in self.guesses:
            self.guesses.append(guess)
            return guess
        else:
            return 'Duplicate'

    def game_over(self):
        # displays a friendly win or loss message and ends the game
        if self.active_phrase.check_complete():
            print('Congratulations! You won!')
        else:
            print('Too bad, you lost! Better luck next time!')
