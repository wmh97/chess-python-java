class Board():
       
        def __init__(self, dimensions):
                self.dimensions = dimensions
                self.board = self._generate_board(
                        self.dimensions
                )
                #self._print_board()
               
        @staticmethod
        def _board_range(section):
                return [index+1
                        for index in range(0,section)]
               
        @property
        def dimensions(self):
                return self._dimensions
               
        @dimensions.setter
        def dimensions(self, value):
                return self._set_dimensions(value)
               
        def _set_dimensions(self, dimensions):
                if not isinstance(dimensions, list):
                        raise TypeError("List Required")
               
                if len(dimensions) != 2:
                        raise ValueError("Must be 2D")
               
                if not all(
                        isinstance(dimension, int)
                        for dimension in dimensions
                ):
                        raise TypeError("Need Numbers")
               
                self._dimensions = dimensions
                return self._dimensions
       
        def _print_board(self):
                for row in self.board:
                        print(" ".join(row))
               
        def _generate_board(self, dimensions):
                width = dimensions[0]
                height = dimensions[1]
                number_rows = self._board_range(height)
               
                board = []
                for i in number_rows:
                        board.append(
                                self._generate_row(width)
                        )
                return board
                               
        def _generate_row(self, length):
               
                squares_across = self._board_range(length)
               
                board_row = []
                for square in squares_across:
                        board_row.append("x")
                return board_row
       
       
class AlternatingBoard(Board):
       
        def __init__(self, dimensions):
                super().__init__(dimensions)
       
        @staticmethod
        def _every_other(section):
                if (section) % 2 != 0:
                        return True
       
        def _generate_board(self, dimensions):
                width = dimensions[0]
                height = dimensions[1]
                number_rows = self._board_range(height)
               
                board = []
                for row in number_rows:
                        if self._every_other(row):
                                board.append(self._generate_forward_row(width))
                        
                        else:
                                board.append(self._generate_reverse_row(width))
                       
                return board
       
       
        def _generate_forward_row(self, length):
                return self._generate_row(length,
                                          "+", "-")   # x --> +, o --> -
       
               
        def _generate_reverse_row(self, length):
                return self._generate_row(length,
                                          "-", "+")
       
               
        def _generate_row(self, length,
                          cell1, cell2 ):
                number_cells = self._board_range(length)
                board_row = []
                for cell in number_cells:
                        if self._every_other(cell):
                                board_row.append(cell1)
                        else:
                                board_row.append(cell2)
                return board_row
       

class ChessBoard(AlternatingBoard):
       
        class_test_attr = ""
        squares_map = []
       
        def __init__(self):
                super().__init__([8, 8])
                self.squares_map = self._get_chess_squares()
                self.linked_map = self._link_squares_map()
               
                ChessBoard.squares_map = self.squares_map
                ChessBoard.class_test_attr = "Inherited variable working!"
               
               
        def __call__(self):
                self._print_chess_squares()
                self._render_board()
       
        def _link_squares_map(self):
               
                linked_map = {}
                for row1, row2 in zip(self.squares_map, self.board):
                        linked_row = {}
                        for square, colour in zip(row1,
                                                  row2):
                                linked_row[square] = [colour]
                        linked_map.update(linked_row)
                       
                self._linked_map = linked_map

                print(self._linked_map)

                return self._linked_map
       
        def _print_chess_squares(self):
                for rank in self.squares_map:
                        print(" ".join(rank))
                       
        def _render_board(self):
                counter = 0
                board_row = []
                for value in self.linked_map.values():
                        #print("value: ", value, "counter: ", counter)
                        if counter < 7:
                                counter +=1
                                board_row.append(value[-1])
                        else:
                                board_row.append(value[-1])
                                print(" ".join(board_row))
                                board_row.clear()
                                counter = 0    
                print()
       
        @staticmethod
        def _get_chess_squares():
                ranks = list("abcdefgh")
                files = list("87654321")
               
                squares_map = []
                squares_row = []
                for filesquare in files:
                        for ranksquare in ranks:
                                squares_row.append(
                                        ranksquare+filesquare
                                )
                       
                        squares_map.append(
                                list(squares_row)
                        )
                        squares_row.clear()
                   
                return squares_map

