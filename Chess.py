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
       

        squares_map = []
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

        def __call__(self):
                #self._print_chess_squares()
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

                #print(self._linked_map)

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
                        return True
                raise ValueError("Invalid Move")
                return False
               
        def _get_valid_dest(self):
                valid_range = self._get_valid_range()
                valid_dest = self._get_valid_orthog_dest(
                        valid_range
                )
                return valid_dest
               
        def _get_valid_range(self):
                valid_range = 1
                if self.start_pos in ChessBoard.squares_map[-2]:
                        valid_range = 2
                return valid_range
               
        def _get_valid_orthog_dest(self, valid_range):
                valid_dest = []
                valid_range = Board._board_range(
                        valid_range
                )
                flag_break = False
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
                                                flag_break = True # break to avoid going through the loop 
                                                break             # beyond finding the right square.
                                if flag_break:
                                        break                                                       
                print("Valid Dests: ", valid_dest)
                return valid_dest


class MoveRook(MovePawn):

        def __init__(self, linked_map, start_pos,
                                         end_pos):
                #super().__init__(linked_map, start_pos,
                #                             end_pos)
                
                self.linked_map = linked_map   ##### Change this block to super() when ready (with necessary args)
                self.start_pos = start_pos
                self.end_pos = end_pos
                self._validate_move()
                self._execute_move()
                MovePiece.MOVE_NUMBER += 1

        def _execute_move(self, piece="r"):   #################### change this to super() (with necessary args).
                self.linked_map[self.start_pos].pop() ############
                self.linked_map[self.end_pos].append(piece) ######


        def _validate_move(self):
                valid_dest = self._get_valid_dest()
                for dest_list in valid_dest:
                        if self.end_pos in dest_list:
                                valid_dest = []
                                return True
                raise ValueError("Invalid Move")
                return False

        def _get_valid_dest(self):
                valid_range_up, valid_range_down, valid_range_left, valid_range_right = self._get_valid_range()
                valid_dest = self._get_valid_orthog_dest(
                        valid_range_up, valid_range_down,
                        valid_range_left, valid_range_right
                )
                valid_dest = self._truncate_dest_list(valid_dest)
                return valid_dest

        def _truncate_dest_list(self, valid_dest_lists):
                # truncates the dest list if there is a piece blocking it.
                for dest_list in valid_dest_lists:
                        for square in dest_list:
                                if len(self.linked_map[square]) == 2:
                                        print(dest_list, "Blocked At:", square)
                                        del dest_list[dest_list.index(square):]
                                        print("Truncating to: ", dest_list)
                
                up, down, left, right = valid_dest_lists
                print("Valid Rook Dests Up: ", up)
                print("Valid Rook Dests Down: ", down)
                print("Valid Rook Dests Left: ", left)
                print("Valid Rook Dests Right: ", right)
                
                return valid_dest_lists

        def _get_valid_range(self):
                
                valid_range_up = ChessBoard.HEIGHT - int(self.start_pos[1])
                valid_range_down = (ChessBoard.HEIGHT - 1) - (ChessBoard.HEIGHT - int(self.start_pos[1]))

                valid_range_left = 0
                valid_range_right = ChessBoard.WIDTH - 1
                for square in ChessBoard.squares_map[valid_range_up]:
                        if self.start_pos == square:
                                break
                        valid_range_left += 1
                        valid_range_right -= 1

                return (valid_range_up, valid_range_down, 
                        valid_range_left, valid_range_right)

        def _get_valid_orthog_dest(self, valid_range_up, valid_range_down, 
                                         valid_range_left, valid_range_right):
                valid_dest_up = []
                valid_dest_down = []
                valid_dest_left = []
                valid_dest_right = []

                valid_range_up = Board._board_range(valid_range_up)
                valid_range_down = Board._board_range(valid_range_down)
                valid_range_left = Board._board_range(valid_range_left)
                valid_range_right = Board._board_range(valid_range_right)
                
                flag_break = False
                for down, rank in enumerate(
                        ChessBoard.squares_map):
                                for right, square in enumerate(
                                        rank
                                ):
                                        if self.start_pos == square:
                                                print("square: ", square)
                                                
                                                for range in valid_range_up:
                                                        valid_dest_up.append(
                                                        ChessBoard.squares_map
                                                        [down-range][right])
                                                for range in valid_range_down:
                                                        valid_dest_down.append(
                                                        ChessBoard.squares_map
                                                        [down+range][right])    
                                                for range in valid_range_left:                                                   
                                                        valid_dest_left.append(
                                                        ChessBoard.squares_map
                                                        [down][right-range]) 
                                                for range in valid_range_right:
                                                        valid_dest_right.append(
                                                        ChessBoard.squares_map
                                                        [down][right+range])
                                                flag_break = True
                                                break
                                if flag_break:
                                        break
                                

                valid_dest = [valid_dest_up, valid_dest_down, 
                        valid_dest_left, valid_dest_right]

                return valid_dest


