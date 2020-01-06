# Anthony Peraza
#Tic Tac Toe
#11/19

#global constants
X = "x"
O ="o"
NUM_SQUARES = 9
TIE = "TIE"
EMPTY = " "

def instructions():
    """Display game instructions."""
    print(
    """
    Welcome to the greatest test of minds the world has ever seen.

    You will make your move know by entering a number, 1-9. The number
    will correspond to the board position as illustrated:

                1 ! 2 ! 3
                ---------
                4 ! 5 ! 6
                ---------
                7 ! 8 ! 9
    Ready begin""")

# tested
def ask_yes_no(qustion):
    """Ask a Yes or no question and give a one letter reponse back"""
    response = None
    while response not in ("y","n"):
        response = input(question).lower()
    x = response[0]
    
    return response

def new_board():
    board = []
    for i in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    print(str.format("""

                {0} ! {1} ! {2}
                ---------
                {3} ! {4} ! {5}
                ---------
                {6} ! {7} ! {8}
                """,board[0],board[1],board[2],
                             board[3],board[4],
                             board[5],board[6],
                             board[7],board[8]))
board = new_board()

display_board(board)

def pieces():
    go_first = ask_yes_no("do you really need the first questions?")
    if go_first == "y":
        print("\n you won't win")
        human = X
        comp = O
    else:
        print("\nYOUR Goog luck and GG")
        comp = X
        human = O
    return comp, human
def ask_number(question, low, high):
    response = None
    while respnse not in range(low,high):
        response = input(question)
        if response.isdigit():
            response = int(response)
    return response
    

def game():
    pass



                
