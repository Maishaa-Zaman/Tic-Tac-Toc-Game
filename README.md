# Tic Tac Toe with Minimax and Alpha-Beta Pruning

This is a Python implementation of the classic **Tic Tac Toe** game that uses the **minimax algorithm with alpha-beta pruning** for optimal AI decision-making. The game includes two modes:
- **Human vs Computer**: The player competes against an AI opponent.
- **Computer vs Computer**: Two AI players compete against each other, with moves fully automated.

The game is implemented using **Python** and the **Tkinter** library for the graphical user interface (GUI).

## Features

- **Graphical Interface**: The game uses Tkinter to display a 3x3 interactive grid.
- **Minimax Algorithm with Alpha-Beta Pruning**:
  - The AI calculates the best possible move by simulating all future game states.
  - Alpha-beta pruning optimizes the minimax algorithm by reducing unnecessary evaluations.
- **Two Game Modes**:
  1. **Human vs Computer**: The human player (X) plays against the AI (O).
  2. **Computer vs Computer**: Both X and O are controlled by the AI, and the game progresses automatically.
- **Automatic Game Over Detection**:
  - The game detects when a player wins or when the board is full (a draw).
  - A pop-up message announces the result, and the game resets.
  - 
## How It Works

### Game Rules:
- Players take turns placing their symbol (X or O) on the grid.
- The first player to align three of their symbols in a row, column, or diagonal wins.
- If all cells are filled without a winner, the game ends in a draw.

### AI Logic:
The AI uses the **minimax algorithm** with alpha-beta pruning:
- **Maximizing Player (O)**: The AI tries to maximize its score.
- **Minimizing Player (X)**: The AI assumes the opponent is trying to minimize the score.
- Alpha-beta pruning improves efficiency by cutting off branches that cannot affect the result.
