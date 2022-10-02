class Jumper:
  """ The character of the game.

  Responsibility: Draw character with parachute.

  """
  def __init__(self):
    self._stages = [
        """
           .---.                
          (_____)
           \   / 
            \ /               
             0   
            /|\  
            ( ) 

          ^^^^^^^
        """, 
        """
          (_____) 
           \   / 
            \ /  
             0   
            /|\  
            ( )

          ^^^^^^^ 
        """,
        """
           \   / 
            \ /  
             0   
            /|\  
            ( )  

          ^^^^^^^
        """,
        """
            \ /  
             0   
            /|\  
            ( )  

          ^^^^^^^
        """,
        """
             x   
            /|\  
            / \  
          
          ^^^^^^^
        """]

  def display_jumper(self, tries):
    """ Displays character for the player.

    Args:
      self (Jumper): an instance of Jumper
    """
    print(self._stages[tries])
        
    

