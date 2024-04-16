# BattleShip
## Overview
This is third projects developed as part of the Code Institute's curriculum.

Project displays the application of Python programming skills and is deployed on Heroku,

demonstrating practical knowledge in web development and cloud deployment.

## About Website
This is a simple implementation of the classic Battleship game in Python. Players take turns guessing the location of their opponent’s ships on a grid. More information can be found here - [Battleship (Game)](https://en.wikipedia.org/wiki/Battleship_(game))

### Deployed website can be found here and runs in the mock terminal on Heroku. - [BattleShip](https://battleship-game-pp3-cci-7084bd9f71a7.herokuapp.com/)

# Index
1. [Overview](#overview)
2. [About](#about-website)
3. [UX](#ux)
  1.  [User stories](#user-stories)
  2.  [Workflow](#workflow)
4. [Deployment](#deployment)
5. [Features](#features)
6. [Testing](#testing)
   1. [Testing User Stories](#testing-user-stories)
   2. [Manual Testing](#manual-testing)
   3. [Validator Testing](#validator-testing)
   4. [Bugs](#bugs)
7. [Languages and Programs](#languages-and-programs)
8. [Credits](#credits)
    1. [Code](#code)
9. [Acknowledgements](#acknowledgements)

# UX
## User Stories
* As a user, I want to easily find and understand the rules of the game.
  * So that I can quickly learn how to play and enjoy the game without confusion.
* As a user, I want to be able to enter my name when starting the game.
  * So that the game can personalize my experience and address me by name during gameplay.
* As a user, I want to be able to select the grid size before starting the game.
  * So that I can customize the complexity and duration of my gameplay experience.
* As a user, I want to be presented with the an option to accept or decline game.
  * So that I can make an informed decision to either proceed with the game or exit if I’m not comfortable with the rules.
* As a user, I want the game to automatically place my ships randomly on the grid.
  * So that I don’t have to manually position them and can start playing quickly.
* I want to see the positions of my ships on the grid during gameplay.
  * So that I can strategize and plan my attacks effectively.
* As a user, I want to be able to select a cell on the grid to make my move.
  * So that I can target my opponent’s ships.
* As a user, I want immediate feedback on whether my shot hit or missed an opponent’s ship.
  * So that I can adjust my strategy accordingly.
* As a user, I want to receive a warning or error message if Im fired of grid or alredy fired in this cell.
   * So that I can avoid making incorrect moves.
* As a user, I want to be able to see the locations where my opponent has fired shots on my grid.
  * So that I can strategize and anticipate their next moves.
* As a user, I want to be clearly notified when the game is over.
   * So that I can understand who won and how many turns it took to finish the game.

# Workflow
## Pseudocode
Before starting to write code, I began with pseudocode. Pseudocode is an essential step in algorithm design, aiding the programmer in strategizing a solution and assisting the reader in grasping the method of tackling the problem.

1. Import the necessary libraries (random and time).
2. Define ANSI escape codes for color formatting in the terminal.
3. Define a class called Battleship.
4. In the class constructor (__init__ method):
   - Ask the user to choose a grid size (6 or 10).
   - Initialize player and computer grids based on the chosen size.
   - Initialize sets to store player and computer ship positions and attempts.
   - Define ship sizes based on the chosen grid size.
5. Define a method to print the current state of the player's and computer's grids.
6. Define a method to print a grid with optional hiding of ships.
7. Define a method to place ships randomly on a grid.
8. Define a method to handle player's guess:
   - Ask the player for a guess.
   - Check if the guess is valid and hasn't been attempted before.
   - If the guess hits a ship, mark it and remove the ship position from the set.
   - If the guess misses, mark it on the grid.
9. Define a method to handle computer's guess:
   - Generate a random guess.
   - Check if the guess hasn't been attempted before.
   - If the guess hits a ship, mark it and remove the ship position from the set.
   - If the guess misses, mark it on the grid.
10. Define the main gameplay loop (play method):
    - Ask the player for their name.
    - Print a welcome message and the rules of the game.
    - Ask the player if they accept the mission.
    - If the player declines, exit the game.
    - If the player accepts, place ships on the player's and computer's grids.
    - While there are still ships on both grids, let the player and computer take turns guessing.
    - After each turn, check if all ships of one player have been sunk.
    - If all ships of one player have been sunk, end the game and declare the other player as the winner.
11. Outside the class, create an instance of the Battleship class and start the game by calling the play method.

## Chart
![Flow Chart](/readme-docs/flow-chart.png)

# Deployment

# Features

# Testing
## Testing User Stories

## Manual Testing
Test | Steps | Expected Outcome | Result
--- | --- | --- | ---
Initialization | Run the script | The script should prompt you to choose a grid size of 6 or 10 | Yes
Grid Size Input | Enter a valid grid size (6 or 10) | The script should accept the input and proceed to the next step | Yes
---- | Enter an invalid grid size (any number other than 6 or 10) | The script should display an error message and prompt you to enter a valid grid size again | Yes
Player Name Input | Enter a valid name | The script should accept the input and display a welcome message | Yes
---- | No name entered | The script should accept the input and display a welcome message with no name | Yes
Game Rules Acceptance | Enter 'Y' to accept the missionEnter | The script should proceed to the game | Yes
---- | Enter 'N' or any key to decline the mission | The script should display a message "Mission declined. Exiting the game." and exit the game | Yes
Grid prints | No input required | The scrip should display selected grid with amount ships based on it size | Yes
Player Guess | Enter a valid guess (e.g., A5) | The script should accept the input and display whether it was a hit or miss | Yes
---- | Enter an invalid guess (e.g., Z20) | The script should display an error message and prompt you to enter a valid guess again | Yes
Computer Guess | No input required | The script should display the computer's guess and whether it was a hit or miss | Yes
Game End | No input required | The script should display a message indicating who won the game and amout trys it took | Yes





## Validator Testing









