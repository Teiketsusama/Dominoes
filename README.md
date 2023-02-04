# Dominoes
> Stage 1
- [X] **Generate a full domino set.** Each domino is represented as a list of two numbers. A full domino set is a list of 28 unique dominoes.
- [X] **Split the full domino set between the players and the stock by random.** 
You should get three parts: Stock pieces (14 domino elements), Computer pieces (7 domino elements), and Player pieces (7 domino elements).
- [X] **Determine the starting piece and the first player.** Modify the parts accordingly. 
You should get four parts with domino pieces and one string indicating the player that goes first: either "player" or "computer".
If the starting piece cannot be determined (no one has a double domino), reshuffle, and redistribute the pieces (step 3).
- [X] Output all five variables.
> Stage 2
- [x] Interface
> Stage 3
- [x] At the end of the game, print one of the following phrases:
Status: The game is over. You won!
Status: The game is over. The computer won!
Status: The game is over. It's a draw!
- [x] Print only the first and the last three pieces of the domino snake separated by three dots if it exceeds six dominoes in length.
- [x] Add a game loop that will repeat the following steps until the game ends:
- Display the current playing field.
- If it's a user's turn, prompt the user for a move and apply it. If the input is invalid (its value is not-integer or it exceeds limitations), request a new input with the following message: Invalid input. Please try again..
- If it's a computer's turn, prompt the user to press Enter, randomly generate a move, and apply it.
- Switch turns.
