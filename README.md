# Chess Game (Python-Java)
Project to create a Chess game using Python for the engine, connected to Java for the GUI.
* The moves are made in python by methods on the controller object 'player' - e.g. 'player.move("a8", "a7")'.
* If the move is unsuccessful (illegal move) then an error is thrown in python.
* After each successful move the unique board position is exported in JSON format along with other game data
  such as positions of the pieces.
* The java GUI parses this JSON information and uses it to set the piece positions on the board.
* When a move is made on the GUI by clicking and dragging a piece, the move command gets sent to
  python in the form above.
* The move is then performed by python and a new board position is returned if the move was
  successful, which the Java GUI then reads and loads the piece positions from.
* If the move was unsuccessful (illegal move) then the Java GUI will reload the board position
    we just tried to move from.


## Improvements to Gameplay:
### Implemented:
* Moving and taking with all pieces
* Castling
* Check
* Checkmate
* Stalemate
* Pawn promotion
* EnPassant
* Three fold repetition

### Needs further testing:
* Pawn promotion
* En Passant
* Castling out of check
* Moving Kings next to each other

## Improvements to Code:
### Python:
* Make sure all static methods are called on classes not instances
* Split up into smaller files (e.g. setting pieces classes, moving classes etc)
### Java:
* Too many getters and setters in some cases.
### General:
* Tidying up of code
* Removing unnecessary print statements
* Better representation of data in a single data structure (ie for board positions/piece properties e.g. colour, position etc)
