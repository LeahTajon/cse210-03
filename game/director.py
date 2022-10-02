from game.jumper import Jumper
from game.puzzle import Puzzle
from game.terminal_service import TerminalService

class Director:
    """ A person who directs the game.

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        jumper (Jumper): The stages of jumper.
        is_playing (boolean): Whether or not to keep playing.
        puzzle (Puzzle): The secret random word
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """ Constructs a new Director.
        
        Args:
            self (Director): an instance of Director
        """
        self._jumper = Jumper()
        self._is_playing = True
        self._puzzle = Puzzle()
        self._terminal_service = TerminalService()
    
    def start_game(self):
        """ Starts the game by running the main game loop. 
        
        Args:
            self (Director): an instance of Director
        """
        while self._is_playing:
            self._get_inputs()
            self._do_outputs()

    def _get_inputs(self):
        """ Displays the secret word, character, and gets the guess letter from the player.

        Args:
            self (Director): an instance of Director
        """
        self._puzzle.display_word()
        self._puzzle.display_jumper()
        new_letter = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        self._puzzle.check_guess(new_letter.lower())
        

    def _do_outputs(self):
        """ Displays whether the player wins or losses the game.

        Args:
            self (Director): an instance of Director
        """
        if self._puzzle.is_win():
            self._puzzle.display_word()
            self._puzzle.display_jumper()
            self._terminal_service.write_text('\nCongratulations! You have guessed the word.\n')
            self._is_playing = False
        
        if self._puzzle.is_loss():
            word = self._puzzle.get_word()
            self._puzzle.display_jumper()
            self._terminal_service.write_text(f'\nGAME OVER! You have ran out of guesses!\nThe word was >> {word.upper()}.\n')
            self._is_playing = False

