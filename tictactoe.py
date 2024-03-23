
X = 'X'  
O = 'O'  
EMPTY = ' '


def display_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[i*3], "|", board[i*3 + 1], "|", board[i*3 + 2], "|")
        print("-------------")


def game_over(board):
    
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != EMPTY:
            return True
        if board[i*3] == board[i*3+1] == board[i*3+2] != EMPTY:
            return True
    if board[0] == board[4] == board[8] != EMPTY:
        return True
    if board[2] == board[4] == board[6] != EMPTY:
        return True
    
    
    if EMPTY not in board:
        return True
    
    return False


def ai_move(board):
    
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = O
            break


def human_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == EMPTY:
                board[move] = X
                break
            else:
                print("Invalid move. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def play_game():
    
    board = [EMPTY] * 9
    
    
    while not game_over(board):
        display_board(board)
        
        
        human_move(board)
        if game_over(board):
            break
        
        ai_move(board)
    
    display_board(board)
    if X in board:
        print("Congratulations! You win!")
    elif O in board:
        print("AI wins!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    play_game()
