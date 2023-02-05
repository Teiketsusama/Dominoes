import random


def generate_domino() -> list:
    random_set = []
    for i in range(0, 7):
        for j in range(i, 7):
            random_set.append([i, j])
    random.shuffle(random_set)
    return random_set


def split_domino(random_set: list) -> (list, list, list):
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


def domino_double(lst: list) -> bool:
    lst_double = []
    for sublist in lst:
        if sublist[0] == sublist[1]:
            lst_double.append(sublist)
    if len(lst_double) == 0:
        return False
    else:
        return True


def best_starting_piece(lst: list) -> (int, list):
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


def player_status(piece1: list, piece2: list) -> (int, list):
    chosen_piece = []
    turn = 0
    if max(piece1) > max(piece2):
        chosen_piece = piece1
        turn += 1
    elif max(piece1) < max(piece2):
        chosen_piece = piece2
    return turn, chosen_piece


def print_header():
    header = 70 * "="
    print(header)


def print_first_last_three_elements(lst: list):
    n = len(lst)
    if n > 6:
        print("{}".format("".join(map(str, lst[:3]))), end="")
        print("...{}".format("".join(map(str, lst[-3:]))))
    else:
        for sublist in lst:
            print("[{}]".format(", ".join(map(str, sublist))), end="")


# A player cannot add a domino to the end of the snake if it doesn't contain the matching number.
def illegal_move(list1: list, sublist: list, num: int) -> bool:
    if num > 0:
        if list1[len(domino_snake) - 1][1] not in sublist:
            return False
        else:
            return True
    elif num < 0:
        if list1[0][0] not in sublist:
            return False
        else:
            return True


# The orientation of the newly added domino ensures that the matching numbers are neighbors.
def make_a_move(lst: list, sublist: list, num: int) -> list:
    if num > 0:
        lst.append(sublist)
        if lst[len(lst) - 2][1] != lst[len(lst) - 1][0]:
            lst[len(lst) - 1] = list(reversed(lst[len(lst) - 1]))
    elif num < 0:
        lst.insert(0, sublist)
        if lst[0][1] != lst[1][0]:
            lst[0] = list(reversed(lst[0]))

    return lst


# The numbers on the ends of the snake are identical and appear within the snake 8 times.
def draw_condition(lst: list) -> int:
    count = 1
    if lst[0][0] == lst[len(lst) - 1][1]:
        for sublist in lst:
            if lst[0][0] in sublist:
                count += 1
    return count


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

    turns = ["Computer is about to make a move. Press Enter to continue...",
             "It's your turn to make a move. Enter your command."]
    turn_index, max_piece = player_status(computer_best_piece, player_best_piece)
    if turn_index == 1:
        computer_pieces.remove(max_piece)
    elif turn_index == 0:
        player_pieces.remove(max_piece)

    domino_snake = [max_piece]

    # Interface
    while (len(computer_pieces) > 0 and len(player_pieces) > 0) \
            or draw_condition(domino_snake) < 8:
        print_header()
        print("Stock size: {}".format(len(stock_pieces)))
        print("Computer pieces: {}".format(len(computer_pieces)))
        print()
        print_first_last_three_elements(domino_snake)
        print()
        print("\nYour pieces:")
        i = 0
        for player_piece in player_pieces:
            i += 1
            print("{}:{}".format(i, player_piece))
        print()

        # End-game condition
        if len(computer_pieces) == 0:
            print("Status: The game is over. The computer won!")
            break
        elif len(player_pieces) == 0:
            print("Status: The game is over. You won!")
            break
        elif draw_condition(domino_snake) >= 8:
            print("Status: The game is over. It's a draw!")
            break
        elif len(stock_pieces) == 0:
            if (not illegal_move(domino_snake, new_snake, input_num)) and (not illegal_move(domino_snake, new_snake, computer_num)):
                print("Status: The game is over. It's a draw!")
                break

        if turn_index % 2 == 1:
            invalid_input = False
            while not invalid_input:
                user_input = input("Status: {}\n".format(turns[turn_index % 2]))
                if user_input == "":
                    print("Invalid input. Please try again.")
                    continue
                try:
                    input_num = int(user_input)
                except ValueError:
                    print("Invalid input. Please try again.")
                    continue
                if abs(input_num) > len(player_pieces):
                    print("Invalid input. Please try again.")
                    continue

                if input_num != 0:
                    new_snake = player_pieces[abs(input_num) - 1]
                    if not illegal_move(domino_snake, new_snake, input_num):
                        print("Illegal move. Please try again.")
                        continue
                    player_pieces.remove(new_snake)
                    domino_snake = make_a_move(domino_snake, new_snake, input_num)
                    invalid_input = True

                elif input_num == 0:
                    if len(stock_pieces) > 0:
                        domino_choice = random.choice(stock_pieces)
                        stock_pieces.remove(domino_choice)
                        player_pieces.append(domino_choice)
                        invalid_input = True
                    else:
                        break

        elif turn_index % 2 == 0:
            input("Status: {}\n".format(turns[turn_index % 2]))
            for computer_num in range(- (len(computer_pieces) - 1), len(computer_pieces)):
                if computer_num != 0:
                    new_snake = computer_pieces[abs(computer_num) - 1]
                    if illegal_move(domino_snake, new_snake, computer_num):
                        computer_pieces.remove(new_snake)
                        domino_snake = make_a_move(domino_snake, new_snake, computer_num)
                        break
                elif computer_num == 0:
                    if len(stock_pieces) > 0:
                        domino_choice = random.choice(stock_pieces)
                        stock_pieces.remove(domino_choice)
                        computer_pieces.append(domino_choice)
                    break

        turn_index += 1
