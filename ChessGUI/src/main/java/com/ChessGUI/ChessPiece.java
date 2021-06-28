package com.ChessGUI;

import java.awt.*;
import java.awt.event.*;
import java.util.HashMap;
import javax.swing.*;

public class ChessPiece extends JLabel implements MouseListener, MouseMotionListener{

    static HashMap<Integer, ChessPiece> squareNumberPieceMap = new HashMap<Integer, ChessPiece>();
    //private static int squareNumber = 0;

    private Point position;
    private ImageIcon pieceIcon;

    JLabel pieceLabel;

    private int squareNumber;
    private String pieceLocation;
    private int boardWidth;
    private int boardHeight;

    static PieceImageParser pieceImageParser;
    static ImageIcon whiteKing;
    static ImageIcon whiteQueen;
    static ImageIcon whiteBishop;
    static ImageIcon whiteKnight;
    static ImageIcon whiteRook;
    static ImageIcon whitePawn;
    static ImageIcon blackKing;
    static ImageIcon blackQueen;
    static ImageIcon blackBishop;
    static ImageIcon blackKnight;
    static ImageIcon blackRook;
    static ImageIcon blackPawn;

    private String pieceSymbol;

    static ChessBoard parentChessBoard;

    ChessPiece(String pieceSymbol, int squareNumber, int boardWidth, int boardHeight){

        this.boardWidth = boardWidth;
        this.boardHeight = boardHeight;

        // piece is a label with a png icon on it.
        // setting the image based on the piece symbol.
        switch(pieceSymbol){
            case "br":  setPieceIcon(blackRook, boardWidth/8, boardHeight/8);
            break;
            case "bk": setPieceIcon(blackKnight, boardWidth/8, boardHeight/8);
            break;
            case "bb": setPieceIcon(blackBishop, boardWidth/8, boardHeight/8);
            break;
            case "bQ": setPieceIcon(blackQueen, boardWidth/8, boardHeight/8);
            break;
            case "bK": setPieceIcon(blackKing, boardWidth/8, boardHeight/8);
            break;
            case "bp": setPieceIcon(blackPawn, boardWidth/8, boardHeight/8);
            break;
            case "wr": setPieceIcon(whiteRook, boardWidth/8, boardHeight/8);
            break;
            case "wk": setPieceIcon(whiteKnight, boardWidth/8, boardHeight/8);
            break;
            case "wb": setPieceIcon(whiteBishop, boardWidth/8, boardHeight/8);
            break;
            case "wQ": setPieceIcon(whiteQueen, boardWidth/8, boardHeight/8);
            break;
            case "wK": setPieceIcon(whiteKing, boardWidth/8, boardHeight/8);
            break;
            case "wp": setPieceIcon(whitePawn, boardWidth/8, boardHeight/8);
            break;
            default: return; // throw error
        }

        setPieceSymbol(pieceSymbol);
        setPosition(squareNumber, boardWidth);

        setSquareNumber(squareNumber);
        setPieceLocation(squareNumber);

        ChessPiece.squareNumberPieceMap.put(squareNumber, this);

        this.addPieceListeners();

    }

    public ImageIcon getPieceIcon(){
        return this.pieceIcon;
    }

    public void setPieceIcon(String iconPath, int width, int height){
        ImageIcon icon = new ImageIcon(iconPath);
        this.pieceIcon = resizeIcon(icon, width, height);
    }

    public void setPieceIcon(ImageIcon icon, int width, int height){
        this.pieceIcon = resizeIcon(icon, width, height);
    }

    public String getPieceSymbol(){
        return this.pieceSymbol;
    }

    public void setPieceSymbol(String pieceSymbol){
        this.pieceSymbol = pieceSymbol;
    }

    public int getSquareNumber(){
        return this.squareNumber;
    }

    public void setSquareNumber(int squareNumber){
        this.squareNumber = squareNumber;
    }

    public String getPieceLocation(){
        return this.pieceLocation;
    }

    public void setPieceLocation(int squareNumber){
        this.pieceLocation = ChessBoard.squareLabels[squareNumber];
    }

    private ImageIcon resizeIcon(ImageIcon icon, int width, int height){

        Image image = icon.getImage(); // transform it
        Image newImage = image.getScaledInstance(width, height, java.awt.Image.SCALE_SMOOTH); // scale it the smooth way

        return (new ImageIcon(newImage)); // transform it back
    }

    public Point getPosition(){
        return this.position;
    }

