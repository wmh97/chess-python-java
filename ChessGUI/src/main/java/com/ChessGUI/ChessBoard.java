package com.ChessGUI;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.util.HashMap;

public class ChessBoard extends JLayeredPane{

    private int boardWidth;
    private int boardHeight;

    JLabel piece;

    private GameData gameData;

    // can look these up by squareNumber as index.
    static final String[] squareLabels = {
            "a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8",
            "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7",
            "a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6",
            "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5",
            "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4",
            "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3",
            "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2",
            "a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"
    };

    static HashMap<String, Integer> squareLabelsMap = new HashMap<String, Integer>();

    static String selectedPieceStartPos;
    static String selectedPieceEndPos;

    ChessBoard(int width, int height){

        this.setBoardWidth(width);
        this.setBoardHeight(height);
        this.setBounds(0, 0, getBoardWidth(), getBoardHeight());

        // setting the square labels map.
        for (int i=0; i<ChessBoard.squareLabels.length; i++){
            ChessBoard.squareLabelsMap.put(ChessBoard.squareLabels[i], i);
        }

        System.out.println(ChessBoard.squareLabelsMap);

        // prototype linked map data structure mimicking what linked map will be.
        // getting the square colour data as an array of chars.
        setGameData();

        // parse the piece images and store them in static variables.
        ChessPiece.parsePieceImages("src//main//java//com//ChessGUI//allPieces.png");

        this.addSquares(gameData.getSquareSymbols());
        //this.addPieces(gameData.getPieceSymbols()); //************ADDD BACK IN !!!!!***********


        // ***********TESTING**************


    }

    public int getBoardWidth(){
        return this.boardWidth;
    }
    public void setBoardWidth(int width){
        this.boardWidth = width;
    }
    public int getBoardHeight(){
        return this.boardHeight;
    }
    public void setBoardHeight(int height){
        this.boardHeight = height;
    }

    public GameData getGameData(){
        return this.gameData;
    }

    public void setGameData(){
        this.gameData = new GameData();
    }

    private void addSquares(char[] squareSymbols){
        for (int i=1; i<=squareSymbols.length; i++){

            int squareIndex = (i-1);
            this.add(
                    new BoardSquare(
                            squareSymbols[squareIndex],
                            squareIndex,
                            this.getBoardWidth(),
                            this.getBoardHeight()
                    ),
                    Integer.valueOf(0)
            );

        }
    }

    private void addPieces(String[] pieceSymbols){

        for (int i=1; i<=pieceSymbols.length; i++){
            if (pieceSymbols[i-1] != ""){

                //System.out.println(pieceSymbols[i-1]);

                int squareIndex = i-1;

                ChessPiece piece = new ChessPiece(
                        pieceSymbols[squareIndex],
                        squareIndex,
                        getBoardWidth(),
                        getBoardHeight()
                );
                this.add(piece.addLabel(), Integer.valueOf(1));

            }
        }

        ChessPiece.parentChessBoard = this;
    }

    public void reloadPieces(String boardSateString){

        // --> "a1-wr", "...", ...
        String[] splitStateString = boardSateString.split("/");

        // squares not in the state string.
        ArrayList<Integer> stateSquares = new ArrayList<Integer>();

        //HashMap<Integer, String> newPiecePositionsMap = new HashMap<Integer, String>();

        for (int i=0; i < splitStateString.length-1; i++){

            // "a1-wr" "--> "a1", "wr"
            String[] pieceData = splitStateString[i].split("-");
            String square = pieceData[0];
            String newPieceSymbol = pieceData[1];
            int squareNumber = ChessBoard.squareLabelsMap.get(square);

            stateSquares.add(Integer.valueOf(squareNumber));

            //System.out.println(String.format("Adding piece on square %s = %d", square, squareNumber));

            // if there is a piece on the square number...
            if (ChessPiece.squareNumberPieceMap.containsKey(squareNumber)) {

                //System.out.println("Square in state string already has a piece on.");

                ChessPiece currentPiece = ChessPiece.squareNumberPieceMap.get(squareNumber);

                // check if the current square piece is the same as the new piece.
                if (!currentPiece.getPieceSymbol().equals(newPieceSymbol)) {

                    //System.out.println(
                    //        String.format("We are removing a %s at %s and replacing it with a %s", currentPiece.getPieceSymbol(), square, newPieceSymbol)
                    //);

                    // remove the old piece from the squares map and also from the board,
                    this.remove(currentPiece);
                    ChessPiece.squareNumberPieceMap.remove(squareNumber, currentPiece);


                    // then add the new piece to the board and the squares map.
                    ChessPiece newPiece = new ChessPiece(newPieceSymbol, squareNumber, getBoardWidth(), getBoardHeight());
                    this.add(newPiece.addLabel(), Integer.valueOf(1));

                    this.revalidate();
                    this.repaint();

                } else {

                    //System.out.println("The current piece is the same as the new one, so skipping this square");
                }

            } else{

                //System.out.println(String.format("Adding %s on empty square %s", newPieceSymbol, square));
                ChessPiece newPiece = new ChessPiece(newPieceSymbol, squareNumber, getBoardWidth(), getBoardHeight());
                this.add(newPiece.addLabel(), Integer.valueOf(1));

                this.revalidate();
                this.repaint();

            }

            ChessPiece.parentChessBoard = this;
        }

        //System.out.println("Squares modified...");
        //System.out.println(stateSquares);

        // removing pieces from squares not included in the state string.
        // removing only if there is a piece on that square.
        for (int sqNo = 0; sqNo < 64; sqNo++){

            if (!stateSquares.contains(sqNo) && ChessPiece.squareNumberPieceMap.containsKey(sqNo)){

                //System.out.println(String.format("Square not in state string %d has a piece on it.", sqNo));

                ChessPiece currentPiece = ChessPiece.squareNumberPieceMap.get(sqNo);

                this.remove(currentPiece);
                ChessPiece.squareNumberPieceMap.remove(sqNo, currentPiece);

                //System.out.println("Removing the piece on the square.");

                this.revalidate();
                this.repaint();
            }

        }

    }


