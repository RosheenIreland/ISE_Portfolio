def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print("\t_____|_____|_____")

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print('\t     |     |     ')
    print("\n")


# Function to print scoreboard
def print_scoreboard(score_board):
    print("\t------------------------")
    print("\t       SCOREBOARD       ")
    print("\t------------------------")

    players = list(score_board.keys())
    print("\t  ", players[0], "\t   ", score_board[players[0]])
    print("\t  ", players[1], "\t   ", score_board[players[1]])

    print("\t------------------------\n")

# Function to check if any player has won

def check_win(player_pos, cur_player):

    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    # Loop to check if any winning combo is satisfied
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):

            # Returns True if any winning combination satisfies
            return True
    # If no combinations satisfie
    return False


# Function to check for draw
def check_draw(player_pos):
    if len(player_pos["X"]) + len(player_pos["O"]) == 9:
        return True
    return False

# Function for a single game
def single_game(cur_player):

    values = [' ' for x in range(9)]

    player_pos = {'X':[], 'O':[]}

    while True:
        print_tic_tac_toe(values)

        try:
            print("Player ", cur_player, " turn. Which box? :", end="")
            move = int(input())
        except ValueError:
            print("Wrong Input! Try Again!")
            continue

        if move < 1 or move > 9:
            print("Wrong Input! Try Again!")
            continue

       # CHeck if the box is occupied
        if values[move-1] != ' ':
            print("Place already filled. Try again!")
            continue

        # Updating grid status
        values[move-1] = cur_player

        player_pos[cur_player].append(move)

        # Function to call for checking winner
        if check_win(player_pos, cur_player):
            print_tic_tac_toe(values)
            print("Player", cur_player, " has won the game!")
            print("\n")
            return cur_player

        # Function to call for checking draw game
        if check_draw(player_pos):
            print_tic_tac_toe(values)
            print("It's a tie!")
            print("\n")
            return 'D'

        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'

if __name__ == "__main__":

    print("Player 1")
    player1 = input("Enter your name :")
    print("\n")

    print("Player 2")
    player2 = input("Enter your name :")
    print("\n")

    cur_player = player1
    

    # Stores the name choice of player
    player_choice = {'X' : "", 'O' : ""}

    # Stores the options
    options = ['X', 'O']

    # Stores the scoreboard
    score_board = {player1: 0, player2: 0}
    print_scoreboard(score_board)


    #Game loop for a series of Tic Tac Toe
    # The loop runs until the player quits
    while True:

        # Player choice menu
        print("Turn to choose for", cur_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit")

        # -Try- exception for CHOICE input
        try:
            choice = int(input())
        except ValueError:
            print("Wrong Input! Try Again\n")
            continue

        # Conditions for player choice
        if choice == 1:
            player_choice['X'] = cur_player
            if cur_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['0'] = player1

        elif choice == 2:
            player_choice['O'] = cur_player
            if cur_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1
            
        elif choice == 3:
            print("Final Scores")
            print_scoreboard(score_board)
            break

        else:
            print("Wrong Choice! Ty Again!\n")

        # Stores the winner in a single game
        winner = single_game(options[choice-1])

        # Edits the scoreboard according to the winner
        if winner != 'D' :
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1

        print_scoreboard(score_board)
        # Switch player who chooses x or O
        if cur_player == player1:
            cur_player = player2
        else:
            cur_player = player1

    

    