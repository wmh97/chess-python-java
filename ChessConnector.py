from Chess import *
import json # convert dictionary x into JSON string: y = json.dumps(x)
import sys

class ChessConnector:

    GAME_JSON = {}

    def __init__(self, controller):
        self.controller = controller

    def __call__(self, *, mode):
        if mode == "export":
            ChessConnector.GAME_JSON = self._get_game_json()
            self._export_game_json(ChessConnector.GAME_JSON)
        if mode == "import":
            ChessConnector.GAME_JSON = self._import_game_json()
            self._load_game_json(ChessConnector.GAME_JSON)

    def _import_game_json(self):
        with open(r"C:\Users\willi\Desktop\Chess_Python\game_json.json", "r") as json_infile:
            game_json = json.load(json_infile)
        json_infile.close()
        return game_json

    def _export_game_json(self, game_json_dict):
        game_json = json.dumps(game_json_dict)
        # need more specific path
        with open(r"C:\Users\willi\Desktop\Chess_Python\game_json.json", "w") as json_outfile:
            json_outfile.write(game_json)
        json_outfile.close()

    def _get_game_json(self):
        # export all the data that is required for the setup of the board and all flags.
        # build a JSON format.
        #
        # Need the following data:
        #
        # ---(A)--- Every data structure that is updated as the game goes on.
        # (1) linked map
        # (2) colour turn - for white, black
        # (3) colour positions - for white, black
        # (4) taken by colour - for white, black
        # (5) colour castling data - rooks/kings have moved
        # (5) current position string
        # (6) game position strings
        # 
        # ---(B)--- Every data structure that is generated at setup.
        # (1) valid move dests per piece
        # (2) valid take dests per piece (for pawns)
        # (3) truncated board dests per piece
        # (4) truncated take dests per piece (for pawns)
        # (5) truncated board check dests      *** what were these?
        # (6) truncated board check take dests ***
        # (7) non truncated board dests
        # (8) non truncated take dests
        # (9) squares map
        # (10) reversed squares map
        # (11) squares coordinate map
        #
        # ---(C)--- Every flag/small data that is not stored in the position string
        # (1) move number
        # (2) colour in check - for white, black
        # (3) colour in surrounding check - for white, black
        # (4) en-passant square
        #
        # ---(D)--- Every flag that shows the final outcome of the game (***NOT CREATED YET***)
        # (1) checkmate
        # (2) stalemate
        # (3) draw by repetition
        # (4) draw by lack of material (*** not yet in the game itself ***)
        #
        # ---(E)--- Further data that allows recreation of the game from this JSON
        # (1) History of moves in the game
        #
        
        game_json = {}
        
        # ---(A)---
        game_json["linked_map"] = ChessBoard.LINKED_MAP #self.linked_map
        game_json["TrackPieces.WHITE_MOVE"] = TrackPieces.WHITE_MOVE
        game_json["TrackPieces.BLACK_MOVE"] = TrackPieces.BLACK_MOVE
        game_json["TrackPieces.WHITE_POSITIONS"] = TrackPieces.WHITE_POSITIONS
        game_json["TrackPieces.BLACK_POSITIONS"] = TrackPieces.BLACK_POSITIONS
        # game_json[""] = taken by white
        # game_json[""] = taken by black

        # game_json[""] = current_position_string
        game_json["Controller.CURRENT_POSITION_STRING"] = Controller.CURRENT_POSITION_STRING

        game_json["TrackPieces.WHITE_ROOKS_HAVE_MOVED"] = TrackPieces.WHITE_ROOKS_HAVE_MOVED
        game_json["TrackPieces.BLACK_ROOKS_HAVE_MOVED"] = TrackPieces.BLACK_ROOKS_HAVE_MOVED
        game_json["TrackPieces.WHITE_KING_HAS_MOVED"] = TrackPieces.WHITE_KING_HAS_MOVED
        game_json["TrackPieces.BLACK_KING_HAS_MOVED"] = TrackPieces.BLACK_KING_HAS_MOVED
        game_json["Controller.GAME_POSITION_STRINGS"] = Controller.GAME_POSITION_STRINGS

        # ---(B)---
        game_json["PieceMoveRanges.VALID_PAWN_DESTS_UP"] = PieceMoveRanges.VALID_PAWN_DESTS_UP
        game_json["PieceMoveRanges.VALID_PAWN_DESTS_DOWN"] = PieceMoveRanges.VALID_PAWN_DESTS_DOWN
        game_json["PieceMoveRanges.VALID_PAWN_TAKE_DESTS_UP"] = PieceMoveRanges.VALID_PAWN_TAKE_DESTS_UP
        game_json["PieceMoveRanges.VALID_PAWN_TAKE_DESTS_DOWN"] = PieceMoveRanges.VALID_PAWN_TAKE_DESTS_DOWN
        game_json["PieceMoveRanges.VALID_ROOK_DESTS"] = PieceMoveRanges.VALID_ROOK_DESTS
        game_json["PieceMoveRanges.VALID_KNIGHT_DESTS"] = PieceMoveRanges.VALID_KNIGHT_DESTS
        game_json["PieceMoveRanges.VALID_BISHOP_DESTS"] = PieceMoveRanges.VALID_BISHOP_DESTS
        game_json["PieceMoveRanges.VALID_QUEEN_DESTS"] = PieceMoveRanges.VALID_QUEEN_DESTS
        game_json["PieceMoveRanges.VALID_KING_DESTS"] = PieceMoveRanges.VALID_KING_DESTS
        game_json["PieceMoveRanges.TRUNCATED_BOARD_DESTS"] = PieceMoveRanges.TRUNCATED_BOARD_DESTS
        game_json["PieceMoveRanges.TRUNCATED_BOARD_TAKE_DESTS"] = PieceMoveRanges.TRUNCATED_BOARD_TAKE_DESTS
        game_json["PieceMoveRanges.TRUNCATED_BOARD_CHECK_DESTS"] = PieceMoveRanges.TRUNCATED_BOARD_CHECK_DESTS
        game_json["PieceMoveRanges.TRUNCATED_BOARD_CHECK_TAKE_DESTS"] = PieceMoveRanges.TRUNCATED_BOARD_CHECK_TAKE_DESTS
        game_json["PieceMoveRanges.NON_TRUNC_BOARD_DESTS"] = PieceMoveRanges.NON_TRUNC_BOARD_DESTS
        game_json["PieceMoveRanges.NON_TRUNC_BOARD_TAKE_DESTS"] = PieceMoveRanges.NON_TRUNC_BOARD_TAKE_DESTS
        game_json["ChessBoard.squares_map"] = ChessBoard.squares_map
        game_json["ChessBoard.rotated_squares_map"] = ChessBoard.rotated_squares_map
        game_json["ChessBoard.SQUARES_MAP_COORDS"] = ChessBoard.SQUARES_MAP_COORDS

        # ---(C)---
        game_json["MovePiece.MOVE_NUMBER"] = MovePiece.MOVE_NUMBER
        game_json["TrackPieces.WHITE_IN_CHECK"] = TrackPieces.WHITE_IN_CHECK
        game_json["TrackPieces.BLACK_IN_CHECK"] = TrackPieces.BLACK_IN_CHECK
        game_json["TrackPieces.WHITE_SURROUNDING_CHECK"] = TrackPieces.WHITE_SURROUNDING_CHECK
        game_json["TrackPieces.BLACK_SURROUNDING_CHECK"] = TrackPieces.BLACK_SURROUNDING_CHECK
        game_json["TrackPieces.EN_PASSANT_SQUARES"] = TrackPieces.EN_PASSANT_SQUARES

        # ---(D)---
        # game_json[""] = check_mate
        # game_json[""] = stalemate
        # game_json[""] = draw_by_repetition
        # game_json[""] = draw_by_lack_of_material

        # ---(E)---
        # game_json[""] = move_history

        return game_json
        
    def _load_game_json(self, game_json):
        
        # ---(A)---
        ChessBoard.LINKED_MAP = game_json["linked_map"]
        TrackPieces.WHITE_MOVE = game_json["TrackPieces.WHITE_MOVE"] 
        TrackPieces.BLACK_MOVE = game_json["TrackPieces.BLACK_MOVE"] 
        TrackPieces.WHITE_POSITIONS = game_json["TrackPieces.WHITE_POSITIONS"] 
        TrackPieces.BLACK_POSITIONS = game_json["TrackPieces.BLACK_POSITIONS"] 
        # game_json[""] = taken by white
        # game_json[""] = taken by black

        # game_json[""] = current_position_string
        Controller.CURRENT_POSITION_STRING = game_json["Controller.CURRENT_POSITION_STRING"]

        TrackPieces.WHITE_ROOKS_HAVE_MOVED = game_json["TrackPieces.WHITE_ROOKS_HAVE_MOVED"] 
        TrackPieces.BLACK_ROOKS_HAVE_MOVED = game_json["TrackPieces.BLACK_ROOKS_HAVE_MOVED"] 
        TrackPieces.WHITE_KING_HAS_MOVED = game_json["TrackPieces.WHITE_KING_HAS_MOVED"] 
        TrackPieces.BLACK_KING_HAS_MOVED = game_json["TrackPieces.BLACK_KING_HAS_MOVED"] 
        Controller.GAME_POSITION_STRINGS = game_json["Controller.GAME_POSITION_STRINGS"] 

        # ---(B)---
        PieceMoveRanges.VALID_PAWN_DESTS_UP = game_json["PieceMoveRanges.VALID_PAWN_DESTS_UP"] 
        PieceMoveRanges.VALID_PAWN_DESTS_DOWN = game_json["PieceMoveRanges.VALID_PAWN_DESTS_DOWN"] 
        PieceMoveRanges.VALID_PAWN_TAKE_DESTS_UP = game_json["PieceMoveRanges.VALID_PAWN_TAKE_DESTS_UP"] 
        PieceMoveRanges.VALID_PAWN_TAKE_DESTS_DOWN = game_json["PieceMoveRanges.VALID_PAWN_TAKE_DESTS_DOWN"] 
        PieceMoveRanges.VALID_ROOK_DESTS = game_json["PieceMoveRanges.VALID_ROOK_DESTS"] 
        PieceMoveRanges.VALID_KNIGHT_DESTS = game_json["PieceMoveRanges.VALID_KNIGHT_DESTS"] 
        PieceMoveRanges.VALID_BISHOP_DESTS = game_json["PieceMoveRanges.VALID_BISHOP_DESTS"] 
        PieceMoveRanges.VALID_QUEEN_DESTS = game_json["PieceMoveRanges.VALID_QUEEN_DESTS"] 
        PieceMoveRanges.VALID_KING_DESTS = game_json["PieceMoveRanges.VALID_KING_DESTS"] 
        PieceMoveRanges.TRUNCATED_BOARD_DESTS = game_json["PieceMoveRanges.TRUNCATED_BOARD_DESTS"]
        PieceMoveRanges.TRUNCATED_BOARD_TAKE_DESTS = game_json["PieceMoveRanges.TRUNCATED_BOARD_TAKE_DESTS"] 
        PieceMoveRanges.TRUNCATED_BOARD_CHECK_DESTS = game_json["PieceMoveRanges.TRUNCATED_BOARD_CHECK_DESTS"] 
        PieceMoveRanges.TRUNCATED_BOARD_CHECK_TAKE_DESTS = game_json["PieceMoveRanges.TRUNCATED_BOARD_CHECK_TAKE_DESTS"] 
        PieceMoveRanges.NON_TRUNC_BOARD_DESTS = game_json["PieceMoveRanges.NON_TRUNC_BOARD_DESTS"] 
        PieceMoveRanges.NON_TRUNC_BOARD_TAKE_DESTS = game_json["PieceMoveRanges.NON_TRUNC_BOARD_TAKE_DESTS"] 
        ChessBoard.squares_map = game_json["ChessBoard.squares_map"] 
        ChessBoard.rotated_squares_map = game_json["ChessBoard.rotated_squares_map"] 
        ChessBoard.SQUARES_MAP_COORDS = game_json["ChessBoard.SQUARES_MAP_COORDS"] 

        # ---(C)---
        MovePiece.MOVE_NUMBER = game_json["MovePiece.MOVE_NUMBER"] 
        TrackPieces.WHITE_IN_CHECK = game_json["TrackPieces.WHITE_IN_CHECK"] 
        TrackPieces.BLACK_IN_CHECK = game_json["TrackPieces.BLACK_IN_CHECK"] 
        TrackPieces.WHITE_SURROUNDING_CHECK = game_json["TrackPieces.WHITE_SURROUNDING_CHECK"] 
        TrackPieces.BLACK_SURROUNDING_CHECK = game_json["TrackPieces.BLACK_SURROUNDING_CHECK"] 
        TrackPieces.EN_PASSANT_SQUARES = game_json["TrackPieces.EN_PASSANT_SQUARES"]

        # ---(D)---
        # game_json[""] = check_mate
        # game_json[""] = stalemate
        # game_json[""] = draw_by_repetition
        # game_json[""] = draw_by_lack_of_material

        # ---(E)---
        # game_json[""] = move_history

