def gamestate(board):
    """
    Docstring for gamestate
    
    :param board: [str] - 3 strings representing each row of the tic tac toe board
    Returns 'win' if O or X has won, 
    Returns 'draw' if it's a draw,
    Returns 'ongoing' if the game is not over yet
    """
    x_pos = []
    o_pos = []
    xwin = False
    owin = False

    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                x_pos.append((row,col))
            if board[row][col] == "O":
                o_pos.append((row,col))

    if len(o_pos) > len(x_pos):
        raise ValueError("Wrong turn order: O started")
    
    # If there are > 1 X's than O's, X went twice
    if len(x_pos) > len(o_pos) + 1:
        raise ValueError("Wrong turn order: X went twice")
    
    # Check if X has won

    # Check if one of the rows is all X's
    for row in range(3):
        if all((row,col) in x_pos for col in range(3)):
            xwin = True
    # Check if one of the columns is all X's
    for col in range(3):
        if all((row,col) in x_pos for row in range(3)):
            xwin = True
    # Check if top-left to bottom-right diagonal is all X's
    if all((index,index) in x_pos for index in range(3)):
        xwin = True
    # Check if top-right to bottom-left diagonal is all X's
    if all((index,2-index) in x_pos for index in range(3)):
        xwin = True

    # Check if O has won

    # Check if one of the rows is all O's
    for row in range(3):
        if all((row,col) in o_pos for col in range(3)):
            owin = True
    # Check if one of the columns is all O's
    for col in range(3):
        if all((row,col) in o_pos for row in range(3)):
            owin = True
    # Check if top-left to bottom-right diagonal is all O's
    if all((index,index) in o_pos for index in range(3)):
        owin = True
    # Check if top-right to bottom-left diagonal is all O's
    if all((index,2-index) in o_pos for index in range(3)): 
        owin = True
    
    # If all boxes are filled and no one won, it is a draw
    if len(o_pos) == 4 and len(x_pos) == 5 and not xwin and not owin:
        return "draw"
    
    # If both X and O won, it is an impossible board
    if xwin and owin:
        raise ValueError("Impossible board: game should have ended after the game was won")
    
    if xwin or owin:
        return "win"

    return "ongoing"
    