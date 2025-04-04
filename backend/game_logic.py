class TicTacToeGame:
    def __init__(self): # Constructor for class TicTacToeGame. 'self' refers to the specific object being created
        self.reset() # Calls reset() function so that when a new game is created, everything is immediately set up like a fresh, empty game board

    # This method is to reset the game
    def reset(self): # self refers to the specific game object we're working with
        # Create a 3x3 board of empty strings
        self.board = [["" for _ in range(3)] for _ in range(3)] # setting variable to this double for loop, array of 3 inside array of three [["" "" ""], ["" "" ""], ["" "" ""]]
        self.winner = None # reseting winner title to no one since it's a new game
        self.is_draw = False # Since the game just started, we don't know yet if it's a draw


    def make_move(self, row, col, player):
        if self.winner or self.is_draw:
            return {"error": "Game is already over", "board": self.board} # You can't make anymore moves if the game is over

        if self.board[row][col] != "":
            return {"error": "Cell already taken", "board": self.board} # Can't make a move if that spot is already taken
        
        # Now we know that we can make a move so lets assign this spot to the player
        self.board[row][col] = player

        if self.check_winner(player): # calls a function that checks to see if this player won when the player makes a new move
            self.winner = player # setting the winner variable to this player
            return {"message": f"{player} wins!", "board": self.board, "winner": self.winner} # Returning message that this player won
        
        elif self.check_draw(): # Calls function that checks to see if the game is completed with a draw
            self.is_draw = True # is_draw variable is set to true if the function returns true
            return {"message": "Draw!", "board": self.board, "is_draw": self.is_draw} # Returning a message that the game ended with a draw
        
        else:
            return {"message": "Move accepted", "board": self.board} # This returns the messagde that the spot has been assigned to the player
            
    
    def check_winner(self, player):
        b = self.board # setting the current board to the b variable
        
        # Check rows, columns, and diagonals
        for i in range(3): # loops three times

            if all(b[i][j] == player for j in range(3)):  # It checks of player is in a all horizontal spots for each row
                return True
            
            if all(b[j][i] == player for j in range(3)):  # It checks if player is in all vertical spots for each column
                return True
            
        if all(b[i][i] == player for i in range(3)):      # It checks to see if player is in positions 00, 11, 22 which makes a main diagonal
            return True
        
        if all(b[i][2 - i] == player for i in range(3)):  # It checks to see if player is in positions 02, 11, 20 which makes an anti-diagonal
            return True
        
        return False # If none of these are the case then the player is not a winner yet
    

    # Checks to see if the game ended in a draw
    def check_draw(self):
        # If there are no empty cells and no winner, it's a draw
        for row in self.board: # Moves through each row in the board
            if "" in row: # The board needs to be complete in order to determine if there's a draw
                return False # If there's there's still moves left to make, then it's not a draw
        return self.winner is None # Since we didn't find any empty spots, then the board is full which means the game is over and we can declare 
                                   # that there's no winner