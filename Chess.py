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
                                          "+", "-")   # "X" = white, "O" = black
       
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
       
        squares_map = []
        rotated_squares_map = []
        WIDTH = None
        HEIGHT = None
       
        def __init__(self):
                self._dimensions = [8,8]
                super().__init__(self._dimensions)

                ChessBoard.WIDTH = self._dimensions[0]
                ChessBoard.HEIGHT = self._dimensions[1]

                self.squares_map = self._get_chess_squares()
                self.linked_map = self._link_squares_map()
               
                ChessBoard.squares_map = self.squares_map

                # creating a duplicate squares map to reverse.
                ChessBoard.rotated_squares_map = [[row for row in list]         # Creating copies of not only the list
                                                  for list in self.squares_map] # but the lists within the list too.
                RotateBoard180.rotate_squares(
                        ChessBoard.rotated_squares_map
                )

        def __call__(self):
                #self._print_chess_squares()
                self._render_board()
                self._render_board_with_colour()
       
        def _link_squares_map(self):
               
                linked_map = {}
                for row1, row2 in zip(self.squares_map, self.board):
                        linked_row = {}
                        for square, colour in zip(row1,
                                                  row2):
                                linked_row[square] = [colour]
                        linked_map.update(linked_row)
                       
                self._linked_map = linked_map
                return self._linked_map
       
        def _print_chess_squares(self):
                for rank in self.squares_map:
                        print(" ".join(rank))
                       
        def _render_board(self):
                
                file_letters = []
                rank_numbers = []
                for square in next(iter(ChessBoard.squares_map)):
                        file_letters.append(
                                square[0]
                        )
                for rank in ChessBoard.squares_map:
                        rank_numbers.append(
                                rank[0][1]
                        )

                horizontal_border = '{:>18}'.format(" ".join(file_letters)) 
                print(horizontal_border)

                counter = 0
                rank_index = 0
                board_row = []
                for value in self.linked_map.values():

                        if counter < 7:
                                counter +=1
                                board_row.append(value[-1])
                        else:
                                board_row.append(value[-1])
                                print(rank_numbers[rank_index]+"|", " ".join(board_row), "|"+rank_numbers[rank_index])
                                board_row.clear()
                                counter = 0
                                rank_index += 1    
                
                print(horizontal_border)
                print()

        def _render_board_with_colour(self):
                
                file_letters = []
                rank_numbers = []
                for square in next(iter(ChessBoard.squares_map)):
                        file_letters.append(
                                square[0]
                        )
                for rank in ChessBoard.squares_map:
                        rank_numbers.append(
                                rank[0][1]
                        )

                horizontal_border = '{:>33}'.format("   ".join(file_letters)) 
                print(horizontal_border)

                counter = 0
                rank_index = 0
                board_row = []
                top_edge_printed = False
                for key, value in self.linked_map.items():
                        if counter < 7:
                                counter +=1

                                print_square = ""
                                if key in TrackPieces.WHITE_POSITIONS:
                                        print_square = ""
                                        print_square = "(" + value[-1] + ")"
                                elif key in TrackPieces.BLACK_POSITIONS:
                                        print_square = ""
                                        print_square = "[" + value[-1] + "]"
                                else:
                                        print_square = " " + value[-1] + " "
                                board_row.append(print_square)

                        else:
                                print_square = ""
                                if key in TrackPieces.WHITE_POSITIONS:
                                        print_square = ""
                                        print_square = "(" + value[-1] + ")"
                                elif key in TrackPieces.BLACK_POSITIONS:
                                        print_square = ""
                                        print_square = "[" + value[-1] + "]"
                                else:
                                        print_square = " " + value[-1] + " "
                                board_row.append(print_square)
                                                                
                                print(rank_numbers[rank_index]+"|", " ".join(board_row), "|"+rank_numbers[rank_index])

                                board_row.clear()
                                counter = 0
                                rank_index += 1    
                
                print(horizontal_border)
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
                self.rotate_squares(ChessBoard.squares_map) # This needs to stay in for printing the board.
               
        def _rotate_board(self):
                self._reverse_linked(
                        self.linked_map
                )
                #print("ROTATED: ", self.linked_map)

        def _reverse_linked(self, linked_map):
                linked_map = dict(
                        reversed(list(linked_map.items()))
                )
                self.linked_map.clear()
                self.linked_map.update(linked_map)

        @staticmethod
        def rotate_squares(map):
                RotateBoard180.reverse_rows(map)
                RotateBoard180.reverse_columns(map)

        @staticmethod
        def reverse_rows(map):
                return map.reverse()

        @staticmethod
        def reverse_columns(map):
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
       
        def __init__(self, linked_map, position,
                                      *positions):
                super().__init__(linked_map, position,
                                            *positions)
                if positions:
                        for position in positions:
                                self.position = position
               
        def _set_position(self, position, piece="K"):
                super()._set_position(position, piece)


class SetQueen(SetChessPieces):
       
        def __init__(self, linked_map, position,
                                      *positions):
                super().__init__(linked_map, position,
                                            *positions)
                if positions:
                        for position in positions:
                                self.position = position
               
        def _set_position(self, position, piece="Q"):
                super()._set_position(position, piece)
               

class SetBishop(SetChessPieces):
       
        def __init__(self, linked_map, position,
                                      *positions):
                super().__init__(linked_map, position,
                                            *positions)
                if positions:
                        for position in positions:
                                self.position = position
               
        def _set_position(self, position, piece="b"):
                super()._set_position(position, piece)


class SetKnight(SetChessPieces):
       
        def __init__(self, linked_map, position,
                                      *positions):
                super().__init__(linked_map, position,
                                            *positions)
                if positions:
                        for position in positions:
                                self.position = position
               
        def _set_position(self, position, piece="k"):
                super()._set_position(position, piece)
               

class SetRook(SetChessPieces):
       
        def __init__(self, linked_map, position,
                                      *positions):
                super().__init__(linked_map, position,
                                            *positions)
                if positions:
                        for position in positions:
                                self.position = position
               
        def _set_position(self, position, piece="r"):
                super()._set_position(position, piece)
               

class SetPawn(SetChessPieces):
       
        def __init__(self, linked_map, position,
                                      *positions):
                super().__init__(linked_map, position,
                                            *positions)
                if positions:
                        for position in positions:
                                self.position = position
                       
        def _set_position(self, position, piece="p"):
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
                for dest_list in valid_dest:
                        if self.end_pos in dest_list:
                                return True
                raise ValueError("Invalid Move")
                return False

        def _get_valid_dest(self):
                valid_dest = PieceMoveRanges.TRUNCATED_BOARD_DESTS[self.start_pos]
                return valid_dest  


class MoveRook(MovePawn):

        def __init__(self, linked_map, start_pos,
                                         end_pos):
                super().__init__(linked_map, start_pos,
                                            end_pos)

        def _execute_move(self, piece="r"):
                super()._execute_move(piece)


class MoveKnight(MovePawn):

        def __init__(self, linked_map, start_pos,
                                         end_pos):
                super().__init__(linked_map, start_pos,
                                            end_pos)

        def _execute_move(self, piece="k"):
                super()._execute_move(piece)