class PawnTake(MovePawn):
    # if target square in take range...
    
    def __init__(self, linked_map, start_pos, end_pos):
        super().__init__(linked_map, start_pos, end_pos)

    def _execute_move(self, piece="p"):
            if self._validate_move():
                    self.linked_map[self.end_pos].pop()
                    super(MovePawn, self)._execute_move(piece="p") # Trimming the MRO so we use the code from MovePiece

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
            
            flag_break = False
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
                                            flag_break = True
                                            break
                            if flag_break:
                                    break
                                                    
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


class PieceMoveRanges:

        VALID_PAWN_DESTS = {}
        VALID_PAWN_TAKE_DESTS = {}
        VALID_ROOK_DESTS = {}
        
        def __init__(self):
                PieceMoveRanges.VALID_PAWN_DESTS = self._get_valid_pawn_dests()
                PieceMoveRanges.VALID_TAKE_PAWN_DESTS = self._get_valid_pawn_take_dests()
                PieceMoveRanges.VALID_ROOK_DESTS = self._get_valid_rook_dests()

        def _get_valid_pawn_dests(self):
                # This returns lists of pawn dests - specifically in one direction
                # up the board.
                valid_pawn_dests = {}

                valid_start_range = 2
                valid_range = 1

                for down, rank in enumerate(ChessBoard.squares_map):
                        for right, square in enumerate(rank):
                                valid_pawn_dests[square] = [ [] ]  # up dests
                                if down == (ChessBoard.HEIGHT - 1) - 1:
                                        valid_pawn_dests[square][0].append(
                                                ChessBoard.squares_map
                                                        [down-valid_range][right]
                                        )
                                        valid_pawn_dests[square][0].append(
                                                ChessBoard.squares_map
                                                        [down-valid_start_range][right]
                                        )
                                if down > 0:
                                        valid_pawn_dests[square][0].append(
                                                ChessBoard.squares_map
                                                        [down-valid_range][right]
                                        )
                for square, dests in valid_pawn_dests.items():
                        print(square, dests)
                return valid_pawn_dests

        def _get_valid_pawn_take_dests(self):
                # This returns lists of pawn dests - specifically in one direction
                # up the board.
                valid_pawn_take_dests = {}

                valid_range_up = 1
                valid_range_along = 1

                for down, rank in enumerate(ChessBoard.squares_map):
                        for right, square in enumerate(rank):
                                valid_pawn_take_dests[square] = [ [],   # up-left dests
                                                                  [] ]  # up-right dests
                                if down > 0:
                                        try:
                                                # make sure we are not looping over the board.
                                                if (right-1) >= 0:
                                                        valid_pawn_take_dests[square][0].append(
                                                                ChessBoard.squares_map
                                                                        [down-valid_range_up][right-valid_range_along]
                                                        )
                                                valid_pawn_take_dests[square][1].append(
                                                        ChessBoard.squares_map
                                                                [down-valid_range_up][right+valid_range_along]
                                                )
                                        except:
                                                pass # pass for index out of range - don't
                                                     # try to generate dests for outside board.
                for square, dests in valid_pawn_take_dests.items():
                        print(square, dests)
                return valid_pawn_ranges

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
                                                             - (ChessBoard.HEIGHT 
                                                             - int(square[1]))       )

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
                for square, dests in valid_rook_dests.items():
                        print(square, dests)
                        
                return valid_rook_dests


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
                        self.board.linked_map, "d8", "h5",
                                               "d3", "c5"
                        # self.board.linked_map, "a2", "b2",
                        #                        "c2", "d2",
                        #                        "e2", "f2",
                        #                        "g2", "h2" 
                    )
                self._white_rook = SetRook(
                        self.board.linked_map, "d5"
                )
                self._white_positions += self._white_pawns.position_list
                self._white_positions += self._white_rook.position_list

        def _setup_black_pieces(self):

                self._black_positions = []
                self._black_pawns = SetPawn(
                        self.board.linked_map, "h8"

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

                if piece == "r":

                        move = MoveRook(
                                self.board.linked_map,
                                start_pos,
                                end_pos
                        )
                        
                        self.track.update_colour_position(start_pos, end_pos)
                        self._refresh_board()                        
               
                elif piece not in list("rbkQKp"):
                        raise ValueError("No Piece Here")
       
        def _display_board(self):
                self.track()
                self.board()
       
        def _refresh_board(self):
                self.board()
                self.rotate()
                self.track()
                self.board()
       
import time

start = time.time()

player = Controller()
player.move("d5", "e5")
player.move("h8", "h7")
player.move("e5", "f5")

end = time.time()

print("Time Taken: ", end-start)



        
# start = time.time()

# testrookrange = PieceMoveRanges()
# testrookrange._get_valid_rook_dests()

# end = time.time()
# print("Time Taken: ", end-start)




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