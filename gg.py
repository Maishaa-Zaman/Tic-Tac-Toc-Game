import tkinter as tk
from tkinter import messagebox
import math

# Constants for the game
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

class TicTacToe:
    def __init__(self, mode="Human vs Computer"):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe with Minimax and Alpha-Beta Pruning")
        self.board = [[EMPTY for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = PLAYER_X  # X always starts
        self.mode = mode  # Game mode: "Human vs Computer" or "Computer vs Computer"
        self.create_board()

        # Start Computer vs. Computer automatically if selected
        if self.mode == "Computer vs Computer":
            self.window.after(500, self.computer_vs_computer)

    def create_board(self):
        """Create the GUI board with buttons."""
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(
                    self.window,
                    text=' ',
                    font=('Arial', 50),
                    height=2,
                    width=5,
                    command=lambda r=row, c=col: self.on_click(r, c)
                )
                self.buttons[row][col].grid(row=row, column=col)

    def on_click(self, row, col):
        """Handle button click for human player in Human vs. Computer mode."""
        if self.board[row][col] == EMPTY and self.current_player == PLAYER_X:
            self.board[row][col] = PLAYER_X
            self.buttons[row][col].config(text=PLAYER_X)
            if self.is_game_over():
                return
            self.current_player = PLAYER_O
            self.window.after(500, self.ai_move)  # Delay AI move for better UX

    def ai_move(self):
        """Make the AI move using minimax with alpha-beta pruning."""
        best_score = -math.inf
        best_move = None

        for row in range(3):
            for col in range(3):
                if self.board[row][col] == EMPTY:
                    self.board[row][col] = self.current_player
                    score = self.minimax(self.board, 0, -math.inf, math.inf, False)
                    self.board[row][col] = EMPTY
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

        if best_move:
            row, col = best_move
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.is_game_over():
                return
            self.current_player = PLAYER_X if self.current_player == PLAYER_O else PLAYER_O

            # Automatically trigger the next move if it's Computer vs Computer
            if self.mode == "Computer vs Computer":
                self.window.after(500, self.computer_vs_computer)

    def computer_vs_computer(self):
        """Automate moves for both players in Computer vs. Computer mode."""
        if not self.is_game_over():
            self.ai_move()

    def minimax(self, board, depth, alpha, beta, maximizing_player):
        """Minimax algorithm with alpha-beta pruning."""
        if self.check_winner(PLAYER_X):
            return -10 + depth
        if self.check_winner(PLAYER_O):
            return 10 - depth
        if self.is_draw():
            return 0

        if maximizing_player:
            max_eval = -math.inf
            for row in range(3):
                for col in range(3):
                    if board[row][col] == EMPTY:
                        board[row][col] = PLAYER_O
                        eval = self.minimax(board, depth + 1, alpha, beta, False)
                        board[row][col] = EMPTY
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
            return max_eval
        else:
            min_eval = math.inf
            for row in range(3):
                for col in range(3):
                    if board[row][col] == EMPTY:
                        board[row][col] = PLAYER_X
                        eval = self.minimax(board, depth + 1, alpha, beta, True)
                        board[row][col] = EMPTY
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
            return min_eval

    def is_game_over(self):
        """Check if the game is over (win or draw)."""
        if self.check_winner(PLAYER_X):
            messagebox.showinfo("Game Over", "Player X wins!")
            self.reset_game()
            return True
        if self.check_winner(PLAYER_O):
            messagebox.showinfo("Game Over", "Player O wins!")
            self.reset_game()
            return True
        if self.is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_game()
            return True
        return False

    def check_winner(self, player):
        """Check if the given player has won the game."""
        # Check rows, columns, and diagonals
        for row in range(3):
            if all(self.board[row][col] == player for col in range(3)):
                return True
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        """Check if the game is a draw."""
        return all(self.board[row][col] != EMPTY for row in range(3) for col in range(3))

    def reset_game(self):
        """Reset the game to its initial state."""
        self.board = [[EMPTY for _ in range(3)] for _ in range(3)]
        self.current_player = PLAYER_X
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=' ')

    def run(self):
        """Run the main event loop."""
        self.window.mainloop()


# Select game mode and start the game
if __name__ == "__main__":
    mode = messagebox.askquestion("Game Mode", "Do you want Computer vs Computer mode? (Click 'Yes' for Computer vs Computer, 'No' for Human vs Computer)")
    if mode == 'yes':
        game = TicTacToe(mode="Computer vs Computer")
    else:
        game = TicTacToe(mode="Human vs Computer")
    game.run()