import random


def generate_domino():
    random_set = []
    for i in range(0, 7):
        for j in range(i, 7):
            random_set.append([i, j])
    random.shuffle(random_set)
    return random_set


def split_domino(random_set):
    player1 = []
    player2 = []
    for i in range(14):
        if i % 2 == 0:
            choice = random.choice(random_set)
            player1.append(choice)
            random_set.remove(choice)
        else:
            choice = random.choice(random_set)
            player2.append(choice)
            random_set.remove(choice)
    return random_set, player1, player2


def domino_double(lst):
    lst_double = []
    for sublist in lst:
        if sublist[0] == sublist[1]:
            lst_double.append(sublist)
    if len(lst_double) == 0:
        return False
    else:
        return True


def best_starting_piece(lst):
    best_index = None
    best_piece = [-1, -1]
    for i in range(len(lst)):
        compare_piece = lst[i]
        if compare_piece[0] == compare_piece[1]:
            best_max = max(best_piece)
            compare_max = max(compare_piece)
            if compare_max > best_max:
                best_index = i
                best_piece = compare_piece
    return best_index, best_piece


def player_status(piece1, piece2):
    chosen_piece = []
    counter = 0
    if max(piece1) > max(piece2):
        chosen_piece = piece1
        counter += 1
    elif max(piece1) < max(piece2):
        chosen_piece = piece2
    return counter, chosen_piece


def print_header():
    header = 70 * "="
    print(header)


if __name__ == "__main__":
    while True:
        domino_set = generate_domino()
        stock_pieces, computer_pieces, player_pieces = split_domino(domino_set)

        computer_double = domino_double(computer_pieces)
        player_double = domino_double(player_pieces)

        if computer_double is not False or player_double is not False:
            break

    computer_best_index, computer_best_piece = best_starting_piece(computer_pieces)
    player_best_index, player_best_piece = best_starting_piece(player_pieces)

    status = ["Computer is about to make a move. Press Enter to continue...",
              "It's your turn to make a move. Enter your command."]
    status_index, max_piece = player_status(computer_best_piece, player_best_piece)
    if status_index == 1:
        computer_pieces.remove(max_piece)
    elif status_index == 0:
        player_pieces.remove(max_piece)

    # Display
    print_header()
    print("Stock size: {}".format(len(stock_pieces)))
    print("Computer pieces: {}".format(len(computer_pieces)))
    print()
    print(max_piece)
    print()
    print("Your pieces:")
    i = 0
    for player_piece in player_pieces:
        i += 1
        print("{}:{}".format(i, player_piece))
    print("Status: {}".format(status[status_index]))
