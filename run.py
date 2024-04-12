# import libraries
import time 
# ANSI Escape Codes
blue = "\033[94m"
green = "\033[92m"
red = "\033[91m"
end_color = "\033[0m"
# Define the Battleship class
class Battleship:
    # The main gameplay loop
    def play(self):
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