# def main():

import time
start = time.time()

Controller.LOAD_FROM_JSON = False

player = Controller()
connector = ChessConnector(player)    


# connector(mode="import")

# #Controller.CURRENT_POSITION_STRING = "b7-wr/e3-wK/e7-wp/g2-wp/a3-bK/b2-bp/b-b.c.0-w.c.0-b.ep.0"

# connector(mode="export")

# print("String is: ", Controller.CURRENT_POSITION_STRING)

# player._display_board()

#player.move("e7", "e8")

# Below is the chess setup for white and black.
# player.add("wp", "a2", "b2", "c2",
#                 "d2", "e2", "f2",
#                 "g2", "h2")
# player.add("bp", "a7", "b7", "c7",
#                 "d7", "e7", "f7",
#                 "g7", "h7")

# player.add("wr", "a1", "h1")                
# player.add("wk", "b1", "g1")
# player.add("wb", "c1", "f1")
# player.add("wQ", "d1")
# player.add("wK", "e1")

# player.add("br", "a8", "h8")                
# player.add("bk", "b8", "g8")
# player.add("bb", "c8", "f8")
# player.add("bQ", "d8")
# player.add("bK", "e8")

# Controller.CURRENT_POSITION_STRING = player._get_current_position_string(ChessBoard.LINKED_MAP, colour="w", opp_colour="b")

