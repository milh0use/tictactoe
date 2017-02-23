board = [['.','.','.'],['.','.','.'],['.','.','.']]
players = [{"name": "player1", "token": "o"},{"name": "player2", "token": "x"}]

def add_move(player,position):
    global board
    (x,y) = position.split(",")
    x = int(x)
    y = int(y)
    cell = board[x][y]
    if cell != '.':
        print "Nope! Already contains a ", cell
        return False
    board[x][y] = player['token']
    return True

def get_move(player):
    prompt = "Enter your move, "+player['name']+":"
    move = raw_input(prompt)
    return move

def print_board():
    global board
    board_string = ''
    for row in board:
        for cell in row:
            board_string += cell
        board_string += "\n"
    print board_string

print_board();
player_up = 0;

while 1:
    player = players[player_up]
    outcome = add_move(player,get_move(player))
    if outcome == False:
        continue
    print_board()
    if player_up == 0:
        player_up = 1
    else:
        player_up = 0