class MoveBishop(MovePawn):

        def __init__(self, linked_map, start_pos,
                                         end_pos):
                super().__init__(linked_map, start_pos,
                                            end_pos)

        def _execute_move(self, piece="b"):
                super()._execute_move(piece)


class MoveQueen(MovePawn):

        def __init__(self, linked_map, start_pos,
                                         end_pos):
                super().__init__(linked_map, start_pos,
                                            end_pos)

        def _execute_move(self, piece="Q"):
                super()._execute_move(piece)


class MoveKing(MovePawn):

        def __init__(self, linked_map, start_pos,
                                         end_pos):
                super().__init__(linked_map, start_pos,
                                            end_pos)

        def _execute_move(self, piece="K"):
                super()._execute_move(piece)


class Castle(MovePiece):
        
        def __init__(self, linked_map, start_pos, end_pos):

                super().__init__(linked_map, start_pos, end_pos)
                # self.linked_map = linked_map
                # self.start_pos = start_pos
                # self.end_pos = end_pos
                # self._execute_castle()
                
                # # Make sure we are still incrementing the 
                # MovePiece.MOVE_NUMBER += 1
        
        def _execute_move(self):
                self._execute_castle()
        
        def _execute_castle(self):
                old_rook_pos, new_rook_pos = self._get_castling_positions()
                
                self.linked_map[self.start_pos].pop()
                self.linked_map[self.end_pos].append("K")
                
                self.linked_map[old_rook_pos].pop()
                self.linked_map[new_rook_pos].append("r")

                if TrackPieces.WHITE_MOVE:
                        TrackPieces.WHITE_POSITIONS.remove(old_rook_pos)
                        TrackPieces.WHITE_POSITIONS.append(new_rook_pos)

                if TrackPieces.BLACK_MOVE:
                        TrackPieces.BLACK_POSITIONS.remove(old_rook_pos)
                        TrackPieces.BLACK_POSITIONS.append(new_rook_pos)                        

                print("old rook pos returned", old_rook_pos)
                print("new rook pos returned", new_rook_pos)

        def _get_castling_positions(self):

                # finding the rook the closest to the end pos.
                if TrackPieces.WHITE_MOVE:
                        back_row = TrackPieces.BACK_ROW_WHITE
                        rook_distances = self._get_back_row_rooks( back_row,
                                                                   TrackPieces.WHITE_KING_HAS_MOVED, 
                                                                   TrackPieces.WHITE_ROOKS_HAVE_MOVED)

                if TrackPieces.BLACK_MOVE:
                        back_row = TrackPieces.BACK_ROW_BLACK
                        rook_distances = self._get_back_row_rooks( back_row,
                                                                   TrackPieces.BLACK_KING_HAS_MOVED, 
                                                                   TrackPieces.BLACK_ROOKS_HAVE_MOVED)

                closest_rook = self._get_closest_rook(rook_distances, back_row)

                old_rook_pos, new_rook_pos = self._get_new_rook_positions(rook_distances, closest_rook, back_row)

                return (old_rook_pos, new_rook_pos)
        
        def _get_back_row_rooks(self, back_row, king_moved, rook_status_dict):

                if not king_moved:
                        rook_distances = {}
                        for rook, has_moved in rook_status_dict.items():
                                # getting the rook that is closest to the king dest position.
                                rook_distances[rook] = ( back_row.index(rook) - back_row.index(self.end_pos) )
                        return rook_distances  
                else:
                        raise ValueError("Cannot castle as King has moved.")

        def _get_closest_rook(self, rook_distances, back_row):
                
                closest_rook = min(rook_distances, key=lambda rook: abs(rook_distances[rook]))

                print(
                        back_row.index(self.start_pos), back_row.index(closest_rook)
                )

                # spaces inbetween the king and rook either side.
                back_row_castle_side_left = back_row[back_row.index(closest_rook)+1:back_row.index(self.start_pos)]
                back_row_castle_side_right = back_row[back_row.index(self.start_pos)+1:back_row.index(closest_rook)]

                # making sure there are no pieces in between the king and rook.
                if back_row_castle_side_left:                
                        for inbetween_square in back_row_castle_side_left:
                                if len(self.linked_map[inbetween_square]) == 2:
                                        raise ValueError("Cannot castle as pieces are in the way.")

                if back_row_castle_side_right:                
                        for inbetween_square in back_row_castle_side_right:
                                if len(self.linked_map[inbetween_square]) == 2:
                                        raise ValueError("Cannot castle as pieces are in the way.")

                if TrackPieces.WHITE_MOVE:
                        if TrackPieces.WHITE_ROOKS_HAVE_MOVED[closest_rook]:
                                raise ValueError("Cannot castle as Rook has already moved.")

                if TrackPieces.BLACK_MOVE:
                        if TrackPieces.BLACK_ROOKS_HAVE_MOVED[closest_rook]:
                                raise ValueError("Cannot castle as Rook has already moved.")

                return closest_rook
   
        def _get_new_rook_positions(self, rook_distances, closest_rook, back_row):
                
                # +ve index numbers show castling to the right.
                if rook_distances[closest_rook] > 0: # right - rook is one to left of king
                        new_rook_pos_index = back_row.index(self.end_pos) - 1
                        new_rook_pos = back_row[new_rook_pos_index]
                        return (closest_rook, new_rook_pos)
                if rook_distances[closest_rook] < 0: # left - rook is one to right of king
                        new_rook_pos_index = back_row.index(self.end_pos) + 1
                        new_rook_pos = back_row[new_rook_pos_index]
                        return (closest_rook, new_rook_pos)        


class PawnTake(MovePawn):
    # if target square in take range...
    
    def __init__(self, linked_map, start_pos, end_pos):
        super().__init__(linked_map, start_pos, end_pos)

    def _execute_move(self, piece="p"):
            if self._validate_move():
                    self.linked_map[self.end_pos].pop()
                    super(MovePawn, self)._execute_move(piece) # Trimming the MRO so we use the code from MovePiece

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
            valid_dest = PieceMoveRanges.TRUNCATED_BOARD_TAKE_DESTS[self.start_pos]
            return valid_dest


class RookTake(PawnTake):
        
        def __init__(self, linked_map, start_pos, end_pos):
                super().__init__(linked_map, start_pos, end_pos)

        def _execute_move(self, piece="r"):
                super()._execute_move(piece)


class KnightTake(PawnTake):
        
        def __init__(self, linked_map, start_pos, end_pos):
                super().__init__(linked_map, start_pos, end_pos)

        def _execute_move(self, piece="k"):
                super()._execute_move(piece)


class BishopTake(PawnTake):
        
        def __init__(self, linked_map, start_pos, end_pos):
                super().__init__(linked_map, start_pos, end_pos)

        def _execute_move(self, piece="b"):
                super()._execute_move(piece)


class QueenTake(PawnTake):
        
        def __init__(self, linked_map, start_pos, end_pos):
                super().__init__(linked_map, start_pos, end_pos)

        def _execute_move(self, piece="Q"):
                super()._execute_move(piece)