# # connector(mode="import")
# player._display_board()
# connector(mode="export")

# print(Controller.CURRENT_POSITION_STRING)

def main():

    connector(mode="import")

    # player._display_board()

    start_pos = sys.argv[1]
    end_pos = sys.argv[2]

    player.move(start_pos, end_pos)

    connector(mode="export")

    print("JSON EXPORTED")

    # player.move("d2", "d4")
    # player.move("g8", "f6")
    # player.move("c2", "c4")
    # player.move("g7", "g6")
    # player.move("f2", "f3")
    # player.move("d7", "d6")
    # player.move("e2", "e4")
    # player.move("e7", "e5")
    # player.move("d4", "d5")
    # player.move("f6", "h5")
    # player.move("c1", "e3")
    # player.move("f8", "g7")
    # player.move("b1", "c3")
    # player.move("e8", "g8")
    # player.move("d1", "d2")
    # player.move("f7", "f5")
    # player.move("e1", "c1")
    # player.move("f5", "f4")
    # player.move("e3", "f2")
    # player.move("g7", "f6")
    # player.move("d2", "e1")
    # player.move("b8", "d7")
    # player.move("c1", "b1")
    # player.move("f6", "e7")
    # player.move("g2", "g3")
    # player.move("c7", "c5")
    # player.move("d5", "c6") # en-passant
    # player.move("b7", "c6")
    # player.move("c4", "c5")
    # player.move("d6", "c5")
    # player.move("c3", "a4")
    # player.move("d8", "c7")
    # player.move("e1", "c3")
    # player.move("a8", "b8")
    # player.move("f1", "h3")
    # player.move("d7", "b6")
    # player.move("a4", "c5")
    # player.move("f8", "f7")
    # player.move("b2", "b3")
    # player.move("f4", "g3")
    # player.move("h2", "g3")
    # player.move("e7", "c5")
    # player.move("c3", "c5")
    # player.move("h5", "g7")
    # player.move("d1", "c1")
    # player.move("c8", "e6")
    # player.move("c5", "c6")
    # player.move("c7", "e7")
    # player.move("c6", "c5")
    # player.move("e7", "f6")
    # player.move("h3", "g2")
    # player.move("f7", "b7")
    # player.move("b1", "a1")
    # player.move("b6", "d7")
    # player.move("c5", "d6")
    # player.move("g7", "e8")
    # player.move("d6", "a6")
    # player.move("e6", "b3")
    # player.move("a6", "f6")
    # player.move("e8", "f6")
    # player.move("a2", "b3")
    # player.move("b7", "b3")
    # player.move("c1", "c2")
    # player.move("b3", "b1")
    # player.move("a1", "a2")
    # player.move("b1", "b4")
    # player.move("a2", "a1")
    # player.move("b4", "b1")
    # player.move("a1", "a2")
    # player.move("b1", "b4")
    # player.move("a2", "a1")

    # connector(mode="export")
    # print(ChessConnector.GAME_JSON)

    # player.move("b4", "b1")


    # player._refresh_board()

    # print(Controller.GAME_POSITION_STRINGS)
    # for key in Controller.GAME_POSITION_STRINGS.keys():
    #         print(key.split("/")[-1])

# end = time.time()

# print("Time Taken: ", end-start)


if __name__ == '__main__':
    main()

