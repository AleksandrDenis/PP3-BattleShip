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
        self.grid_size = int(input(green + "Choose grid size 6 or 10: "))
        while self.grid_size not in [6, 10]:
            print(red + "Invalid grid size. Please choose 6 or 10." + end_color)
            self.grid_size = int(input(green + "Choose grid size 6 or 10: "))
        self.player_grid = [["~"] * self.grid_size for _ in range(self.grid_size)]
        self.computer_grid = [["~"] * self.grid_size for _ in range(self.grid_size)]
    
    # Print the grid state
    def print_grids(self):
        print("Player's Grid:")
        self.print_grid(self.player_grid)
        print("Computer's Grid:")
        self.print_grid(self.computer_grid)

    # Print grid numbers
    def print_grid(self, grid):
        print(green + "  " + " ".join(str(i) for i in range(self.grid_size)) + end_color)
    # Print grid row in letters
        for i, row in enumerate(grid):
            print(green +chr(65 + i) + end_color + " " + " ".join(blue + "~" + end_color if cell == "~" else cell for cell in row))
            
    

        

        
        

        



    # The main gameplay loop
    def play(self):
        print() # Print a blank line
        self.player_name = input(green + "Please enter your name: ")
        print() # Print a blank line
        welcome_message = f"Welcome to Battleship Captain {self.player_name}!\n----------------------"
        print(welcome_message) # Test the welcome message        
        rules = "RULES will be printed" #" Rules of Engagement:\n You will be playing against the computer.\n Each of you will have a grid with ships.\n The goal is to sink all of the opponent's ships by\n guessing their positions on the grid.\n If you hit a ship, it will be marked with 'X'.\n If you miss, it will be marked with 'O'.\n The battle continues until all ships of one player are sunk.\n-------------------------------\n"
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
        
        self.print_grids()
            

           
        






# Run the game
game = Battleship()
game.play()