class KingTake(PawnTake):
        
        def __init__(self, linked_map, start_pos, end_pos):
                super().__init__(linked_map, start_pos, end_pos)

        def _execute_move(self, piece="K"):
                super()._execute_move(piece)


class PromotePawn():
        
        def __init__(self, linked_map, end_pos):
                self.linked_map = linked_map
                self.end_pos = end_pos
                self._promote_pawn()

        def _promote_pawn(self):
                valid_promotion = False
                while valid_promotion == False:
                        promotion = input("Which Piece would you like to promote to: r, b, k, Q? ")
                        if promotion not in list("rbkQ"):
                                raise ValueError("Can't promote to that piece.")
                        else:
                                valid_promotion = True
                self.linked_map[self.end_pos].pop()
                self.linked_map[self.end_pos].append(promotion) 


class TrackPieces:
       
        WHITE_MOVE = True
        BLACK_MOVE = False

        WHITE_POSITIONS = []
        BLACK_POSITIONS = []

        # Keeping track for castling
        WHITE_KING_HAS_MOVED = False
        BLACK_KING_HAS_MOVED = False
        WHITE_ROOKS_HAVE_MOVED = {}
        BLACK_ROOKS_HAVE_MOVED = {}
        BACK_ROW_WHITE = []
        BACK_ROW_BLACK = []

        def __init__(self, linked_map, white_positions,
                                       black_positions):
                
                self.linked_map = linked_map

                self._initial_white_positions = white_positions
                self._initial_black_positions = black_positions

                TrackPieces.WHITE_POSITIONS = self._initial_white_positions
                TrackPieces.BLACK_POSITIONS = self._initial_black_positions

                self._taken_by_white = []
                self._taken_by_black = []

                TrackPieces.BACK_ROW_WHITE = ChessBoard.squares_map[ChessBoard.HEIGHT-1]
                TrackPieces.BACK_ROW_BLACK = ChessBoard.squares_map[0]
                self.detect_rook_positions()
               
        def __call__(self):
                self._get_colour()
                self._print_turn()
                self._print_colour_positions()
                self._print_colour_taken()

        # each call, finds out if white is in check, and if black is in check.
        # if a colour is in check then it can only move if that move makes it no longer in check.
        # if e.g. after white move and then white in check, its an invalid move.
        # ... then need to find some way to reverse the move ...
        def detect_check(self):

                TrackPieces.WHITE_IN_CHECK = False
                for position in TrackPieces.WHITE_POSITIONS:
                        if self.linked_map[position][-1] == "K":
                                for square in TrackPieces.BLACK_POSITIONS:
                                        for dest_lists in PieceMoveRanges.TRUNCATED_BOARD_TAKE_DESTS[square]:
                                                for dest_list in dest_lists:
                                                        if position in dest_list:
                                                                TrackPieces.WHITE_IN_CHECK = True
                                                                #return "White in Check!"
                TrackPieces.BLACK_IN_CHECK = False
                for position in TrackPieces.BLACK_POSITIONS:
                        # finding the king position(s!)
                        if self.linked_map[position][-1] == "K":
                                # getting the dest lists for each white position
                                for square in TrackPieces.WHITE_POSITIONS:
                                        # looking at the take ranges for each of those squares.
                                        for dest_lists in PieceMoveRanges.TRUNCATED_BOARD_TAKE_DESTS[square]:
                                                for dest_list in dest_lists:
                                                        # in check if the king position is in a dest list.
                                                        if position in dest_list:
                                                                TrackPieces.BLACK_IN_CHECK = True
                                                                #return "Black in Check!"

        def detect_rook_positions(self):
                
                # on initialisation store rook positions as 'not moved'.
                for square, contents in self.linked_map.items():
                        if contents[-1] == "r":
                                if square in TrackPieces.WHITE_POSITIONS:
                                        TrackPieces.WHITE_ROOKS_HAVE_MOVED[square] = False
                                if square in TrackPieces.BLACK_POSITIONS:
                                        TrackPieces.BLACK_ROOKS_HAVE_MOVED[square] = False
        
        @staticmethod
        def update_rook_moves(start_pos):
                if TrackPieces.WHITE_MOVE:
                        TrackPieces.WHITE_ROOKS_HAVE_MOVED[start_pos] = True
                if TrackPieces.BLACK_MOVE:
                        TrackPieces.BLACK_ROOKS_HAVE_MOVED[start_pos] = True

        @staticmethod
        def update_king_move():
                if TrackPieces.WHITE_MOVE:
                        TrackPieces.WHITE_KING_HAS_MOVED = True
                if TrackPieces.BLACK_MOVE:
                        TrackPieces.BLACK_KING_HAS_MOVED = True

        def update_take(self, target_position, piece_taken):
            if TrackPieces.WHITE_MOVE:
                TrackPieces.BLACK_POSITIONS.remove(target_position)
                self._taken_by_white.append(piece_taken)
            if TrackPieces.BLACK_MOVE:
                TrackPieces.WHITE_POSITIONS.remove(target_position)
                self._taken_by_black.append(piece_taken)

        @staticmethod
        def query_take(target_position):
            if TrackPieces.WHITE_MOVE:
                if target_position in TrackPieces.BLACK_POSITIONS:
                    return True
            if TrackPieces.BLACK_MOVE:
                if target_position in TrackPieces.WHITE_POSITIONS:
                    return True
            return False

        @staticmethod
        def validate_colour_move(current_position):
            if TrackPieces.WHITE_MOVE:
                if current_position in TrackPieces.WHITE_POSITIONS:
                    return True
            if TrackPieces.BLACK_MOVE:
                if current_position in TrackPieces.BLACK_POSITIONS:
                    return True
            return False
        
        @staticmethod
        def update_colour_position(old_position, new_position):
            if TrackPieces.WHITE_MOVE:
                TrackPieces.WHITE_POSITIONS.remove(old_position)
                TrackPieces.WHITE_POSITIONS.append(new_position)
            if TrackPieces.BLACK_MOVE:
                TrackPieces.BLACK_POSITIONS.remove(old_position)
                TrackPieces.BLACK_POSITIONS.append(new_position)

        def _print_colour_taken(self):
            #if TrackPieces.WHITE_MOVE:
            print("Taken by White: ", self._taken_by_white)
            #if TrackPieces.BLACK_MOVE:
            print("Taken by Black: ", self._taken_by_black)
        
        @staticmethod
        def _print_colour_positions():
            #if TrackPieces.WHITE_MOVE:
            print("White: ", TrackPieces.WHITE_POSITIONS)
            #if TrackPieces.BLACK_MOVE:
            print("Black: ", TrackPieces.BLACK_POSITIONS)
       
        def _get_colour(self):
                if MovePiece.MOVE_NUMBER % 2 != 0:
                        TrackPieces.BLACK_MOVE = False
                        TrackPieces.WHITE_MOVE = True
                        return
                TrackPieces.WHITE_MOVE = False
                TrackPieces.BLACK_MOVE = True
                return
               
        def _print_turn(self):
                print("Move: ", MovePiece.MOVE_NUMBER)
                if TrackPieces.WHITE_MOVE:
                        print("White to move")
                if TrackPieces.BLACK_MOVE:
                        print("Black to move")