class RotateBoard180():
       
        def __init__(self, linked_map):
                self.linked_map = linked_map
               
        def __call__(self):
                self._rotate_board()
                self._rotate_squares()
               
        def _rotate_board(self):
                self._reverse_linked(
                        self.linked_map
                )
                #print("ROTATED: ", self.linked_map)
               
        def _rotate_squares(self):
                self._reverse_rows(
                        ChessBoard.squares_map
                )
                self._reverse_columns(
                        ChessBoard.squares_map
                )

        def _reverse_rows(self, map):
                return map.reverse()
               
        def _reverse_linked(self, linked_map):
                linked_map = dict(
                        reversed(list(linked_map.items()))
                )
                self.linked_map.clear()
                self.linked_map.update(linked_map)

       
        def _reverse_columns(self, map):
                for row in map:
                        row.reverse()


class SetChessPieces():
       
        def __init__(self, linked_map, position,
                                       *positions):
                self.linked_map = linked_map
                self.position = position
               
                self.position_list = self._store_position_list(
                        position, positions
                )
               
        @staticmethod
        def _store_position_list(position,
                                 positions):
                position_list = []
                position_list.append(position)
                for extra_position in positions:
                        position_list.append(extra_position)
                return position_list
               
        @property
        def position(self):
                return self._position
               
        @position.setter
        def position(self, value):
                return self._set_position(value)
               
        def _set_position(self, position,
                                   piece):
                if self._validate_position(position):
                        self.linked_map[position].append(piece)
                        self._position = position
                        return self._position
               
        def _validate_position(self, position):
                if self.linked_map[position]:
                        return True
                raise ValueError("Invalid Position")
                return False
       
               
class SetKing(SetChessPieces):
       
        def __init__(self, linked_map, position):
                super().__init__(linked_map, position)
               
        def _set_position(self, position,
                                piece="K"):
                super()._set_position(position, piece)

class SetQueen(SetChessPieces):
       
        def __init__(self, linked_map, position):
                super().__init__(linked_map, position)
               
        def _set_position(self, position,
                                piece="Q"):
                super()._set_position(position, piece)
               

class SetBishop(SetChessPieces):
       
        def __init__(self, linked_map, position):
                super().__init__(linked_map, position)
               
        def _set_position(self, position,
                                piece="b"):
                super()._set_position(position, piece)


class SetKnight(SetChessPieces):
       
        def __init__(self, linked_map, position):
                super().__init__(linked_map, position)
               
        def _set_position(self, position,
                                piece="k"):
                super()._set_position(position, piece)
               

class SetRook(SetChessPieces):
       
        def __init__(self, linked_map, position):
                super().__init__(linked_map, position)
               
        def _set_position(self, position,
                                piece="r"):
                super()._set_position(position, piece)
               

class SetPawn(SetChessPieces):
       
        def __init__(self, linked_map, position,
                                      *positions):
                super().__init__(linked_map, position,
                                            *positions)
                if positions:
                        for position in positions:
                                self.position = position
                       
        def _set_position(self, position,
                                piece="p"):
                super()._set_position(position, piece)


class MovePiece(SetChessPieces):
       
        MOVE_NUMBER = 1
       
        def __init__(self, linked_map, start_pos,
                                         end_pos):
                self.linked_map = linked_map
                self.start_pos = start_pos
                self.end_pos = end_pos
                self._execute_move()
                MovePiece.MOVE_NUMBER += 1
               
        @property
        def start_pos(self):
                return self._start_pos
       
        @start_pos.setter
        def start_pos(self, value):
                if self._validate_position(value):
                        if not self._check_occupancy(value):
                                raise ValueError(
                                        "No Piece to Move"
                                )
                        self._start_pos = value
                        return self._start_pos
               
        @property
        def end_pos(self):
                return self._end_pos
       
        @end_pos.setter
        def end_pos(self, value):
                return self._end_pos(value)

        def _end_pos(self, end_pos): 
            if self._validate_position(end_pos):
                    if self._check_occupancy(end_pos):
                            raise ValueError("Take/Blocked")
                    self._end_pos = end_pos
                    return self._end_pos
                       
        def _check_occupancy(self, position):
                if len(self.linked_map[position]) == 2:
                        return True
                return False
                               
        def _execute_move(self, piece):
                self.linked_map[self.start_pos].pop()
                self.linked_map[self.end_pos].append(piece)
                       
               
