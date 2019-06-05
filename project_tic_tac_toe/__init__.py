my_list = [" " for x in range(1, 11)]
my_list[0] = "None"


def print_board():
    print(f"""    
     |   |
  {my_list[1]}  | {my_list[2]} | {my_list[3]}
     |   |
------------------
     |   |
  {my_list[4]}  | {my_list[5]} | {my_list[6]}
     |   |
------------------
     |   |
  {my_list[7]}  | {my_list[8]} | {my_list[9]}
     |   |
""")


def draw_symbol(symbol, location):
    if symbol == "O":
        my_list[location] = "O"
        print_board()
    elif symbol == "X":
        my_list[location] = "X"
        print_board()


def show_menu():
    global player2_symbol
    global player1_symbol
    player1_symbol = input("First Player:What do you want 'X' or 'O':")
    if player1_symbol == "X":
        player2_symbol = "O"
    elif player1_symbol == "O":
        player2_symbol = "X"
    else:
        print("Please enter a valid option:")
        show_menu()


def check_if_draw():
    is_draw = True

    for letter in my_list:
        if letter == " ":
            is_draw = False
            break
    if is_draw:
        print("Draw!")
        exit()


def try_for_location(symbol):
    if symbol == player1_symbol:
        location = ask_player_for_position(player1_symbol)
        check_location(player1_symbol, location)
    elif symbol == player2_symbol:
        location = ask_player_for_position(player2_symbol)
        check_location(player2_symbol, location)


def check_location(symbol, location):
    if my_list[location] == "X" or my_list[location] == "O":
        print("Sorry cannot draw symbol at that location, as other player may have drawn symbol there")
        try_for_location(symbol)
    else:
        draw_symbol(symbol, location)
        check_if_won()


def ask_player_for_position(symbol):
    if symbol == player1_symbol:
        return int(input("Enter location for player1:"))
    else:
        return int(input("Enter location for player2:"))


def play_tic_tac_toe():
    while True:
        try_for_location(player1_symbol)
        try_for_location(player2_symbol)


def check_if_player_won(symbol, start, end, step=1):
    player_winning = False
    for i in my_list[start:end:step]:
        if i == symbol:
            player_winning = True
        else:
            player_winning = False
            break
    if symbol == player1_symbol:
        if player_winning:
            print("Player 1 won")
            exit()
    elif symbol == player2_symbol:
        if player_winning:
            print("Player 2 won")
            exit()


def check_if_won():
    check_if_draw()
    check_if_player_won(player1_symbol, 1, 4)
    check_if_player_won(player1_symbol, 4, 7)
    check_if_player_won(player1_symbol, 7, 10)
    check_if_player_won(player1_symbol, 3, 8, 2)
    check_if_player_won(player1_symbol, 1, 10, 4)

    check_if_player_won(player2_symbol, 1, 4)
    check_if_player_won(player2_symbol, 4, 7)
    check_if_player_won(player2_symbol, 7, 10)
    check_if_player_won(player2_symbol, 3, 8, 2)
    check_if_player_won(player2_symbol, 1, 10, 4)


show_menu()
play_tic_tac_toe()
