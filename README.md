# ChessAI
This is a basic Chess AI that utilizes a variety of data structures to help make decisions and prune the game tree of possible moves
in order to determine which move is the best for the AI given any board state. 

This program can be written more efficiently with more classes and data structures but the original contraint from the course that motivated this project imposed the writing of this program in this way.

Communication to and from the program is done through board indices according to the chessboard indices picture provided. All moves are 
given in the format of (index of piece being moved)(space)(index of the space the piece is being moved to).

Using the PlayChess function, you are able to play the program through the console and the game will be printed for you in the console as
well, however if you prefer a better viewing of the game, the moves that the program makes are also given so you can utilize an online
chess playing platform to better visualize the game. 

Using the ai_vs_ai function the program is able to play itself, however it is only for interest and does not improve by playing itself 
as no machine learning techniques are involved in the making of this AI.

The chessplayer_tree file contains the class of the tree that is utilized to generate the gametree used by the program to analyze and
prune possible moves via an optimization algorithm. The current algorithm used is Alpha-Beta pruning.

This program can be improved by having a better evaluation function that can allow the program to distinguish boardstates on a more detailed level in order to better decide which move is the best option. Furthermore, the pruning algorithm implemented is not perfect and can definitely be optimized for faster calculation times. 
