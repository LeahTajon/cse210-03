import random
from game.jumper import Jumper
from game.terminal_service import TerminalService
class Puzzle:
    """ A puzzle that player will guess.

    The responsibility of Puzzle is to hold words, select random word, and process the player guesses.

    Attributes:
        words (list): List of words
        random_word (string): A word randomly selected from the list of words.
        jumper (Jumper): The game's jumper character.
        terminal_service: For getting and displaying information on the terminal.
        tries (int): The number of tries the player guessed the word.
        guess (string): The guessed letter.
        blank (list): For hiding the secret word.


   
    """
    def __init__(self):
        """ Constructs a new Puzzle.

        Args:
            self (Puzzle): an instance of Puzzle.
        """
        self._words = ['affix', 'avenue', 'awkward','beekeeper', 'boogle', 'cobweb', 'cycle', 'disavow', 'duplex', 'equip',
        'exodus', 'funny', 'galaxy', 'gossip', 'icebox', 'injury', 'ivory', 'jackpot', 'jelly', 'jockey',
         'joking', 'joyful', 'jumbo', 'kayak', 'khaki', 'kiosk', 'lengths', 'lucky', 'luxury', 'lymph',
         'million', 'onyx', 'ovary', 'pajama', 'pneumonia', 'pshaw', 'puppy', 'scratch', 'staff', 'stretch']

        self._random_word = random.choice(self._words)
        self._jumper = Jumper()
        self._terminal_service = TerminalService()
        self._tries = 0
        self._guess = ''
        self._blank = ['_' for letter in self._random_word]
        
    def get_word(self):
        """ Gets a random word.

        Args:
            self (Puzzle): An instance of Puzzle.

        Returns:
            string: A random word for the game.
        """
        return self._random_word

    def _display_puzzle(self):
        """ Shows the secret word.

        Args:
            self (Puzzle): An instance of Puzzle.
        """
        display = ' '.join(self._blank)

        print(f'\nThe word is: {display}')
        
    def display_word(self):
        """ Displays the puzzle.

        Args: 
            self (Puzzle): An instance of Puzzle.
        """
        self._display_puzzle()
    
    def display_jumper(self):
        """ Displays the jumper character.

        Args:
            self (Puzzle): An instance of Puzzle.
        """
        self._jumper.display_jumper(self._tries)

    def get_guess(self, letter):
        """ Gets the correct guess letter and adds the index to the location.

        Args:
            self (Puzzle): An instance of Puzzle.
        
        Returns:
            int: The index of the correct letter.
        """
        locations = []
        for index, char in enumerate(list(self._random_word)):
            if char == letter:
                locations.append(index)
        return locations

    def update_puzzle(self, idx, letter):
        """ Updates the masked puzzle with the correct letter.

        Args:
            self (Puzzle): An instance of Puzzle
        """
        for number in idx:
            self._blank[number] = letter

    def check_guess(self, letter):
        """ Checks if the guess letter is in the puzzle word or not.

        Args:
            self (Puzzle): An instance of Puzzle
        """
        
        if letter in self._random_word:
            idx = self.get_guess(letter)
            self.update_puzzle(idx, letter)    
        else:
            self._tries += 1
            
    def is_win(self):
        """ Checks if the player guessed the word.

        Args:
            self (Puzzle): An instance of Puzzle.

        Returns:
            Boolean: When the player won. 
        
        """
        display = ''.join(self._blank)
        word = self._random_word
        if display == word:
            return True 
        
    def is_loss(self):
        """ Checks if the player made four tries. 
        
        Args:
            self (Puzzle): An instance of Puzzle.
        
        Returns:
            Boolean: When the player made four tries.
        """

        number_of_tries = self._tries
        if number_of_tries == 4:
            return True


