# import libraries



# Define the Battleship class
class Battleship:
    # The main gameplay loop
    def play(self):
        self.player_name = input("Please enter your name: ")
        print() # Print a blank line
        welcome_message = f"Welcome to Battleship Captain {self.player_name}!\n----------------------"
        print(welcome_message) # Test the welcome message
        



# Run the game
game = Battleship()
game.play()