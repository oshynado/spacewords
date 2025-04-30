# Space Words - A Typing Game

Space Words is a fun and educational typing game where players control a spaceship and defeat word-based enemies by typing their words correctly. The game helps improve typing speed and accuracy while providing an engaging space-themed experience.

## Features

- **Three Difficulty Levels**: Enemies with words of varying lengths (easy, medium, hard)
- **Health System**: Players start with 3 lives and can gain extra lives from special "health" enemies
- **Dynamic Difficulty**: Game gets harder as you progress
- **Score Tracking**: Keep track of your progress and aim for a high score
- **Beautiful Space Theme**: Engaging visuals with scrolling background

## How to Play

1. **Controls**:

   - Type the letters of the word shown above the nearest enemy
   - Letters must be typed in the correct order
   - Complete the word to defeat the enemy

2. **Game Mechanics**:

   - Enemies slowly move toward your spaceship
   - If an enemy reaches you, you lose a life
   - Special "health" enemies occasionally appear - defeat them to gain an extra life
   - The game ends when you lose all your lives

3. **Scoring**:
   - Each defeated enemy gives you 1 point
   - The game gets progressively harder as you score more points

## Installation

1. Ensure you have Python 3.x installed
2. Install the required dependencies: pip install pygame english-words
3. Download or clone this repository
4. Run the game: python spaceword.py

## File Structure

spaceword.py - Main game file
graphics/ - Contains all game images
background.jpg - Scrolling background image
space_ship.png - Player spaceship image
enemies/ - Enemy images
easy_enemy.png
mid_enemy.png
hard_enemy.png
health_enemy.png
font/ - Contains the game font
Jersey10-Regular.ttf

## Requirements

- Python 3.x
- Pygame library
- english-words package

Enjoy the game and happy typing!