class MovePawn(MovePiece):
       
        def __init__(self, linked_map, start_pos,
                                         end_pos):
                super().__init__(linked_map, start_pos,
                                             end_pos)
       
        def _execute_move(self, piece="p"):
                if self._validate_move():
                        super()._execute_move(piece)
       
        def _validate_move(self):
                valid_dest = self._get_valid_dest()
                if self.end_pos in valid_dest:
                        valid_dest = []
                        return True
                raise ValueError("Invalid Move")
                return False
               
        def _get_valid_dest(self):
                valid_range = self._get_valid_range()
                valid_dest = self._get_valid_vert_dest(
                        valid_range
                )
                return valid_dest
               
        def _get_valid_range(self):
                valid_range = 1
                # Amend this considering new layout of linked_map. **********
                # Maybe reuse logic, except on squares_map.        **********
                # if self.start_pos in self.linked_map[1] or self.start_pos in self.linked_map[-2]:
                #         valid_range = 2
                return valid_range
               
        def _get_valid_vert_dest(self, valid_range):
                valid_dest = []
                valid_range = Board._board_range(
                        valid_range
                )
                for down, rank in enumerate(
                        ChessBoard.squares_map):
                                for right, square in enumerate(
                                        rank
                                ):
                                        if self.start_pos == square:
                                                for range in valid_range:
                                                        valid_dest.append(
                                                        ChessBoard.squares_map
                                                        [down-range][right])
                                                       
                print("Valid Dests: ", valid_dest)
                return valid_dest
               
class PawnTake(MovePawn):
    # if target square in take range...
    
    def __init__(self, linked_map, start_pos, end_pos):
        super().__init__(linked_map, start_pos, end_pos)

    def _execute_move(self, piece="p"):
            if self._validate_move():
                    self.linked_map[self.end_pos].pop()
                    super()._execute_move(piece="p")

    def _end_pos(self, end_pos):
        if self._validate_position(end_pos):
                if not self._check_occupancy(end_pos):
                    raise ValueError("No Piece to Take")
                self._end_pos = end_pos
                return self._end_pos

    def _check_occupancy(self, position):
        if len(self.linked_map[position]) == 2:
                self.piece_taken = self.linked_map[position][-1]
                return True
        return False

    def _get_valid_dest(self):
            valid_range_up, valid_range_along = self._get_valid_range()
            valid_dest = self._get_valid_diag_dest(
                    valid_range_up, 
                    valid_range_along
            )
            return valid_dest

    # diagonal range
    def _get_valid_range(self):
            valid_range_up = 1
            valid_range_along = 1
            return (valid_range_up, valid_range_along)
            
    def _get_valid_diag_dest(self, valid_range_up, valid_range_along):
            valid_dest = []
            print("valid take dests???")
            for down, rank in enumerate(
                    ChessBoard.squares_map):
                            for right, square in enumerate(
                                    rank
                            ):
                                    if self.start_pos == square:
                                            valid_dest.append(
                                                ChessBoard.squares_map
                                                [down-valid_range_up][right+valid_range_along]
                                            )
                                            valid_dest.append(
                                                ChessBoard.squares_map
                                                [down-valid_range_up][right-valid_range_along]
                                            )
                                                    
            print("Valid Pawn Take Dests: ", valid_dest)
            return valid_dest

