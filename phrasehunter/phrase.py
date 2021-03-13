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
        # converts the active phrase into dashes for display at the start of the game

        self.hidden_phrase_as_list = copy.deepcopy(self.phrase_as_list)
        for i in range(len(self.phrase_as_list)):
            if self.phrase_as_list[i] != ' ':
                self.hidden_phrase_as_list[i] = '_'
        self.hidden_phrase = ''.join(self.hidden_phrase_as_list)
        return self.hidden_phrase

    def check_letter(self, letter):
        if letter in self.phrase_as_list:
            return letter
        else:
            return False

    def display(self, letter):
        # gets correctly guessed letter from check_letter()
        # displays phrase, un-guessed letters as dash, guessed as letter

        for i in range(len(self.phrase_as_list)):
            if self.phrase_as_list[i] == letter:
                self.hidden_phrase_as_list[i] = letter

        self.display_phrase = ''.join(self.hidden_phrase_as_list)
        print(f'The phrase is: {self.display_phrase}')
        return self.display_phrase

    def check_complete(self):
        # checks to see if the whole phrase has been guessed
        if '_' not in self.hidden_phrase_as_list:
            return True
        else:
            return False