    public void setPosition(int squareNumber, int boardLength){

        // remove the old position from the hash map and add the new one,
        // only if we have a position stored already.
        if (this.position != null){
            ChessPiece.squareNumberPieceMap.remove(
                    BoardSquare.calcSquareNumber((int)this.position.getX(), (int)this.position.getY())
            );
            ChessPiece.squareNumberPieceMap.put(squareNumber, this);
        }

        int newXPos = BoardSquare.calcBoardXPos(squareNumber, boardLength);
        int newYPos = BoardSquare.calcBoardYPos(squareNumber, boardLength);
        this.position = new Point(newXPos, newYPos);
    }

    public void setPosition(Point pos){
        this.position = new Point((int)pos.getX(), (int)pos.getY());
    }

    public JLabel addLabel(){

        this.setIcon(this.getPieceIcon());
        this.setVerticalAlignment(JLabel.CENTER);
        this.setHorizontalAlignment(JLabel.CENTER);
        this.setBounds(
                (int)this.getPosition().getX(),
                (int)this.getPosition().getY(),
                this.boardWidth/8,
                this.boardHeight/8
        );
        this.setVisible(true);

        return this;
    }

    public void refreshPiece(){

        this.setBounds(
                (int)this.getPosition().getX(),
                (int)this.getPosition().getY(),
                this.boardWidth/8,
                this.boardHeight/8
        );

    }

    public void movePiece(MouseEvent e, boolean dropped){

        // the listener is on the label itself so the coordinate is relative
        // to the corner of the label (0,0). Therefore any movement will simply
        // cause an offset from zero on this coordinate.
        Point newPos = e.getPoint();

        // for the first move - speed is sometimes slow and you can see the
        // y pos go negative. testing flipping positive again *** this might not work ***
//        if (newPos.getY() < 0){
//            System.out.println("Flipping y pos");
//            newPos = new Point((int)newPos.getX(), (int)newPos.getY()*-1);
//        }

        System.out.println(newPos);

        // making a point at the centre of the piece label.
        // This coordinate is relative to the whole board.
        Point piecePos = new Point(
                (int)this.getPosition().getX() - (int)boardWidth/16,
                (int)this.getPosition().getY() - (int)boardHeight/16
        );

        // moving the piece label by the amount the mouse has moved.
        // i.e. the offset from zero.
        piecePos.translate((int)newPos.getX(), (int)newPos.getY());

        this.setPosition(piecePos);

        // leaves behind label on square after move - this might be a good thing though.
        // *************************************************************************************************************
         // **** NOTE: this is making the first move slow for some reason ************
        // ***** must be because none of the squares are highlighted with label????? ***********************************
        ChessBoard.removeHighlightPrevSquare();
        ChessBoard.highlightPositionSquare(piecePos);



        if (!dropped){
            this.setPosition(piecePos);

        } else {


            Point dropSquare = this.getDropSquare(piecePos);
            int dropSqNo = BoardSquare.calcSquareNumber(
                    (int)dropSquare.getX(),
                    (int)dropSquare.getY()
            );


            // remove the piece from where it was unless we are putting it back on the square it started on.
            if (!ChessBoard.selectedPieceStartPos.equals(ChessBoard.selectedPieceEndPos)){


                ChessPiece.squareNumberPieceMap.remove(this.getSquareNumber(), this);


                // if we are dropping it on a square with a different piece on, we remove that piece
                // from the board and the sqNo piece map.
                if (ChessPiece.squareNumberPieceMap.containsKey(dropSqNo)){

                    ChessPiece pieceToRemove = ChessPiece.squareNumberPieceMap.get(dropSqNo);
                    this.parentChessBoard.remove(pieceToRemove);
                    ChessPiece.squareNumberPieceMap.remove(
                        dropSqNo,
                        pieceToRemove
                    );

                }

                // REMOVE?????????????????????????????????????????????????????????????????????
                // putting the new sq no and piece we have dropped into the sq no piece map.
                ChessPiece.squareNumberPieceMap.put(dropSqNo, this);


            }

            // if we have dropped the piece, update the position and the square number of the piece.
            this.setPosition(dropSquare);
            this.setSquareNumber(dropSqNo);




        }
        this.refreshPiece();




    }

    public Point getDropSquare(Point droppedPos){

        // get the position, work out which square it is in,
        // then drop it to the centre of that square.
        double xPos = droppedPos.getX();
        double yPos = droppedPos.getY();

        System.out.println(String.format("Drop Square No. %d", BoardSquare.calcSquareNumber((int)xPos, (int)yPos)));

        int squareNumber = BoardSquare.calcSquareNumber((int)xPos, (int)yPos);
        int squareCentredXPos = BoardSquare.calcBoardXPos(squareNumber, boardWidth);
        int squareCentredYPos = BoardSquare.calcBoardYPos(squareNumber, boardHeight);

        // These coords are actually the corner of the square, but the
        // label position is set by the corner of the label, so setting the corner
        // of the label to the corner of the square means the piece is centred.
        Point centredPos = new Point(squareCentredXPos, squareCentredYPos);
        return centredPos;

    }