class TrackPieces:
       
        def __init__(self, white_positions,
                           black_positions):
                self._white_positions = white_positions
                self._black_positions = black_positions
                self._taken_by_white = []
                self._taken_by_black = []
               
        def __call__(self):
                self._get_colour()
                self._print_turn()
                self._print_colour_positions()
                self._print_colour_taken()

        def update_take(self, target_position, piece_taken):
            if self._white_move:
                self._black_positions.remove(target_position)
                self._taken_by_white.append(piece_taken)
            if self._black_move:
                self._white_positions.remove(target_position)
                self._taken_by_black.append(piece_taken)

        def query_take(self, target_position):
            if self._white_move:
                if target_position in self._black_positions:
                    return True
            if self._black_move:
                if target_position in self._white_positions:
                    return True
            return False

        def validate_colour_move(self, current_position):
            if self._white_move:
                if current_position in self._white_positions:
                    return True
            if self._black_move:
                if current_position in self._black_positions:
                    return True
            return False
        
        def update_colour_position(self, old_position, new_position):
            if self._white_move:
                self._white_positions.remove(old_position)
                self._white_positions.append(new_position)
            if self._black_move:
                self._black_positions.remove(old_position)
                self._black_positions.append(new_position)

        def _print_colour_taken(self):
            if self._white_move:
                print("Taken by White: ", self._taken_by_white)
            if self._black_move:
                print("Taken by Black: ", self._taken_by_black)
        
        def _print_colour_positions(self):
            if self._white_move:
                print("White: ", self._white_positions)
            if self._black_move:
                print("Black: ", self._black_positions)
       
        def _get_colour(self):
                if MovePiece.MOVE_NUMBER % 2 != 0:
                        self._black_move = False
                        self._white_move = True
                        return
                self._white_move = False
                self._black_move = True
                return
               
        def _print_turn(self):
                print("Move: ", MovePiece.MOVE_NUMBER)
                if self._white_move:
                        print("White to move")
                if self._black_move:
                        print("Black to move")


class Controller:
       
        def __init__(self):
                self.board = ChessBoard()
                self.rotate = RotateBoard180(
                        self.board.linked_map
                )
                self._setup_board()

                self.track = TrackPieces(
                        self._white_positions,
                        self._black_positions
                )
                self._display_board()
       
        def _setup_board(self):
                self._setup_white_pieces()
                self._setup_black_pieces()
               
        def _setup_white_pieces(self):
               
                self._white_positions = [] 
                self._white_pawns = SetPawn(
                        self.board.linked_map, "d3", "a2" 
                        # self.board.linked_map, "a2", "b2",
                        #                        "c2", "d2",
                        #                        "e2", "f2",
                        #                        "g2", "h2" 
                    )
                self._white_positions += self._white_pawns.position_list

        def _setup_black_pieces(self):

                self._black_positions = [] 
                self._black_pawns = SetPawn(
                        self.board.linked_map, "c4", "d5"
                        # self.board.linked_map, "a7", "b7",
                        #                        "c7", "d7",
                        #                        "e7", "f7",
                        #                        "g7", "h7" 
                    )
                self._black_positions += self._black_pawns.position_list

        def move(self, start_pos, end_pos):
                
                if not self.track.validate_colour_move(start_pos):
                    raise ValueError("Not Your Turn/Invalid Move")
                
                
                piece = self.board.linked_map[start_pos][-1]
                if piece == "p":
                        
                        if not self.track.query_take(end_pos):
                            move = MovePawn(
                                    self.board.linked_map,
                                    start_pos,
                                    end_pos
                            )
                        else:
                            #raise ValueError("Potential Take")
                            take = PawnTake(
                                self.board.linked_map,
                                start_pos,
                                end_pos
                            )
                            self.track.update_take(end_pos, take.piece_taken)

                        self.track.update_colour_position(start_pos, end_pos)
                        self._refresh_board()
               
                else:
                        raise ValueError("No Pawn Here")
       
        def _display_board(self):
                self.track()
                self.board()
       
        def _refresh_board(self):
                self.board()
                self.rotate()
                self.track()
                self.board()
       

player = Controller()
player.move("d3", "c4")
player.move("d5", "c4")
player.move("a2", "a3")

print(player.board.linked_map is player.rotate.linked_map)

#Board([4, 4])
#AlternatingBoard([20,2])

#piece = SetCastle(board.linked_map, "a8")
#piece = SetKnight(board.linked_map, "a7")
#piece = SetBishop(board.linked_map, "a6")

#piece = SetQueen(board.linked_map, "a5")
#piece = SetKing(board.linked_map, "a4")

#piece = SetRook(board.linked_map, "a1")
#piece = SetKnight(board.linked_map, "a2")
#piece = SetBishop(board.linked_map, "a3")