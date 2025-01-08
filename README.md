# Snake Game Project

## Overview
This project implements a simple Snake game using Python, developed as part of the AP Computer Science Principles coursework. The game builds on concepts from Unit 3 (Programming) and Unit 4 (Algorithms) by integrating structured programming techniques and logical flow to create an interactive gaming experience.

## Features
- **Grid-based Playfield**: A 16x16 grid represents the game board.
- **Snake Movement**: The snake starts at a random position and moves based on user input.
- **Food System**: Apples spawn at random positions; eating them increases the score and grows the snake.
- **Dynamic Speed**: The snake's speed increases as the score goes up.
- **Collision Detection**: The game ends when the snake hits a wall or itself.
- **Color Cycle**: The snake changes colors cyclically as it grows.
- **Scoring System**: A live score display tracks the player's progress.

## Relevance to Curriculum
### Unit 3: Programming
- **Functions**: The game uses modular functions to handle different aspects of gameplay, like `drawGrid`, `move_snake`, and `adjust_snake`.
- **Control Structures**: `if-elif` and `for` loops manage gameplay mechanics and grid drawing.

### Unit 4: Algorithms (Better Fit)
- **Variables and Data Types**: Random positions for the snake and food are determined using variables and the `random` library.
- **Algorithm Design**: Implements complex algorithms for:
  - Movement of the snake.
  - Collision detection for both walls and the snake's body.
  - Adjusting the snake's speed and growing its length.
- **Abstraction**: Encapsulation of gameplay logic into reusable functions.
- **Efficiency**: Use of modular arithmetic and list traversal for gameplay updates.

## How to Play
1. Use arrow keys to control the snake's direction:
   - **Up Arrow**: Move up
   - **Down Arrow**: Move down
   - **Left Arrow**: Move left
   - **Right Arrow**: Move right
2. Avoid hitting the walls or the snake's own body.
3. Collect apples to increase your score and grow the snake.
4. The game ends if the snake collides with itself or the border.

## Game Design
### Grid System
- The game board is a 400x400 pixel grid divided into 16x16 cells, each measuring 25x25 pixels.
- The snake and apple align with the grid for precise movement and placement.

### Snake Logic
- The snake's head controls movement, and each segment follows the previous one.
- The snake's speed dynamically increases as the score rises.
- Colors cycle through a predefined rainbow palette as the snake grows.

### Apple Placement
- Apples spawn randomly on the grid, but not on the snake's body.
- Eating an apple adds a new segment to the snake.

### Scoring System
- Each apple increases the score by 1.
- Score updates dynamically in real-time, with visual feedback on the game interface.

## Future Enhancements
- **Difficulty Levels**: Add options for easy, medium, and hard modes.
- **High Score Tracker**: Save and display the highest score.
- **Obstacles**: Introduce barriers to increase challenge.
- **Sound Effects**: Add audio feedback for movement, apple collection, and game over.

## Conclusion
This Snake game showcases programming concepts and algorithms effectively, making it more suitable for Unit 4 as it demonstrates abstraction, efficiency, and algorithmic thinking. The game offers a fun way to explore these concepts while creating an engaging project.

---

**Author**: KeiraOMG0  
**Developed For**: AP Computer Science Principles  Cmu
**Unit Focus**: Unit 4 (Algorithms)

