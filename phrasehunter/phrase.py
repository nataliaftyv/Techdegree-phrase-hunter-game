import copy

class Phrase:

    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.phrase_as_list = list(self.phrase)
        self.hidden_phrase = None
        self.hidden_phrase_as_list = []
        self.display_phrase = None


    def __str__(self):
        return f'{self.phrase}'

    def convert_to_hidden(self):
        self.hidden_phrase_as_list = copy.deepcopy(self.phrase_as_list)
        for i in range(len(self.phrase_as_list)):
            if self.phrase_as_list[i] != ' ':
                self.hidden_phrase_as_list[i] = '-'
        self.hidden_phrase = ''.join(self.hidden_phrase_as_list)
        return self.hidden_phrase

    def check_letter(self, letter):
        if letter in self.phrase_as_list:
            return letter
        else:
            return False

    def display(self, correct_guesses):
        # display phrase, un-guessed letters as dash, guessed as letter

        if len(correct_guesses) == 0:
            self.convert_to_hidden()
            print(f'Hidden phrase is: {self.hidden_phrase}')
            return self.hidden_phrase

        else:
            letter = correct_guesses[-1]
            for i in range(len(self.phrase_as_list)):
                if self.phrase_as_list[i] == letter:
                    self.hidden_phrase_as_list[i] = letter

            self.display_phrase = ''.join(self.hidden_phrase_as_list)
            print(f'Display phrase is: {self.display_phrase}')
            # TODO: for testing purposes, remove print when done
            return self.display_phrase

    def check_complete(self):
        print('check_complete called!')
        # checks to see if the whole phrase has been guessed
        #display_phrase_as_list = list(self.display_phrase)
        if '-' not in self.hidden_phrase_as_list:
            print('Check Complete is True')
            return True
        else:
            print('Check Complete is False')
            return False