class PieceMoveRanges:

        VALID_PAWN_DESTS = {} # dictionary to be assigned to up or down depending on which turn it is.
        VALID_PAWN_DESTS_UP = {}
        VALID_PAWN_DESTS_DOWN = {}

        VALID_PAWN_TAKE_DESTS = {} # same here
        VALID_PAWN_TAKE_DESTS_UP = {}
        VALID_PAWN_TAKE_DESTS_DOWN = {}

        VALID_ROOK_DESTS = {}
        VALID_KNIGHT_DESTS = {}
        VALID_BISHOP_DESTS = {}
        VALID_QUEEN_DESTS = {}
        VALID_KING_DESTS = {}

        TRUNCATED_BOARD_DESTS = {}
        TRUNCATED_BOARD_TAKE_DESTS = {}
        
        def __init__(self, linked_map):
                self.linked_map = linked_map

                PieceMoveRanges.VALID_PAWN_DESTS_UP = self._get_valid_pawn_dests(
                        ChessBoard.squares_map
                )
                PieceMoveRanges.VALID_PAWN_DESTS_DOWN = self._get_valid_pawn_dests(
                        ChessBoard.rotated_squares_map
                )

                PieceMoveRanges.VALID_PAWN_TAKE_DESTS_UP = self._get_valid_pawn_take_dests(
                        ChessBoard.squares_map
                )
                PieceMoveRanges.VALID_PAWN_TAKE_DESTS_DOWN = self._get_valid_pawn_take_dests(
                        ChessBoard.rotated_squares_map
                )

                PieceMoveRanges.VALID_ROOK_DESTS = self._get_valid_rook_dests()
                PieceMoveRanges.VALID_KNIGHT_DESTS = self._get_valid_knight_dests()
                PieceMoveRanges.VALID_BISHOP_DESTS = self._get_valid_bishop_dests()        
                
                PieceMoveRanges.VALID_QUEEN_DESTS = self._get_valid_queen_dests(
                        PieceMoveRanges.VALID_ROOK_DESTS,
                        PieceMoveRanges.VALID_BISHOP_DESTS
                )

                PieceMoveRanges.VALID_KING_DESTS = self._get_valid_king_dests()

        def __call__(self): # not yet used - needs testing first.
                self._generate_board_dests()

        def _generate_board_dests(self):
                PieceMoveRanges.TRUNCATED_BOARD_DESTS = {}
                PieceMoveRanges.TRUNCATED_BOARD_TAKE_DESTS = {} # May not be necessart to reset these - need to test.
                
                valid_board_dests, valid_board_take_dests = self._get_board_dests_per_turn()
                PieceMoveRanges.TRUNCATED_BOARD_DESTS = self._get_truncated_board_dests_per_turn(
                        valid_board_dests
                )

                PieceMoveRanges.TRUNCATED_BOARD_TAKE_DESTS = self._get_truncated_board_take_dests_per_turn(
                        valid_board_dests, # when this gets here it has been truncated by the previous call.
                        valid_board_take_dests
                )

                print("Truncated Move Dests:")
                print(PieceMoveRanges.TRUNCATED_BOARD_DESTS)
                print("Truncated Take Dests:")
                print(PieceMoveRanges.TRUNCATED_BOARD_TAKE_DESTS)
 
        def _get_board_dests_per_turn(self):
                # get valid move destinations for all pieces on the board, without truncation.
                
                valid_board_dests = {}
                valid_board_take_dests = {}

                for square in TrackPieces.WHITE_POSITIONS + TrackPieces.BLACK_POSITIONS:
                        piece = self.linked_map[square][1]

                        if piece == "p":
                                # use up or down direction for pawns depending on the piece's colour.
                                # creating copies of the dictionary entries so that the originals are not changed.
                                if square in TrackPieces.WHITE_POSITIONS:
                                        valid_board_dests[square] = [[dest_square for dest_square in dest_list] 
                                                                      for dest_list in PieceMoveRanges.VALID_PAWN_DESTS_UP[square]]

                                        valid_board_take_dests[square] = [[dest_square for dest_square in dest_list] 
                                                                           for dest_list in PieceMoveRanges.VALID_PAWN_TAKE_DESTS_UP[square]]   
                                if square in TrackPieces.BLACK_POSITIONS:                                                                     
                                        
                                        valid_board_dests[square] = [[dest_square for dest_square in dest_list]
                                                                      for dest_list in PieceMoveRanges.VALID_PAWN_DESTS_DOWN[square]]
                                        
                                        valid_board_take_dests[square] = [[dest_square for dest_square in dest_list]
                                                                           for dest_list in PieceMoveRanges.VALID_PAWN_TAKE_DESTS_DOWN[square]]
                        if piece == "r":
                                valid_board_dests[square] = [[dest_square for dest_square in dest_list]
                                                              for dest_list in PieceMoveRanges.VALID_ROOK_DESTS[square]]
                                
                                valid_board_take_dests[square] = [[dest_square for dest_square in dest_list]
                                                                   for dest_list in PieceMoveRanges.VALID_ROOK_DESTS[square]]
                                                                   
                        if piece == "k":
                                valid_board_dests[square] = [[dest_square for dest_square in dest_list]
                                                              for dest_list in PieceMoveRanges.VALID_KNIGHT_DESTS[square]]
                                
                                valid_board_take_dests[square] = [[dest_square for dest_square in dest_list]
                                                                   for dest_list in PieceMoveRanges.VALID_KNIGHT_DESTS[square]]

                        if piece == "b":
                                valid_board_dests[square] = [[dest_square for dest_square in dest_list]
                                                              for dest_list in PieceMoveRanges.VALID_BISHOP_DESTS[square]]
                                
                                valid_board_take_dests[square] = [[dest_square for dest_square in dest_list]
                                                                   for dest_list in PieceMoveRanges.VALID_BISHOP_DESTS[square]]

                        if piece == "Q":
                                valid_board_dests[square] = [[dest_square for dest_square in dest_list]
                                                              for dest_list in PieceMoveRanges.VALID_QUEEN_DESTS[square]]
                                
                                valid_board_take_dests[square] = [[dest_square for dest_square in dest_list]
                                                                   for dest_list in PieceMoveRanges.VALID_QUEEN_DESTS[square]]

                        if piece == "K":
                                valid_board_dests[square] = [[dest_square for dest_square in dest_list]
                                                              for dest_list in PieceMoveRanges.VALID_KING_DESTS[square]]
                                
                                valid_board_take_dests[square] = [[dest_square for dest_square in dest_list]
                                                                   for dest_list in PieceMoveRanges.VALID_KING_DESTS[square]]

                return (valid_board_dests, valid_board_take_dests)
        
        # Needs further testing.
        def _get_truncated_board_take_dests_per_turn(self, truncated_board_dests,
                                                           valid_board_take_dests):

                # need to add condition below for different truncation
                # for knights.
                truncated_board_take_dests = {}

                for square in TrackPieces.WHITE_POSITIONS + TrackPieces.BLACK_POSITIONS:
                        
                        # only the pawn take destinations will differ between the truncated move dests
                        # and the truncated take dests.
                        if self.linked_map[square][1] == "p":
                                dest_lists = valid_board_take_dests[square]
                                truncated_board_take_dests[square] = dest_lists
                                for dest_list in truncated_board_take_dests[square]:
                                        for dest_square in dest_list:
                                                if dest_square in TrackPieces.WHITE_POSITIONS + TrackPieces.BLACK_POSITIONS:
                                                        if square in TrackPieces.WHITE_POSITIONS:                            
                                                                if dest_square in TrackPieces.WHITE_POSITIONS:               
                                                                        print(square, self.linked_map[square][1])            
                                                                        print(dest_list, "Blocked At:", dest_square)
                                                                        del dest_list[dest_list.index(dest_square):]
                                                                        print("Truncating to: ", dest_list)
                                                                if dest_square in TrackPieces.BLACK_POSITIONS:
                                                                        print(square, self.linked_map[square][1])
                                                                        print(dest_list, "Blocked By Opponent At:", dest_square)
                                                                        del dest_list[dest_list.index(dest_square)+1:]
                                                                        print("Truncating to: ", dest_list)
                                                        if square in TrackPieces.BLACK_POSITIONS:
                                                                if dest_square in TrackPieces.BLACK_POSITIONS:
                                                                        print(square, self.linked_map[square][1])
                                                                        print(dest_list, "Blocked At:", dest_square)
                                                                        del dest_list[dest_list.index(dest_square):]
                                                                        print("Truncating to: ", dest_list)
                                                                if dest_square in TrackPieces.WHITE_POSITIONS:
                                                                        print(square, self.linked_map[square][1])
                                                                        print(dest_list, "Blocked By Opponent At:", dest_square)
                                                                        del dest_list[dest_list.index(dest_square)+1:]
                                                                        print("Truncating to: ", dest_list)
                        else: # for pieces other than pawns, take the truncated lists from the
                              # truncated dest lists directly.
                                dest_lists = truncated_board_dests[square]
                                truncated_board_take_dests[square] = dest_lists                         
                return truncated_board_take_dests

        # get take dests/ranges for all pieces on the board.
        def _get_truncated_board_dests_per_turn(self, valid_board_dests):
                
                # results added to a separate dict.
                # need to add condition below for different truncation
                # for knights.
                truncated_board_dests = {}

                for square in TrackPieces.WHITE_POSITIONS + TrackPieces.BLACK_POSITIONS:
                        dest_lists = valid_board_dests[square]
                        truncated_board_dests[square] = dest_lists # initialising the list for that square to contain the dest lists.
                        for dest_list in truncated_board_dests[square]:
                                for dest_square in dest_list:
                                        if dest_square in TrackPieces.WHITE_POSITIONS + TrackPieces.BLACK_POSITIONS:
                                                # if its a white or black move, compare the square to pieces of
                                                # the same and opposite colours and truncate accordingly.
                                                if square in TrackPieces.WHITE_POSITIONS:                            # even though each turn
                                                        # if same colour truncate from incl that square.             # one side's pieces haven't moved their
                                                        if dest_square in TrackPieces.WHITE_POSITIONS:               # range/dests may be changed by
                                                                print(square, self.linked_map[square][1])            # movement of the opponent's piece.
                                                                print(dest_list, "Blocked At:", dest_square)
                                                                del dest_list[dest_list.index(dest_square):]
                                                                print("Truncating to: ", dest_list)
                                                        # if opposite colour truncate after that square.
                                                        if dest_square in TrackPieces.BLACK_POSITIONS:
                                                                print(square, self.linked_map[square][1])
                                                                print(dest_list, "Blocked By Opponent At:", dest_square)
                                                                
                                                                if self.linked_map[square][1] == "p":                  # if the current piece is a pawn then 
                                                                        del dest_list[dest_list.index(dest_square):]   # an opponent piece will block it too
                                                                                                                       # as it can't take forward.
                                                                elif self.linked_map[square][1] == "K" and self.linked_map[dest_square][1] == "K":
                                                                        del dest_list[dest_list.index(dest_square):] # *** making it so you cant take a king with a king
                                                                else:                                                # but need to make it so you cant go near a king ***
                                                                        del dest_list[dest_list.index(dest_square)+1:]       
                                                                
                                                                print("Truncating to: ", dest_list)
                                                if square in TrackPieces.BLACK_POSITIONS:
                                                        if dest_square in TrackPieces.BLACK_POSITIONS:
                                                                print(square, self.linked_map[square][1])
                                                                print(dest_list, "Blocked At:", dest_square)
                                                                del dest_list[dest_list.index(dest_square):]
                                                                print("Truncating to: ", dest_list)
                                                        if dest_square in TrackPieces.WHITE_POSITIONS:
                                                                print(square, self.linked_map[square][1])
                                                                print(dest_list, "Blocked By Opponent At:", dest_square)

                                                                if self.linked_map[square][1] == "p":                  # if the current piece is a pawn then 
                                                                        del dest_list[dest_list.index(dest_square):]   # an opponent piece will block it too
                                                                                                                       # as it can't take forward.
                                                                elif self.linked_map[square][1] == "K" and self.linked_map[dest_square][1] == "K":
                                                                        del dest_list[dest_list.index(dest_square):] # *** making it so you cant take a king with a king
                                                                else:                                                # but need to make it so you cant go near a king ***                                               
                                                                        del dest_list[dest_list.index(dest_square)+1:]
        
                                                                print("Truncating to: ", dest_list)
                return truncated_board_dests



        def _get_valid_pawn_dests(self, squares_map):
                # This returns lists of pawn dests - specifically in one direction
                # up the board.
                valid_pawn_dests = {}

                valid_start_range = 2
                valid_range = 1

                for down, rank in enumerate(squares_map):
                        for right, square in enumerate(rank):
                                valid_pawn_dests[square] = [ [] ]  # up dests
                                if down == (ChessBoard.HEIGHT - 1) - 1:
                                        valid_pawn_dests[square][0].append(
                                                squares_map[down-valid_range][right]
                                        )
                                        valid_pawn_dests[square][0].append(
                                                squares_map[down-valid_start_range][right]
                                        )
                                elif down > 0:
                                        valid_pawn_dests[square][0].append(
                                                squares_map[down-valid_range][right]
                                        )
                print("Pawn Dests:")
                for square, dests in valid_pawn_dests.items():
                        print(square, dests)
                return valid_pawn_dests

        def _get_valid_pawn_take_dests(self, squares_map):
                # This returns lists of pawn dests - specifically in one direction
                # up the board.
                valid_pawn_take_dests = {}

                valid_range_up = 1
                valid_range_along = 1

                for down, rank in enumerate(squares_map):
                        for right, square in enumerate(rank):
                                valid_pawn_take_dests[square] = [ [],   # up-left dests in the direction of white or black.
                                                                  [] ]  # up-right dests in the direction of white or black.
                                if down > 0:
                                        try:
                                                # make sure we are not looping over the 
                                                # other side of the board.
                                                if (right-1) >= 0:
                                                        valid_pawn_take_dests[square][0].append(
                                                                squares_map
                                                                [down-valid_range_up][right-valid_range_along]
                                                        )
                                                valid_pawn_take_dests[square][1].append(
                                                        squares_map
                                                        [down-valid_range_up][right+valid_range_along]
                                                )
                                        except IndexError:
                                                pass # pass for index out of range - don't
                                                     # try to generate dests for outside board.
                print("Pawn Take Dests:")
                for square, dests in valid_pawn_take_dests.items():
                        print(square, dests)
                return valid_pawn_take_dests

        def _get_valid_rook_dests(self):

                valid_rook_dests = {}

                for down, rank in enumerate(ChessBoard.squares_map):
                                for right, square in enumerate(rank):
                                        valid_rook_dests[square] = [ [],  # up range
                                                                     [],  # down range
                                                                     [],  # left range
                                                                     [] ] # right range

                                        valid_range_up = ChessBoard.HEIGHT - int(square[1])
                                        valid_range_down = ( (ChessBoard.HEIGHT - 1) 
                                                             - (ChessBoard.HEIGHT - int(square[1])) )

                                        valid_range_left = 0
                                        valid_range_right = ChessBoard.WIDTH - 1
                                        for position in ChessBoard.squares_map[valid_range_up]:
                                                if position == square:
                                                        break
                                                valid_range_left += 1
                                                valid_range_right -= 1

                                        valid_range_up = Board._board_range(valid_range_up)
                                        valid_range_down = Board._board_range(valid_range_down)
                                        valid_range_left = Board._board_range(valid_range_left)
                                        valid_range_right = Board._board_range(valid_range_right)

                                        for range in valid_range_up:
                                                valid_rook_dests[square][0].append(
                                                        ChessBoard.squares_map
                                                                [down-range][right]
                                                )
                                        for range in valid_range_down:
                                                valid_rook_dests[square][1].append(
                                                        ChessBoard.squares_map
                                                                [down+range][right]
                                                )    
                                        for range in valid_range_left:                                                   
                                                valid_rook_dests[square][2].append(
                                                        ChessBoard.squares_map
                                                                [down][right-range]
                                                ) 
                                        for range in valid_range_right:
                                                valid_rook_dests[square][3].append(
                                                        ChessBoard.squares_map
                                                                [down][right+range]
                                                )
                print("Valid Rook Dests:")
                for square, dests in valid_rook_dests.items():
                        print(square, dests)
                return valid_rook_dests


        def _get_valid_knight_dests(self):

                valid_knight_dests = {}
                for down, rank in enumerate(ChessBoard.squares_map):
                                for right, square in enumerate(rank):

                                        valid_knight_dests[square] = [ [],  # up-left range
                                                                       [],  # up-right range
                                                                       [],  # down-left range
                                                                       [],  # down-right range
                                                                       [],  # left-up
                                                                       [],  # left-down
                                                                       [],  # right-up
                                                                       [] ] # right-down

                                        valid_range_vert = 2    # Must be 2 only.
                                        valid_range_along = 1

                                        # first block is for vertical range greater than horizontal range
                                        if down > 1:                                        
                                                try:    
                                                        if (right-1) >= 0:
                                                                # up-left
                                                                valid_knight_dests[square][0].append(
                                                                        ChessBoard.squares_map
                                                                                [down-valid_range_vert][right-valid_range_along]
                                                                )

                                                        # up-right
                                                        valid_knight_dests[square][1].append(
                                                                ChessBoard.squares_map
                                                                        [down-valid_range_vert][right+valid_range_along]
                                                        )

                                                except IndexError:
                                                        pass

                                        if down < (ChessBoard.HEIGHT - 2):
                                                try:
                                                        if (right-1) >= 0:
                                                                # down-left
                                                                valid_knight_dests[square][2].append(
                                                                        ChessBoard.squares_map
                                                                                [down+valid_range_vert][right-valid_range_along]
                                                                )
                                                        # down-right
                                                        valid_knight_dests[square][3].append(
                                                                ChessBoard.squares_map
                                                                        [down+valid_range_vert][right+valid_range_along]
                                                        )
                                                except IndexError:
                                                        pass                                                     
                                        
                                        # second block is for horizontal range greater than vertical range.
                                        valid_range_along = 2
                                        valid_range_vert = 1

                                        # for along-up directions
                                        if down > 0:
                                                try:
                                                        if (right-2) >=0:
                                                                # left-up
                                                                valid_knight_dests[square][4].append(
                                                                        ChessBoard.squares_map
                                                                                [down-valid_range_vert][right-valid_range_along]
                                                                )
                                                        # right-up
                                                        valid_knight_dests[square][6].append(
                                                                ChessBoard.squares_map
                                                                        [down-valid_range_vert][right+valid_range_along]
                                                        )
                                                except IndexError:
                                                        pass

                                        # for along-down directions
                                        if down < (ChessBoard.HEIGHT - 1):
                                                try:
                                                        if (right-2) >= 0:
                                                                # left-down
                                                                valid_knight_dests[square][5].append(
                                                                        ChessBoard.squares_map
                                                                                [down+valid_range_vert][right-valid_range_along]
                                                                )                                                        
                                                        # right-down
                                                        valid_knight_dests[square][7].append(
                                                                ChessBoard.squares_map
                                                                        [down+valid_range_vert][right+valid_range_along]
                                                        )
                                                except IndexError:
                                                        pass
                print("Valid Knight Dests:")
                for square, dests in valid_knight_dests.items():
                        print(square, dests)
                return valid_knight_dests

        def _get_valid_bishop_dests(self):

                valid_bishop_dests = {}

                for down, rank in enumerate(ChessBoard.squares_map):
                                for right, square in enumerate(rank):
                            
                                        valid_bishop_dests[square] = [ [],  # up-left range
                                                                       [],  # up-right range
                                                                       [],  # down-left range
                                                                       [] ] # down-right range

                                        valid_range_up = ChessBoard.HEIGHT - int(square[1])
                                        valid_range_down = ( (ChessBoard.HEIGHT - 1) 
                                                                - (ChessBoard.HEIGHT - int(square[1])) )

                                        valid_range_left = 0
                                        valid_range_right = ChessBoard.WIDTH - 1
                                        for position in ChessBoard.squares_map[valid_range_up]:
                                                if position == square:
                                                        break
                                                valid_range_left += 1
                                                valid_range_right -= 1

                                        valid_range_up_left = Board._board_range(
                                                min(valid_range_up, valid_range_left)
                                        )
                                        valid_range_up_right = Board._board_range(
                                                min(valid_range_up, valid_range_right)
                                        )

                                        valid_range_down_left = Board._board_range(
                                                min(valid_range_down, valid_range_left)
                                        )
                                        valid_range_down_right = Board._board_range(
                                                min(valid_range_down, valid_range_right)
                                        )

                                        for range in valid_range_up_left:
                                                valid_bishop_dests[square][0].append(
                                                        ChessBoard.squares_map
                                                                [down-range][right-range]
                                                ) 
                                        for range in valid_range_up_right:
                                                valid_bishop_dests[square][1].append(
                                                        ChessBoard.squares_map
                                                                [down-range][right+range]
                                                )
                                        for range in valid_range_down_left:
                                                valid_bishop_dests[square][2].append(
                                                        ChessBoard.squares_map
                                                                [down+range][right-range]
                                                )
                                        for range in valid_range_down_right:
                                                valid_bishop_dests[square][3].append(
                                                        ChessBoard.squares_map
                                                                [down+range][right+range]
                                                )
                print("Valid Bishop Dests:")
                for square, dests in valid_bishop_dests.items():
                        print(square, dests)
                return valid_bishop_dests

        def _get_valid_queen_dests(self, valid_orthog_dests, valid_diag_dests):
                # combination of valid_rook_dests and valid_bishop_dests to
                # make up the valid queen dests.

                # merging the two dictionaries together - without modifying
                # the dictionaries in-place.
                valid_queen_dests = {square: dest_lists + valid_diag_dests[square] 
                                     for square, dest_lists in valid_orthog_dests.items()}
                
                print("Valid Queen Dests:")
                for square, dests in valid_queen_dests.items():
                        print(square, dests)

                return valid_queen_dests

        def _get_valid_king_dests(self):
                # This returns lists of pawn dests - specifically in one direction
                # up the board.
                valid_king_dests = {}

                valid_range_vert = 1
                valid_range_along = 1

                for down, rank in enumerate(ChessBoard.squares_map):
                        for right, square in enumerate(rank):
                                                              
                                valid_king_dests[square] = [ [],   # up dest
                                                             [],   # down dest
                                                             [],   # left dest
                                                             [],   # right dest
                                                             [],   # up-left dest
                                                             [],   # up-right dest
                                                             [],   # down-left dest
                                                             [] ]  # down-right dest
                                
                                if down > 0:
                                        # up
                                        valid_king_dests[square][0].append(
                                                ChessBoard.squares_map
                                                [down-valid_range_vert][right]
                                        )                                        
                                        try:
                                                # make sure we are not looping over the 
                                                # other side of the board.
                                                if (right-1) >= 0:
                                                        # up-left
                                                        valid_king_dests[square][4].append(
                                                                ChessBoard.squares_map
                                                                [down-valid_range_vert][right-valid_range_along]
                                                        )
                                                # up-right
                                                valid_king_dests[square][5].append(
                                                        ChessBoard.squares_map
                                                        [down-valid_range_vert][right+valid_range_along]
                                                )
                                        except IndexError:
                                                pass # pass for index out of range - don't
                                                # try to generate dests for outside board.
                                
                                if down < (ChessBoard.HEIGHT - 1):
                                        # down
                                        valid_king_dests[square][1].append(
                                                ChessBoard.squares_map
                                                [down+valid_range_vert][right]
                                        )                                        
                                        try:
                                                if (right-1) >= 0:
                                                        # down-left
                                                        valid_king_dests[square][6].append(
                                                                ChessBoard.squares_map
                                                                [down+valid_range_vert][right-valid_range_along]
                                                        )
                                                # down-right
                                                valid_king_dests[square][7].append(
                                                        ChessBoard.squares_map
                                                        [down+valid_range_vert][right+valid_range_along]
                                                )
                                        except IndexError:
                                                pass

                                try:
                                        if (right-1) >= 0:
                                                # left
                                                valid_king_dests[square][2].append(
                                                        ChessBoard.squares_map
                                                        [down][right-valid_range_along]
                                                )
                                        # right
                                        valid_king_dests[square][3].append(
                                                ChessBoard.squares_map
                                                [down][right+valid_range_along]
                                        )
                                except IndexError:
                                        pass                              
                
                print("Valid King Dests:")
                for square, dests in valid_king_dests.items():
                        print(square, dests)
                return valid_king_dests