    static void highlightPositionSquare(Point position){

        int positionSquareNumber = BoardSquare.calcSquareNumber((int)position.getX(), (int)position.getY());
        BoardSquare square = BoardSquare.squareNumberMap.get(positionSquareNumber);

        // getting the pos marker associated with a square and
        // adding it to the square.
        square.displaySquarePosMarker();
    }

    static void removeHighlightPrevSquare(){

        // This method attempts to use less looping in order to remove the highlighting
        // from the previous square a piece was dragged over.
        //
        // This method removes highlights from the last square and surrounding squares.
        // This seems to improve the issues with the piece lagging on the first move, however
        // the 'refresh' rate is not as great as the for loop in the function above,
        // so there is some clipping of the piece as it passes over squares at high speed.
        //
        // Therefore there may be a tradeoff between number of squares refreshed,
        // and the smoothness of dragging/clipping of the piece icon.

        if (BoardSquare.lastHighlightedSquareNumber != -1){

            // Below lists for:
            //   - surrounding squares - 1 dist
            //   - surrounding squares - 2 dist (commented)

            int[] surroundingSquares = {
                    BoardSquare.lastHighlightedSquareNumber,
                    BoardSquare.lastHighlightedSquareNumber + 1,
                    BoardSquare.lastHighlightedSquareNumber - 1,
                    BoardSquare.lastHighlightedSquareNumber + 7,
                    BoardSquare.lastHighlightedSquareNumber + 8,
                    BoardSquare.lastHighlightedSquareNumber + 9,
                    BoardSquare.lastHighlightedSquareNumber - 7,
                    BoardSquare.lastHighlightedSquareNumber - 8,
                    BoardSquare.lastHighlightedSquareNumber - 9,
            };

//            int[] surroundingSquares = {
//                    BoardSquare.lastHighlightedSquareNumber,
//                    BoardSquare.lastHighlightedSquareNumber + 1,
//                    BoardSquare.lastHighlightedSquareNumber + 2,
//                    BoardSquare.lastHighlightedSquareNumber - 1,
//                    BoardSquare.lastHighlightedSquareNumber - 2,
//
//                    BoardSquare.lastHighlightedSquareNumber + 6,
//                    BoardSquare.lastHighlightedSquareNumber + 7,
//                    BoardSquare.lastHighlightedSquareNumber + 8,
//                    BoardSquare.lastHighlightedSquareNumber + 9,
//                    BoardSquare.lastHighlightedSquareNumber + 10,
//
//                    BoardSquare.lastHighlightedSquareNumber - 6,
//                    BoardSquare.lastHighlightedSquareNumber - 7,
//                    BoardSquare.lastHighlightedSquareNumber - 8,
//                    BoardSquare.lastHighlightedSquareNumber - 9,
//                    BoardSquare.lastHighlightedSquareNumber - 10
//            };

            for (int i = 0; i < surroundingSquares.length; i++){
                if ( 0 <= surroundingSquares[i] && surroundingSquares[i] < 64 ){

                    //System.out.println(String.format("Last h.sq = %d",  surroundingSquares[i]));
                    BoardSquare lastHighlightedSquare = BoardSquare.squareNumberMap.get(surroundingSquares[i]);
                    lastHighlightedSquare.setBackground(lastHighlightedSquare.getSquareColour());

                    lastHighlightedSquare.revalidate();
                    lastHighlightedSquare.repaint();
                }
            }
        }
    }
}
