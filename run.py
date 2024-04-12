# import libraries
import time 
# ANSI Escape Codes
blue = "\033[94m"
green = "\033[92m"
red = "\033[91m"
end_color = "\033[0m"
# Define the Battleship class
class Battleship:
    # Initialize the game with grid size and ships chosen by the player
    def __init__(self):
        self.grid_size = int(input(green + "Choose grid size 6 or 10: " ))
        while self.grid_size not in [6, 10]:
            print(red + "Invalid grid size. Please choose 6 or 10." + end_color)
            self.grid_size = int(input(green + "Choose grid size 6 or 10: "))
    # The main gameplay loop
    def play(self):
        print() # Print a blank line
        self.player_name = input(green + "Please enter your name: ")
        print() # Print a blank line
        welcome_message = f"Welcome to Battleship Captain {self.player_name}!\n----------------------"
        print(welcome_message) # Test the welcome message        
        rules = " Rules of Engagement:\n You will be playing against the computer.\n Each of you will have a grid with ships.\n The goal is to sink all of the opponent's ships by\n guessing their positions on the grid.\n If you hit a ship, it will be marked with 'X'.\n If you miss, it will be marked with 'O'.\n The battle continues until all ships of one player are sunk.\n-------------------------------\n"
        for char in rules:
            print(char, end='', flush=True)
            time.sleep(0.05)
        promt = "Do you accept the mission? Press 'Y' to accept or 'N' to decline: "
        for char in promt:
            print(green + char, end='', flush=True)
            time.sleep(0.05)
        accept_mission = input()
        if accept_mission.lower() != 'y':
            print(red + "Mission declined. Exiting the game." + end_color)
            return






# Run the game
game = Battleship()
game.play()