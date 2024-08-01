# Tic-Tac-Toe game
# OIT Code Challenge
# Alyce Rios

import random

# Welcome the user to the game and ask them whether or not they want to go first
def welcome():
    print("Welcome to Tic-Tac-Toe game!")
    while True:
        choice = input("Do you want to go first? (yes/no): ").lower()
        if choice in ['yes', 'no']:
            break
        # Handle exceptions
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    
    # The following return statement checks if the user wants to go first.
    return choice == 'yes'

# Print the board's state to the terminal.
# The board is displayed in a 3x3 grid format with columns separated by ' | '.
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

# Start a new game board.
def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

# Check whether a move is valid or not.
# True if cells is empty, false if not.
def is_valid_move(board, row, col):
    return board[row][col] == " "

# Place a move on the board for user or computer.
def make_move(board, row, col, player):
    board[row][col] = player

# Check if the player has won the game.
# True if the player has won, false if not. 
def check_win(board, player):
    win_conditions = [
        # Horizontal
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # Vertical
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # Diagonal
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    return any(all(board[row][col] == player for row, col in condition) for condition in win_conditions)

# Check if the game is a tie: the board is full, but there is no winner.
# True if game is a tie, false if not. 
def check_tie(board):
    return all(cell != " " for row in board for cell in row)

# Prompt the user to make a move, returns their chosen row and column.
def player_move(board):
    while True:
        try:
            # Prompt the user to input a row and a column and adjust for 0-based index
            row = int(input("Enter the row (1-3): ")) - 1
            col = int(input("Enter the column (1-3): ")) - 1

            # Check if the move is within the board limits and if the chosen cell is empty
            if (0 <= row < 3) and (0 <= col < 3):
                if is_valid_move(board, row, col):
                    return row, col
            # Handle exceptions
                else:
                    print("Invalid move. The position is already taken by the computer. Please try again.")
            else:
                print("Invalid move. Position is out of range. Please enter row and column between 1 and 3.")
        except ValueError:
            print("Please enter numbers only.")

# Select a random available move for the computer ('0').
def computer_move(board):
    # Generate a list of available moves based on the board state
    available_moves = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    # Randomly choose one of the available moves and display it on the board
    return random.choice(available_moves)

# Main function to run the Tic-Tac-Toe game in the console.
def main():
    # Initialize the board, assigns symbols to players.
    while True:
        board = initialize_board()
        player = 'X'
        computer = 'O'
        
        # Run the welcome function
        player_turn = welcome()

        # Inform the user of their symbol and the computer's symbol
        print(f"You are '{player}' and the computer is '{computer}'")
        
        if player_turn:
            # Display the board if the player goes first
            display_board(board)

        # Run the game
        while True:
            if player_turn:
                print("Your turn.")
                row, col = player_move(board)
                make_move(board, row, col, player)
                if check_win(board, player):
                    display_board(board)
                    print("Congratulations! You win!")
                    break
                player_turn = False
            else:
                print("Computer's turn.")
                row, col = computer_move(board)
                make_move(board, row, col, computer)
                if check_win(board, computer):
                    display_board(board)
                    print("Computer wins!")
                    break
                player_turn = True

            # Display the board after the computer makes its move
                display_board(board)
            
            # Run the check_tie function to check for a tie
            if check_tie(board):
                display_board(board)
                print("It's a tie!")
                break
        
        # Ask if the user wants to play again
        while True:
            try:
                play_again = input("Do you want to play again? (yes/no): ").lower()
                if play_again not in ['yes', 'no']:
                    raise ValueError("Invalid input. Please enter 'yes' or 'no'.")
                if play_again == 'yes':
                    break  # Exit the inner while loop to start a new game
                else:
                    print("Thanks for playing! Come back another time")
                    return  # Exit the main function to end the game
            except ValueError as e:
                print(e)

# Ensure the main function runs
if __name__ == "__main__":
    main()

# I spent 1 hour and 30 minutes creating this code for the "Tic-Tac-Toe" OIT Application Engineering Code Challenge