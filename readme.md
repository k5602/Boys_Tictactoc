# Boys_Tictactoc

A command-line based Tic-Tac-Toe game with two gameplay modes: Player vs AI (using the Minimax algorithm with alpha-beta pruning) and Player vs Player. Recently refactored for improved stability and user experience.

## Features

- Two game modes:
  - **Player vs AI**: Challenge a computer opponent that uses the Minimax algorithm with alpha-beta pruning
  - **Player vs Player**: Play against a friend on the same computer
- Command-line interface with simple text-based board visualization
- Input validation to prevent illegal moves
- Ability to play multiple games in succession

## Requirements

- Python 3.x

## How to Play

1. Clone this repository
2. Navigate to the project directory in your terminal
3. Run the game:
   ```
   python game_logic.py
   ```
4. Select a game mode:
   - 1: Player vs AI
   - 2: Player vs Player
5. Enter moves as row-column coordinates (e.g., "1 2" for the middle-right position)
   - Rows and columns are zero-indexed (0-2)
   - The board layout is as follows:
     ```
     0,0 | 0,1 | 0,2
     ---------------
     1,0 | 1,1 | 1,2
     ---------------
     2,0 | 2,1 | 2,2
     ```

## Project Structure

- `game_logic.py`: Main game loop and UI logic
- `minimax.py`: Implementation of the Minimax algorithm for AI opponent
- `gui.py`: Reserved for future graphical interface implementation

## How the AI Works

The AI uses the Minimax algorithm with alpha-beta pruning to determine the optimal move. This algorithm:

1. Evaluates all possible future game states
2. Assigns scores to terminal states (win: +10, loss: -10, draw: 0)
3. Chooses the move that maximizes the AI's chances of winning
4. Uses alpha-beta pruning to optimize the search by eliminating branches that won't affect the final decision

## Future Enhancements

- Graphical user interface using Pygame or Tkinter
- Difficulty levels for the AI
- Score tracking across multiple games
- Network play functionality
- Improved visual design
- Custom player symbols

- **Development Opportunities**:
  - Empty `gui.py` file suggests an intended GUI implementation
  - Code could benefit from a refactoring into proper classes
  - Test coverage would improve reliability

## License

This project is open source and available for educational purposes.

## Acknowledgements

This project was created to demonstrate the implementation of the Minimax algorithm in a simple game environment.