    static void parsePieceImages(String allPiecesImage){

        PieceImageParser parsePieceImages = new PieceImageParser(allPiecesImage);

        whiteKing = new ImageIcon(parsePieceImages.getWhiteKing());
        whiteQueen = new ImageIcon(parsePieceImages.getWhiteQueen());
        whiteBishop = new ImageIcon(parsePieceImages.getWhiteBishop());
        whiteKnight = new ImageIcon(parsePieceImages.getWhiteKnight());
        whiteRook = new ImageIcon(parsePieceImages.getWhiteRook());
        whitePawn = new ImageIcon(parsePieceImages.getWhitePawn());

        blackKing = new ImageIcon(parsePieceImages.getBlackKing());
        blackQueen = new ImageIcon(parsePieceImages.getBlackQueen());
        blackBishop = new ImageIcon(parsePieceImages.getBlackBishop());
        blackKnight = new ImageIcon(parsePieceImages.getBlackKnight());
        blackRook = new ImageIcon(parsePieceImages.getBlackRook());
        blackPawn = new ImageIcon(parsePieceImages.getBlackPawn());

    }

    public void addPieceListeners(){
        this.addMouseListener(this);
        this.addMouseMotionListener(this);
    }

    private void setPiecePaneLayer(Component component, String layer){
        this.parentChessBoard.setLayer(component, Integer.valueOf(layer));
    }

    @Override
    public void mouseClicked(MouseEvent e) {

    }

    @Override
    public void mousePressed(MouseEvent e) {
        // getting the start pos of the selected piece.
        ChessBoard.selectedPieceStartPos = this.getPieceLocation();

        System.out.println("Start Pos:");
        System.out.println(ChessBoard.selectedPieceStartPos);

        this.movePiece(e, false);
        setPiecePaneLayer(this, "2");
    }

    @Override
    public void mouseReleased(MouseEvent e) {

        int dropSqNo = BoardSquare.calcSquareNumber(
                (int)this.getPosition().getX(),
                (int)this.getPosition().getY()
        );

        // getting the end pos of the selected pos
        ChessBoard.selectedPieceEndPos = ChessBoard.squareLabels[dropSqNo];

        System.out.println("This is the sq we are dropping on...");
        System.out.println(ChessBoard.selectedPieceEndPos);




        // if there is another piece on that square remove it.
//        if (
//                ChessPiece.squareNumberPieceMap.containsKey(dropSqNo)
//                &&
//                !ChessBoard.selectedPieceStartPos.equals(ChessBoard.selectedPieceEndPos)
//        ){
//
//            ChessPiece pieceToRemove = ChessPiece.squareNumberPieceMap.get(dropSqNo);
//
//
//            this.parentChessBoard.remove(pieceToRemove);
//
//            ChessPiece.squareNumberPieceMap.remove(
//                    dropSqNo,
//                    pieceToRemove
//            );
//
//
//        }




        this.movePiece(e, true);
        setPiecePaneLayer(this, "1");



        // ***** send the command to python and then read back in the board state *****
        // as long as we are not dropping the piece where it started.
        if (!ChessBoard.selectedPieceStartPos.equals(ChessBoard.selectedPieceEndPos)){



            //TODO execute the move in python and load back in the game json.
            //TODO create a new class for the connector? or maybe use game data class.
            GameData.sendMoveToPython(
                    ChessBoard.selectedPieceStartPos,
                    ChessBoard.selectedPieceEndPos
            );


            this.parentChessBoard.setGameData();


            this.parentChessBoard.reloadPieces(
                    this.parentChessBoard.getGameData().getBoardStateString()
            );

            //TODO need to sort out how to call this... ***********
            //tempBoardRef.reloadPieces(gameData.getBoardStateString());


        }

        // resetting the start pos and end pos of the now dropped piece.
        ChessBoard.selectedPieceStartPos = "";
        ChessBoard.selectedPieceEndPos = "";
    }

    @Override
    public void mouseEntered(MouseEvent e) {}

    @Override
    public void mouseExited(MouseEvent e) {}

    @Override
    public void mouseDragged(MouseEvent e) {
        setPiecePaneLayer(this, "2");
        this.movePiece(e, false);
    }

    @Override
    public void mouseMoved(MouseEvent e) {}
}
