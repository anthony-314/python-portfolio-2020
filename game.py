def ask_yes_no(question):
    """ Ask a yes no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Ask for a number within a range"""
    response = None
    while response not in range(low, high):
        try:
            response + int(input(question))
        except:
            print("not good answer")
    return response

def get_Name(question):
    name = ""
    while name == "":
        try:
            name = input(question)
        except:
            print("something went wrong")
        return name

class Player(object):
    """A player for a game"""
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep


def switchTurn(turn):
    """Switches the turn between players chooses whether it is you turn or not."""
    if turn == 0:
        turn = 1
        notturn =0
    else:
        turn = 0
        notturn = 1
    return turn, notturn