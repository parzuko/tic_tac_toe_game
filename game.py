# --------------------Global Variables-----------------

# Game board
board = ['-','-', '-',
        '-', '-', '-',
        '-', '-', '-',]

# If game still going 
game_is_still_going = True

#Who won? or tie??
winner = None 

#Who's Player One 
current_player = "X"


#-----------------FUNCTIONS-----------------

# Play a game of tic tac toe
def play_game() :
    # Displaying Initial Board
    display_board()

    # literally while the game is still going
    while game_is_still_going :

        # Handle turn of a single arbitrary player 
        handle_turn(current_player)

        # Checking if game is over 
        check_if_game_over()

        # flipping the turn
        flip_player()

        # The game has ended 
    if winner == "X" or winner == "O":
        print(winner + "  WON!")
    elif winner == None:
        print("It's a tie :(((((")

def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")

def handle_turn(player):

  # Get position from player
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  valid = False
  while not valid :

    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Choose a position from 1-9: ")


    position = int(position) - 1

    if board[position] == '-':
        valid = True
    else:
        print("You cant do that. Retry")

    board[position] = player
    display_board() 

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
      # Set global variables
  global winner
  # Check if there was a winner anywhere
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  # Get the winner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None

def check_rows():
      # Set global variables
  global game_is_still_going
  # Check if any of the rows have all the same value (and is not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_is_still_going = False
  # Return the winner
  if row_1:
    return board[0] 
  elif row_2:
    return board[3] 
  elif row_3:
    return board[6] 
  # Or return None if there was no winner
  else:
    return None

def check_columns():
      # Set global variables
  global game_is_still_going
  # Check if any of the columns have all the same value (and is not empty)
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_is_still_going = False
  # Return the winner
  if column_1:
    return board[0] 
  elif column_2:
    return board[1] 
  elif column_3:
    return board[2] 
  # Or return None if there was no winner
  else:
    return None

def check_diagonals():
      # Set global variables
  global game_is_still_going
  # Check if any of the columns have all the same value (and is not empty)
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  # If any row does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_is_still_going = False
  # Return the winner
  if diagonal_1:
    return board[0] 
  elif diagonal_2:
    return board[2]
  # Or return None if there was no winner
  else:
    return None

def check_if_tie():
    global game_is_still_going
    if "-" not in board :
        game_is_still_going = False
    else:
        return False

def flip_player():
    #global variables we need 
    global current_player
    # If current player was X we switch to 0
    if current_player == "X":
        current_player = '0'
    # vice versa
    elif current_player == "0":
        current_player = 'X'

# ------------ Start Execution -------------
# Play a game of tic tac toe
play_game()