class Controller:
       
        def __init__(self):
                self.board = ChessBoard()
                self.callibrate = PieceMoveRanges(
                        self.board.linked_map
                )
                self.rotate = RotateBoard180(
                        self.board.linked_map
                )
                self._setup_board()

                self.track = TrackPieces(
                        self.board.linked_map,
                        self._initial_white_positions,
                        self._initial_black_positions
                )
                self._display_board()
       
        def _setup_board(self):
                self._setup_white_pieces()
                self._setup_black_pieces()
               
        def _setup_white_pieces(self):
               
                self._initial_white_positions = [] 
                # self._white_pawns = SetPawn(
                #         self.board.linked_map, "d8", "h5",
                #                                "d3", "c5",
                #         # self.board.linked_map, "a2", "b2",
                #         #                        "c2", "d2",
                #         #                        "e2", "f2",
                #         #                        "g2", "h2" 
                # )
                # self._white_rook = SetRook(
                #         self.board.linked_map, "d5"
                # )
                # self._initial_white_positions += self._white_pawns.position_list
                # self._initial_white_positions += self._white_rook.position_list

                # ***** for setting rooks, need to include: ******
                        # Update rook positions to keep track of whether they
                        # have been moved.
                        # self.track.detect_rook_positions()

        def _setup_black_pieces(self):

                self._initial_black_positions = []
                # self._black_pawns = SetPawn(
                #         self.board.linked_map, "h8"#, "c6"
                #         # self.board.linked_map, "a7", "b7",
                #         #                        "c7", "d7",
                #         #                        "e7", "f7",
                #         #                        "g7", "h7" 
                # )
                # self._initial_black_positions += self._black_pawns.position_list

                # ***** for setting rooks, need to include: ******
                        # Update rook positions to keep track of whether they
                        # have been moved.
                        # self.track.detect_rook_positions()

        def move(self, start_pos, end_pos):
                
                self.callibrate() # should do this at the beginning or the end of the move - or both?
                
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
                            if end_pos in ChessBoard.squares_map[0] or end_pos in ChessBoard.squares_map[ChessBoard.HEIGHT-1]:
                                    promotion = PromotePawn(self.board.linked_map, end_pos)

                        else: # use take if end pos is in the list of positions
                              # for the opposite colour.
                            take = PawnTake(
                                self.board.linked_map,
                                start_pos,
                                end_pos
                            )
                            self.track.update_take(end_pos, take.piece_taken)

                        self.track.update_colour_position(start_pos, end_pos)
                        self._refresh_board()

                if piece == "r":

                        if not self.track.query_take(end_pos):
                                move = MoveRook(
                                        self.board.linked_map,
                                        start_pos,
                                        end_pos
                                )
                        else: # use take if end pos is in the list of positions
                              # for the opposite colour.
                                take = RookTake(
                                        self.board.linked_map,
                                        start_pos,
                                        end_pos
                                )
                                self.track.update_take(end_pos, take.piece_taken)
                        
                        if TrackPieces.WHITE_MOVE:
                                if start_pos in TrackPieces.WHITE_ROOKS_HAVE_MOVED.keys():
                                        self.track.update_rook_moves(start_pos)

                        if TrackPieces.BLACK_MOVE:
                                if start_pos in TrackPieces.BLACK_ROOKS_HAVE_MOVED.keys():
                                        self.track.update_rook_moves(start_pos)

                        self.track.update_colour_position(start_pos, end_pos)
                        self._refresh_board()                        

                if piece == "k":
                        if not self.track.query_take(end_pos):
                                move = MoveKnight(
                                        self.board.linked_map,
                                        start_pos,
                                        end_pos
                                )
                        else:# use take if end pos is in the list of positions
                              # for the opposite colour.
                                take = KnightTake(
                                        self.board.linked_map,
                                        start_pos,
                                        end_pos
                                )
                                self.track.update_take(end_pos, take.piece_taken)
                        
                        self.track.update_colour_position(start_pos, end_pos)
                        self._refresh_board()        

                if piece == "b":
                        if not self.track.query_take(end_pos):
                                move = MoveBishop(
                                        self.board.linked_map,
                                        start_pos,
                                        end_pos
                                )
                        else:# use take if end pos is in the list of positions
                              # for the opposite colour.
                                take = BishopTake(
                                        self.board.linked_map,
                                        start_pos,
                                        end_pos
                                )
                                self.track.update_take(end_pos, take.piece_taken)
                        
                        self.track.update_colour_position(start_pos, end_pos)
                        self._refresh_board() 

                if piece == "Q":
                        if not self.track.query_take(end_pos):
                                move = MoveQueen(
                                        self.board.linked_map,
                                        start_pos,
                                        end_pos
                                )
                        else:# use take if end pos is in the list of positions
                              # for the opposite colour.
                                take = QueenTake(
                                        self.board.linked_map,
                                        start_pos,
                                        end_pos
                                )
                                self.track.update_take(end_pos, take.piece_taken)
                        
                        self.track.update_colour_position(start_pos, end_pos)
                        self._refresh_board() 

                if piece == "K":
                        # check for castling - end pos two squares left or right of 
                        if (start_pos in TrackPieces.BACK_ROW_WHITE and
                            end_pos in TrackPieces.BACK_ROW_WHITE and 
                            end_pos == TrackPieces.BACK_ROW_WHITE[TrackPieces.BACK_ROW_WHITE.index(start_pos)+2] 
                            or 
                            start_pos in TrackPieces.BACK_ROW_WHITE and 
                            end_pos in TrackPieces.BACK_ROW_WHITE and 
                            end_pos == TrackPieces.BACK_ROW_WHITE[TrackPieces.BACK_ROW_WHITE.index(start_pos)-2]):

                                if TrackPieces.WHITE_MOVE:
                                                white_castle = Castle(
                                                        self.board.linked_map,
                                                        start_pos,
                                                        end_pos
                                                )

                        if (start_pos in TrackPieces.BACK_ROW_BLACK and
                            end_pos in TrackPieces.BACK_ROW_BLACK and 
                            end_pos == TrackPieces.BACK_ROW_BLACK[TrackPieces.BACK_ROW_BLACK.index(start_pos)+2] 
                            or 
                            start_pos in TrackPieces.BACK_ROW_BLACK and 
                            end_pos in TrackPieces.BACK_ROW_BLACK and 
                            end_pos == TrackPieces.BACK_ROW_BLACK[TrackPieces.BACK_ROW_BLACK.index(start_pos)-2]):
                                
                                if TrackPieces.BLACK_MOVE:
                                                black_castle = Castle(
                                                        self.board.linked_map,
                                                        start_pos,
                                                        end_pos
                                                )
                        
                        elif not self.track.query_take(end_pos):
                                move = MoveKing(
                                        self.board.linked_map,
                                        start_pos,
                                        end_pos
                                )
                        else: # use take if end pos is in the list of positions
                              # for the opposite colour.
                                take = KingTake(
                                        self.board.linked_map,
                                        start_pos,
                                        end_pos
                                )
                                self.track.update_take(end_pos, take.piece_taken)
                        
                        # this is executing every turn...
                        self.track.update_king_move()
                        self.track.update_colour_position(start_pos, end_pos)
                        self._refresh_board() 

                elif piece not in list("rbkQKp"):
                        raise ValueError("No Piece Here")

        def add(self, colour_piece, position, *positions):
                # for debug and testing purposes only.
                
                piece = colour_piece[1]
                if piece not in list("rbkQKp"):
                        raise ValueError("Invalid Piece Specified")

                position_list = []
                position_list.append(position)
                if positions:
                        for extra_position in list(positions):
                                position_list.append(extra_position)
                for square in position_list:
                        if len(self.board.linked_map[square]) == 2:
                                raise ValueError("Can't add piece here")

                colour = colour_piece[0]
                if colour == "w":
                        TrackPieces.WHITE_POSITIONS += position_list
                elif colour == "b":
                        TrackPieces.BLACK_POSITIONS += position_list
                else:
                        raise ValueError("Invalid Colour")

                if piece == "p":
                        new_piece = SetPawn( self.board.linked_map,
                                                          position,
                                                         *positions )                                             
                if piece == "r":
                        new_piece = SetRook( self.board.linked_map,
                                                          position,
                                                         *positions )
                        # Update rook positions to keep track of whether they
                        # have been moved.
                        self.track.detect_rook_positions()
                if piece == "k":
                        new_piece = SetKnight( self.board.linked_map,
                                                            position,
                                                           *positions ) 

                if piece == "b":
                        new_piece = SetBishop( self.board.linked_map,
                                                            position,
                                                           *positions )

                if piece == "Q":
                        new_piece = SetQueen( self.board.linked_map,
                                                            position,
                                                           *positions )

                if piece == "K":
                        new_piece = SetKing( self.board.linked_map,
                                                          position,
                                                         *positions )

                self._display_board()

        def white(self):
                # change to white turn - for debugging.
                TrackPieces.WHITE_MOVE = True
                TrackPieces.BLACK_MOVE = False
       
        def black(self):
                # change to black turn - for debugging.
                TrackPieces.WHITE_MOVE = False
                TrackPieces.BLACK_MOVE = True

        def _display_board(self):
                self.track()
                self.callibrate()
                self.board()
       
        def _refresh_board(self):
                self.board()
                self.rotate()
                self.track()
                self.board()


             







import time

start = time.time()

player = Controller()


# Below is the chess setup for white and black.
# player.add("wp", "a2", "b2", "c2",
#                  "d2", "e2", "f2",
#                  "g2", "h2")
# player.add("bp", "a7", "b7", "c7",
#                  "d7", "e7", "f7",
#                  "g7", "h7")

player.add("wr", "a1", "h1")                
# player.add("wk", "b1", "g1")
# player.add("wb", "c1", "f1")
# player.add("wQ", "d1")
player.add("wK", "e1")

player.add("br", "a8", "h8")                
# player.add("bk", "b8", "g8")
# player.add("bb", "c8", "f8")
# player.add("bQ", "d8")
player.add("bK", "e8")


player.move("e1", "e2")
player.move("e8", "c8")
player.move("e2", "e1")


end = time.time()

print("Time Taken: ", end-start)

# t = TestCastle(player.board.linked_map, "e1", "c1")
# t._execute_castle()






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