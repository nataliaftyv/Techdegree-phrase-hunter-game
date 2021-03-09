import copy
#from game import Game


class Phrase:

    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.phrase_as_list = list(self.phrase)
        self.hidden_phrase = None
        self.hidden_phrase_as_list = None

    def __str__(self):
        return f'{self.phrase}'

    def check_letter(self, letter):
        if letter in self.phrase_as_list:
            return letter
        else:
            return False

    def display(self, guessed_letters_list):
        # display phrase, un-guessed letters as dash, guessed as letter
        hidden_phrase_list = copy.deepcopy(self.phrase_as_list)
        display_phrase_list = copy.deepcopy(self.phrase_as_list)

        if len(guessed_letters_list) == 0:
            for i in range(len(hidden_phrase_list)):
                if hidden_phrase_list[i] != ' ':
                    hidden_phrase_list[i] = '-'
            hidden_phrase = ''.join(hidden_phrase_list)
            print(f'Hidden phrase is: {hidden_phrase}')
            return hidden_phrase

        else:
            for i in range(len(self.phrase_as_list)):
                for letter in guessed_letters_list:
                    if self.phrase_as_list[i] == letter:
                        display_phrase_list[i] = letter
                    elif self.phrase_as_list[i] != ' ':
                        display_phrase_list[i] = '-'

            display_phrase = ''.join(display_phrase_list)
            print(f'Display phrase is: {display_phrase}')
            # TODO: for testing purposes, remove print when done
            return display_phrase



    def check_complete(self, display_phrase):
        if '-' not in display_phrase:
            return True
        # checks to see if the whole phrase has been guessed
        # TODO: figure this out, should  not be static


