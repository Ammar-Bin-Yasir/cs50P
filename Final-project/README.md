# Connect Four - Player vs AI

A strategic Connect Four game featuring an AI opponent powered by the minimax algorithm with alpha-beta pruning.

## Features

- **Player vs AI Gameplay**: Compete against an intelligent AI opponent
- **Optimized AI Engine**: Uses minimax algorithm with alpha-beta pruning for efficient decision-making
- **Visual Board**: Real-time graphics rendering with Pygame
- **Background Music**: Immersive audio accompaniment during gameplay
- **Difficulty Level**: Configurable AI search depth (default: 4)

## How to Play

1. **Installation**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Running the Game**:
   ```bash
   python project.py
   ```

3. **Gameplay**:
   - Move your mouse over the board to preview your move
   - Click to drop your piece (RED) in the selected column
   - The AI (YELLOW) automatically plays its turn
   - First player to connect 4 pieces horizontally, vertically, or diagonally wins!

## Game Architecture

### Main Game Loop (`main()`)
- Initializes Pygame and the game board
- Handles player input via mouse events
- Manages AI turn execution
- Implements win condition detection
- Displays game status and results

### Board Management
- **`create_board()`**: Creates an empty 6x7 game board
- **`drop_piece()`**: Places a piece at the specified position
- **`is_valid_location()`**: Validates column availability
- **`get_next_open_row()`**: Finds the lowest empty row in a column
- **`print_board()`**: Console output for debugging

### Graphics Rendering
- **`draw_board()`**: Renders the game board with pieces using Pygame
- Smooth circle rendering with proper coordinate mapping
- Real-time display updates

### AI Engine - Minimax Algorithm
The AI uses the minimax algorithm with alpha-beta pruning for optimal move selection:

- **`minimax()`**: Core recursive function that explores game trees to a specified depth
- **`score_position()`**: Evaluates board positions using strategic heuristics
- **`evaluate_window()`**: Scores 4-piece windows for pattern recognition
- **`is_terminal_node()`**: Detects game-ending conditions

#### Strategic Scoring
- Center column preference (×3 multiplier for piece count)
- Horizontal/vertical/diagonal pattern recognition
- Offensive scoring: rewards potential wins
- Defensive scoring: blocks opponent threats
- Draws are scored as neutral

### Win Detection
- **`winning_move()`**: Checks all possible 4-in-a-row configurations
  - Horizontal lines
  - Vertical lines
  - Positive-slope diagonals
  - Negative-slope diagonals

## Configuration

Edit these constants in `project.py` to customize gameplay:

```python
AI_DIFFICULTY = 4          # Search depth (higher = stronger AI, slower)
WINDOW_LENGTH = 4          # Winning condition (4 in a row)
MUSIC_VOLUME = 0.5         # Background music volume (0.0-1.0)
GAME_OVER_DELAY_MS = 3000  # Delay before quit after game ends (ms)
```

## Dependencies

- **pygame-ce** (2.5.0+): Graphics and audio rendering
- **numpy** (1.20.0+): Efficient board state management

## Testing

Run the unit test suite:
```bash
python -m unittest test_project
```

Tests cover:
- Board creation and piece placement
- Win condition detection (horizontal, vertical, diagonal)
- Valid location checking
- AI evaluation functions
- Game configuration validation

## Technical Details

### Algorithm Complexity
- **Time**: O(b^d) where b is branching factor (~7) and d is depth (4)
- **Space**: O(d) for recursion stack
- **Alpha-Beta Pruning**: Reduces nodes evaluated by ~50-70%

### Performance Optimizations
- Alpha-beta pruning eliminates unnecessary branches
- Board copying for state exploration
- Integer piece representation (0, 1, 2)
- NumPy arrays for efficient board operations

## Future Enhancements

- Difficulty selection UI
- Game history/replay
- Networked multiplayer
- Opening book optimization
- Transposition table caching
- Enhanced visual effects

## Author Notes

The minimax algorithm with alpha-beta pruning is the highlight of this project. It enables the AI to play optimally while maintaining responsive gameplay even at depth 4. The scoring heuristics provide strategic positioning awareness beyond simple win/loss detection.

## License

CS50P Final Project
