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
> Stage 4
-  When it's a player's turn, the program should:
- [x] Verify that the move entered by the player is legal (requirement #1).
If not, request a new input with the following message: Illegal move. Please try again..
- [x] Place dominoes with the correct orientation (requirement #2).
> Requirements 
> 1. A player cannot add a domino to the end of the snake if it doesn't contain the matching number.
> 2. The orientation of the newly added domino ensures that the matching numbers are neighbors.
- When it's a computer's turn, the program should:
- [x] Try random moves until it finds a legal one.
- [x] Place dominoes with the correct orientation.
> Stage 5
- The AI should use the following algorithm to calculate the score:
1. Count the number of 0's, 1's, 2's, etc., in your hand, and in the snake.
2. Each domino in your hand receives a score equal to the sum of appearances of each of its numbers.
> The AI will now attempt to play the domino with the largest score, trying both the left and the right sides of the snake. If the rules prohibit this move, the AI will move down the score list and try another domino. The AI will skip the turn if it runs out of options.
- [x] Replace the random move generator with the algorithm described above.
